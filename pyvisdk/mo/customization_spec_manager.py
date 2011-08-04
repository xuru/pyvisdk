
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationSpecManager(BaseEntity):
    '''
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.CustomizationSpecManager):
        # MUST define these
        super(CustomizationSpecManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def encryptionKey(self):
        '''Gets a binary public encryption key that can be used to encrypt passwords in
        stored specifications.
        '''
        return self.update('encryptionKey')

    @property
    def info(self):
        '''Gets a list of information on available specifications.
        '''
        return self.update('info')


    def CheckCustomizationResources(self, guestOs):
        '''Validate that required resources are available on the server to customize a
        particular guest operating system. These would include sysprep for Windows
        and the debugfs and changefs volume editors for Linux guests.

        :param guestOs: Short name from the guest OS descriptor list describing the OS we intend to
        customize.

        '''
        
        return self.delegate("CheckCustomizationResources")(guestOs)
        

    def CreateCustomizationSpec(self):
        '''Creates a new specification.
        '''
        
        return self.delegate("CreateCustomizationSpec")()
        

    def CustomizationSpecItemToXml(self):
        '''Converts a specification item to XML text

        :rtype: xsd:string 

        '''
        
        return self.delegate("CustomizationSpecItemToXml")()
        

    def DeleteCustomizationSpec(self):
        '''Deletes a specification.
        '''
        
        return self.delegate("DeleteCustomizationSpec")()
        

    def DoesCustomizationSpecExist(self):
        '''Whether or not a specification exists.

        :rtype: xsd:boolean 

        '''
        
        return self.delegate("DoesCustomizationSpecExist")()
        

    def DuplicateCustomizationSpec(self):
        '''Duplicates a specification.
        '''
        
        return self.delegate("DuplicateCustomizationSpec")()
        

    def GetCustomizationSpec(self, name):
        '''Obtains a specification for the given name.

        :param name: Unique name identifying the requested customization specification.


        :rtype: CustomizationSpecItem 

        '''
        
        return self.delegate("GetCustomizationSpec")(name)
        

    def OverwriteCustomizationSpec(self):
        '''Overwrites an existing specification, possibly after retrieving (by using 'get')
        and editing it. If, based on the item's changeVersion value, the overwrite
        process detects that the specification has changed since its retrieval,
        then the API uses the SpecModified exception to warn the client that he
        might overwrite another client's change.
        '''
        
        return self.delegate("OverwriteCustomizationSpec")()
        

    def RenameCustomizationSpec(self):
        '''Renames a specification.
        '''
        
        return self.delegate("RenameCustomizationSpec")()
        

    def XmlToCustomizationSpecItem(self):
        '''Converts an XML string to a specification item

        :rtype: CustomizationSpecItem 

        '''
        
        return self.delegate("XmlToCustomizationSpecItem")()
        
