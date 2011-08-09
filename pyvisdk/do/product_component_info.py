
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProductComponentInfo(DynamicData):
    '''ProductComponentInfo data object type describes installed components. Product
        component is defined as a software module that is released and versioned
        independently but has dependency relationship with other products. If one
        product, for usability or any other reason, bundles other products,
        ProductComponentInfo type may be used to describe installed components.
        For example, ESX product may bundle VI Client in its releases.
    '''
    
    def __init__(self, id, name, release, version):
        # MUST define these
        super(ProductComponentInfo, self).__init__()
    
        self.data['id'] = id
        self.data['name'] = name
        self.data['release'] = release
        self.data['version'] = version
    
    
    @property
    def id(self):
        '''Opaque identifier that is unique for this product component
        '''
        return self.data['id']

    @property
    def name(self):
        '''Canonical name of product component
        '''
        return self.data['name']

    @property
    def release(self):
        '''Release property is a number which increments with each new release of product.
        Product release may not rev version but release number is always
        incremented.
        '''
        return self.data['release']

    @property
    def version(self):
        '''Version of product component
        '''
        return self.data['version']

