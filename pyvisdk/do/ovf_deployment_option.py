
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OvfDeploymentOption(DynamicData):
    '''A deployment option as defined in the OVF specfication.This corresponds to the
        Configuration element of the DeploymentOptionSection in the specification.
    '''
    
    def __init__(self, description, key, label):
        # MUST define these
        super(OvfDeploymentOption, self).__init__()
    
        self.data['description'] = description
        self.data['key'] = key
        self.data['label'] = label
    
    
    @property
    def description(self):
        '''A localizable description for the deployment option.
        '''
        return self.data['description']

    @property
    def key(self):
        '''The key of the deployment option, corresponding to the ovf:id attribute in the OVF
        descriptor
        '''
        return self.data['key']

    @property
    def label(self):
        '''A localized label for the deployment option
        '''
        return self.data['label']

