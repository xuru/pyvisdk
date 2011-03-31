#!/usr/bin/env python
from pyvisdk.consts import ManagedEntityTypes
from pyvisdk.managedObjects.datacenter import Datacenter
from pyvisdk.managedObjects.host import HostSystem
from pyvisdk.managedObjects.vm import VirtualMachine
import logging
import pyvisdk.core
import types
"""
Assumptions:  Must connect to the vSphere vCenter
              Must be version 4.0 or greater

"""
log = logging.getLogger(__name__)

class Vim(pyvisdk.core.VimBase):
    def __init__(self, server, connect=True, verbose=3):
        super(Vim, self).__init__(server, connect, verbose)
        self.loggedin = False
        
    def login(self, username, password):
        self.username = username
        self.password = password
        
        if self.verbose > 5:
            self.displayAbout()

        self.client.service.Login(self.managers['sessionManager'], self.username, self.password)
        if self.verbose > 2:
            log.info("Successfully logged into %s" % self.client.url)
        self.loggedin = True

    def logout(self):
        self.client.service.Logout(self.managers['sessionManager'])
        self.loggedin = False

    def displayAbout(self):
        print "=" * 40
        print "Connected to %s" % self.server
        print "  %s" % self.service_content.about.fullName
        print "  OS: %s" % self.service_content.about.osType
        print "  License: %s %s" % (
                self.service_content.about.licenseProductName, self.service_content.about.licenseProductVersion)
        print "=" * 40
        
    def getApiType(self):
        return self.service_content.about.apiType

    #------------------------------------------------------------
    # Hosts
    #------------------------------------------------------------
    def getHosts(self):
        return self.getHostSystem()
    
    def getHostSystem(self, name=None):
        mo = self.getDecendentsByName(_type=ManagedEntityTypes.HostSystem, properties=["name"], name=name)
        if type(mo) == types.ListType:
            return [HostSystem(self, ref=x.obj) for x in mo]
        return HostSystem(self, name=mo[0].propSet[0].val, ref=mo.obj)
    
    #------------------------------------------------------------
    # Datacenters
    #------------------------------------------------------------
    def getDatacenters(self):
        mo = self.getDecendentsByName(_type=ManagedEntityTypes.Datacenter, properties=["name"], name=name)
        return [Datacenter(self, name=mo[0].propSet[0].val, ref=x.obj) for x in mo]
    
    def getDatacenter(self, name):
        mo = self.getDecendentsByName(_type=ManagedEntityTypes.Datacenter, properties=["name"], name=name)
        return Datacenter(self, name=mo[0].propSet[0].val, ref=mo[0].obj)

    #------------------------------------------------------------
    # Virtual Machines
    #------------------------------------------------------------
    def getVirtualMachine(self, name):
        mo = self.getDecendentsByName(_type=ManagedEntityTypes.VirtualMachine, properties=["name", "runtime.powerState"], name=name)
        return VirtualMachine(self, name=mo.propSet[0].val, ref=mo.obj)
        
    def getVirtualMachines(self):
        mo = self.getDecendentsByName(_type=ManagedEntityTypes.VirtualMachine, properties=["name", "runtime.powerState"])
        return [VirtualMachine(self, name=mo[0].propSet[0].val, ref=x.obj) for x in mo]
   
    def getVirtualMachinesIter(self):
        refs = self.getDecendentsByName(_type=ManagedEntityTypes.VirtualMachine, properties=["name", "runtime.powerState"])
        for ref in refs:
            yield VirtualMachine(self, name=ref.propSet[0].val, ref=ref.obj)
    
    #------------------------------------------------------------
    # Hierarchy
    #------------------------------------------------------------
    def getHierarchy(self):
        mo = self.getContentsRecursively(props=["configIssue", "configStatus", "name", "parent"])
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
    
    vms = vim.getAllVirtualMachineRefs()
    for ref in vms:
        name = ref.propSet[0].val
        power = ref.propSet[1].val
        print "%-20s %s" % (name, power)
            
        vm = vim.getVirtualMachine(name)
        sname = vm.createSnapshot()
        print sname
        
        snap = vm.getSnapshotByName(sname)
        print snap
        break
    
    vim.logout()


