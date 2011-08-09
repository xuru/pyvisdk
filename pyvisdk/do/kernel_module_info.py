
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class KernelModuleInfo(DynamicData):
    '''Information about a kernel module.
    '''
    
    def __init__(self, bssSection, dataSection, enabled, filename, id, loaded, name, optionString, readOnlySection, textSection, useCount, version, writableSection):
        # MUST define these
        super(KernelModuleInfo, self).__init__()
    
        self.data['bssSection'] = bssSection
        self.data['dataSection'] = dataSection
        self.data['enabled'] = enabled
        self.data['filename'] = filename
        self.data['id'] = id
        self.data['loaded'] = loaded
        self.data['name'] = name
        self.data['optionString'] = optionString
        self.data['readOnlySection'] = readOnlySection
        self.data['textSection'] = textSection
        self.data['useCount'] = useCount
        self.data['version'] = version
        self.data['writableSection'] = writableSection
    
    
    @property
    def bssSection(self):
        '''BSS section information.
        '''
        return self.data['bssSection']

    @property
    def dataSection(self):
        '''Data section information.
        '''
        return self.data['dataSection']

    @property
    def enabled(self):
        '''Is the module enabled?
        '''
        return self.data['enabled']

    @property
    def filename(self):
        '''Module filename, without the path.
        '''
        return self.data['filename']

    @property
    def id(self):
        '''Module ID.
        '''
        return self.data['id']

    @property
    def loaded(self):
        '''Is the module loaded?
        '''
        return self.data['loaded']

    @property
    def name(self):
        '''Module name.
        '''
        return self.data['name']

    @property
    def optionString(self):
        '''Option string configured to be passed to the kernel module when loaded. Note that
        this is not necessarily the option string currently in use by the kernel
        module.
        '''
        return self.data['optionString']

    @property
    def readOnlySection(self):
        '''Read-only section information.
        '''
        return self.data['readOnlySection']

    @property
    def textSection(self):
        '''Text section information.
        '''
        return self.data['textSection']

    @property
    def useCount(self):
        '''Number of references to this module.
        '''
        return self.data['useCount']

    @property
    def version(self):
        '''Version string.
        '''
        return self.data['version']

    @property
    def writableSection(self):
        '''Writable section information.
        '''
        return self.data['writableSection']

