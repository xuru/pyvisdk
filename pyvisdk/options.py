import os.path
from pyvisdk.thirdparty import Enum

vi_options = Enum(
    "VI_CONFIG", "VI_PASSWORD", "VI_PORTNUMBER", "VI_PROTOCOL", "VI_SERVER", "VI_SERVICEPATH", "VI_SESSIONFILE",
    "VI_URL", "VI_USERNAME", "VI_VERBOSE",
    "VI_EXTENSION_CERTIFICATE", "VI_EXTENSION_PRIVATEKEY", "VI_EXTENSION_KEY")

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
            for n, v in self.vals.items():
                outfile.writeline("%s=%s" % (n, v))
            outfile.close()

    def __str__(self):
        return str(self.vals)







