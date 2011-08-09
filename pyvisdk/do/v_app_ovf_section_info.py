
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VAppOvfSectionInfo(DynamicData):
    '''The OvfSection encapsulates uninterpreted meta-data sections in an OVF descriptor.
        When an OVF package is imported, non-required / non-interpreted sections
        will be stored as OvfSection object. During the creation of an OVF
        package, these sections will be placed in the OVF descriptor.
    '''
    
    def __init__(self, atEnvelopeLevel, contents, key, namespace, type):
        # MUST define these
        super(VAppOvfSectionInfo, self).__init__()
    
        self.data['atEnvelopeLevel'] = atEnvelopeLevel
        self.data['contents'] = contents
        self.data['key'] = key
        self.data['namespace'] = namespace
        self.data['type'] = type
    
    
    @property
    def atEnvelopeLevel(self):
        '''Whether this is a global envelope section
        '''
        return self.data['atEnvelopeLevel']

    @property
    def contents(self):
        '''The XML fragment including the top-level <Section...> element. The fragment is
        self-contained will all required namespace definitions.
        '''
        return self.data['contents']

    @property
    def key(self):
        '''A unique key to identify a section.
        '''
        return self.data['key']

    @property
    def namespace(self):
        '''The namespace for the value in xsi:type attribute.
        '''
        return self.data['namespace']

    @property
    def type(self):
        '''The value of the xsi:type attribute not including the namespace prefix.
        '''
        return self.data['type']

