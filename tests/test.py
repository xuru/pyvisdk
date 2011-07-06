'''
Created on Feb 11, 2011

@author: eplaster
'''
import unittest
import os.path
import sys

here = os.path.expanduser(os.path.dirname(__file__))
sys.path.insert(0, os.path.join("..", "src"))

from pyvisdk import Vim

ident = open("ident.cnf").readlines()
server = ident[0].strip()
username = ident[1].strip()
password = ident[2].strip()

class Test(unittest.TestCase):
    def testConnection(self):
        vim = Vim(server, verbose=0, connect=False)
        assert(vim.connected == False)
        
        vim.connect()
        assert(vim.connected == True)
    
    def testAbout(self):
        vim = Vim(server, verbose=0)
        vim.displayAbout()

    def testLogin(self):
        vim = Vim(server, verbose=0)
        vim.login(username, password)
        assert(vim.loggedin == True)
        vim.logout()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()