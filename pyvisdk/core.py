'''
Created on Feb 15, 2011

@author: eplaster
'''
from suds.sudsobject import Property
import types, time
import logging
import urllib2
import lxml.etree as etree

from .base.base_entity import ManagedObjectReference, BaseEntity
from .base.data_object_types import DataObjectTypes
from .base.managed_object_types import ManagedObjectTypes
from .do.object_spec import ObjectSpec
from .do.traversal_spec import TraversalSpec
from .do.property_filter_spec import PropertyFilterSpec
from .do.property_spec import PropertySpec
from .do.selection_spec import SelectionSpec
from .do.retrieve_options import RetrieveOptions
from .enums.task_info_state import TaskInfoState
from .exceptions import VisdkTaskError
from .mo.service_instance import ServiceInstance
from .utils import camel_to_under
from brownie.importing import import_string

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

HTTP_TUNNEL = 'sdkTunnel:8089'

class VimBase(object):
    '''
    Base class to hold the nuts and bolts for the web services grunt work.
    '''


    def __init__(self, server, connect=True, verbose=3, certfile=None, keyfile=None):
        '''
        Constructor
        '''
        self.server = server
        self.verbose = verbose
        self.connected = False
        self.certfile = certfile
        self.keyfile = keyfile
        self.proxy = None
        if certfile and keyfile:
            self.server = HTTP_TUNNEL
            self.proxy = '%s:80' % server

        # setup logging...
        logging.getLogger('suds.client').setLevel(logging.INFO)
        logging.getLogger('suds.wsdl').setLevel(logging.INFO)
        logging.getLogger('suds.transport').setLevel(logging.INFO)
        logging.getLogger('suds.xsd.schema').setLevel(logging.INFO)

        if self.verbose > 5:
            logging.getLogger('suds.client').setLevel(logging.DEBUG)
            logging.getLogger('suds.transport').setLevel(logging.DEBUG)

        if connect:
            self.connect()

    def connect(self, timeout=1800):
        from .client import Client
        from .transport import HttpAuthenticated
        if self.connected:
            return

        self.client = Client(self.server, timeout=timeout)
        transport = HttpAuthenticated(proxy=self.proxy, certfile=self.certfile, keyfile=self.keyfile)
        self.client.client.set_options(transport=transport)
        # create the Service Instance managed object
        ref = Property('ServiceInstance')
        ref._type = 'ServiceInstance'
        self.service_instance = ServiceInstance(self, name='ServiceInstance', ref=ref)

        # get the service content
        self.service_content = self.service_instance.RetrieveServiceContent()
        self.property_collector = self.service_content.propertyCollector
        self.session_manager = self.service_content.sessionManager

        self.root = self.service_content.rootFolder
        self.connected = True

    def getVersions(self):
        versions = []

        def get_namespace_name(elem):
            for child in list(elem):
                if child.tag == "name":
                    return child.text

        url = urllib2.urlopen("https://" + self.server + "/sdk/vimServiceVersions.xml")
        root = etree.fromstring(url.read())
        names = root.findall(".//namespace")
        for namesp in names:
            if "urn:vim25" in get_namespace_name(namesp):
                versions = [x.text for x in namesp.findall(".//version")]
                log.debug("versions found: " + str(versions))
        return versions

    def getObjectProperties(self, mobj, properties, parent=None):
        """
        * Retrieve contents for a single object based on the property collector
        * registered with the service.
        *
        * @param mobj Managed Object Reference to get contents for
        * @param properties names of properties of object to retrieve
        * @param mo_instance: Managed Object instance to update
        *
        * @return retrieved object contents
        """
        all = False
        if not properties:
            all = True

        pspec = PropertySpec(self, all=all, type=mobj._type, pathSet=properties)
        ospec = ObjectSpec(self, obj=ManagedObjectReference(mobj._type, mobj.value), skip=False)
        spec = PropertyFilterSpec(self, propSet=[pspec], objectSet=[ospec])

        obj_content = self.property_collector.RetrieveProperties([spec])
        return self._parse_object_content(obj_content, parent=parent)

    def getDecendentsByName(self, _type, properties=["name"], name=None, root=None):
        """
         * Get the ManagedObjectReference for an item under the specified root
         * folder that has the type and name specified.
         * 
         * @param _type
         *            type of the managed object
         * @param properties 
         *            names of properties of object to retrieve
         * @param name
         *            name to match
         * @param root
         *            a root folder if available, or null for default
         * 
         * @return First ManagedObjectReference of the type / name pair found
        """
        if not "name" in properties:
            properties += ["name"]
        ocary = self.getContentsRecursively(_type=str(_type), props=properties, root=root)

        if not name:
            return ocary
        else:
            for obj in ocary:
                if obj.name == name:
                    return obj

    def getContentsRecursively(self, props=[], _type=None, collector=None, root=None, recurse=True):
        if not collector:
            collector = self.property_collector
        if not root:
            root = self.root
        if not _type:
            _type = ManagedObjectTypes.ManagedEntity #@UndefinedVariable

        pspec = PropertySpec(self, type=str(_type), pathSet=props)
        typeinfo = [ pspec ]

        selectionSpecs = []
        if recurse:
            selectionSpecs = self._buildFullTraversal()

        spec = PropertyFilterSpec(self, propSet=typeinfo, objectSet=[ ObjectSpec(self, root.ref, selectSet=selectionSpecs) ])
        obj_content = self.property_collector.RetrieveProperties([spec])
        return self._parse_object_content(obj_content)

    def _parse_object_content(self, obj_content, parent=None):
        rv = None
        class_name = obj_content.__class__.__name__
        class_name_upper = class_name[0].upper() + class_name[1:]
        if isinstance(obj_content, list):
            rv = []
            for obj in obj_content:
                rv.append(self._parse_object_content(obj, parent))

        elif type(obj_content) == types.NoneType:
            return obj_content

        elif issubclass(obj_content.__class__, BaseEntity):
            rv = obj_content

        elif class_name == 'ObjectContent':
            # create the managed object
            if not parent:
                rv = self._create_mo_obj(class_name, obj_content, parent)
            else:
                rv = []
                # now, run through the propSet
                if hasattr(obj_content, "propSet"):
                    for prop in obj_content.propSet:
                        rv.append(self._parse_object_content(prop.val))
                if len(rv) == 1:
                    rv = rv[0]

        elif class_name == "ManagedObjectReference":
            # managed object reference is too generic, so we get to the real type
            mo_f = import_string('pyvisdk.mo.%s.%s' % (camel_to_under(obj_content._type), obj_content._type))
            rv = mo_f(self, ref=obj_content)

        elif class_name in DataObjectTypes:
            rv = self._create_do_obj(class_name, obj_content, parent)

        elif class_name == 'Text':
            # obj_context is instance of suds.sax.text.Text which is a subclass of unicode
            # we need to return the text in proper encoding
            rv = str(obj_content.encode('UTF-8'))

        elif class_name in ['long', 'bool', 'int', 'datetime', 'str']:
            return obj_content

        elif "ArrayOf" in class_name:
            rv = []
            _type = class_name[7:]
            if not hasattr(obj_content, _type):
                _type = _type.lower()
            _list = getattr(obj_content, _type)
            for obj in _list:
                rv.append(self._parse_object_content(obj, parent))

        elif hasattr(obj_content, 'value') and hasattr(obj_content, '_type'):
            name = obj_content._type
            mod_name = 'pyvisdk.mo.%s' % camel_to_under(name)
            mo = import_string('%s.%s' % (mod_name, name))
            rv = mo(self, ref=obj_content)

        # TODO: ArrayOf....  ArrayOfManagedObjectReference ArrayOfAlarmState ArrayOfString ArrayOfInt ArrayOfPermission
        # TODO: val datetime datastore  entity host vm key

        elif class_name_upper in DataObjectTypes:
            rv = self._create_do_obj(class_name_upper, obj_content, parent)

        #elif class_name_upper in ManagedObjectTypes:
        #    rv = self._create_mo_obj(class_name_upper, obj_content, parent)

        else:
            log.warning("Unknown content type: %s" % class_name)
            rv = obj_content

        return rv

    def _create_do_obj(self, class_name, obj_content, parent):
        mod_name = 'pyvisdk.do.%s' % camel_to_under(class_name)
        do = import_string('%s.%s' % (mod_name, class_name))

        kwargs = {}
        for attr_name in filter(lambda x: not x.startswith('_'), dir(obj_content)):
            attr_data = eval('obj_content.%s' % attr_name)
            kwargs[attr_name] = self._parse_object_content(attr_data, parent=do)

        rv = do(self, **kwargs)
        return rv

    def _create_mo_obj(self, class_name, obj_content, parent):
        mo_f = import_string('pyvisdk.mo.%s.%s' % (camel_to_under(obj_content.obj._type), obj_content.obj._type))
        rv = mo_f(self, ref=obj_content.obj)

        # now, run through the propSet
        #if hasattr(obj_content, "propSet"):
        #    for prop in obj_content.propSet:
        #        # for each prop of the new object, create any data/managed objects
        #        setattr(rv, prop.name, self._parse_object_content(prop.val, parent=rv))
        return rv

    def _buildFullTraversal(self):
        """
         * This method creates a SelectionSpec[] to traverses the entire inventory
         * tree starting at a Folder
         * 
         * @return The SelectionSpec[]
        """
        # Recurse through all ResourcePools
        rpToRp = TraversalSpec(self, name="rpToRp", type=ManagedObjectTypes.ResourcePool, path="resourcePool", #@UndefinedVariable
                        selectSet=[ SelectionSpec(self, name="rpToRp"), SelectionSpec(self, name="rpToVm") ])

        # Recurse through all ResourcePools
        rpToVm = TraversalSpec(self, name="rpToVm", type=ManagedObjectTypes.ResourcePool, path="vm") #@UndefinedVariable

        # Traversal through ResourcePool branch
        crToRp = TraversalSpec(self, name="crToRp", type=ManagedObjectTypes.ComputeResource, path="resourcePool", #@UndefinedVariable
                        selectSet=[ SelectionSpec(self, name="rpToRp"), SelectionSpec(self, name="rpToVm") ])

        # Traversal through host branch
        crToH = TraversalSpec(self, name="crToH", type=ManagedObjectTypes.ComputeResource, path="host") #@UndefinedVariable

        # Traversal through hostFolder branch
        dcToHf = TraversalSpec(self, name="dcToHf", type=ManagedObjectTypes.Datacenter, path="hostFolder", #@UndefinedVariable
                        selectSet=[SelectionSpec(self, name="visitFolders")])

        # Traversal through vmFolder branch
        dcToVmf = TraversalSpec(self, name="dcToVmf", type=ManagedObjectTypes.Datacenter, path="vmFolder", #@UndefinedVariable
                        selectSet=[SelectionSpec(self, name="visitFolders")])

        # Recurse through all Hosts
        HToVm = TraversalSpec(self, name="HToVm", type=ManagedObjectTypes.HostSystem, path="vm", #@UndefinedVariable
                        selectSet=[SelectionSpec(self, name="visitFolders")])

        # Recurse through the folders
        visitFolders = TraversalSpec(self, name="visitFolders", type=ManagedObjectTypes.Folder, path="childEntity", #@UndefinedVariable
                        selectSet=[ SelectionSpec(self, name="visitFolders"),
                                     SelectionSpec(self, name="dcToHf"),
                                     SelectionSpec(self, name="dcToVmf"),
                                     SelectionSpec(self, name="crToH"),
                                     SelectionSpec(self, name="crToRp"),
                                     SelectionSpec(self, name="HToVm"),
                                     SelectionSpec(self, name="rpToVm"), ])

        return (visitFolders, dcToVmf, dcToHf, crToH, crToRp, rpToRp, HToVm, rpToVm)

    def update(self, _type="", root=None, properties=[], version="", wait_time=2):
        if not root:
            root = self.root

        pSpec = PropertyFilterSpec(self,
                propSet=[PropertySpec(self, type=_type, pathSet=properties)],
                objectSet=[ObjectSpec(self, root.ref)])

        filter = self.property_collector.CreateFilter(pSpec, partialUpdates=False)

        changeData = self.property_collector.CheckForUpdates(version=version)

        # Destroy the filter when we are done.
        filter.DestroyPropertyFilter()

        if hasattr(changeData, "filterSet"):
            changeData = changeData.filterSet[0].objectSet[0]

        if hasattr(changeData, "changeSet"):
            changeData = changeData.changeSet

        return changeData, version

    #############################################################
    # end untested...
    #############################################################

    def waitForTask(self, objmor):
        version = ""

        objmor = ManagedObjectReference("Task", objmor.value)

        myObjSpec = ObjectSpec(self, objmor)
        myPropSpec = PropertySpec(self, type=objmor._type, pathSet=["info.state", "info.error"])
        pSpec = PropertyFilterSpec(self, propSet=[myPropSpec], objectSet=[myObjSpec])

        filter = self.property_collector.CreateFilter(pSpec, partialUpdates=True)

        updateset = self.property_collector.WaitForUpdates(version)

        status = self._parseTaskResponse(updateset)
        while status['info.state'] in ['running', 'queued']: #@UndefinedVariable
            log.debug("Waiting for task to complete...")

            version = updateset.version
            updateset = self.property_collector.WaitForUpdates(version)
            status = self._parseTaskResponse(updateset)
            log.debug("**** status: %s" % status)
            time.sleep(0.1)

        log.debug("Finished task...")
        # Destroy the filter when we are done.
        filter.DestroyPropertyFilter()

        if status['info.state'] == TaskInfoState.error: #@UndefinedVariable
            error = status['info.error']
            raise VisdkTaskError(error.localizedMessage)
        return status['info.state']

    def _parseTaskResponse(self, response):
        status = {}
        for x in response.filterSet[0].objectSet[0].changeSet:
            if hasattr(x, 'val'):
                status[x.name] = x.val
            else:
                status[x.name] = x.op
        return status







