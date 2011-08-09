'''
Created on Jul 6, 2011

@author: eplaster
'''
import unittest,types
from pyvisdk import Vim
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.host_system import HostSystem
from pyvisdk.mo.folder import Folder
from pyvisdk.mo.datastore import Datastore
from pyvisdk.mo.cluster_compute_resource import ClusterComputeResource
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
        self.assertEqual(host.type, ManagedObjectTypes.HostSystem, "Host's type isn't HostSystem...")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testHosts']
    unittest.main()