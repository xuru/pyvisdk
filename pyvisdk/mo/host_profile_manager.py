
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
    
    
    
    
    
    def ApplyHostConfig_Task(self, host, configSpec):
        '''Apply the configuration to the host.
        
        :param host: to a HostSystemHost to which the configuration needs to be applied. Depending on the contents of the configSpec, user has to have different privileges to perform this operation.
        
        :param configSpec: Set of configuration changes that need to be applied to the host.
        
        :rtype: ManagedObjectReference to a Task
        
        '''
        return self.delegate("ApplyHostConfig_Task")(host, configSpec)
    
    def CreateDefaultProfile(self):
        '''Create a default profile of a given type. e.g: VirtualSwitchProfile. The
        profileTypes are defined in Vmodl. Once the default profile dataObject is
        generated, it can be modified and a profile can be created on the server.
        
        '''
        return self.delegate("CreateDefaultProfile")()
    
    def GenerateConfigTaskList(self, configSpec, host):
        '''Generate a list of configuration tasks that will be performed on the host
        during HostProfile application.
        
        :param configSpec: ConfigSpec which was proposed by ExecuteHostProfile method.
        
        :param host: to a HostSystemHost on which the HostProfile application needs to be carried out.
        
        '''
        return self.delegate("GenerateConfigTaskList")(configSpec, host)
    
    def QueryHostProfileMetadata(self, profileName):
        '''Query the metadata for the Profiles.
        
        :param profileName: Names of the profiles for which metadata is requested. If profileName is not set, metadata for all the profiles will be returned.
        
        '''
        return self.delegate("QueryHostProfileMetadata")(profileName)