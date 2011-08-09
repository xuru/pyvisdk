
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineCloneSpec(DynamicData):
    '''Specification for a virtual machine cloning operation.
    '''
    
    def __init__(self, config, customization, location, powerOn, snapshot, template):
        # MUST define these
        super(VirtualMachineCloneSpec, self).__init__()
    
        self.data['config'] = config
        self.data['customization'] = customization
        self.data['location'] = location
        self.data['powerOn'] = powerOn
        self.data['snapshot'] = snapshot
        self.data['template'] = template
    
    
    @property
    def config(self):
        '''An optional specification of changes to the virtual hardware. For example, this
        can be used to, (but not limited to) reconfigure the networks the virtual
        switches are hooked up to in the cloned virtual machine.
        '''
        return self.data['config']

    @property
    def customization(self):
        '''An optional guest operating system customization specification. This value is
        ignored if a template is being created.
        '''
        return self.data['customization']

    @property
    def location(self):
        '''A type of RelocateSpec that specifies the location of resources the newly cloned
        virtual machine will use. The location specifies: * A datastore where the
        virtual machine will be located on physical storage. This is always
        provided because it indicates where the newly created close will be
        copied. * a resource pool and optionally a host. The resource pool
        determines what compute resources will be available to the clone and the
        host indicates which machine will host the clone.
        '''
        return self.data['location']

    @property
    def powerOn(self):
        '''Specifies whether or not the new VirtualMachine should be powered on after
        creation. As part of a customization, this flag is normally set to true,
        since the first power-on operation completes the customization process.
        This flag is ignored if a template is being created.
        '''
        return self.data['powerOn']

    @property
    def snapshot(self):
        '''Snapshot reference from which to base the clone.
        '''
        return self.data['snapshot']

    @property
    def template(self):
        '''Specifies whether or not the new virtual machine should be marked as a template.
        '''
        return self.data['template']

