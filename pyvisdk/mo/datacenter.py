
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.managed_entity import ManagedEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class Datacenter(ManagedEntity):
    '''The Datacenter managed object provides the interface to the common container
        object for hosts, virtual machines, networks, and datastores. These
        entities must be under a distinct datacenter in the inventory, and
        datacenters may not be nested under other datacenters.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.Datacenter):
        # MUST define these
        super(Datacenter, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def QueryConnectionInfo(self, username, password, hostname, port):
        '''This method provides a way of getting basic information about a host without
        adding it to a datacenter. Connection wizards typically use this method to
        show information about a host so a user can confirm a set of changes
        before applying them.

        :param username: The name of the user.

        :param password: The password of the user.

        :param hostname: The target of the query.

        :param port: The port number of the target host. For ESX 2.x this is the authd port (902 by default). For ESX 3.x and above and for VMware Server hosts this is the https port (443 by default). You can specify -1 to have the vCenter Server try the default ports.


        :rtype: HostConnectInfo 

        '''
        
        return self.delegate("QueryConnectionInfo")(username,password,hostname,port)
        

    def PowerOnMultiVM_Task(self):
        '''Powers on multiple virtual machines in a data center. If the virtual machines are
        suspended, this method resumes execution from the suspend point. The
        virtual machines can belong to different clusters in the data center.If
        any virtual machine in the list is manually managed by DRS, or DRS has to
        migrate any manually managed virtual machine or power on any manually
        managed host in order to power on these virtual machines, a DRS
        recommendation will be generated, and the users need to manually apply the
        recommendation for actually powering on these virtual machines. Otherwise,
        all the virtual machine will be automatically powered on. The virtual
        machines on stand alone hosts or DRS disabled will be powered-on on the
        current host. The DRS automatically managed virtual machines will be
        powered-on on the recommended hosts.When powering on a virtual machine in
        a cluster, the system might do an implicit relocation of the virtual
        machine to another host.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("PowerOnMultiVM_Task")()
        
