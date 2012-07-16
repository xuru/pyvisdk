
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationSpecManager(BaseEntity):
    '''The CustomizationSpecManager managed object is used to manage customization
    specifications stored on the VirtualCenter server.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.CustomizationSpecManager):
        super(CustomizationSpecManager, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def encryptionKey(self):
        '''Gets a binary public encryption key that can be used to encrypt passwords in
        stored specifications.'''
        return self.update('encryptionKey')
    @property
    def info(self):
        '''Gets a list of information on available specifications.'''
        return self.update('info')

    
    
    def CheckCustomizationResources(self, guestOs):
        '''Validate that required resources are available on the server to customize a
        particular guest operating system. These would include sysprep for Windows and
        the debugfs and changefs volume editors for Linux guests.
        
        :param guestOs: Short name from the guest OS descriptor list describing the OS we intend to customize.
        
        '''
        return self.delegate("CheckCustomizationResources")(guestOs)
    
    def CreateCustomizationSpec(self, item):
        '''Creates a new specification.
        
        :param item: 
        
        '''
        return self.delegate("CreateCustomizationSpec")(item)
    
    def CustomizationSpecItemToXml(self, item):
        '''Converts a specification item to XML text
        
        :param item: 
        
        '''
        return self.delegate("CustomizationSpecItemToXml")(item)
    
    def DeleteCustomizationSpec(self, name):
        '''Deletes a specification.
        
        :param name: 
        
        '''
        return self.delegate("DeleteCustomizationSpec")(name)
    
    def DoesCustomizationSpecExist(self, name):
        '''Whether or not a specification exists.
        
        :param name: 
        
        '''
        return self.delegate("DoesCustomizationSpecExist")(name)
    
    def DuplicateCustomizationSpec(self, name, newName):
        '''Duplicates a specification.
        
        :param name: 
        
        :param newName: 
        
        '''
        return self.delegate("DuplicateCustomizationSpec")(name, newName)
    
    def GetCustomizationSpec(self, name):
        '''Obtains a specification for the given name.
        
        :param name: Unique name identifying the requested customization specification.
        
        '''
        return self.delegate("GetCustomizationSpec")(name)
    
    def OverwriteCustomizationSpec(self, item):
        '''Overwrites an existing specification, possibly after retrieving (by using
        'get') and editing it. If, based on the item's changeVersion value, the
        overwrite process detects that the specification has changed since its
        retrieval, then the API uses the SpecModified exception to warn the client that
        he might overwrite another client's change.
        
        :param item: 
        
        '''
        return self.delegate("OverwriteCustomizationSpec")(item)
    
    def RenameCustomizationSpec(self, name, newName):
        '''Renames a specification.
        
        :param name: 
        
        :param newName: 
        
        '''
        return self.delegate("RenameCustomizationSpec")(name, newName)
    
    def XmlToCustomizationSpecItem(self, specItemXml):
        '''Converts an XML string to a specification item
        
        :param specItemXml: 
        
        '''
        return self.delegate("XmlToCustomizationSpecItem")(specItemXml)