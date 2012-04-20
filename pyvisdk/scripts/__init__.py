

def main():
        from optparse import OptionParser
        from ..vim import Vim
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
