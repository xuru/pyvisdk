from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.do.managed_object_reference import ManagedObjectReference
from brownie.importing import import_string
from pyvisdk.utils import camel_to_under

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
        self.facades = dict()

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
        self.facades = dict()

    def loginByExtensionCertificate(self, extension_key, locale=None):
        """
        Log into the vmware server with extension key
        """
        self.extension_key = extension_key
        if not locale:
            if hasattr(self.session_manager, 'defaultLocale'):
                locale = self.session_manager.defaultLocale
            else:
                locale = 'en_US'

        if self.verbose > 5:
            self.displayAbout()
        session = self.session_manager.LoginExtensionByCertificate(extension_key, locale)
        if self.verbose > 2:
            log.info("Successfully logged into %s" % self.proxy)
        self.username = session.userName
        self.loggedin = True
        self.facades = dict()

    def logout(self):
        """
        Log out of the vmware server.
        """
        self.session_manager.Logout()
        self.loggedin = False
        self.facades = dict()

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

    def getManagedObjectByReference(self, moref):
        """
        Returns the managed object
        :param moref: moref string. For example: VirtualMachine:vm-16
        :rtype: :py:class:`ManagedEntity`
        """
        # http://www.doublecloud.org/2011/03/how-to-get-a-managed-object-with-its-id-like-task-id/
        class_name, object_id = moref.split(':', 1)
        ref = ManagedObjectReference(self, type=class_name, value=object_id)
        return self._getManagedObjectType(class_name)(self, ref=ref)

    def _getManagedObjectType(self, class_name):
        # inspired by pyvisdk.vim
        return import_string("pyvisdk.mo.{}.{}".format(camel_to_under(class_name), class_name))
