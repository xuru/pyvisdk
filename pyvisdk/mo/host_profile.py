
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.profile import Profile

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostProfile(Profile):
    '''A host profile describes ESX Server configuration. The HostProfile managed
    object provides access to profile data and it defines methods to manipulate the
    profile. A host profile is a combination of subprofiles, each of which contains
    configuration data for a specific capability. Some examples of host
    capabilities are authentication, memory, networking, and security. For access
    to individual subprofiles, see the HostApplyProfile data object
    (HostProfile.config.applyProfile).Host profiles are part of the stateless
    configuration architecture. In the stateless environment, a Profile Engine runs
    on each ESX host, but an ESX host does not store its own configuration state.
    Instead, host configuration data is stored on vCenter Servers. Every time a
    host boots or reboots, it obtains its profile from the vCenter Server.* To
    create a base host profile use the HostProfileManager.CreateProfile method. To
    create a profile from an ESX host, specify a HostProfileHostBasedConfigSpec. To
    create a profile from a file, specify a HostProfileSerializedHostProfileSpec. *
    To create a subprofile for a particular host capability, use the
    HostProfileManager.CreateDefaultProfile method. After you create the default
    profile you can modify it and save it in the base profile. * To update an
    existing profile, use the HostProfile.UpdateHostProfile method. * To apply a
    host profile to an ESX host, use the ExecuteHostProfile method to generate
    configuration changes, then call the HostProfileManager.ApplyHostConfig_Task
    method to apply them.An individual host or a set of hosts may have some
    configuration settings that are different from the settings specified in the
    host profile. For example, the IP configuration for the host's virtual network
    adapters must be unique.* To verify host-specific data, use the parameter to
    the ExecuteHostProfile method. The Profile Engine will determine if you have
    specified all of the required parameters for the host configuration. If
    additional data is required, call the ExecuteHostProfile method again as many
    times as necessary to verify a complete set of parameters. * To apply host-
    specific data, use the parameter to the HostProfileManager.ApplyHostConfig_Task
    method.The Profile Engine saves host-specific data in an AnswerFile that is
    stored on the vCenter Server. The HostProfileManager provides several methods
    to manipulate answer files.You can create associations between hosts and
    profiles to support compliance checking. When you perform compliance checking,
    you can determine if a host configuration conforms to a host profile.* To
    create an association between a host and a profile, use the AssociateProfile
    method. The method adds the host to the HostProfile.entity[] list. * To
    retrieve the list of profiles associated with a host, use the
    HostProfileManager.FindAssociatedProfile method. * To check host compliance,
    use the CheckProfileCompliance_Task method. If you do not specify any hosts,
    the method will check the compliance of all hosts that are associated with the
    profile.You can also use the Profile Compliance Manager to check compliance by
    specifying profiles, entities (hosts), or both. See
    ProfileComplianceManager.CheckCompliance_Task.The vSphere architecture uses
    VMware profile plug-ins to define profile extensions. For information about
    using a plug-in to extend a host profile, see the VMware Technical Note .For
    access to host configuration data that is defined by plug-ins, use the
    ApplyProfile.policy[] and ApplyProfile.property[] lists. The HostApplyProfile
    and its subprofiles, which collectively define host configuration data, are
    derived from the ApplyProfile.* Policies store ESX configuration data in
    PolicyOption objects. * Profile property lists contain subprofiles defined by
    plug-ins. Subprofiles can be nested. * Subprofile lists are available as an
    extension to the base host profile
    (HostProfile.config.applyProfile.property[]). * Subprofile lists are available
    as extensions to the host subprofiles - for example, the network subprofile
    (HostApplyProfile.network.property[]).If you make changes to host profile data,
    later versions of profile plug-ins may not support the host configuration
    implied by the changes that you make. When a subsequent vSphere version becomes
    available, you must verify that the new version supports any previous
    configuration changes that you have made.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostProfile):
        super(HostProfile, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def referenceHost(self):
        '''Reference host in use for this host profile. To set this property, use the
        UpdateReferenceHost method. If you do not specify a host for validation
        (HostProfileCompleteConfigSpec.validatorHost), the Profile Engine uses the
        reference host to validate the profile.'''
        return self.update('referenceHost')

    
    
    def ExecuteHostProfile(self, host, deferredParam=None):
        '''Run the Profile Engine to determine the list of configuration changes needed
        for the specified host. The method generates configuration changes based on the
        host profile.Run the Profile Engine to determine the list of configuration
        changes needed for the specified host. The method generates configuration
        changes based on the host profile.
        
        :param host: Host on which to execute the profile. The host does not have to be associated with the profile.
        
        :param deferredParam: Additional configuration data to be applied to the host. This should contain all of the host-specific data, including data from from previous calls to the method.
        
        '''
        return self.delegate("ExecuteHostProfile")(host, deferredParam)
    
    def UpdateHostProfile(self, config):
        '''Update the <code>HostProfile</code> with the specified configuration data.
        
        :param config: Specification containing the new data.
        
        '''
        return self.delegate("UpdateHostProfile")(config)
    
    def UpdateReferenceHost(self, host=None):
        '''Sets the HostProfile.referenceHost property.
        
        :param host: Reference host to use. If unset, the referenceHost property is cleared.
        
        '''
        return self.delegate("UpdateReferenceHost")(host)