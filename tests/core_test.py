'''
Created on Feb 11, 2011

@author: eplaster
'''

import unittest
from pyvisdk import Vim
from tests.common import get_options

class Test(unittest.TestCase):
    def setUp(self):
        self.options = get_options()

    def tearDown(self):
        pass

    def testConnection(self):
        vim = Vim(self.options.server, verbose=0, connect=False)
        assert(vim.connected == False)
        assert(vim.loggedin == False)

        vim.connect()
        assert(vim.connected == True)
        assert(vim.loggedin == False)

    def testAbout(self):
        vim = Vim(self.options.server, verbose=0)
        vim.displayAbout()
        assert(vim.connected == True)
        assert(vim.loggedin == False)

    def testLogin(self):
        vim = Vim(self.options.server, verbose=0)
        assert(vim.connected == True)

        vim.login(self.options.username, self.options.password)
        assert(vim.loggedin == True)

        vim.logout()
        assert(vim.loggedin == False)

    def testApiType(self):
        vim = Vim(self.options.server, verbose=0)
        assert("VirtualCenter" == vim.getApiType())

    def testLoginExtensionByCertificate(self):
        self.fail('make this test pass')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
