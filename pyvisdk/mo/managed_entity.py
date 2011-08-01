
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ManagedEntity(ExtensibleManagedObject):
    '''ManagedEntity is an abstract base type for all managed objects present in the
        inventory tree. The base type provides common functionality for traversing
        the tree structure, as well as health monitoring and other basic
        functions.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.ManagedEntity):
        # MUST define these
        super(ManagedEntity, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def alarmActionsEnabled(self):
        '''
        Whether alarm actions are enabled for this entity. True if enabled; false
        otherwise.
        '''
        return self.update('alarmActionsEnabled')

    @property
    def disabledMethod(self):
        '''
        List of operations that are disabled, given the current runtime state of the
        entity. For example, a power-on operation always fails if a virtual
        machine is already powered on. This list can be used by clients to enable
        or disable operations in a graphical user interface.
        '''
        return self.update('disabledMethod')

    @property
    def effectiveRole(self):
        '''
        Access rights the current session has to this entity.
        '''
        return self.update('effectiveRole')

    @property
    def name(self):
        '''
        Name of this entity, unique relative to its parent.
        '''
        return self.update('name')


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
        

    def Destroy_Task(self):
        '''Destroys this object, deleting its contents and removing it from its parent folder
        (if any).NOTE: The appropriate privilege must be held on the parent of the
        destroyed entity as well as the entity itself.This method can throw one of
        several exceptions. The exact set of exceptions depends on the kind of
        entity that is being removed. See comments for each entity for more
        information on destroy behavior.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("Destroy_Task")()
        

    def Rename_Task(self):
        '''Renames this managed entity.Any % (percent) character used in this name parameter
        must be escaped, unless it is used to start an escape sequence. Clients
        may also escape any other characters in this name parameter.See name

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("Rename_Task")()
        
