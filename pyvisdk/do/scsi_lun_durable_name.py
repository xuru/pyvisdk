
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ScsiLunDurableName(DynamicData):
    '''This data object type represents an SMI-S "Correlatable and Durable Name" which is
        an identifier for a logical unit number (LUN) that is generated using a
        common algorithm. The algorithm divides the identifier into multiple
        namespaces where each namespace uses a different set of properties of the
        LUN to generate the identifier. The namespace itself is encoded in the
        identifier.
    '''
    
    def __init__(self, data, namespace, namespaceId):
        # MUST define these
        super(ScsiLunDurableName, self).__init__()
    
        self.data['data'] = data
        self.data['namespace'] = namespace
        self.data['namespaceId'] = namespaceId
    
    
    @property
    def data(self):
        '''The variable length byte array containing the namespace-specific data. For a
        SCSI-3 compliant device this field is the descriptor header along with the
        payload for data obtained from page 83h, and is the payload for data
        obtained from page 80h of the Vital Product Data (VPD).
        '''
        return self.data['data']

    @property
    def namespace(self):
        '''The string describing the namespace used for the durable name.
        '''
        return self.data['namespace']

    @property
    def namespaceId(self):
        '''The byte used by the ESX Server product to represent the namespace.
        '''
        return self.data['namespaceId']

