# -*- coding: ascii -*-

========================================
HostEvent
========================================


.. describe:: Extended by
    
    AccountCreatedEvent, AccountRemovedEvent, AccountUpdatedEvent,
    AdminPasswordNotChangedEvent, CanceledHostOperationEvent,
    DatastoreDiscoveredEvent, DatastorePrincipalConfigured,
    DatastoreRemovedOnHostEvent, DatastoreRenamedOnHostEvent,
    DrsResourceConfigureFailedEvent, DrsResourceConfigureSyncedEvent,
    DuplicateIpDetectedEvent, EnteredMaintenanceModeEvent, EnteredStandbyModeEvent,
    EnteringMaintenanceModeEvent, EnteringStandbyModeEvent, ExitedStandbyModeEvent,
    ExitingStandbyModeEvent, ExitMaintenanceModeEvent, ExitStandbyModeFailedEvent,
    GhostDvsProxySwitchDetectedEvent, GhostDvsProxySwitchRemovedEvent,
    HostAddedEvent, HostAddFailedEvent, HostAdminDisableEvent, HostAdminEnableEvent,
    HostCnxFailedAccountFailedEvent, HostCnxFailedAlreadyManagedEvent,
    HostCnxFailedBadCcagentEvent, HostCnxFailedBadUsernameEvent,
    HostCnxFailedBadVersionEvent, HostCnxFailedCcagentUpgradeEvent,
    HostCnxFailedEvent, HostCnxFailedNetworkErrorEvent, HostCnxFailedNoAccessEvent,
    HostCnxFailedNoConnectionEvent, HostCnxFailedNoLicenseEvent,
    HostCnxFailedNotFoundEvent, HostCnxFailedTimeoutEvent,
    HostComplianceCheckedEvent, HostCompliantEvent, HostConfigAppliedEvent,
    HostConnectedEvent, HostConnectionLostEvent, HostDasDisabledEvent,
    HostDasDisablingEvent, HostDasEnabledEvent, HostDasEnablingEvent,
    HostDasErrorEvent, HostDasEvent, HostDasOkEvent, HostDisconnectedEvent,
    HostEnableAdminFailedEvent, HostGetShortNameFailedEvent, HostIpChangedEvent,
    HostIpInconsistentEvent, HostIpToShortNameFailedEvent, HostNonCompliantEvent,
    HostProfileAppliedEvent, HostReconnectionFailedEvent, HostRemovedEvent,
    HostShortNameToIpFailedEvent, HostShutdownEvent, HostSyncFailedEvent,
    HostUpgradeFailedEvent, HostUserWorldSwapNotEnabledEvent,
    HostVnicConnectedToCustomizedDVPortEvent, HostWwnChangedEvent,
    HostWwnConflictEvent, IScsiBootFailureEvent, LocalDatastoreCreatedEvent,
    LocalTSMEnabledEvent, NASDatastoreCreatedEvent, NoDatastoresConfiguredEvent,
    RemoteTSMEnabledEvent, TimedOutHostOperationEvent,
    UpdatedAgentBeingRestartedEvent, UserAssignedToGroup, UserPasswordChanged,
    UserUnassignedFromGroup, VcAgentUninstalledEvent, VcAgentUninstallFailedEvent,
    VcAgentUpgradedEvent, VcAgentUpgradeFailedEvent, VimAccountPasswordChangedEvent,
    VMFSDatastoreCreatedEvent, VMFSDatastoreExpandedEvent,
    VMFSDatastoreExtendedEvent
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.event.Event`
    
.. autoclass:: pyvisdk.do.host_event.HostEvent
    :members:
    :inherited-members: