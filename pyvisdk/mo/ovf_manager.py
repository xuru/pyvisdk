
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OvfManager(BaseEntity):
    '''The purpose of this interface is to make it easier for callers to import VMs and
        vApps from OVF packages and to export VI packages to OVF. In the following
        description, the term "client" is used to mean any caller of the
        interface.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.OvfManager):
        # MUST define these
        super(OvfManager, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def CreateDescriptor(self, obj, cdp):
        '''Create an OVF descriptor for the specified ManagedEntity, which may be a
        VirtualMachine or a VirtualApp.To create the complete OVF descriptor, the
        client must already have downloaded the files that are part of the entity,
        because information about these files (compression, chunking, filename
        etc.) is part of the descriptor.However, these downloads can be quite
        time-consuming, so if the descriptor for some reason cannot be generated,
        the client will want to know this before downloading the files.For this
        reason, the client may do an initial "dry run" with the ovfFiles parameter
        unset. Default filenames will then be used in the descriptor, and the
        client can examine any warnings and/or errors before downloading the
        files.After the final call to this method, client must release the lock on
        the entity given to it by VirtualMachine.exportVm or
        VirtualApp.exportVApp.

        :param obj: The entity to export. Supported types are VirtualMachine and VirtualApp.

        :param cdp: Parameters to the method, bundled in an instance of CreateDescriptorParams.


        :rtype: OvfCreateDescriptorResult 

        '''
        
        return self.delegate("CreateDescriptor")(obj,cdp)
        

    def CreateImportSpec(self, ovfDescriptor, resourcePool, datastore, cisp):
        '''Validate the OVF descriptor against the hardware supported by the host system. If
        the validation succeeds, return a result containing:

        :param ovfDescriptor: The OVF descriptor of the entity.

        :param resourcePool: The resource pool to import the entity to. May be a vApp.

        :param datastore: The datastore on which to create the inventory objects of the entity, for example
        "storage1". The privilege Datastore.AllocateSpace is required on the
        datastore.

        :param cisp: Additional parameters to the method, bundled in an instance of
        CreateImportSpecParams.


        :rtype: OvfCreateImportSpecResult 

        '''
        
        return self.delegate("CreateImportSpec")(ovfDescriptor,resourcePool,datastore,cisp)
        

    def ParseDescriptor(self, ovfDescriptor, pdp):
        '''Parse the OVF descriptor and return as much information about it as possible
        without knowing the host on which it will be imported.Typically, this
        method is called once without a deploymentOption parameter to obtain the
        values for the default deployment option. Part of the result is the list
        of possible deployment options. To obtain the values for a particular
        deployment option, call this method again, specifying that option.

        :param ovfDescriptor: The OVF descriptor to examine.

        :param pdp: Additional parameters for parseDescriptor, wrapped in an instance of
        ParseDescriptorParams.


        :rtype: OvfParseDescriptorResult 

        '''
        
        return self.delegate("ParseDescriptor")(ovfDescriptor,pdp)
        

    def ValidateHost(self, ovfDescriptor, host, vhp):
        '''Validate that the given OVF can be imported on the host.More specifically, this
        means whether or not the host supports the virtual hardware required by
        the OVF descriptor.

        :param ovfDescriptor: The OVF descriptor to examine.

        :param host: The host to validate against.

        :param vhp: Additional parameters for validateHost, wrapped in a ValidateHostParams instance.


        :rtype: OvfValidateHostResult 

        '''
        
        return self.delegate("ValidateHost")(ovfDescriptor,host,vhp)
        
