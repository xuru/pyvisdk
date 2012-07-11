'''
Created on Jul 6, 2011

@author: eplaster
'''
from os.path import expanduser, expandvars, exists
import unittest

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

def get_options(config_path="~/.visdkrc.vcenter"):
    '''
    Returns an options object, populated from name value pairs in the .visdkrc files
    '''

    config = expanduser(expandvars(config_path))
    options = TestOptions()

    if exists(config):
        lines = open(config).readlines()
        for line in lines:
            name, value = line.split("=")

            if 'VI_SERVER' == name.strip():
                options.server = value.strip()

            elif 'VI_USERNAME' in name:
                options.username = value.strip()

            elif 'VI_PASSWORD' in name:
                options.password = value.strip()

            elif 'VI_EXTENSION_CERTIFICATE' in name:
                options.certfile = value.strip()

            elif 'VI_EXTENSION_PRIVATEKEY' in name:
                options.keyfile = value.strip()

            elif 'VI_EXTENSION_KEY' in name:
                options.extension_key = value.strip()
    else:
        raise TestError("Configuration file %s does not exist." % config)
    return options





