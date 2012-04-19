#!/usr/bin/env python
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.datacenter import Datacenter
from pyvisdk.mo.host_system import HostSystem
from pyvisdk.mo.virtual_machine import VirtualMachine
import logging
import pyvisdk.core

#
# Assumptions:  Must connect to the vSphere vCenter
#               Must be version 4.0 or greater
# 

log = logging.getLogger(__name__)

class Vim(pyvisdk.core.VimBase):
    def __init__(self, server, connect=True, verbose=3, certfile=None, keyfile=None):
        super(Vim, self).__init__(server, connect, verbose, certfile, keyfile)
        self.loggedin = False
        self.username = None
        self.password = None

    def login(self, username, password, locale=None):
        """
        Log into the vmware server.
        """
        self.username = username
        self.password = password

        if not locale:
            if hasattr(self.session_manager, 'defaultLocale'):
                locale = self.session_manager.defaultLocale
            else:
                locale = 'en_US'

        if self.verbose > 5:
            self.displayAbout()

        self.session_manager.Login(self.username, self.password, locale)
        if self.verbose > 2:
            log.info("Successfully logged into %s" % self.client.url)
        self.loggedin = True

    def logout(self):
        """
        Log out of the vmware server.
        """
        self.session_manager.Logout()
        self.loggedin = False

    def relogin(self):
        """
        Re-logs in to the vmware server.
        """
        try:
            self.logout()
        except Exception:
            pass

        if self.username and self.password:
            self.login(self.username, self.password)

    def displayAbout(self):
        """
        Display version information about the vmware server and library
        """
        print "=" * 40
        print "Connected to %s" % self.server
        print "  %s" % self.service_content.about.fullName
        print "  OS: %s" % self.service_content.about.osType
        print "  License: %s %s" % (
                self.service_content.about.licenseProductName, self.service_content.about.licenseProductVersion)
        print "  Current Sessions: "
        for session in self.session_manager.sessionList:
            print "%-30s %-20s Last Active: %-20s Logged In: %-20s" % ("%s(%s)" % (session.fullName, session.userName), session.key, session.lastActiveType, session.loginTime)
        print "=" * 40

    def getApiType(self):
        """
        Get the API type
        
        :returns: Indicates whether or not the service instance represents a standalone host. If the service instance represents a standalone host, then the physical inventory for that service instance is fixed to that single host. VirtualCenter server provides additional features over single hosts. For example, VirtualCenter offers multi-host management. 
        :rtype: xsd:string
        """
        return self.service_content.about.apiType

    #------------------------------------------------------------
    # Hosts
    #------------------------------------------------------------
    def getHostSystems(self):
        """
        Get all the hosts on the server
        
        :rtype: :py:class:`HostSystem`
        """
        return self.getDecendentsByName(_type=ManagedObjectTypes.HostSystem, properties=["name"]) #@UndefinedVariable

    def getHostSystem(self, _name=None):
        """
        Get the host system by name
        
        :rtype: :py:class:`HostSystem`
        """
        return self.getDecendentsByName(_type=ManagedObjectTypes.HostSystem, properties=["name"], name=_name) #@UndefinedVariable

    #------------------------------------------------------------
    # Datacenters
    #------------------------------------------------------------
    def getDatacenters(self):
        """
        Get all the data centers on the server
        
        :rtype: :py:class:`Datacenter`
        """
        return self.getDecendentsByName(_type=ManagedObjectTypes.Datacenter, properties=["name"]) #@UndefinedVariable

    def getDatacenter(self, _name):
        """
        Get the data center by name
        
        :rtype: :py:class:`Datacenter`
        """
        return self.getDecendentsByName(_type=ManagedObjectTypes.Datacenter, properties=["name"], name=_name) #@UndefinedVariable

    #------------------------------------------------------------
    # Resource pool
    #------------------------------------------------------------
    def getResourcePools(self):
        return self.getDecendentsByName(_type=ManagedObjectTypes.ResourcePool, properties=["name"]) #@UndefinedVariable

    def getResourcePool(self, _name):
        return self.getDecendentsByName(_type=ManagedObjectTypes.ResourcePool, properties=["name"], name=_name) #@UndefinedVariable

    #------------------------------------------------------------
    # Virtual Machines
    #------------------------------------------------------------
    def getVirtualMachine(self, _name):
        """
        Get the virtual machine by name
        
        :rtype: :py:class:`VirtualMachine`
        """
        return self.getDecendentsByName(_type=ManagedObjectTypes.VirtualMachine, properties=["name", "runtime.powerState"], name=_name) #@UndefinedVariable

    def getVirtualMachines(self):
        """
        Get all the virtual machines on the server
        
        :rtype: :py:class:`VirtualMachine`
        """
        return self.getDecendentsByName(_type=ManagedObjectTypes.VirtualMachine, properties=["name", "runtime.powerState"]) #@UndefinedVariable

    #------------------------------------------------------------
    # Hierarchy
    #------------------------------------------------------------
    def _getHierarchy(self):
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


