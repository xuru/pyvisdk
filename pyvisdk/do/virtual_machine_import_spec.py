
from pyvisdk.do.import_spec import ImportSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineImportSpec(ImportSpec):
    '''A VmImportSpec is used by ResourcePool.importVApp when importing entities.It
        provides all information needed to import a VirtualMachine. So far, this
        coincides with VirtualMachineConfigSpec.A VmImportSpec can be contained in
        a VirtualAppImportSpec as part of the ImportSpec for an entity.See also
        ImportSpec.
    '''
    
    def __init__(self, configSpec, resPoolEntity):
        # MUST define these
        super(VirtualMachineImportSpec, self).__init__()
    
        self.data['configSpec'] = configSpec
        self.data['resPoolEntity'] = resPoolEntity
    
    
    @property
    def configSpec(self):
        '''Configuration for the virtual machine.
        '''
        return self.data['configSpec']

    @property
    def resPoolEntity(self):
        '''If specified, this resource pool will be used as the parent resource pool and the
        virtual machine will be made a linked child to the parent vApp. This field
        is ignored for the root node in an ImportSpec tree.
        '''
        return self.data['resPoolEntity']

