import unittest
import mock
from pyvisdk.facade.property_collector import CachedPropertyCollector, HostSystemCachedPropertyCollector, PROPERTY_NAME_PATTERN
from re import findall, findall
from bunch import Bunch

HBAAPI_PROPERTY_PATH = 'config.storageDevice.hostBusAdapter'
TOPOLOGY_PROPERTY_PATH = 'config.storageDevice.scsiTopology.adapter'
HBA_KEY = "key-vim.host.ScsiTopology.Interface-vmhba0"
TARGET_KEY = "key-vim.host.ScsiTopology.Target-vmhba0:0:0"
LUN_KEY = "key-vim.host.ScsiTopology.Lun-020c0000006742b0f000004e2b0000000000000000496e66696e69"

class PropertyCollectorFacadeTestCase(unittest.TestCase):
    def test_simple_property(self):
        result = findall(PROPERTY_NAME_PATTERN, 'foo.bar')
        self.assertEquals(result, ['foo', 'bar'])

    def test_nested_property__no_property(self):
        result = findall(PROPERTY_NAME_PATTERN, 'foo.bar["moshe"]')
        self.assertEquals(result, ['foo', 'bar', '["moshe"]'])

    def test_nested_property(self):
        result = findall(PROPERTY_NAME_PATTERN, 'foo.bar["moshe"].qaz')
        self.assertEquals(result, ['foo', 'bar', '["moshe"]', 'qaz'])

    def test_nested_property__twice(self):
        key = 'config.storageDevice.scsiTopology.adapter["key-vim.host.ScsiTopology.Interface-vmhba2"].target["key-vim.host.ScsiTopology.Target-vmhba2:0:0"]'
        result = findall(PROPERTY_NAME_PATTERN, key)
        self.assertEquals(result, ['config', 'storageDevice', 'scsiTopology', 'adapter',
                                   '["key-vim.host.ScsiTopology.Interface-vmhba2"]', 'target', 
                                   '["key-vim.host.ScsiTopology.Target-vmhba2:0:0"]'])

    def _get_fake_property_collector(self, vim, filterSet=[]):
        fake = mock.Mock()
        update_set = Bunch(filterSet=filterSet, truncated=False, version='1')
        fake.WaitForUpdatesEx.return_value = update_set
        vim.service_content.propertyCollector.CreatePropertyCollector.return_value = fake
        return fake

    def _set_update_on_fake_property_collector(self, fake, filterSet=[]):
        version = str(int(fake.WaitForUpdatesEx.return_value.version) + 1)
        update_set = Bunch(filterSet=filterSet, truncated=False, version=version)
        fake.WaitForUpdatesEx.return_value = update_set

    def _assert_fake_methods_were_called(self, vim, fake):
        self.assertTrue(vim.service_content.propertyCollector.CreatePropertyCollector.called)
        self.assertTrue(fake.WaitForUpdatesEx.called)

    def test_get_properties__empty(self):
        vim = mock.Mock()
        fake = self._get_fake_property_collector(vim)
        facade = HostSystemCachedPropertyCollector(vim, [HBAAPI_PROPERTY_PATH, TOPOLOGY_PROPERTY_PATH])
        properties = facade.getProperties()
        self._assert_fake_methods_were_called(vim, fake)

    def _get_initial_filter_update(self, vim):
        managed_object_reference = Bunch(ref=Bunch(_type="HostSystem", value="host-1"))
        adapter_list = [Bunch(adapter="adapter", key=HBA_KEY, target=[])]
        property_change = Bunch(name=TOPOLOGY_PROPERTY_PATH, op="add", val=adapter_list)
        object_update = Bunch(kind="enter", missingSet=[], changeSet=[property_change], obj=managed_object_reference)
        filter_update = Bunch(filter=None, missingSet=[], objectSet=[object_update])
        return filter_update

    def _get_filter_update__target_added(self, vim):
        managed_object_reference = Bunch(ref=Bunch(_type="HostSystem", value="host-1"))
        target = Bunch(key=TARGET_KEY, lun=[], target=0, transport=None)
        name = """{}["{}"].target["{}"]"""
        property_change = Bunch(name=name.format(TOPOLOGY_PROPERTY_PATH, HBA_KEY, TARGET_KEY), op="add", val=target)
        object_update = Bunch(kind="modify", missingSet=[], changeSet=[property_change], obj=managed_object_reference)
        filter_update = Bunch(filter=None, missingSet=[], objectSet=[object_update])
        return filter_update

    def _get_filter_update__target_removed(self, vim):
        filter_update = self._get_filter_update__target_added(vim)
        filter_update.objectSet[0].changeSet[0].op = "remove"
        filter_update.objectSet[0].changeSet[0].val = None
        return filter_update

    def _get_filter_update__lun_added(self, vim):
        managed_object_reference = Bunch(ref=Bunch(_type="HostSystem", value="host-1"))
        lun = Bunch(key=LUN_KEY, lun=0, scsiLun=LUN_KEY, transport=None)
        name = """{}["{}"].target["{}"].lun["{}"]"""
        property_change = Bunch(name=name.format(TOPOLOGY_PROPERTY_PATH, HBA_KEY, TARGET_KEY, LUN_KEY), op="add", val=lun)
        object_update = Bunch(kind="modify", missingSet=[], changeSet=[property_change], obj=managed_object_reference)
        filter_update = Bunch(filter=None, missingSet=[], objectSet=[object_update])
        return filter_update

    def _get_filter_update__lun_removed(self, vim):
        filter_update = self._get_filter_update__lun_added(vim)
        filter_update.objectSet[0].changeSet[0].op = "remove"
        filter_update.objectSet[0].changeSet[0].val = None
        return filter_update

    def test_get_properties__first_time(self):
        vim = mock.Mock()
        filter_update = self._get_initial_filter_update(vim)
        fake = self._get_fake_property_collector(vim, [filter_update])
        facade = HostSystemCachedPropertyCollector(vim, [HBAAPI_PROPERTY_PATH, TOPOLOGY_PROPERTY_PATH])
        properties = facade.getProperties()
        self._assert_fake_methods_were_called(vim, fake)
        self.assertEquals(properties.keys(), ["HostSystem:host-1"])
        self.assertEquals(properties["HostSystem:host-1"][TOPOLOGY_PROPERTY_PATH][0].key, HBA_KEY)

    def test_get_properties__target_added(self):
        vim = mock.Mock()
        first_update = self._get_initial_filter_update(vim)
        fake = self._get_fake_property_collector(vim, [first_update])
        facade = HostSystemCachedPropertyCollector(vim, [HBAAPI_PROPERTY_PATH, TOPOLOGY_PROPERTY_PATH])
        properties = facade.getProperties()
        second_update = self._get_filter_update__target_added(vim)
        self._set_update_on_fake_property_collector(fake, [second_update])
        properties = facade.getProperties()
        self.assertEquals(properties["HostSystem:host-1"][TOPOLOGY_PROPERTY_PATH][0].target[0].key, TARGET_KEY)

    def test_get_properties__target_removed(self):
        vim = mock.Mock()
        first_update = self._get_initial_filter_update(vim)
        fake = self._get_fake_property_collector(vim, [first_update])
        facade = HostSystemCachedPropertyCollector(vim, [HBAAPI_PROPERTY_PATH, TOPOLOGY_PROPERTY_PATH])
        properties = facade.getProperties()
        second_update = self._get_filter_update__target_added(vim)
        self._set_update_on_fake_property_collector(fake, [second_update])
        properties = facade.getProperties()
        third_update = self._get_filter_update__target_removed(vim)
        self._set_update_on_fake_property_collector(fake, [third_update])
        properties = facade.getProperties()
        self.assertEquals(properties["HostSystem:host-1"][TOPOLOGY_PROPERTY_PATH][0].target, [])

    def test_get_properties__lun_added(self):
        vim = mock.Mock()
        first_update = self._get_initial_filter_update(vim)
        fake = self._get_fake_property_collector(vim, [first_update])
        facade = HostSystemCachedPropertyCollector(vim, [HBAAPI_PROPERTY_PATH, TOPOLOGY_PROPERTY_PATH])
        properties = facade.getProperties()
        second_update = self._get_filter_update__target_added(vim)
        self._set_update_on_fake_property_collector(fake, [second_update])
        properties = facade.getProperties()
        third_update = self._get_filter_update__lun_added(vim)
        self._set_update_on_fake_property_collector(fake, [third_update])
        properties = facade.getProperties()
        self.assertEquals(properties["HostSystem:host-1"][TOPOLOGY_PROPERTY_PATH][0].target[0].lun[0].key, LUN_KEY)

    def test_get_properties__lun_removed(self):
        vim = mock.Mock()
        first_update = self._get_initial_filter_update(vim)
        fake = self._get_fake_property_collector(vim, [first_update])
        facade = HostSystemCachedPropertyCollector(vim, [HBAAPI_PROPERTY_PATH, TOPOLOGY_PROPERTY_PATH])
        properties = facade.getProperties()
        second_update = self._get_filter_update__target_added(vim)
        self._set_update_on_fake_property_collector(fake, [second_update])
        properties = facade.getProperties()
        third_update = self._get_filter_update__lun_added(vim)
        self._set_update_on_fake_property_collector(fake, [third_update])
        properties = facade.getProperties()
        fourth_update = self._get_filter_update__lun_removed(vim)
        self._set_update_on_fake_property_collector(fake, [fourth_update])
        properties = facade.getProperties()
        self.assertEquals(properties["HostSystem:host-1"][TOPOLOGY_PROPERTY_PATH][0].target[0].lun, [])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testHosts']
    unittest.main()

