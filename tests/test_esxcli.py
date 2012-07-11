
import unittest, types
from pyvisdk import Vim
from tests.common import get_options
from pyvisdk.esxcli import Generator, EsxCLI

class TestEsxCLI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.options = get_options()
        cls.vim = Vim(cls.options.server)
        cls.vim.login(cls.options.username, cls.options.password)

    @classmethod
    def tearDownClass(cls):
        cls.vim.logout()

    def test_xsd_generator(self):
        host = self.vim.getHostSystems()[1]
        generator = Generator(self.vim, host)
        generator.generate_xsd()

    def test_cli_handlers_generator(self):
        host = self.vim.getHostSystems()[1]
        generator = Generator(self.vim, host)
        generator.generate_cli_handlers()

    def test_list_adapters(self):
        host = self.vim.getHostSystems()[1]
        esxcli = EsxCLI(self.vim, host)
        esxcli.get('storage.core.adapter').list()

    def test_list_devices(self):
        host = self.vim.getHostSystems()[1]
        esxcli = EsxCLI(self.vim, host)
        esxcli.get('storage.core.device').list()

    def test_add_claiming_rule(self):
        host = self.vim.getHostSystems()[1]
        esxcli = EsxCLI(self.vim, host)
        rule = esxcli.get('storage.nmp.satp.rule')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testHosts']
    unittest.main()

