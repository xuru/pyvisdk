
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationSpecManager(BaseEntity):
    '''The CustomizationSpecManager managed object is used to manage customization
        specifications stored on the VirtualCenter server.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.CustomizationSpecManager):
        # MUST define these
        super(CustomizationSpecManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def encryptionKey(self):
        '''
        Gets a binary public encryption key that can be used to encrypt passwords in
        stored specifications.
        '''
        return self.update('encryptionKey')


    def CustomizationSpecItemToXml(self, item):
        '''Converts a specification item to XML text

        :param item: 


        :rtype: xsd:string 

        '''
        
        return self.delegate("CustomizationSpecItemToXml")(item)
        

    def XmlToCustomizationSpecItem(self, specItemXml):
        '''Converts an XML string to a specification item

        :param specItemXml: 


        :rtype: CustomizationSpecItem 

        '''
        
        return self.delegate("XmlToCustomizationSpecItem")(specItemXml)
        

    def OverwriteCustomizationSpec(self, item):
        '''Overwrites an existing specification, possibly after retrieving (by using 'get')
        and editing it. If, based on the item's changeVersion value, the overwrite
        process detects that the specification has changed since its retrieval,
        then the API uses the SpecModified exception to warn the client that he
        might overwrite another client's change.

        :param item: 

        '''
        
        return self.delegate("OverwriteCustomizationSpec")(item)
        

    def DuplicateCustomizationSpec(self, newName, name):
        '''Duplicates a specification.

        :param newName: 

        :param name: 

        '''
        
        return self.delegate("DuplicateCustomizationSpec")(newName,name)
        

    def DeleteCustomizationSpec(self, name):
        '''Deletes a specification.

        :param name: 

        '''
        
        return self.delegate("DeleteCustomizationSpec")(name)
        

    def RenameCustomizationSpec(self, newName, name):
        '''Renames a specification.

        :param newName: 

        :param name: 

        '''
        
        return self.delegate("RenameCustomizationSpec")(newName,name)
        

    def CheckCustomizationResources(self, guestOs):
        '''Validate that required resources are available on the server to customize a
        particular guest operating system. These would include sysprep for Windows
        and the debugfs and changefs volume editors for Linux guests.

        :param guestOs: Short name from the guest OS descriptor list describing the OS we intend to customize.

        '''
        
        return self.delegate("CheckCustomizationResources")(guestOs)
        

    def GetCustomizationSpec(self, name):
        '''Obtains a specification for the given name.

        :param name: Unique name identifying the requested customization specification.


        :rtype: CustomizationSpecItem 

        '''
        
        return self.delegate("GetCustomizationSpec")(name)
        

    def DoesCustomizationSpecExist(self, name):
        '''Whether or not a specification exists.

        :param name: 


        :rtype: xsd:boolean 

        '''
        
        return self.delegate("DoesCustomizationSpecExist")(name)
        

    def CreateCustomizationSpec(self, item):
        '''Creates a new specification.

        :param item: 

        '''
        
        return self.delegate("CreateCustomizationSpec")(item)
        
