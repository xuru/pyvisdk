
from pyvisdk.do.import_spec import ImportSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualAppImportSpec(ImportSpec):
    '''A VAppImportSpec is used by ResourcePool.importVApp when importing vApps (single
        VM or multi-VM).It provides all information needed to import a
        VirtualApp.See also ImportSpec.
    '''
    
    def __init__(self, child, name, resourcePoolSpec, vAppConfigSpec):
        # MUST define these
        super(VirtualAppImportSpec, self).__init__()
    
        self.data['child'] = child
        self.data['name'] = name
        self.data['resourcePoolSpec'] = resourcePoolSpec
        self.data['vAppConfigSpec'] = vAppConfigSpec
    
    
    @property
    def child(self):
        '''Contains a list of children (VirtualMachines and VirtualApps).
        '''
        return self.data['child']

    @property
    def name(self):
        '''The name of the vApp
        '''
        return self.data['name']

    @property
    def resourcePoolSpec(self):
        '''Resource pool specification.
        '''
        return self.data['resourcePoolSpec']

    @property
    def vAppConfigSpec(self):
        '''vApp configuration
        '''
        return self.data['vAppConfigSpec']

