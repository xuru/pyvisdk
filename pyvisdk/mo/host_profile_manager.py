
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.profile_manager import ProfileManager
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostProfileManager(ProfileManager):
    '''This Class is responsible for managing Host Profiles.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostProfileManager):
        # MUST define these
        super(HostProfileManager, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def ApplyHostConfig_Task(self, configSpec):
        '''Apply the configuration to the host.

        :param configSpec: Set of configuration changes that need to be applied to the host.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("ApplyHostConfig_Task")(configSpec)
        

    def CreateDefaultProfile(self, profileType):
        '''Create a default profile of a given type. e.g: VirtualSwitchProfile. The
        profileTypes are defined in Vmodl. Once the default profile dataObject is
        generated, it can be modified and a profile can be created on the server.

        :param profileType: 


        :rtype: ApplyProfile 

        '''
        
        return self.delegate("CreateDefaultProfile")(profileType)
        

    def GenerateConfigTaskList(self, configSpec):
        '''Generate a list of configuration tasks that will be performed on the host during
        HostProfile application.

        :param configSpec: ConfigSpec which was proposed by ExecuteHostProfile method.


        :rtype: HostProfileManagerConfigTaskList 

        '''
        
        return self.delegate("GenerateConfigTaskList")(configSpec)
        

    def QueryHostProfileMetadata(self):
        '''Query the metadata for the Profiles.

        :rtype: ProfileMetadata[] 

        '''
        
        return self.delegate("QueryHostProfileMetadata")()
        
