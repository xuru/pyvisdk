'''
Created on Jul 6, 2011

@author: eplaster
'''
import unittest
from pyvisdk import Vim
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.datacenter import Datacenter
from pyvisdk.mo.folder import Folder
from tests.common import get_options


class TestFolder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.options = get_options()
        cls.vim = Vim(cls.options.server)
        cls.vim.login(cls.options.username, cls.options.password)
        cls.datacenter = cls.vim.getDatacenters()[0]

    @classmethod
    def tearDownClass(cls):
        cls.vim.logout()

    def testFolder(self):
        folder = self.datacenter.vmFolder
        
        self.assertIsNotNone(folder, "Couldn't get folder: %s" % folder.name)
        self.assertEqual(folder.type, ManagedObjectTypes.Folder, "Folder's type isn't Folder...")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testFolder']
    unittest.main()