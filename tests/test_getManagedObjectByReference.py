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


class Test_getManagedObjectByReference(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.options = get_options()
        cls.vim = Vim(cls.options.server)
        cls.vim.login(cls.options.username, cls.options.password)

    @classmethod
    def tearDownClass(cls):
        cls.vim.logout()

    def test_method(self):
        hosts = self.vim.getHostSystems()
        expected = self.vim.getHostSystem(hosts[0].name)
        actual = self.vim.getManagedObjectByReference("{}:{}".format(expected.ref._type, expected.ref.value))

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testHosts']
    unittest.main()
