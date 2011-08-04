'''
Created on Jul 6, 2011

@author: eplaster
'''
import unittest, types
from pyvisdk import Vim
from pyvisdk.mo.datacenter import Datacenter
from pyvisdk.mo.datastore import Datastore
from pyvisdk.mo.folder import Folder
from tests.common import get_options

class TestDatacenter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.options = get_options()
        cls.vim = Vim(cls.options.server)
        cls.vim.login(cls.options.username, cls.options.password)

    @classmethod
    def tearDownClass(cls):
        cls.vim.logout()

    def testDatacenters(self):
        dcs = self.vim.getDatacenters()
        self.assertGreaterEqual(len(dcs), 1, "vcenter has no datastores")
        
    def testDatacenter(self):
        dcs = self.vim.getDatacenters()
        self.assertGreaterEqual(len(dcs), 1, "vcenter has no datastores")
        
        _name = dcs[0].name
        dc = self.vim.getDatacenter(_name)
        self.assertIsNotNone(dc, "Couldn't get DC: %s" % _name)
        self.assertEqual(dc.type, 'Datacenter', "Datacenter's type isn't Datacenter...")
        
    def testProps(self):
        dcs = self.vim.getDatacenters()
        for dc in dcs:
            self.assertIsInstance(dc, Datacenter, "Not an Datacenter instance")
            
            self.assertTrue(hasattr('datastore'), "Datacenter instance does not have a datastore property")
            self.assertTrue(hasattr('datastoreFolder'), "Datacenter instance does not have a datastoreFolder property")
            self.assertTrue(hasattr('hostFolder'), "Datacenter instance does not have a hostFolder property")
            self.assertTrue(hasattr('network'), "Datacenter instance does not have a network property")
            self.assertTrue(hasattr('networkFolder'), "Datacenter instance does not have a networkFolder property")
            self.assertTrue(hasattr('vmFolder'), "Datacenter instance does not have a vmFolder property")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDatacenter']
    unittest.main()