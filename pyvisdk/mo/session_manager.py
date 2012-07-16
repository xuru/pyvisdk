
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class SessionManager(BaseEntity):
    '''This managed object type includes methods for logging on and logging off
    clients, determining which clients are currently logged on, and forcing clients
    to log off.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.SessionManager):
        super(SessionManager, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def currentSession(self):
        '''This property contains information about the client's current session. If the
        client is not logged on, the value is null.'''
        return self.update('currentSession')
    @property
    def defaultLocale(self):
        '''This is the default server locale.'''
        return self.update('defaultLocale')
    @property
    def message(self):
        '''The system global message from the server.'''
        return self.update('message')
    @property
    def messageLocaleList(self):
        '''Provides the list of locales for which the server has localized messages.'''
        return self.update('messageLocaleList')
    @property
    def sessionList(self):
        '''The list of currently active sessions.'''
        return self.update('sessionList')
    @property
    def supportedLocaleList(self):
        '''Provides the list of locales that the server supports. Listing a locale ensures
        that some standardized information such as dates appear in the appropriate
        format. Other localized information, such as error messages, are displayed, if
        available. If localized information is not available, the message is returned
        using the system locale.'''
        return self.update('supportedLocaleList')

    
    
    def AcquireCloneTicket(self):
        '''Acquire a session-specific ticket string which can be used to clone the current
        session. The caller of this operation can pass the ticket value to another
        entity on the client. The recipient can then call CloneSession with the ticket
        string on an unauthenticated session and avoid having to re-enter
        credentials.Acquire a session-specific ticket string which can be used to clone
        the current session. The caller of this operation can pass the ticket value to
        another entity on the client. The recipient can then call CloneSession with the
        ticket string on an unauthenticated session and avoid having to re-enter
        credentials.Acquire a session-specific ticket string which can be used to clone
        the current session. The caller of this operation can pass the ticket value to
        another entity on the client. The recipient can then call CloneSession with the
        ticket string on an unauthenticated session and avoid having to re-enter
        credentials.
        
        '''
        return self.delegate("AcquireCloneTicket")()
    
    def AcquireGenericServiceTicket(self, spec):
        '''Creates and returns a one-time credential that may be used to make the
        specified request.
        
        :param spec: specification for the service request which will be invoked with the ticket.
        
        '''
        return self.delegate("AcquireGenericServiceTicket")(spec)
    
    def AcquireLocalTicket(self, userName):
        '''Acquires a one-time ticket for mutual authentication between a server and
        client.Acquires a one-time ticket for mutual authentication between a server
        and client.Acquires a one-time ticket for mutual authentication between a
        server and client.Acquires a one-time ticket for mutual authentication between
        a server and client.
        
        :param userName: User requesting one-time password.
        
        '''
        return self.delegate("AcquireLocalTicket")(userName)
    
    def CloneSession(self, cloneTicket):
        '''Clone the session specified by the clone ticket and associate it with the
        current connection. The current session will take on the identity and
        authorization level of the UserSession associated with the specified cloning
        ticket.See AcquireCloneTicket
        
        :param cloneTicket: ticket string acquired via AcquireCloneTicket.See AcquireCloneTicket
        
        '''
        return self.delegate("CloneSession")(cloneTicket)
    
    def ImpersonateUser(self, userName, locale=None):
        '''Converts current session to impersonate the specified user. The current session
        will take on the identity and authorization level of the user. That user must
        have a currently-active session. If the given userName is an extension key and
        this key does not overlap with a user name of any currently-active session, it
        will take on the identity and authorization level of that extension provided
        the current session has the same authorization level of that extension.
        
        :param userName: The user or extension key to impersonate.
        
        :param locale: A two-character ISO-639 language ID (like "en") optionally followed by an underscore and a two-character ISO 3166 country ID (like "US").
        
        '''
        return self.delegate("ImpersonateUser")(userName, locale)
    
    def Login(self, userName, password, locale=None):
        '''Log on to the server. This method fails if the user name and password are
        incorrect, or if the user is valid but has no permissions granted.
        
        :param userName: The ID of the user who is logging on to the server.
        
        :param password: The password of the user who is logging on to the server.
        
        :param locale: A two-character ISO-639 language ID (like "en") optionally followed by an underscore and a two-character ISO 3166 country ID (like "US").
        
        '''
        return self.delegate("Login")(userName, password, locale)
    
    def LoginBySSPI(self, base64Token, locale=None):
        '''Log on to the server using SSPI pass-through authentication.Log on to the
        server using SSPI pass-through authentication.Log on to the server using SSPI
        pass-through authentication.Log on to the server using SSPI pass-through
        authentication.Log on to the server using SSPI pass-through authentication.Log
        on to the server using SSPI pass-through authentication.
        
        :param base64Token: The partially formed context returned from InitializeSecurityContext().
        
        :param locale: A two-character ISO-639 language ID (like "en") optionally followed by an underscore and a two-character ISO 3166 country ID (like "US").
        
        '''
        return self.delegate("LoginBySSPI")(base64Token, locale)
    
    def LoginExtensionByCertificate(self, extensionKey, locale=None):
        '''Creates a special privileged session that includes the Sessions.ImpersonateUser
        privilege. Requires that the client connect over SSL and provide an X.509
        certificate for which they hold the private key. The certificate must match the
        certificate used in an earlier call to SetExtensionCertificate.Creates a
        special privileged session that includes the Sessions.ImpersonateUser
        privilege. Requires that the client connect over SSL and provide an X.509
        certificate for which they hold the private key. The certificate must match the
        certificate used in an earlier call to SetExtensionCertificate.
        
        :param extensionKey: Key of extension that is logging in.
        
        :param locale: A two-character ISO-639 language ID (like "en") optionally followed by an underscore and a two-character ISO 3166 country ID (like "US").
        
        '''
        return self.delegate("LoginExtensionByCertificate")(extensionKey, locale)
    
    def LoginExtensionBySubjectName(self, extensionKey, locale=None):
        '''Creates a special privileged session that includes the Sessions.ImpersonateUser
        privilege. Requires that the extension connected using SSL, with a certificate
        that has a subject name that matches the subject name registered for the
        extension.Creates a special privileged session that includes the
        Sessions.ImpersonateUser privilege. Requires that the extension connected using
        SSL, with a certificate that has a subject name that matches the subject name
        registered for the extension.
        
        :param extensionKey: Key of extension that is logging in.
        
        :param locale: A two-character ISO-639 language ID (like "en") optionally followed by an underscore and a two-character ISO 3166 country ID (like "US").
        
        '''
        return self.delegate("LoginExtensionBySubjectName")(extensionKey, locale)
    
    def Logout(self):
        '''Log out and terminate the current session.
        
        '''
        return self.delegate("Logout")()
    
    def SessionIsActive(self, sessionID, userName):
        '''Validates that a currently-active session exists with the specified sessionID
        and userName associated with it. Returns true if session exists.
        
        :param sessionID: Session ID to validate.
        
        :param userName: User name to validate.
        
        '''
        return self.delegate("SessionIsActive")(sessionID, userName)
    
    def SetLocale(self, locale):
        '''Sets the session locale.
        
        :param locale: A two-character ISO-639 language ID (like "en") optionally followed by an underscore and a two-character ISO 3166 country ID (like "US").
        
        '''
        return self.delegate("SetLocale")(locale)
    
    def TerminateSession(self, sessionId):
        '''Log off and terminate the provided list of sessions.Log off and terminate the
        provided list of sessions.
        
        :param sessionId: A list of sessions to terminate.
        
        '''
        return self.delegate("TerminateSession")(sessionId)
    
    def UpdateServiceMessage(self, message):
        '''Updates the system global message. If not blank, the message is immediately
        displayed to currently logged-on users. When set, the message is shown by new
        clients upon logging in.
        
        :param message: The message to send. Newline characters may be included.
        
        '''
        return self.delegate("UpdateServiceMessage")(message)