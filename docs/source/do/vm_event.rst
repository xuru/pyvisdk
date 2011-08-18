# -*- coding: ascii -*-

========================================
VmEvent
========================================


.. describe:: Extended by
    
    CustomizationEvent, DrsRuleComplianceEvent, DrsRuleViolationEvent,
    MigrationEvent, NoMaintenanceModeDrsRecommendationForVM,
    NotEnoughResourcesToStartVmEvent, VmAcquiredMksTicketEvent,
    VmAcquiredTicketEvent, VmAutoRenameEvent, VmBeingCreatedEvent,
    VmBeingDeployedEvent, VmBeingHotMigratedEvent, VmBeingMigratedEvent,
    VmCloneEvent, VmConfigMissingEvent, VmConnectedEvent, VmCreatedEvent,
    VmDasBeingResetEvent, VmDasResetFailedEvent, VmDasUpdateErrorEvent,
    VmDasUpdateOkEvent, VmDateRolledBackEvent, VmDeployedEvent, VmDeployFailedEvent,
    VmDisconnectedEvent, VmDiscoveredEvent, VmDiskFailedEvent, VmEmigratingEvent,
    VmEndRecordingEvent, VmEndReplayingEvent, VmFailedMigrateEvent,
    VmFailedRelayoutEvent, VmFailedRelayoutOnVmfs2DatastoreEvent,
    VmFailedStartingSecondaryEvent, VmFailedToPowerOffEvent, VmFailedToPowerOnEvent,
    VmFailedToRebootGuestEvent, VmFailedToResetEvent, VmFailedToShutdownGuestEvent,
    VmFailedToStandbyGuestEvent, VmFailedToSuspendEvent,
    VmFailedUpdatingSecondaryConfig, VmFailoverFailed,
    VmFaultToleranceStateChangedEvent, VmFaultToleranceTurnedOffEvent,
    VmFaultToleranceVmTerminatedEvent, VmGuestRebootEvent, VmGuestShutdownEvent,
    VmGuestStandbyEvent, VmInstanceUuidAssignedEvent, VmInstanceUuidChangedEvent,
    VmInstanceUuidConflictEvent, VmMacAssignedEvent, VmMacChangedEvent,
    VmMacConflictEvent, VmMaxFTRestartCountReached, VmMaxRestartCountReached,
    VmMessageErrorEvent, VmMessageEvent, VmMessageWarningEvent, VmMigratedEvent,
    VmNoCompatibleHostForSecondaryEvent, VmNoNetworkAccessEvent, VmOrphanedEvent,
    VmPoweredOffEvent, VmPoweredOnEvent, VmPoweringOnWithCustomizedDVPortEvent,
    VmPrimaryFailoverEvent, VmReconfiguredEvent, VmRegisteredEvent,
    VmRelayoutSuccessfulEvent, VmRelayoutUpToDateEvent, VmReloadFromPathEvent,
    VmReloadFromPathFailedEvent, VmRelocateSpecEvent, VmRemoteConsoleConnectedEvent,
    VmRemoteConsoleDisconnectedEvent, VmRemovedEvent, VmRenamedEvent,
    VmResettingEvent, VmResourcePoolMovedEvent, VmResourceReallocatedEvent,
    VmResumingEvent, VmSecondaryAddedEvent, VmSecondaryDisabledBySystemEvent,
    VmSecondaryDisabledEvent, VmSecondaryEnabledEvent, VmSecondaryStartedEvent,
    VmStartingEvent, VmStartingSecondaryEvent, VmStartRecordingEvent,
    VmStartReplayingEvent, VmStaticMacConflictEvent, VmStoppingEvent,
    VmSuspendedEvent, VmSuspendingEvent, VmTimedoutStartingSecondaryEvent,
    VmUpgradeCompleteEvent, VmUpgradeFailedEvent, VmUpgradingEvent,
    VmUuidAssignedEvent, VmUuidChangedEvent, VmUuidConflictEvent,
    VmWwnAssignedEvent, VmWwnChangedEvent, VmWwnConflictEvent
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.event.Event`
    
.. autoclass:: pyvisdk.do.vm_event.VmEvent
    :members:
    :inherited-members: