
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ManagedEntity(ExtensibleManagedObject):
    '''Most Virtual Infrastructure managed object types extend this type.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.ManagedEntity):
        # MUST define these
        super(ManagedEntity, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def alarmActionsEnabled(self):
        '''Whether alarm actions are enabled for this entity. True if enabled; false
        otherwise.
        '''
        return self.update('alarmActionsEnabled')

    @property
    def configIssue(self):
        '''Current configuration issues that have been detected for this entity. Typically,
        these issues have already been logged as events. The entity stores these
        events as long as they are still current. The configStatus property
        provides an overall status based on these events.
        '''
        return self.update('configIssue')

    @property
    def configStatus(self):
        '''The configStatus indicates whether or not the system has detected a configuration
        issue involving this entity. For example, it might have detected a
        duplicate IP address or MAC address, or a host in a cluster might be out
        of compliance. The meanings of the configStatus values are: * red: A
        problem has been detected involving the entity. * yellow: A problem is
        about to occur or a transient condition has occurred (For example,
        reconfigure fail-over policy). * green: No configuration issues have been
        detected. * gray: The configuration status of the entity is not being
        monitored. A green status indicates only that a problem has not been
        detected; it is not a guarantee that the entity is problem-free.
        '''
        return self.update('configStatus')

    @property
    def customValue(self):
        '''Custom field values.
        '''
        return self.update('customValue')

    @property
    def declaredAlarmState(self):
        '''A set of alarm states for alarms that apply to this managed entity. The set
        includes alarms defined on this entity and alarms inherited from the
        parent entity, or from any ancestors in the inventory hierarchy.
        '''
        return self.update('declaredAlarmState')

    @property
    def disabledMethod(self):
        '''List of operations that are disabled, given the current runtime state of the
        entity. For example, a power-on operation always fails if a virtual
        machine is already powered on. This list can be used by clients to enable
        or disable operations in a graphical user interface.
        '''
        return self.update('disabledMethod')

    @property
    def effectiveRole(self):
        '''Access rights the current session has to this entity.
        '''
        return self.update('effectiveRole')

    @property
    def overallStatus(self):
        '''General health of this managed entity. The value combines the status of all the
        alarms attached to a managed entity.
        '''
        return self.update('overallStatus')

    @property
    def parent(self):
        '''Parent of this entity.
        '''
        return self.update('parent')

    @property
    def permission(self):
        '''List of permissions defined for this entity.
        '''
        return self.update('permission')

    @property
    def recentTask(self):
        '''The set of recent tasks operating on this managed entity. This is a subset of
        recentTask belong to this entity. A task in this list could be in one of
        the four states: pending, running, success or error.
        '''
        return self.update('recentTask')

    @property
    def tag(self):
        '''The set of tags associated with this managed entity. Experimental. Subject to
        change.
        '''
        return self.update('tag')

    @property
    def triggeredAlarmState(self):
        '''A set of alarm states for alarms triggered by this entity or by its descendants.
        '''
        return self.update('triggeredAlarmState')


    def Destroy_Task(self):
        '''Destroys this object, deleting its contents and removing it from its parent folder
        (if any).NOTE: The appropriate privilege must be held on the parent of the
        destroyed entity as well as the entity itself.This method can throw one of
        several exceptions. The exact set of exceptions depends on the kind of
        entity that is being removed. See comments for each entity for more
        information on destroy behavior.

        :rtype: Task 

        '''
        
        return self.delegate("Destroy_Task")()
        

    def Reload(self):
        '''Reload the entity state. Clients only need to call this method if they changed
        some external state that affects the service without using the Web service
        interface to perform the change. For example, hand-editing a virtual
        machine configuration file affects the configuration of the associated
        virtual machine but the service managing the virtual machine might not
        monitor the file for changes. In this case, after such an edit, a client
        would call "reload" on the associated virtual machine to ensure the
        service and its clients have current data for the virtual machine.
        '''
        
        return self.delegate("Reload")()
        

    def Rename_Task(self, newName):
        '''Renames this managed entity.Any % (percent) character used in this name parameter
        must be escaped, unless it is used to start an escape sequence. Clients
        may also escape any other characters in this name parameter.See name

        :param newName: See name


        :rtype: Task 

        '''
        
        return self.delegate("Rename_Task")(newName)
        
