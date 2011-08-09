
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.base.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OvfManager(BaseEntity):
    '''Service interface to parse and generate OVF descriptors.The purpose of this
        interface is to make it easier for callers to import VMs and vApps from
        OVF packages and to export VI packages to OVF. In the following
        description, the term "client" is used to mean any caller of the
        interface.This interface only converts between OVF and VI types. To
        actually import and export entities, use ResourcePool.importVApp,
        VirtualMachine.exportVm and VirtualApp.exportVApp.For the import scenario,
        the typical sequence of events is as follows:The client calls
        parseDescriptor to obtain information about the OVF descriptor. This
        typically includes information (such as a list of networks) that must be
        mapped to VI infrastructure entities.The OVF descriptor is validated
        against the OVF Specification, and any errors or warnings are returned as
        part of the ParseResult. For example, the parser might encounter a section
        marked required that it does not understand, or the XML descriptor might
        be malformed.The client decides on network mappings, datastore, properties
        etc. It then calls createImportSpec to obtain the parameters needed to
        call ResourcePool.importVApp.If any warnings are present, the client will
        review these and decide whether to proceed or not. If errors are present,
        the ImportSpec will be missing, so the client is forced to give up or fix
        the problems and then try again.The client now calls
        ResourcePool.importVApp, passing the ImportSpec as a parameter. This will
        create the virtual machines and VirtualApp objects in VI and return
        locations to which the files of the entity can be uploaded. It also
        returns a lease that controls the duration of the lock taken on the newly
        created inventory objects. When all files have been uploaded, the client
        must release this lease.Creating the OVF descriptor is the last part of
        exporting an entity to OVF. At this point, the client has already
        downloaded all files for the entity, optionally compressing and/or
        chunking them (however, the client may do a "dry run" of creating the
        descriptor before downloading the files. See
        OvfManager.createDescriptor).In addition to the entity reference itself,
        information about the choices made on these files is passed to
        createDescriptor as a list of OvfFile instances.The client must inspect
        and act upon warnings and errors as previously described.No matter if the
        export succeeds or fails, the client is responsible for releasing the
        shared state lock taken on the entity (by VirtualMaching.exportVm or
        VirtualApp.exportVApp) during the export.All result types contain warning
        and error lists. Warnings do not cause processing to fail, but the caller
        (typically, the user of a GUI client) may choose to reject the result
        based on the warnings issued.Errors cause processing to abort by
        definition.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.OvfManager):
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

        :param obj: to a ManagedEntityThe entity to export. Supported types are VirtualMachine and
        VirtualApp.

        :param cdp: Parameters to the method, bundled in an instance of CreateDescriptorParams.


        :rtype: OvfCreateDescriptorResult 

        '''
        
        return self.delegate("CreateDescriptor")(obj,cdp)
        

    def CreateImportSpec(self, ovfDescriptor, resourcePool, datastore, cisp):
        '''Validate the OVF descriptor against the hardware supported by the host system. If
        the validation succeeds, return a result containing:* An ImportSpec to use
        when importing the entity. * A list of items to upload (for example disk
        backing files, ISO images etc.)

        :param ovfDescriptor: The OVF descriptor of the entity.

        :param resourcePool: to a ResourcePoolThe resource pool to import the entity to. May be a vApp.

        :param datastore: to a DatastoreThe datastore on which to create the inventory objects of the
        entity, for example "storage1". The privilege Datastore.AllocateSpace is
        required on the datastore.

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

        :param host: to a HostSystemThe host to validate against.

        :param vhp: Additional parameters for validateHost, wrapped in a ValidateHostParams instance.


        :rtype: OvfValidateHostResult 

        '''
        
        return self.delegate("ValidateHost")(ovfDescriptor,host,vhp)
        
