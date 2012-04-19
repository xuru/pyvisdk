'''
Created on Mar 6, 2011

@author: eplaster
'''
from suds import MethodNotFound
import logging
import os.path
import suds
from suds.plugin import MessagePlugin

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

class MyPlugin(MessagePlugin):
    def addAttributeForValue(self, node):
        if node.name == 'value':
            node.set('xsi:type', 'xsd:string')
    def marshalled(self, context):
        context.envelope.walk(self.addAttributeForValue)

class SudsClientFactory(object):
    _client = None
    @classmethod
    def get_suds_client(cls):
        if cls._client is None:
            wsdl_dir = os.path.abspath(os.path.dirname(__file__))
            cls._client = suds.client.Client("file://" + os.path.join(wsdl_dir, 'wsdl', 'vimService.wsdl'), plugins=[MyPlugin()])
        return cls._client.clone()

class Client(object):
    '''
    The Client class acts as a proxy to the suds.client.Client class, in that it fixes the
    ManagedObjectReference objects and provides a more streamline interface specific to VISDK
    '''
    def __init__(self, server, timeout=90):
        '''
        Constructor
        '''
        url = "https://" + server + '/sdk'
        client = SudsClientFactory.get_suds_client()
        client.set_options(faults=True)
        client.set_options(location=url)
        client.set_options(timeout=timeout)
        self.service = client.service
        self.url = url
        self.client = client
        self.server = server

    #
    # proxying (special cases)
    #
    def __getattribute__(self, attr):
        service = super(Client, self).__getattribute__("service")

        # try the service
        try:
            _attr = getattr(service, attr)
            if _attr.__class__ == suds.client.Method:
                # we need to do something about getting to the right method here...
                return _attr
            else:
                return _attr
        except (AttributeError, MethodNotFound):
            # see if it's in the client object
            try:
                client = super(Client, self).__getattribute__("client")
                _attr = getattr(client, attr)
                return _attr
            except (AttributeError, MethodNotFound):
                # if it's a member of this class...
                return super(Client, self).__getattribute__(attr)
