'''
Created on Feb 25, 2011

@author: eplaster
'''
from optparse import OptionParser
import sys, logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

class PyvisdkApp(object):
    '''
    classdocs
    '''


    def __init__(self, usage):
        '''
        Constructor
        '''
        if not usage:
            usage = "usage: %prog [options]"
        self.parser = OptionParser(usage=usage)
        self.parser.add_option("-s", "--server", dest="server", help="Server name or IP of the vSphere vCenter")
        self.parser.add_option("-u", "--username", dest="username", help="Username to log in with")
        self.parser.add_option("-p", "--password", dest="password", help="Password")
        self.parser.add_option("-c", "--config", dest="config", help="Configuration file that follows the convention outlined in vSphere Command-Line Interface Installation and Scripting Guide")
        
    def parse(self):
        (self.options, args) = self.parser.parse_args(sys.argv[1:])
        if self.options.config:
            self._parse_config()
        else:
            # need to have server, username, and password or fail
            if not (self.options.username and self.options.password and self.options.server):
                raise RuntimeError("Must have the --config argument OR --username, --password and --server")

    def _parse_config(self): 
        lines = open(self.options.config).readlines()
        for line in lines:
            name, value = line.split("=")
            if 'VI_SERVER' in name:
                self.options.server = value.strip()
            elif 'VI_USERNAME' in name:
                self.options.username = value.strip()
            elif 'VI_PASSWORD' in name:
                self.options.password = value.strip()
            else:
                log.warning("[WARN] unknown option: " + line)