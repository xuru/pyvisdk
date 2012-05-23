
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def SSPIAuthentication(vim, *args, **kwargs):
    '''SSPIAuthentication contains the information necessary to initiate a ticketed
    authentication session in the guest using SSPI credentials. The ticketed
    session is not stateless and stores state inside of the guest.To use
    SSPIAuthentication, populate sspiToken with a base64 encoded SSPI token. Then
    call AcquireCredentialsInGuest with the SSPIAuthentication object and no
    sessionID. After issuing the AcquireCredentialsInGuest call, a
    GuestAuthenticationChallenge will be thrown. Use the serverChallenge sspiToken
    in GuestAuthenticationChallenge to generate the proper SSPI response token.
    Populate an SSPIAuthentication object with the base64 encoded SSPI response
    token, and call AcquireCredentialsInGuest with the SSPIAuthentication object
    and the sessionID found in GuestAuthenticationChallenge.Successful
    authentication will result in a TicketedSessionAuthentication object being
    returned. You can use the TicketedSessionAuthentication in any guest operations
    function call. You should NOT attempt to use SSPIAuthentication in any guest
    operations function call.When you no longer need the
    TicketedSessionAuthentication object, you should call ReleaseCredentialsInGuest
    to free associated resources and session data.Usage notes: SSPI authentication
    has the same limitations as a duplicated primary token obtained from the
    Windows API function LogonUser with the LOGON32_LOGON_NETWORK logon type. This
    will affect programs started with StartProgramInGuest. For example, launched
    programs will be unable to use WMI functions unless the "Remote Enable"
    privilege is enabled for the user. Similarly, access to network resources may
    fail due to the limitations of the token.'''
    
    obj = vim.client.factory.create('ns0:SSPIAuthentication')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'sspiToken', 'interactiveSession' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    