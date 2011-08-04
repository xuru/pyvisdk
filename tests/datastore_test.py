'''
Created on Jul 6, 2011

@author: eplaster
'''
import unittest, types
from pyvisdk import Vim
from pyvisdk.mo.datastore import Datastore
from pyvisdk.mo.folder import Folder
from tests.common import get_options


class TestDatastore(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.options = get_options()
        cls.vim = Vim(cls.options.server)
        cls.vim.login(cls.options.username, cls.options.password)
        cls.datacenter = cls.vim.getDatacenters()[0]

    @classmethod
    def tearDownClass(cls):
        cls.vim.logout()

    def testDatastores(self):
        datastores = self.datacenter.datastore
        self.assertGreaterEqual(len(datastores), 1, "vcenter has no datastores")

    def testDatastore(self):
        datastores = self.datacenter.datastore
        datastore = datastores[0]
        
        self.assertIsNotNone(datastore, "Couldn't get datastore: %s" % datastore.name)
        self.assertEqual(datastore.type, "Datastore", "Datastore's type isn't Datastore...")
        
    def testProps(self):
        datastores = self.datacenter.datastore
        for datastore in datastores:
            self.assertIsInstance(datastore, Datastore, "Not an Datastore instance: %s" % datastore)
            
            self.assertTrue(hasattr('browser'), "Datacenter instance does not have a browser property")
            self.assertTrue(hasattr('capability'), "Datacenter instance does not have a capability property")
            self.assertTrue(hasattr('host'), "Datacenter instance does not have a host property")
            self.assertTrue(hasattr('info'), "Datacenter instance does not have a info property")
            self.assertTrue(hasattr('iormConfiguration'), "Datacenter instance does not have a iormConfiguration property")
            self.assertTrue(hasattr('summary'), "Datacenter instance does not have a summary property")
            self.assertTrue(hasattr('vm'), "Datacenter instance does not have a vm property")
            self.assertTrue(hasattr('browser'), "Datacenter instance does not have a browser property")
            self.assertTrue(hasattr('browser'), "Datacenter instance does not have a browser property")
            self.assertTrue(hasattr('browser'), "Datacenter instance does not have a browser property")
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDatastore']
    unittest.main()