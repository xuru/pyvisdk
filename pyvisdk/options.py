'''
Created on Jul 22, 2011

@author: eplaster

The information here is taken from the `Perl Toolkit Programming Guide`_ found on the `VMware APIs and SDKs Documentation page`_.

You can provide the required parameters to pyvisdk utility applications in several different ways:

    Pass parameters at the command line, using the required option flag followed by the value for the option:
    --optionname optionvalue

    Set as environment variables in a Linux profile; in the Environment properties dialog 
    of the Windows System control panel; or at the command-line, for the current session:
    set VI_SERVER=your_server_name

    Create a configuration file (a plaintext file) that contains variable names (for the parameters) 
    and settings. Variables for the built-in options are shown in Table 1, below. Any option with the 
    variable attribute set in the python script or application (.py) can also be specified 
    in a configuration file.
    VI_PROTOCOL=https
    VI_SERVER=prod01.vmware.com
    VI_SERVICEPATH=/sdk
    VI_USERNAME=Administrator
    VI_PASSWORD=*******

The pyvisdk runtime processes options set in the config file first, environment variables next, 
    and command-line entries last. As shown in the example above, you can use a combination of these 
    three approaches.

For example, assuming that most of your administrative chores take place through a central 
    VirtualCenter Management Server, you can create a configuration file for executing applications 
    and avoid repeatedly entering connection details. If you have multiple VirtualCenter Management 
    Server or ESX Server systems and you need to administer them individually, you can create multiple 
    configuration files using different names for each and then simply pass the --config option with 
    the appropriate filename when you run the applications.

Furthermore, each option can be set in multiple ways. Since command-line flags take precedence over 
    environment variables, and environment variables take precedence over settings in the configuration 
    file, you can easily over-ride any parameter when necessary.
    
Table 1: Built-in Parameters and Variables
==============  ===============  =====================================================================================
Parameter       Variable         Description
==============  ===============  =====================================================================================
config          VI_CONFIG        Specify non-default name or location for the pyvisdk configuration file. 
                                 Default name and location for Linux is ~/.visdkrc and for Windows is %HOME%\visdk.rc.
help            ~                Displays usage information about a script or application to standard output 
                                 (command console).
password        VI_PASSWORD      for the specified username. Sucessful authentication with username and 
                                 password returns a session object that can be saved and used for subsequent 
                                 connections using the same or different script. See sessionfile.
portnumber      VI_PORTNUMBER    Port used for server connection.
protocol        VI_PROTOCOL      Protocol used to connect to server. Default is HTTPS. If the server has been 
                                 configured for HTTP, set to HTTP.
server          VI_SERVER        ESX Server or VirtualCenter Management Server host to which you want the 
                                 application or script to connect. Default is localhost if none specified.
servicepath     VI_SERVICEPATH   Service path for server connection. Default is /sdk/webService.
sessionfile     VI_SESSIONFILE   Name of file containing the token saved from successful login. Alternative 
                                 to specifying username and password. Sessions time out after 30 minutes 
                                 of inactivity.
url             VI_URL           Complete URL for SDK connection. An alternative to specifying protocol, 
                                 server, and servicepath as individual connection parameters. For example, 
                                 perl app_name.pl --url https://myserver.mycompany.com/sdk --username root 
                                 --password mypassword
username        VI_USERNAME      User account that has privileges to connect to the server.
verbose         VI_VERBOSE       Increase loglevel. Use in conjunction with Util::trace subroutine to display 
                                 additional debugging information. By default, value of --verbose (loglevel) 
                                 is 0.
version         ~                Displays script version information, if available.


.. _Perl Toolkit Programming Guide: http://www.vmware.com/support/developer/viperltoolkit/doc/perl_toolkit_guide.html
.. _VMware APIs and SDKs Documentation page: http://www.vmware.com/support/pubs/sdk_pubs.html
'''
import os.path
from thirdparty.enum import Enum

vi_options = Enum(
    "VI_CONFIG", "VI_PASSWORD", "VI_PORTNUMBER","VI_PROTOCOL","VI_SERVER","VI_SERVICEPATH","VI_SESSIONFILE",
    "VI_URL","VI_USERNAME","VI_VERBOSE" )

class Options(object):
    '''
    Options for pyvisdk that will read in the .visdkrc files
    '''
    def __init__(self, **kw):
        '''
        Constructor
        '''
        # default filename...
        self.filename = os.path.expanduser("~/.visdkrc")
        
        self.vals = {
            str(vi_options.VI_SERVER): 'localhost',
            str(vi_options.VI_USERNAME): 'root',
            str(vi_options.VI_PASSWORD): 'password',
            str(vi_options.VI_URL): 'https://localhost/sdk',
        }
        if kw:
            self.update(kw)
        self.file_changed = False
        
    def __del__(self):
        if self.file_changed:
            self.save()
            
    def __getattr__(self, attr):
        return self.vals.get(attr, "")
        
    def __iter__(self):
        def do_iter():
            for key in self.vals:
                yield key, self[key]
        return do_iter()
    
    def __getitem__(self, attr):
        return self.__getattr__(attr)

    def __setitem__(self, attr, val):
        self.vals[attr] = str(val)
        self.file_changed = True
        
    def update(self, d):
        self.vals.update(d)
        
    def load(self, filename=None):
        """ Load saved options from a file.  The format is explained in the `Perl Toolkit Programming Guide, table 1`_ .
        Most variables are supported, where appropriate.
        
        Currently only VI_SERVER, VI_USERNAME, and VI_PASSWORD are supported.  More to follow...
        
        :param filename: `Optional` The filename to load.  Defaults to ~/.visdkrc.
        
        .. _Perl Toolkit Programming Guide, table 1: http://www.vmware.com/support/developer/viperltoolkit/doc/perl_toolkit_guide.html#table1
        """
        if filename:
            self.filename = os.path.expanduser(filename)
            self._read()
        else:
            if os.path.exists(self.filename):
                self._read()
    
    def load_env(self):
        for var in os.environ.items():
           if var in vi_options:
               self.vals[var] = os.environ[var]
                    
    def _read(self):
        for line in open(self.filename).readlines():
            if line[0] == '#':
                continue
            name, value = line.split("=")
            self.vals[name.strip()] = value.strip()
            
    def save(self):
        if self.file_changed:
            outfile = open(self.filename, 'w')
            for n,v in self.vals.items():
                outfile.writeline("%s=%s" % (n,v))
            outfile.close()
            
    def __str__(self):
        return str(self.vals)
        
        
        
        
        
        
        
            