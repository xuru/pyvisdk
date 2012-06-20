import unittest,types
from pyvisdk import Vim
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.host_system import HostSystem
from pyvisdk.mo.folder import Folder
from pyvisdk.mo.datastore import Datastore
from pyvisdk.mo.cluster_compute_resource import ClusterComputeResource
from pyvisdk.facade.property_collector import CachedPropertyCollector, HostSystemCachedPropertyCollector, PROPERTY_PATTERN
from tests.common import get_options
from time import sleep
from re import match

class Test_Facades(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.options = get_options()
        cls.vim = Vim(cls.options.server)
        cls.vim.login(cls.options.username, cls.options.password)

    @classmethod
    def tearDownClass(cls):
        cls.vim.logout()

    def test_HostPropertyCollectorFacade(self):
        facade = HostSystemCachedPropertyCollector(self.vim, ["config.storageDevice"])
        properties = facade.getProperties()
        self.assertGreater(len(properties.keys()), 0)
        self.assertEqual(len(properties.values()[0].keys()), 1)
        self.assertEqual(len(properties.keys()[0].split(':')), 2)
        self.assertNotEqual(properties.keys()[0].split(':')[1], '')

    def test_PropertyCollectorFacade(self):
        facade = CachedPropertyCollector(self.vim, "HostSystem", ["summary.quickStats"])
        properties = facade.getProperties()
        self.assertGreater(len(properties.keys()), 0)
        self.assertEqual(len(properties.values()[0].keys()), 1)
        self.assertEqual(len(properties.keys()[0].split(':')), 2)
        self.assertNotEqual(properties.keys()[0].split(':')[1], '')

    def test_simple_property(self):
        result = match(PROPERTY_PATTERN, 'foo.bar').groupdict()
        print result
        assert result['name'] == "foo.bar"

    def test_nested_property__no_property(self):
        result = match(PROPERTY_PATTERN, 'foo.bar["moshe"]').groupdict()
        print result
        assert result['name'] == "foo" and result['collection'] == "bar" and result['key'] == "moshe"

    def test_nested_property(self):
        result = match(PROPERTY_PATTERN, 'foo.bar["moshe"].qaz').groupdict()
        print result
        assert result['name'] == "foo" and result['collection'] == "bar" and result['key'] == "moshe" and result['property'] == "qaz"

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testHosts']
    unittest.main()
