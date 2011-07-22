'''
Created on Jul 22, 2011

@author: eplaster
'''
import os.path, exceptions
from ConfigParser import ConfigParser, DEFAULTSECT

class Options(ConfigParser):
    '''
    Options for pyvisdk that will read in the .visdkrc files
    '''
    _defaults = {
        'VI_SERVER': 'localhost',
        'VI_USERNAME': 'root',
        'VI_PASSWORD': 'password',
        'VI_URL': 'https://localhost/sdk',
    }
    
    def __init__(self, defaults = None):
        '''
        Constructor
        '''
        # default filename...
        self.filename = os.path.expanduser("~/.visdkrc.vcenter")
        
        self.def_vals = Options._defaults
        if defaults:
            self.def_vals = defaults
        self.changed = False
        ConfigParser.__init__(self)
        
    def __del__(self):
        if self.changed:
            self.save()
            
    def __getattr__(self, attr):
        return self.def_vals.get(attr, "")
        
    def __iter__(self):
        def do_iter():
            for key in self.def_vals:
                yield key, self[key]
        return do_iter()
    
    def __getitem__(self, attr):
        return self.__getattr__(attr)

    def __setitem__(self, attr, val):
        self.set(DEFAULTSECT, attr, str(val))
        self.changed = True
    
    def load(self, filename=None):
        if not filename:
            if os.path.exists(self.filename):
                self.read(self.filename)
            else:
                raise exceptions.IOError("File not found: %s" % self.filename)
        else:
            self.filename = filename
            self.read(self.filename)
            
    def save(self):
        if self.changed:
            outfile = open(self.filename, 'w')
            self.write(outfile)
            outfile.close()
            
            