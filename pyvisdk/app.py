'''
Created on Feb 25, 2011

@author: eplaster
'''
from optparse import OptionParser
from pyvisdk import Vim
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
        self.parser.add_option("-c", "--config", dest="VI_CONFIG", help="Specify non-default name or location for the VI Perl Toolkit configuration file. Default name and location for Linux is ~/.visdkrc and for Windows is %HOME%\visdk.rc.")
        self.parser.add_option("-p", "--password", dest="VI_PASSWORD", help="Password for the specified username. Sucessful authentication with username and password returns a session object that can be saved and used for subsequent connections using the same or different script. See sessionfile.")
        self.parser.add_option("--portnumber", dest="VI_PORTNUMBER", help="Port used for server connection.")
        self.parser.add_option("--protocol", dest="VI_PROTOCOL", help="Protocol used to connect to server. Default is HTTPS. If the server has been configured for HTTP, set to HTTP. ")
        self.parser.add_option("-s", "--server", dest="VI_SERVER", help="ESX Server or VirtualCenter Management Server host to which you want the application or script to connect. Default is localhost if none specified.")
        self.parser.add_option("--servicepath", dest="VI_SERVICEPATH", help="Service path for server connection. Default is /sdk/webService.")
        self.parser.add_option("--sessionfile", dest="VI_SESSIONFILE", help="Name of file containing the token saved from successful login. Alternative to specifying username and password. Sessions time out after 30 minutes of inactivity.")
        self.parser.add_option("--url", dest="VI_URL", help="Complete URL for SDK connection. An alternative to specifying protocol, server, and servicepath as individual connection parameters. For example, python app_name.py --url https://myserver.mycompany.com/sdk --username root --password mypassword")
        self.parser.add_option("-u", "--username", dest="VI_USERNAME", help="User account that has privileges to connect to the server.")
        self.parser.add_option("-v", "--verbose", dest="VI_VERBOSE", help="Increase loglevel. Use in conjunction with Util::trace subroutine to display additional debugging information. By default, value of --verbose (loglevel) is 0. ")
        self.parser.add_option("-V", "--version", help="Displays script version information, if available.")
        
    def parse(self):
        (cmd_opts, _) = self.parser.parse_args(sys.argv[1:]) # IGNORE W0201
        
        # load up options from the visdkrc file if there is any
        if cmd_opts.VI_CONFIG:
            self.options.load(cmd_opts.VI_CONFIG)
        else:
            self.options.load()
            
        # also, update options with environmental values, overriding those in the configuration file.
        self.options.load_env()
            
        # update our options with what was entered on the command line.  This will override previously
        # entered options
        for name, value in cmd_opts.__dict__.items():
            if value:
                self.options.update({name:value})
        
        # need to have server, username, and password or fail
        if not (self.options.VI_USERNAME and self.options.VI_PASSWORD and self.options.VI_SERVER):
            raise RuntimeError("Must specify --username, --password and --server")


    def connect(self):
        self.vim = Vim(self.options.VI_SERVER)
        self.vim.login(self.options.VI_USERNAME, self.options.VI_PASSWORD)
    
    def disconnect(self):
        self.vim.logout()