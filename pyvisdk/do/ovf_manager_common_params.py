
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OvfManagerCommonParams(DynamicData):
    '''A common super-class for basic OVF descriptor parameters
    '''
    
    def __init__(self, deploymentOption, locale, msgBundle):
        # MUST define these
        super(OvfManagerCommonParams, self).__init__()
    
        self.data['deploymentOption'] = deploymentOption
        self.data['locale'] = locale
        self.data['msgBundle'] = msgBundle
    
    
    @property
    def deploymentOption(self):
        '''The key of the chosen deployment option. If empty, the default option is chosen.
        The list of possible deployment options is returned in the result of
        parseDescriptor.
        '''
        return self.data['deploymentOption']

    @property
    def locale(self):
        '''The locale-identifier to choose from the descriptor. If empty, the default locale
        on the server is used.
        '''
        return self.data['locale']

    @property
    def msgBundle(self):
        '''An optional set of localization strings to be used. The server will use these
        message strings to localize information in the result and in error and
        warning messages.
        '''
        return self.data['msgBundle']

