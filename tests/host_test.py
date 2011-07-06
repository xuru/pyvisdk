'''
Created on Jul 6, 2011

@author: eplaster
'''
import unittest,types
from pyvisdk import Vim
from pyvisdk.managedObjects.host import HostSystem
from pyvisdk.managedObjects.folder import Folder
from pyvisdk.managedObjects.datastore import Datastore
from pyvisdk.managedObjects.clusterComputeResource import ClusterComputeResource
from tests.common import get_options


class TestHosts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.options = get_options()
        cls.vim = Vim(cls.options.server)
        cls.vim.login(cls.options.username, cls.options.password)

    @classmethod
    def tearDownClass(cls):
        cls.vim.logout()

    def testHosts(self):
        hosts = self.vim.getHosts()
        self.assertGreaterEqual(len(hosts), 1, "vcenter has no hosts")

    def testHost(self):
        hosts = self.vim.getHosts()
        
        host = self.vim.getHostSystem(hosts[0].name)
        self.assertIsNotNone(host, "Couldn't get host: %s" % host.name)
        self.assertEqual(host.type, "HostSystem", "Host's type isn't HostSystem...")
        
    def testMethods(self):
        hosts = self.vim.getHosts()
        host = self.vim.getHostSystem(hosts[0].name)
        
        self.assertIsInstance(host.methods, list, "Host.methods is not a list")
        for method in host.methods:
            self.assertTrue(hasattr(host, method), "Host doesn't have method %s" % method)
        
    def testProps(self):
        hosts = self.vim.getHosts()
        for host in hosts:
            self.assertIsInstance(host, HostSystem, "Not an Host instance: %s" % host)
            self.assertIsNotNone(host.props, "props is None")
            
            # test each possible prop for the right object type
            for prop in host.props:
                # first three are common props
                if prop in ["configIssue", "configStatus"]:
                    self.assertIsNotNone(eval("host.%s" % prop), "Prop %s is None." % prop)
                elif prop == "name":
                    self.assertGreaterEqual(len(host.name), 1, "Name has no length...")
                
                # parent of a host is a cluster compute resource
                elif prop == "parent":
                    self.assertIsInstance(host.parent, ClusterComputeResource, "parent prop is not a ClusterComputeResource instance: %s" % host.parent)
                
                elif prop in ["vmFolder", "networkFolder", "hostFolder"]:
                    self.assertIsInstance(eval("host.%s" % prop), Folder, "%s prop is not a Folder instance" % prop)
                
                elif prop == "datastore":
                    if type(host.datastore) == types.ListType:
                        for ds in host.datastore:
                            self.assertIsInstance(ds, Datastore, "%s is not type Datastore" % ds)
                    else:
                        self.assertIsInstance(ds, Datastore, "%s is not type Datastore" % ds)
                        
                elif prop in ["capability", "config", "configManager", "datastoreBrowser", "hardware", \
                              "network", "runtime", "summary", "systemResources", "vm"]:
                    self.assertIsNotNone(eval("host.%s" % prop), "%s is None" % prop)
                    
                else:
                    print "---- "+prop+" "+"-"*70
                    print eval("host.%s" % prop)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testHosts']
    unittest.main()