
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OvfParseDescriptorResult(DynamicData):
    '''
    '''
    
    def __init__(self, annotation, approximateDownloadSize, approximateFlatDeploymentSize, approximateSparseDeploymentSize, defaultDeploymentOption, defaultEntityName, deploymentOption, entityName, error, eula, ipAllocationScheme, ipProtocols, network, productInfo, property, virtualApp, warning):
        # MUST define these
        super(OvfParseDescriptorResult, self).__init__()
    
        self.data['annotation'] = annotation
        self.data['approximateDownloadSize'] = approximateDownloadSize
        self.data['approximateFlatDeploymentSize'] = approximateFlatDeploymentSize
        self.data['approximateSparseDeploymentSize'] = approximateSparseDeploymentSize
        self.data['defaultDeploymentOption'] = defaultDeploymentOption
        self.data['defaultEntityName'] = defaultEntityName
        self.data['deploymentOption'] = deploymentOption
        self.data['entityName'] = entityName
        self.data['error'] = error
        self.data['eula'] = eula
        self.data['ipAllocationScheme'] = ipAllocationScheme
        self.data['ipProtocols'] = ipProtocols
        self.data['network'] = network
        self.data['productInfo'] = productInfo
        self.data['property'] = property
        self.data['virtualApp'] = virtualApp
        self.data['warning'] = warning
    
    
    @property
    def annotation(self):
        '''The annotation info contained in the OVF
        '''
        return self.data['annotation']

    @property
    def approximateDownloadSize(self):
        '''The OVF Manager's best guess as to the total amount of data that must be
        transferred to download the entity.
        '''
        return self.data['approximateDownloadSize']

    @property
    def approximateFlatDeploymentSize(self):
        '''The OVF Manager's best guess as to the total amount of space required to deploy
        the entity if using flat disks.
        '''
        return self.data['approximateFlatDeploymentSize']

    @property
    def approximateSparseDeploymentSize(self):
        '''The OVF Manager's best guess as to the total amount of space required to deploy
        the entity using sparse disks.
        '''
        return self.data['approximateSparseDeploymentSize']

    @property
    def defaultDeploymentOption(self):
        '''The key of the default deployment option. Empty only if there are no deployment
        options.
        '''
        return self.data['defaultDeploymentOption']

    @property
    def defaultEntityName(self):
        '''The default name to use for the entity, if a product name is not specified. This
        is the ID of the OVF top-level entity, or taken from a ProductSection.
        '''
        return self.data['defaultEntityName']

    @property
    def deploymentOption(self):
        '''The list of possible deployment options.
        '''
        return self.data['deploymentOption']

    @property
    def entityName(self):
        '''A list of the child entities contained in this package and their location in the
        vApp hierarchy. Each entry is a (key,value) pair, where the key is the
        display name, and the value is a unique path identifier for the entity in
        the vApp. The path is constructed by appending the id of each entity of
        the path down to the entity, separated by slashes. For example, the path
        for a child of the root entity with id = "vm1", would simply be "vm1". If
        the vm is the child of a VirtualSystemCollection called "webTier", then
        the path would be "webTier/vm".
        '''
        return self.data['entityName']

    @property
    def error(self):
        '''Errors that happened during processing. Something will be wrong with the result.
        '''
        return self.data['error']

    @property
    def eula(self):
        '''The list of all EULAs contained in the OVF
        '''
        return self.data['eula']

    @property
    def ipAllocationScheme(self):
        '''The kind of IP allocation supported by the guest.
        '''
        return self.data['ipAllocationScheme']

    @property
    def ipProtocols(self):
        '''The IP protocols supported by the guest.
        '''
        return self.data['ipProtocols']

    @property
    def network(self):
        '''The list of networks required by the OVF
        '''
        return self.data['network']

    @property
    def productInfo(self):
        '''The product info contained in the OVF
        '''
        return self.data['productInfo']

    @property
    def property_(self):
        '''Metadata about the properties contained in the OVF
        '''
        return self.data['property']

    @property
    def virtualApp(self):
        '''True if the OVF contains a vApp (containing one or more vApps and/or virtual
        machines), as opposed to a single virtual machine.
        '''
        return self.data['virtualApp']

    @property
    def warning(self):
        '''Non-fatal warnings from the processing. The result will be valid, but the user may
        choose to reject it based on these warnings.
        '''
        return self.data['warning']

