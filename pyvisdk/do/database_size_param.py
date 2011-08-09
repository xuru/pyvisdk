
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DatabaseSizeParam(DynamicData):
    '''DatabaseSizeParam contains information about a sample inventory. Using this
        information, database size requirements for that sample inventory can be
        computed. Depending on the accuracy of estimate desired, users can choose
        to specify the number of different types of managed entities. The numHosts
        and numVirtualMachines are the only two required fields. Rest are all
        optional fields filled up by Virtual Center based on some heuristics.
        These parameters need not represent a real inventory. The user can use
        these parameters to estimate the database size required by a hypothetical
        VirtualCenter setup.
    '''
    
    def __init__(self, inventoryDesc, perfStatsDesc):
        # MUST define these
        super(DatabaseSizeParam, self).__init__()
    
        self.data['inventoryDesc'] = inventoryDesc
        self.data['perfStatsDesc'] = perfStatsDesc
    
    
    @property
    def inventoryDesc(self):
        '''Object to capture inventory description
        '''
        return self.data['inventoryDesc']

    @property
    def perfStatsDesc(self):
        '''Object to capture performance statistics related parameters
        '''
        return self.data['perfStatsDesc']

