#!/usr/bin/env python
import suds, sys
from suds.sudsobject    import Property

"""
Assumptions:  Must connect to the vSphere vCenter
              Must be version 4.0 or greater

"""


import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.INFO)
logging.getLogger('suds.wsdl').setLevel(logging.INFO)
logging.getLogger('suds.transport').setLevel(logging.INFO)
logging.getLogger('suds.xsd.schema').setLevel(logging.INFO)


meTree = [
      "ManagedEntity", 
      "ComputeResource", 
      "ClusterComputeResource", 
      "Datacenter", 
      "Folder",
      "HostSystem",
      "ResourcePool",
      "VirtualMachine"
      ]
crTree = [
      "ComputeResource", 
      "ClusterComputeResource"
      ]

hcTree = [
      "HistoryCollector",
      "EventHistoryCollector",
      "TaskHistoryCollector"
      ]

serviceTypes = {
    'alarmManager'              : 'AlarmManager',
    'authorizationManager'      : 'AuthorizationManager',
    'clusterProfileManager'     : 'ClusterProfileManager',
    'complianceManager'         : 'ProfileComplianceManager',
    'customFieldsManager'       : 'CustomFieldsManager',
    'customizationSpecManager'  : 'CustomizationSpecManager',
    'diagnosticManager'         : 'DiagnosticManager',
    'dvSwitchManager'           : 'DistributedVirtualSwitchManager',
    'eventManager'              : 'EventManager',
    'extensionManager'          : 'ExtensionManager',
    'fileManager'               : 'FileManager',
    'hostProfileManager'        : 'HostProfileManager',
    'ipPoolManager'             : 'IpPoolManager',
    'licenseManager'            : 'LicenseManager',
    'localizationManager'       : 'LocalizationManager',
    'ovfManager'                : 'OvfManager',
    'perfManager'               : 'PerformanceManager',
    'propertyCollector'         : 'PropertyCollector',
    'rootFolder'                : 'Folder',
    'scheduledTaskManager'      : 'ScheduledTaskManager',
    'searchIndex'               : 'SearchIndex',
    'sessionManager'            : 'SessionManager',
    'setting'                   : 'OptionManager',
    'snmpSystem'                : 'HostSnmpSystem',
    'storageResourceManager'    : 'StorageResourceManager',
    'taskManager'               : 'TaskManager',
    'userDirectory'             : 'UserDirectory',
    'viewManager'               : 'ViewManager',
    'virtualDiskManager'        : 'VirtualDiskManager',
    'vmCompatibilityChecker'    : 'VirtualMachineCompatibilityChecker',
    'vmProvisioningChecker'     : 'VirtualMachineProvisioningChecker',
}


class Vim(object):
    def __init__(self, server, connect=True, verbose=3):
        self.server = server
        self.verbose = verbose
        if self.verbose > 5:
            logging.getLogger('suds.client').setLevel(logging.DEBUG)
        self.connected = False
        
        if connect:
            self.connect()
    
    def connect(self):
        if self.connected:
            return
        
        self.url = "https://" + self.server + '/sdk'

        # create the soap client
        self.client = suds.client.Client(self.url + '/vimService.wsdl')
        self.client.set_options(location=self.url)

        # create the Service Instance managed object
        self.service_instance = Property('ServiceInstance')
        self.service_instance._type = 'ServiceInstance'

        # get the service content
        self.service_content = self.client.service.RetrieveServiceContent(self.service_instance)
        self.managers = {}
        
        # bundle up all the managed objects that we need
        for name, _type in serviceTypes.items():
            try:
                self.managers[name] = ManagedObjectRef(_type, eval("self.service_content.%s.value" % name))
            except AttributeError, e:
                pass  # it may not support all the listed services

        self.root = self.managers['rootFolder']
        self.connected = True
            
    def login(self, username, password):
        self.username = username
        self.password = password
        
        if self.verbose > 5:
            self.displayAbout()

        self.client.service.Login(self.managers['sessionManager'], self.username, self.password)
        if self.verbose > 2:
            print "Successfully logged into %s" % self.url

    def logout(self):
        self.client.service.Logout(self.managers['sessionManager'])

    def displayAbout(self):
        print dir(self.service_content.about)
        print "=" * 40
        print "Connected to %s" % self.server
        print "  %s" % self.service_content.about.fullName
        print "  OS: %s" % self.service_content.about.osType
        print "  License: %s %s" % (
                self.service_content.about.licenseProductName, self.service_content.about.licenseProductVersion)
        print "=" * 40

    def getApiType(self):
        return self.service_content.about.apiType
    
    def callRetrievePropertiesEx(self, maxObjects=0):
        myPropSpec = self.PropertySpec(all=False, _type="VirtualMachine", pathSet=["name"])
       
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


    def getDatacenter(self, dcName):
        #pSpec = self.PropertySpec("Datacenter", pathSet=["name"])
        
        # The following TraversalSpec and SelectionSpec
        # objects create the following relationship:
        #
        # a. Folder -> childEntity
        # b. recurse to a.
        dcMoRef = self.getDecendentMoRef(_type="Datacenter", name=dcName)
        return dcMoRef
        
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
    def getDecendentMoRef(self, name, _type=None, root=None):

        typeinfo = [ self.PropertySpec(_type=_type, pathSet=["name"]) ]

        ocary = self.getContentsRecursively(root=root, props=typeinfo, recurse=True)

        if not ocary:
            return

        mos = []
        for oc in ocary:
            found = False
            if not _type or _type == oc.obj.type:
                if oc.propSet:
                    propval = str(oc.propSet[0].value)
                    
                    if propval and name == propval:
                        found = True
            if not found:
                mos.append(oc)
        return mos

    """
    * Retrieve all the ManagedObjectReferences of the type specified.
    *
    * @param root a root folder if available, or null for default
    * @param type type of container refs to retrieve
    *
    * @return List of MORefs
    """
    def getDecendentMoRefs(self, root, type, filters=[]):
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
            props = [ self.PropertySpec(_type="ManagedEntity") ]
            
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
        rpToRp = self.TraversalSpec(name="rpToRp", _type="ResourcePool", path="resourcePool",
                        selectSet=[ self.SelectionSpec("rpToRp"), self.SelectionSpec("rpToVm") ])

        # Recurse through all ResourcePools
        rpToVm = self.TraversalSpec(name="rpToVm", _type="ResourcePool", path="vm")

        # Traversal through ResourcePool branch
        crToRp = self.TraversalSpec(name="crToRp", _type="ComputeResource", path="resourcePool",
                        selectSet=[ self.SelectionSpec("rpToRp"), self.SelectionSpec("rpToVm") ])

        # Traversal through host branch
        crToH = self.TraversalSpec(name="crToH", _type="ComputeResource", path="host")
        
        # Traversal through hostFolder branch
        dcToHf = self.TraversalSpec(name="dcToHf", _type="Datacenter", path="hostFolder",
                        selectSet=[self.SelectionSpec("visitFolders")])

        # Traversal through vmFolder branch
        dcToVmf = self.TraversalSpec(name="dcToVmf", _type="Datacenter", path="vmFolder",
                        selectSet=[self.SelectionSpec("visitFolders")])

        # Recurse through all Hosts
        HToVm = self.TraversalSpec(name="HToVm", _type="HostSystem", path="vm",
                        selectSet=[self.SelectionSpec("visitFolders")])

        # Recurse through the folders
        visitFolders = self.TraversalSpec(name="visitFolders", _type="Folder", path="childEntity",
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
        collector = ManagedObjectRef(serviceTypes['propertyCollector'], propCol.value)
        
        if self.verbose > 5:
            print "="*80
            print collector
            print "="*80
      
        pSpec = self.PropertyFilterSpec(
                propSet=[
                    self.PropertySpec(_type="VirtualMachine", all=False, pathSet=["name"])
                ], 
                objectSet=[
                    self.ObjectSpec(self.root, 
                                    selectSet = self.buildFullTraversal())
                ])
         
        rOptions = self.RetrieveOptions()     
        
        retrieveResult = self.client.service.RetrievePropertiesEx( collector, pSpec, rOptions)      
        self.client.service.DestroyPropertyCollector(collector)
        return retrieveResult

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

    def getProperties(self, moRef, properties=None):
        pSpec = self.vim.create_object('PropertySpec')
        if not properties:
            pSpec.all = True
        else:
            pSpec.all = True
            pSpec.pathSet = properties
        pSpec.type = moRef

        oSpec = self.vim.create_object('ObjectSpec')
        oSpec.obj = moRef

        pfs = self.vim.create_object('PropertyFilterSpec')
        pfs.propSet = [pSpec]
        pfs.objectSet = [oSpec]

        object_contents = self.vim.invoke('RetrieveProperties',
                  _this=self.vim.property_collector, specSet=pfs)

        if self.verbose > 5:
            for object_content in object_contents:
                print object_content.obj._type, object_content


class ManagedObjectRef(suds.sudsobject.Property):
    """Custom class to replace the suds generated class, which lacks _type."""
    def __init__(self, _type, value):
        suds.sudsobject.Property.__init__(self, value)
        self._type = _type
        
if __name__ == '__main__':
    from optparse import OptionParser
    
    # Some command line argument parsing gorp to make the script a little more
    # user friendly.
    usage = '''Usage: %prog [options]

      This program will dump the containers of the ESX environment from the host specified with
      the -s option.'''
    
    parser = OptionParser(usage=usage)
    parser.add_option('-s', '--server', dest='server',
                  help='Specify the vCenter to connect to')
    parser.add_option('-u', '--username', dest='username',
                      help='Username (default is root)')
    parser.add_option('-p', '--password', dest='password',
                      help='Password (default is blank)')
    (options, args) = parser.parse_args()
    if options.server is None:
        print 'You must specify a server to connect to.  Use --help for usage'
        sys.exit(1)
    if options.username is None:
        options.username = 'root'
    if options.password is None:
        options.password = ''


    vim = Vim(options.server, verbose=3)
    vim.login(options.username, options.password)
    
    # get all the containers and their contents
    containers = vim.getAllContainerContents()
    for container in containers:
        obj = container.obj
        print "%s: %s" % (obj._type, obj.value)
            
    # these may not work...
    #print vim.callCreatePropertyCollectorEx()
    #print vim.callRetrievePropertiesEx()
    #print vim.getDatacenter("KS-PROD-Datacenter")
    vim.logout()


