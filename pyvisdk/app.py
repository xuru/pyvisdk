'''
Created on Feb 25, 2011

@author: eplaster
'''
from optparse import OptionParser
import sys, logging
from options import Options

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

class PyvisdkApp(object):
    '''
    classdocs
    '''


    def __init__(self, usage=None):
        '''
        Constructor
        '''
        self.options = Options()
        if not usage:
            usage = "usage: %prog [options]"
        self.parser = OptionParser(usage=usage)
        self.parser.add_option("-s", "--server", dest="server", help="Server name or IP of the vSphere vCenter")
        self.parser.add_option("-u", "--username", dest="username", help="Username to log in with")
        self.parser.add_option("-p", "--password", dest="password", help="Password")
        self.parser.add_option("-c", "--config", dest="config", help="Configuration file that follows the convention outlined in vSphere Command-Line Interface Installation and Scripting Guide")
        
    def parse(self):
        (cmd_opts, _) = self.parser.parse_args(sys.argv[1:]) # IGNORE W0201
        
        keys = ["server","username","password","config"]
        
        for key in keys:
            self.options.update({key:eval("cmd_opts.%s" % key)})
        
        if cmd_opts.config:
            self.options.load(cmd_opts.config)
        else:
            self.options.load()
        
        # need to have server, username, and password or fail
        if not (self.options.username and self.options.password and self.options.server):
            raise RuntimeError("Must have the --config argument OR --username, --password and --server")

