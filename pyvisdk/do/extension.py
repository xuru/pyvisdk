
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class Extension(DynamicData):
    '''This data object type contains all information about an extension. An extension
        may contain zero or more server interfaces and zero or more clients.
    '''
    
    def __init__(self, client, company, description, eventList, faultList, healthInfo, key, lastHeartbeatTime, privilegeList, resourceList, server, subjectName, taskList, type, version):
        # MUST define these
        super(Extension, self).__init__()
    
        self.data['client'] = client
        self.data['company'] = company
        self.data['description'] = description
        self.data['eventList'] = eventList
        self.data['faultList'] = faultList
        self.data['healthInfo'] = healthInfo
        self.data['key'] = key
        self.data['lastHeartbeatTime'] = lastHeartbeatTime
        self.data['privilegeList'] = privilegeList
        self.data['resourceList'] = resourceList
        self.data['server'] = server
        self.data['subjectName'] = subjectName
        self.data['taskList'] = taskList
        self.data['type'] = type
        self.data['version'] = version
    
    
    @property
    def client(self):
        '''Clients for this extension.
        '''
        return self.data['client']

    @property
    def company(self):
        '''Company information.
        '''
        return self.data['company']

    @property
    def description(self):
        '''Description of extension.
        '''
        return self.data['description']

    @property
    def eventList(self):
        '''Definitions of events defined by this extension.
        '''
        return self.data['eventList']

    @property
    def faultList(self):
        '''Definitions of faults defined by this extension.
        '''
        return self.data['faultList']

    @property
    def healthInfo(self):
        '''Health specification provided by this extension.
        '''
        return self.data['healthInfo']

    @property
    def key(self):
        '''Extension key. Should follow java package naming conventions for uniqueness (e.g.
        "com.example.management").
        '''
        return self.data['key']

    @property
    def lastHeartbeatTime(self):
        '''Last extension heartbeat time.
        '''
        return self.data['lastHeartbeatTime']

    @property
    def privilegeList(self):
        '''Definitions privileges defined by this extension.
        '''
        return self.data['privilegeList']

    @property
    def resourceList(self):
        '''Resource data for all locales
        '''
        return self.data['resourceList']

    @property
    def server(self):
        '''Servers for this extension.
        '''
        return self.data['server']

    @property
    def subjectName(self):
        '''Subject name from client certificate.
        '''
        return self.data['subjectName']

    @property
    def taskList(self):
        '''Definitions of tasks defined by this extension.
        '''
        return self.data['taskList']

    @property
    def type(self):
        '''Type of extension (example may include CP-DVS, NUOVA-DVS, etc.).
        '''
        return self.data['type']

    @property
    def version(self):
        '''Extension version number as a dot-separated string. For example, "1.0.0"
        '''
        return self.data['version']

