'''
Created on Jul 6, 2011

@author: eplaster
'''
import unittest, types
from pyvisdk import Vim
from pyvisdk.base.managed_object_types import ManagedObjectTypes
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
        self.assertEqual(datastore.type, ManagedObjectTypes.Datastore, "Datastore's type isn't Datastore...")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDatastore']
    unittest.main()