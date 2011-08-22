
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.profile_manager import ProfileManager
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostProfileManager(ProfileManager):
    '''This Class is responsible for managing Host Profiles.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostProfileManager):
        super(HostProfileManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    
    
    
    def ApplyHostConfig_Task(self):
        '''Apply the configuration to the host.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("ApplyHostConfig_Task")()
    
    def CreateDefaultProfile(self):
        '''Create a default profile of a given type. e.g: VirtualSwitchProfile. The
        profileTypes are defined in Vmodl. Once the default profile dataObject is
        generated, it can be modified and a profile can be created on the server.
        :rtype: 
        :returns: 
        '''
        return self.delegate("CreateDefaultProfile")()
    
    def GenerateConfigTaskList(self):
        '''Generate a list of configuration tasks that will be performed on the host
        during HostProfile application.
        :rtype: 
        :returns: 
        '''
        return self.delegate("GenerateConfigTaskList")()
    
    def QueryHostProfileMetadata(self):
        '''Query the metadata for the Profiles.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryHostProfileMetadata")()