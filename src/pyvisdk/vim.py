#!/usr/bin/env python
from pyvisdk import consts
from pyvisdk.core import VimBase
from pyvisdk.vm import VirtualMachine
import time

"""
Assumptions:  Must connect to the vSphere vCenter
              Must be version 4.0 or greater

"""

class Vim(VimBase):
    def __init__(self, server, connect=True, verbose=3):
        super(Vim, self).__init__(server, connect, verbose)
        
    def login(self, username, password):
        self.username = username
        self.password = password
        
        if self.verbose > 5:
            self.displayAbout()

        self.client.service.Login(self.managers['sessionManager'], self.username, self.password)
        if self.verbose > 2:
            print "Successfully logged into %s" % self.url

    def logout(self):
        self.client.service.Logout(self.managers['sessionManager'])

    def displayAbout(self):
        print dir(self.service_content.about)
        print "=" * 40
        print "Connected to %s" % self.server
        print "  %s" % self.service_content.about.fullName
        print "  OS: %s" % self.service_content.about.osType
        print "  License: %s %s" % (
                self.service_content.about.licenseProductName, self.service_content.about.licenseProductVersion)
        print "=" * 40

    def getApiType(self):
        return self.service_content.about.apiType

    def getVirtualMachine(self, name):
        return VirtualMachine(self, name)
        
    def getAllVirtualMachines(self):
        typeinfo = [ 
            self.PropertySpec(_type=consts.VirtualMachine, pathSet=[
                        "parent","name","summary.config","snapshot","config.hardware.device"]) 
        ]
        
        refs = self.getContentsRecursively(root=self.root, props=typeinfo, recurse=True)
        out = []
        for ref in refs:
            out.append( VirtualMachine(self, mo=ref) )
        return out

    def getHostSystem(self, name):
        mo = self.getDecendentsByName(_type=consts.HostSystem, name=name)
        return mo

    def getDatacenter(self, name):
        mo = self.getDecendentsByName(_type=consts.Datacenter, name=name)
        return mo
        
if __name__ == '__main__':
    from optparse import OptionParser
    import sys
    
    # Some command line argument parsing gorp to make the script a little more
    # user friendly.
    usage = '''Usage: %prog [options]

      This program will dump the containers of the ESX environment from the host specified with
      the -s option.'''
    
    parser = OptionParser(usage=usage)
    parser.add_option('-s', '--server', dest='server',
                  help='Specify the vCenter to connect to')
    parser.add_option('-u', '--username', dest='username',
                      help='Username (default is root)')
    parser.add_option('-p', '--password', dest='password',
                      help='Password (default is blank)')
    (options, args) = parser.parse_args()
    if options.server is None:
        print 'You must specify a server to connect to.  Use --help for usage'
        sys.exit(1)
    if options.username is None:
        options.username = 'root'
    if options.password is None:
        options.password = ''


    print "Connecting to " + options.server
    vim = Vim(options.server, verbose=3)
    vim.login(options.username, options.password)
    
    name = "puppetTestAppServer"
    
    print "Getting Virtual Machine: " + name
    vm = vim.getVirtualMachine(name)
    print vm
    
    vm.enableChangedBlockTracking(True)
    
    
    vim.logout()


