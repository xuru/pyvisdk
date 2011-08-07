
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
    
    

    def ApplyHostConfig_Task(self, profileName):
        '''Apply the configuration to the host.

        :param profileName: Names of the profiles for which metadata is requested. If profileName is not set,
        metadata for all the profiles will be returned.


        :rtype: ProfileMetadata[] 

        '''
        
        return self.delegate("ApplyHostConfig_Task")(profileName)
        

    def CreateDefaultProfile(self, profileName):
        '''Create a default profile of a given type. e.g: VirtualSwitchProfile. The
        profileTypes are defined in Vmodl. Once the default profile dataObject is
        generated, it can be modified and a profile can be created on the server.

        :param profileName: Names of the profiles for which metadata is requested. If profileName is not set,
        metadata for all the profiles will be returned.


        :rtype: ProfileMetadata[] 

        '''
        
        return self.delegate("CreateDefaultProfile")(profileName)
        

    def GenerateConfigTaskList(self, profileName):
        '''Generate a list of configuration tasks that will be performed on the host during
        HostProfile application.

        :param profileName: Names of the profiles for which metadata is requested. If profileName is not set,
        metadata for all the profiles will be returned.


        :rtype: ProfileMetadata[] 

        '''
        
        return self.delegate("GenerateConfigTaskList")(profileName)
        

    def QueryHostProfileMetadata(self, profileName):
        '''Query the metadata for the Profiles.

        :param profileName: Names of the profiles for which metadata is requested. If profileName is not set,
        metadata for all the profiles will be returned.


        :rtype: ProfileMetadata[] 

        '''
        
        return self.delegate("QueryHostProfileMetadata")(profileName)
        
