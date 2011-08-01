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
        
    def testMethods(self):
        dcs = self.vim.getDatacenters()
        dc = self.vim.getDatacenter(dcs[0].name)
        
        self.assertIsInstance(dc.methods, list, "Datacenter.methods is not a list")
        for method in dc.methods:
            self.assertTrue(hasattr(dc, method), "Datacenter doesn't have method %s" % method)
        
    def testProps(self):
        dcs = self.vim.getDatacenters()
        for dc in dcs:
            self.assertIsInstance(dc, Datacenter, "Not an Datacenter instance")
            self.assertIsNotNone(dc.props, "props is None")
            
            # test each possible prop for the right object type
            for prop in dc.props:
                if prop == "name":
                    self.assertGreaterEqual(len(dc.name), 1, "Name has no length...")
                
                elif prop in ["vmFolder", "parent", "networkFolder", "hostFolder"]:
                    self.assertIsInstance(eval("dc.%s" % prop), Folder, "%s prop is not a Folder instance" % prop)
                
                elif prop == "datastore":
                    if type(dc.datastore) == types.ListType:
                        for ds in dc.datastore:
                            self.assertIsInstance(ds, Datastore, "%s is not type Datastore" % ds)
                    else:
                        self.assertIsInstance(ds, Datastore, "%s is not type Datastore" % ds)
                        
                elif prop == "network":
                    pass  # currently doesn't have a class defined
                
                elif prop in ["configIssue", "configStatus"]:
                    self.assertIsNotNone(eval("dc.%s" % prop), "Prop %s is None." % prop)
                    
                else:
                    print "---- "+prop+" "+"-"*70
                    print eval("dc.%s" % prop)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDatacenter']
    unittest.main()