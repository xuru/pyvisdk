'''
Created on Jul 22, 2011

@author: eplaster
'''
import os.path

class Options(object):
    '''
    Options for pyvisdk that will read in the .visdkrc files
    '''
    _defaults = {
        'VI_SERVER': 'localhost',
        'VI_USERNAME': 'root',
        'VI_PASSWORD': 'password',
        'VI_URL': 'https://localhost/sdk',
    }
    
    def __init__(self, **kw):
        '''
        Constructor
        '''
        # default filename...
        self.filename = os.path.expanduser("~/.visdkrc.vcenter")
        
        self.def_vals = Options._defaults
        if kw:
            self.update(kw)
        self.changed = False
        
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
        self.def_vals[attr] = str(val)
        self.changed = True
        
    def update(self, d):
        self.def_vals.update(d)
        
    def load(self, filename=None):
        if not filename:
            if os.path.exists(self.filename):
                self._read()
            else:
                raise IOError("File not found: %s" % self.filename)
        else:
            self.filename = os.path.expanduser(filename)
            self._read()
    
    def _read(self):
        for line in open(self.filename).readlines():
            if line[0] == '#':
                continue
            name, value = line.split("=")
            self.def_vals[name.strip()] = value.strip()
            
    def save(self):
        if self.changed:
            outfile = open(self.filename, 'w')
            for n,v in self.def_vals.items():
                outfile.writeline("%s=%s" % (n,v))
            outfile.close()
            
    def __str__(self):
        return str(self.def_vals)
        
        
        
        
        
        
        
            