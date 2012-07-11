
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.profile_manager import ProfileManager

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostProfileManager(ProfileManager):
    '''The HostProfileManager provides access to a list of HostProfiles and it defines
    methods to manipulate profiles and AnswerFiles.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostProfileManager):
        super(HostProfileManager, self).__init__(core, name=name, ref=ref, type=type)

    

    
    
    def ApplyHostConfig_Task(self, host, configSpec, userInput=None):
        '''Apply the configuration to the host. If you specify any user input, the
        configuration will be saved in the AnswerFile associated with the host. If
        there is no answer file, the Profile Engine will create one.
        
        :param host: Host to be updated. User must have sufficient credentials and privileges to satisfy the contents of the.
        
        :param configSpec: Set of configuration changes to be applied to the host. The changes are returned by the HostProfile.ExecuteHostProfile method in the ProfileExecuteResult.configSpec property.
        
        :param userInput: Additional host-specific data to be applied to the host. This data is the complete list of deferred parameters verified by the HostProfile.ExecuteHostProfile method, contained in the ProfileExecuteResult object returned by the method.vSphere API 5.0
        
        '''
        return self.delegate("ApplyHostConfig_Task")(host, configSpec, userInput)
    
    def CheckAnswerFileStatus_Task(self, host):
        '''Check the validity of the answer files for the specified hosts. The Profile
        Engine uses the profile associated with a host to check the answer file.
        
        :param host: Set of hosts for which the answer file status will be checked.
        
        '''
        return self.delegate("CheckAnswerFileStatus_Task")(host)
    
    def CreateDefaultProfile(self, profileType, profileTypeName=None, profile=None):
        '''Create a default subprofile of a given type (for example, a
        VirtualSwitchProfile). After you create the subprofile, you can add it to a
        configuration specification and update the host profile:Create a default
        subprofile of a given type (for example, a VirtualSwitchProfile). After you
        create the subprofile, you can add it to a configuration specification and
        update the host profile:
        
        :param profileType: Type of profile to create. The profile types are system-defined (ApplyProfile.profileTypeName).
        
        :param profileTypeName: If specified, the method returns a profile object containing data for the named profile. The type name does not have to be system-defined. A user-defined profile can include various dynamically-defined profiles.vSphere API 5.0
        
        :param profile: Base profile used during the operation.vSphere API 5.0
        
        '''
        return self.delegate("CreateDefaultProfile")(profileType, profileTypeName, profile)
    
    def ExportAnswerFile_Task(self, host):
        '''Export a host's answer file into a serialized form. The method returns a string
        that contains only the list of user input options. See AnswerFile.userInput.
        
        :param host: Host with which the answer file is associated.
        
        '''
        return self.delegate("ExportAnswerFile_Task")(host)
    
    def GenerateConfigTaskList(self, configSpec, host):
        '''Generate a list of configuration tasks that will be performed on the host
        during HostProfile application.
        
        :param configSpec: ConfigSpec which was proposed by ExecuteHostProfile method.
        
        :param host: Host on which the HostProfile application needs to be carried out.
        
        '''
        return self.delegate("GenerateConfigTaskList")(configSpec, host)
    
    def QueryAnswerFileStatus(self, host):
        '''Returns the status of the answer files associated with specified hosts. This
        method returns the most recent status determined by CheckAnswerFileStatus_Task.
        See HostProfileManagerAnswerFileStatus for valid values.
        
        :param host: The hosts the answer file is associated with.
        
        '''
        return self.delegate("QueryAnswerFileStatus")(host)
    
    def QueryHostProfileMetadata(self, profileName=None, profile=None):
        '''Retrieve the metadata for a set of profiles.
        
        :param profileName: Names of the profiles for which metadata is requested. If not set, the method returns metadata for all the profiles.
        
        :param profile: Base profile whose context needs to be used during the operationvSphere API 5.0
        
        '''
        return self.delegate("QueryHostProfileMetadata")(profileName, profile)
    
    def QueryProfileStructure(self, profile=None):
        '''Get information about the structure of the profile.
        
        :param profile: Base profile whose context needs to be used during the operationvSphere API 5.0
        
        '''
        return self.delegate("QueryProfileStructure")(profile)
    
    def RetrieveAnswerFile(self, host):
        '''Returns the answer file associated with a particular host.
        
        :param host: Host with which the answer file is associated.
        
        '''
        return self.delegate("RetrieveAnswerFile")(host)
    
    def UpdateAnswerFile_Task(self, host, configSpec):
        '''Update the AnswerFile for the specified host. If there is no answer file
        associated with the host, the Profile Engine uses the answer file configuration
        specification to create a new one.
        
        :param host: Host with which the answer file is associated.
        
        :param configSpec: Host-specific configuration data. If the configuration specification does not contain any host-specific user input (.userInput), the method does not perform any operation on the answer file.
        
        '''
        return self.delegate("UpdateAnswerFile_Task")(host, configSpec)