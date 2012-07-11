
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ManagedEntity(ExtensibleManagedObject):
    '''ManagedEntity is an abstract base type for all managed objects present in the
    inventory tree. The base type provides common functionality for traversing the
    tree structure, as well as health monitoring and other basic functions.Most
    Virtual Infrastructure managed object types extend this type.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.ManagedEntity):
        super(ManagedEntity, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def alarmActionsEnabled(self):
        '''Whether alarm actions are enabled for this entity. True if enabled; false
        otherwise.'''
        return self.update('alarmActionsEnabled')
    @property
    def configIssue(self):
        '''Current configuration issues that have been detected for this entity.
        Typically, these issues have already been logged as events. The entity stores
        these events as long as they are still current. The configStatus property
        provides an overall status based on these events.'''
        return self.update('configIssue')
    @property
    def configStatus(self):
        '''The configStatus indicates whether or not the system has detected a
        configuration issue involving this entity. For example, it might have detected
        a duplicate IP address or MAC address, or a host in a cluster might be out of
        compliance. The meanings of the configStatus values are: * red: A problem has
        been detected involving the entity. * yellow: A problem is about to occur or a
        transient condition has occurred (For example, reconfigure fail-over policy). *
        green: No configuration issues have been detected. * gray: The configuration
        status of the entity is not being monitored. A green status indicates only that
        a problem has not been detected; it is not a guarantee that the entity is
        problem-free.'''
        return self.update('configStatus')
    @property
    def customValue(self):
        '''Custom field values.'''
        return self.update('customValue')
    @property
    def declaredAlarmState(self):
        '''A set of alarm states for alarms that apply to this managed entity. The set
        includes alarms defined on this entity and alarms inherited from the parent
        entity, or from any ancestors in the inventory hierarchy.'''
        return self.update('declaredAlarmState')
    @property
    def disabledMethod(self):
        '''List of operations that are disabled, given the current runtime state of the
        entity. For example, a power-on operation always fails if a virtual machine is
        already powered on. This list can be used by clients to enable or disable
        operations in a graphical user interface.'''
        return self.update('disabledMethod')
    @property
    def effectiveRole(self):
        '''Access rights the current session has to this entity.'''
        return self.update('effectiveRole')
    @property
    def name(self):
        '''Name of this entity, unique relative to its parent.'''
        return self.update('name')
    @property
    def overallStatus(self):
        '''General health of this managed entity. The overall status of the managed entity
        is computed as the worst status among its alarms and the configuration issues
        detected on the entity. The status is reported as one of the following values:
        * red: The entity has alarms or configuration issues with a red status. *
        yellow: The entity does not have alarms or configuration issues with a red
        status, and has at least one with a yellow status. * green: The entity does not
        have alarms or configuration issues with a red or yellow status, and has at
        least one with a green status. * gray: All of the entity's alarms have a gray
        status and the configuration status of the entity is not being monitored.'''
        return self.update('overallStatus')
    @property
    def parent(self):
        '''Parent of this entity.'''
        return self.update('parent')
    @property
    def permission(self):
        '''List of permissions defined for this entity.'''
        return self.update('permission')
    @property
    def recentTask(self):
        '''The set of recent tasks operating on this managed entity. This is a subset of
        recentTask belong to this entity. A task in this list could be in one of the
        four states: pending, running, success or error.'''
        return self.update('recentTask')
    @property
    def tag(self):
        '''The set of tags associated with this managed entity. Experimental. Subject to
        change.'''
        return self.update('tag')
    @property
    def triggeredAlarmState(self):
        '''A set of alarm states for alarms triggered by this entity or by its
        descendants.'''
        return self.update('triggeredAlarmState')

    
    
    def Destroy_Task(self):
        '''Destroys this object, deleting its contents and removing it from its parent
        folder (if any).Destroys this object, deleting its contents and removing it
        from its parent folder (if any).Destroys this object, deleting its contents and
        removing it from its parent folder (if any).
        
        '''
        return self.delegate("Destroy_Task")()
    
    def Reload(self):
        '''Reload the entity state. Clients only need to call this method if they changed
        some external state that affects the service without using the Web service
        interface to perform the change. For example, hand-editing a virtual machine
        configuration file affects the configuration of the associated virtual machine
        but the service managing the virtual machine might not monitor the file for
        changes. In this case, after such an edit, a client would call "reload" on the
        associated virtual machine to ensure the service and its clients have current
        data for the virtual machine.
        
        '''
        return self.delegate("Reload")()
    
    def Rename_Task(self, newName):
        '''Renames this managed entity.Renames this managed entity.Renames this managed
        entity.
        
        :param newName: See name
        
        '''
        return self.delegate("Rename_Task")(newName)