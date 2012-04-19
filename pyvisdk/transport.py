# http://stackoverflow.com/questions/1875052/using-paired-certificates-with-urllib2

# We need to login to vCenter server as an extension and this means that
# vCenter needs to be able to see our certificate.
# If we just connect to the vCenter server HTTPS
# reverse proxy at https://<vcenter>/sdk, the certificate is not forwarded to
# the vCenter server endpoint. We will get an HTTPS connection to the reverse
# proxy, but the connection from the reverse proxy to vCenter will be HTTP.
#
# To handle this we need to tunnel all our traffic through the proxy server
# when talking to vCenter.

import urllib2
import suds.client

class HTTPSClientAuthHandler(urllib2.HTTPSHandler):
    def __init__(self, key, cert):
        urllib2.HTTPSHandler.__init__(self)
        self.key = key
        self.cert = cert

    def https_open(self, req):
        # Rather than pass in a reference to a connection class, we pass in
        # a reference to a function which, for all intents and purposes,
        # will behave as a constructor
        return self.do_open(self.getConnection, req)

    def getConnection(self, host, timeout=300):
        from httplib import HTTPSConnection
        return HTTPSConnection(host, key_file=self.key, cert_file=self.cert)

class HttpAuthenticated(suds.client.HttpAuthenticated):
    def __init__(self, certfile=None, keyfile=None, proxy=None, **kwargs):
        suds.client.HttpAuthenticated.__init__(self, **kwargs)
        self._certfile = certfile
        self._keyfile = keyfile
        self._proxy = proxy

    def u2handlers(self):
        handlers = suds.client.HttpAuthenticated.u2handlers(self)
        if self._certfile and self._keyfile:
            handlers.append(urllib2.ProxyHandler({'https':self._proxy}))
            handlers.append(HTTPSClientAuthHandler(self._keyfile,
                                                   self._certfile))
        return handlers
