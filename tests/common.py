'''
Created on Jul 6, 2011

@author: eplaster
'''
from os.path import expanduser, expandvars, exists

class TestOptions(dict):
    """
    Options for testing purposes.
    http://code.activestate.com/recipes/389916-example-setattr-getattr-overloading/
    """
    def __init__(self, indict=None, attribute=None):
        if indict is None:
            indict = {}
        # set any attributes here - before initialisation
        # these remain as normal attributes
        self.attribute = attribute
        dict.__init__(self, indict)
        self.__initialised = True
        # after initialisation, setting attributes is the same as setting an item

    def __getattr__(self, item):
        """Maps values to attributes.
        Only called if there *isn't* an attribute with this name
        """
        try:
            return self.__getitem__(item)
        except KeyError:
            raise AttributeError(item)

    def __setattr__(self, item, value):
        """Maps attributes to values.
        Only if we are initialised
        """
        if not self.__dict__.has_key('_TestOptions__initialised'):  # this test allows attributes to be set in the __init__ method
            return dict.__setattr__(self, item, value)
        elif item in self:
            dict.__setattr__(self, item, value)
        else:
            self.__setitem__(item, value)

class TestError(Exception):
    pass

class TestBase(object):
    '''
    Base class for all unit tests
    '''

    def __init__(self, config_path="~/.visdkrc.vcenter"):
        '''
        Constructor.  This loads up the test parameters or throws an exception if it doesn't exist.
        '''
        self.config = expanduser(expandvars(config_path)) 
        self.options = TestOptions()
        
        if exists(self.config):
            self._parse_config()
        else:
            raise TestError("Configuration file %s does not exist." % self.config)
        
    def _parse_config(self): 
        lines = open(self.config).readlines()
        for line in lines:
            name, value = line.split("=")
            
            if 'VI_SERVER' == name.strip():
                self.options.server = value.strip()
                
            elif 'VI_USERNAME' in name:
                self.options.username = value.strip()
                
            elif 'VI_PASSWORD' in name:
                self.options.password = value.strip()
                
                
                
                
                
                
                