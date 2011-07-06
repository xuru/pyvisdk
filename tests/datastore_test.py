'''
Created on Jul 6, 2011

@author: eplaster
'''
import unittest, types
from pyvisdk import Vim
from pyvisdk.managedObjects.datastore import Datastore
from pyvisdk.managedObjects.folder import Folder
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
        
    def testMethods(self):
        datastores = self.datacenter.datastore
        datastore = datastores[0]
        
        self.assertIsInstance(datastore.methods, list, "Datastore.methods is not a list")
        for method in datastore.methods:
            self.assertTrue(hasattr(datastore, method), "Datastore doesn't have method %s" % method)
        
    def testProps(self):
        datastores = self.datacenter.datastore
        for datastore in datastores:
            self.assertIsInstance(datastore, Datastore, "Not an Datastore instance: %s" % datastore)
            self.assertIsNotNone(datastore.props, "props is None")
            
            # test each possible prop for the right object type
            for prop in datastore.props:
                # first three are common props
                if prop in ["configIssue", "configStatus"]:
                    self.assertIsNotNone(eval("datastore.%s" % prop), "Prop %s is None." % prop)
                elif prop == "name":
                    self.assertGreaterEqual(len(datastore.name), 1, "Name has no length...")
                elif prop == "parent":
                    self.assertIsInstance(datastore.parent, Folder, "parent prop is not a Folder instance")
                
                elif prop in ["browser", "info", "summary", "capability", "vm"]:
                    self.assertIsNotNone(eval("datastore.%s" % prop), "%s is None" % prop)
                    
                else:
                    print "---- "+prop+" "+"-"*70
                    print eval("datastore.%s" % prop)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDatastore']
    unittest.main()