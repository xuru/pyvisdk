'''
Created on Jul 6, 2011

@author: eplaster
'''
import unittest, types
from pyvisdk import Vim
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.host_system import HostSystem
from pyvisdk.facade.property_collector import CachedPropertyCollector, HostSystemCachedPropertyCollector
from tests.common import get_options
from time import sleep

TEXT = """&lt;typeName xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:vim25"&gt;vim.EsxCLI.esxcli&lt;/typeName&gt;"""

class TestIternalAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.options = get_options()
        cls.vim = Vim(cls.options.server)
        cls.vim.login(cls.options.username, cls.options.password)

    @classmethod
    def tearDownClass(cls):
        cls.vim.logout()

    def test_RetrieveManagedMethodExecuter(self):
        host = self.vim.getHostSystems()[1]
        host.RetrieveManagedMethodExecuter()

    def test_RetrieveDynamicTypeManager(self):
        from pyvisdk.do.dynamic_type_mgr_filter_spec import DynamicTypeMgrTypeFilterSpec
        host = self.vim.getHostSystems()[1]
        obj = host.RetrieveDynamicTypeManager()
        spec = DynamicTypeMgrTypeFilterSpec(self.vim, "vim.CLIInfo")
        obj.DynamicTypeMgrQueryTypeInfo(spec)

    def test_DynamicTypeMgrQueryMoInstances(self):
        host = self.vim.getHostSystems()[1]
        obj = host.RetrieveDynamicTypeManager()
        obj.DynamicTypeMgrQueryMoInstances(None)

    def test_ExecuteSoap(self):
        from pyvisdk.do.reflect_managed_method_executer_soap_argument import ReflectManagedMethodExecuterSoapArgument
        host = self.vim.getHostSystems()[1]
        executer = host.RetrieveManagedMethodExecuter()
        argument = ReflectManagedMethodExecuterSoapArgument(self.vim, "typeName", TEXT)
        executer.executeSoap(moid="ha-dynamic-type-manager-local-cli-cliinfo",
                             version="urn:vim25/5.0",
                             method="vim.CLIInfo.FetchCLIInfo",
                             argument=[argument])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testHosts']
    unittest.main()

