'''
Created on Feb 15, 2011

@author: eplaster
'''
from pyvisdk import consts
from pyvisdk.consts import ManagedObjectRef, TaskInfoState
from suds.sudsobject import Property
import logging
import os
import os.path
import suds
import time

class VisdkTaskError(Exception):
    pass

class VimBase(object):
    '''
    Base class to hold the nuts and bolts for the web services grunt work.
    '''


    def __init__(self, server, connect=True, verbose=3):
        '''
        Constructor
        '''
        self.server = server
        self.verbose = verbose
        self.connected = False
         
        # setup logging...
        logging.basicConfig(level=logging.INFO)
        logging.getLogger('suds.client').setLevel(logging.INFO)
        logging.getLogger('suds.wsdl').setLevel(logging.INFO)
        logging.getLogger('suds.transport').setLevel(logging.INFO)
        logging.getLogger('suds.xsd.schema').setLevel(logging.INFO)
       
        if self.verbose > 5:
            logging.getLogger('suds.client').setLevel(logging.DEBUG)
        
        if connect:
            self.connect()
        
    def connect(self):
        if self.connected:
            return
        self.url = "https://" + self.server + '/sdk'
        wsdl_dir = os.path.dirname(__file__)
      
        # create the soap client
        self.client = suds.client.Client("file://"+os.path.join(wsdl_dir, 'wsdl', 'vimService.wsdl'))
        self.client.set_options(location=self.url)

        # create the Service Instance managed object
        self.service_instance = Property('ServiceInstance')
        self.service_instance._type = 'ServiceInstance'

        # get the service content
        self.service_content = self.client.service.RetrieveServiceContent(self.service_instance)
        self.managers = {}
        
        # bundle up all the managed objects that we need
        for name, _type in consts.serviceTypes.items():
            try:
                self.managers[name] = ManagedObjectRef(_type, eval("self.service_content.%s.value" % name))
            except AttributeError, e:
                pass  # it may not support all the listed services

        self.root = self.managers['rootFolder']
        self.connected = True
        
    def callRetrievePropertiesEx(self, maxObjects=0):
        myPropSpec = self.PropertySpec(all=False, _type=consts.VirtualMachine, pathSet=["name"])
       
        myObjSpec = self.ObjectSpec(self.root, selectSet=self.buildFullTraversal())
       
        pSpec = self.PropertyFilterSpec(propSet=[myPropSpec], objectSet=[myObjSpec])
       
        rOptions = self.RetrieveOptions(int(maxObjects))
      
        retrieveResult = self.client.service.RetrievePropertiesEx(self.managers["propertyCollector"], [pSpec], rOptions)      
      
        #objContentArrayList = Arrays.asList(retrieveResult.getObjects())
        #if(retrieveResult.getToken() != null && maxObjects == null) {
        #   callContinueRetrieveProperties(retrieveResult.getToken())
        #}            
        #ObjectContent [] objectContentArray = (ObjectContent [])objContentArrayList.toArray()
        #for(int i=0; i<objectContentArray.length; i++) {
        #   System.out.println("VM Managed Object Reference Value: " + objectContentArray[i].getObj().get_value());
        #}
        return retrieveResult

        
    """
     * Get the ManagedObjectReference for an item under the specified root
     * folder that has the type and name specified.
     * 
     * @param root
     *            a root folder if available, or null for default
     * @param type
     *            type of the managed object
     * @param name
     *            name to match
     * 
     * @return First ManagedObjectReference of the type / name pair found
    """
    def getDecendentsByName(self, _type, pathSet=["name"], name=None, root=None):

        typeinfo = [ self.PropertySpec(_type=_type, pathSet=pathSet) ]

        ocary = self.getContentsRecursively(root=root, props=typeinfo, recurse=True)

        if not ocary:
            return

        if not name:
            return ocary
        
        for vm in ocary:
            found = False
            if vm.propSet:
                for prop in vm.propSet:
                    if prop.name == "name" and prop.val == name:
                        found = True
                        break
            if found:
                return vm
        return None

    """
    * Retrieve all the ManagedObjectReferences of the type specified.
    *
    * @param root a root folder if available, or null for default
    * @param type type of container refs to retrieve
    *
    * @return List of MORefs
    """
    def getDecendentsByFilter(self, type, filters=[], root=None):
        props = [ self.PropertySpec(type, pathSet=["name"]) ]
        ocary = self.getContentsRecursively(collector=root, props=props, recurse=True)
        refs = []
        if ocary == None or len(ocary) == 0:
            return refs
        
        for oc in ocary:
            refs.append(oc.obj)
            
        if filters:
            filtered = []
            for ref in refs:
                rejected = False
                for filter in filters:
                    if hasattr(ref, filter):
                        rejected = True
                        break
                if not rejected:
                    filtered.append(ref)
            return filtered
        else:
            return refs
   

    """
     * Retrieve Container contents for all containers recursively from root
     *
     * @return retrieved object contents
    """
    def getAllContainerContents(self):
        ocary = self.getContentsRecursively(recurse=True)
        return ocary
   
    def getContentsRecursively(self, collector=None, root=None, props=[], recurse=True):
        usecoll = collector
        if not usecoll:
            usecoll = self.managers["propertyCollector"]
           
        useroot = root
        if not useroot:
            useroot = self.root
        
        if not props:
            props = [ self.PropertySpec(_type=consts.ManagedEntity) ]
            
        selectionSpecs = []
        if recurse:
            selectionSpecs = self.buildFullTraversal()
         
        spec = self.PropertyFilterSpec(propSet=props, objectSet=[ self.ObjectSpec(useroot, selectSet=selectionSpecs) ])
        return self.client.service.RetrieveProperties(usecoll, [ spec ])
   
    """
     * This method creates a SelectionSpec[] to traverses the entire inventory
     * tree starting at a Folder
     * 
     * @return The SelectionSpec[]
    """
    def buildFullTraversal(self):
        # Recurse through all ResourcePools
        rpToRp = self.TraversalSpec(name="rpToRp", _type=consts.ResourcePool, path="resourcePool",
                        selectSet=[ self.SelectionSpec("rpToRp"), self.SelectionSpec("rpToVm") ])

        # Recurse through all ResourcePools
        rpToVm = self.TraversalSpec(name="rpToVm", _type=consts.ResourcePool, path="vm")

        # Traversal through ResourcePool branch
        crToRp = self.TraversalSpec(name="crToRp", _type=consts.ComputeResource, path="resourcePool",
                        selectSet=[ self.SelectionSpec("rpToRp"), self.SelectionSpec("rpToVm") ])

        # Traversal through host branch
        crToH = self.TraversalSpec(name="crToH", _type=consts.ComputeResource, path="host")
        
        # Traversal through hostFolder branch
        dcToHf = self.TraversalSpec(name="dcToHf", _type=consts.Datacenter, path="hostFolder",
                        selectSet=[self.SelectionSpec("visitFolders")])

        # Traversal through vmFolder branch
        dcToVmf = self.TraversalSpec(name="dcToVmf", _type=consts.Datacenter, path="vmFolder",
                        selectSet=[self.SelectionSpec("visitFolders")])

        # Recurse through all Hosts
        HToVm = self.TraversalSpec(name="HToVm", _type=consts.HostSystem, path="vm",
                        selectSet=[self.SelectionSpec("visitFolders")])
        
        # Recurse through the folders
        visitFolders = self.TraversalSpec(name="visitFolders", _type=consts.Folder, path="childEntity",
                        selectSet=[ self.SelectionSpec("visitFolders"),
                                     self.SelectionSpec("dcToHf"),
                                     self.SelectionSpec("dcToVmf"),
                                     self.SelectionSpec("crToH"),
                                     self.SelectionSpec("crToRp"),
                                     self.SelectionSpec("HToVm"),
                                     self.SelectionSpec("rpToVm"), ])
        
        return (visitFolders, dcToVmf, dcToHf, crToH, crToRp, rpToRp, HToVm, rpToVm)
 
    """
    * Illustrating how to create, use and destroy additional property collectors
    * This allows multiple modules to create their own property filter and process updates independently.
    * Also applow to get time-sensitive updated being monitored on one collector, 
    * while a large updatyed being monitored by another.
    """
    def callCreatePropertyCollectorEx(self):
        propCol = self.client.service.CreatePropertyCollector( self.managers['propertyCollector'] )
        collector = ManagedObjectRef(consts.serviceTypes['propertyCollector'], propCol.value)
        
        if self.verbose > 5:
            print "="*80
            print collector
            print "="*80
      
        pSpec = self.PropertyFilterSpec(
                propSet=[
                    self.PropertySpec(_type=consts.VirtualMachine, all=False, pathSet=["name"])
                ], 
                objectSet=[
                    self.ObjectSpec(self.root, 
                                    selectSet = self.buildFullTraversal())
                ])
         
        rOptions = self.RetrieveOptions()     
        
        retrieveResult = self.client.service.RetrievePropertiesEx( collector, pSpec, rOptions)      
        self.client.service.DestroyPropertyCollector(collector)
        return retrieveResult
    
    def _parseTaskResponse(self, response):
        status = {}
        for x in response.filterSet[0].objectSet[0].changeSet:
            if hasattr(x, 'val'):
                status[x.name] = x.val
            else:
                status[x.name] = x.op
        return status

    def waitForTask(self, objmor, wait_time=2):
        version = ""

        objmor = ManagedObjectRef("Task", objmor.value)

        myObjSpec = self.ObjectSpec(objmor)
        myPropSpec = self.PropertySpec(_type=objmor._type, pathSet=["info.state", "info.error"])
        pSpec = self.PropertyFilterSpec(propSet=[myPropSpec], objectSet=[myObjSpec])

        filterSpecRef = self.client.service.CreateFilter(self.managers["propertyCollector"], pSpec, True)
        filterSpecRef = ManagedObjectRef("PropertyFilter", filterSpecRef.value)
        
        
        updateset = self.client.service.WaitForUpdates(self.managers["propertyCollector"], version)
        
        status = self._parseTaskResponse(updateset)
        while status['info.state'] in [ TaskInfoState.running, TaskInfoState.queued ]:
            print "Waiting for task to complete...  sleeping for %d seconds" % wait_time
            time.sleep(wait_time)
            version = updateset.version
            updateset = self.client.service.WaitForUpdates(self.managers["propertyCollector"], version)
            status = self._parseTaskResponse(updateset)
        
        print "Finished task..."
        # Destroy the filter when we are done.
        self.client.service.DestroyPropertyFilter(filterSpecRef)
        
        if status['info.state'] == TaskInfoState.error:
            fault = objmor.info.getError()
            error = "Error Occured"
            if fault:
                error += ": " + fault.fault.reason + " code: " + str(fault.fault.code)
            raise VisdkTaskError(error)

    def update(self, objmor, properties=[], version="", wait_time=2):
        myObjSpec = self.ObjectSpec(objmor)
        myPropSpec = self.PropertySpec(_type=objmor._type, pathSet=properties)
        pSpec = self.PropertyFilterSpec(propSet=[myPropSpec], objectSet=[myObjSpec])

        filterSpecRef = self.client.service.CreateFilter(self.managers["propertyCollector"], pSpec, False)
        filterSpecRef = ManagedObjectRef("PropertyFilter", filterSpecRef.value)
        
        changeData = self.client.service.CheckForUpdates(self.managers["propertyCollector"], version)
        
        print "Finished update..."
        # Destroy the filter when we are done.
        self.client.service.DestroyPropertyFilter(filterSpecRef)
        
        if hasattr(changeData, "filterSet"):
            changeData = changeData.filterSet[0].objectSet[0]
            
        if hasattr(changeData, "changeSet"):
            changeData = changeData.changeSet
            
        return changeData, version
        
    """ Factory Objects """
    def RetrieveOptions(self, maxObjects=0):
        spec = self.client.factory.create('ns0:RetrieveOptions')
        if int(maxObjects):
            spec.maxObjects = int(maxObjects)
        return spec
        
    # ObjectSpec factory
    def ObjectSpec(self, view, skip=False, selectSet=[]):
        spec = self.client.factory.create('ns0:ObjectSpec')
        spec.obj = view
        spec.skip = skip
        if selectSet:
            spec.selectSet = selectSet
        return spec
    
    # TraversalSpec factory
    def TraversalSpec(self, name, _type, path, skip=False, selectSet=[]):
        spec = self.client.factory.create('ns0:TraversalSpec')
        spec.name = name
        spec.path = path
        spec.type = _type
        spec.skip = skip
        if selectSet:
            spec.selectSet = selectSet
        return spec

    # PropertySpec factory
    def PropertySpec(self, _type, all=False, pathSet=[]):
        spec = self.client.factory.create('ns0:PropertySpec')
        spec.type = _type
        spec.all = all
        spec.pathSet = pathSet
        return spec

    # PropertyFilterSpec factory
    def PropertyFilterSpec(self, propSet=[], objectSet=[]):
        spec = self.client.factory.create('ns0:PropertyFilterSpec')
        spec.objectSet = objectSet
        spec.propSet = propSet
        return spec

    # SelectionSpec factory
    def SelectionSpec(self, name):
        spec = self.client.factory.create('ns0:SelectionSpec')
        spec.name = name
        return spec

        
        
        
        
        
        
        
        
        
    
    