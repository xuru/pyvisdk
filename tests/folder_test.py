'''
Created on Jul 6, 2011

@author: eplaster
'''
import unittest
from pyvisdk import Vim
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
        self.assertEqual(folder.type, "Folder", "Folder's type isn't Folder...")
        
    def testMethods(self):
        folder = self.datacenter.vmFolder
        
        self.assertIsInstance(folder.methods, list, "Folder.methods is not a list")
        for method in folder.methods:
            self.assertTrue(hasattr(folder, method), "Folder doesn't have method %s" % method)
        
    def testProps(self):
        folder = self.datacenter.vmFolder
        
        self.assertIsNotNone(folder.props, "props is None")
            
        # test each possible prop for the right object type
        for prop in folder.props:
            # first three are common props
            if prop in ["configIssue", "configStatus"]:
                self.assertIsNotNone(eval("folder.%s" % prop), "Prop %s is None." % prop)
            elif prop == "name":
                self.assertGreaterEqual(len(folder.name), 1, "Name has no length...")
                
            # vmFolder should have the Datacenter as a parent
            elif prop == "parent":
                self.assertIsInstance(folder.parent, Datacenter, "parent prop is not a Datacenter instance")
                    
            elif prop == "childType":
                self.assertIsInstance(folder.childType, list, "Childtype is not a list")
            
            elif prop == "childEntity":
                self.assertIsInstance(folder.childEntity, list, "ChildEntity is not a list")
                for obj in folder.childEntity:
                    self.assertIn(obj.__class__.__name__, folder.childType, "Not a valid child type: %s" % obj.__class__.__name__)
                
            else:
                print "---- "+prop+" "+"-"*70
                print eval("folder.%s" % prop)
                    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testFolder']
    unittest.main()