'''
Created on Jul 6, 2011

@author: eplaster
'''
import unittest
from pyvisdk import Vim
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from tests.common import get_options


class TestSnapshot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.options = get_options()
        cls.vim = Vim(cls.options.server)
        cls.vim.login(cls.options.username, cls.options.password)

    @classmethod
    def tearDownClass(cls):
        cls.vim.logout()

    def testSnapshot(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSnapshot']
    unittest.main()