
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class SessionManager(BaseEntity):
    '''This managed object type includes methods for logging on and logging off clients,
        determining which clients are currently logged on, and forcing clients to
        log off.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.SessionManager):
        # MUST define these
        super(SessionManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def currentSession(self):
        '''
        This property contains information about the client's current session. If the
        client is not logged on, the value is null.
        '''
        return self.update('currentSession')

    @property
    def defaultLocale(self):
        '''
        This is the default server locale.
        '''
        return self.update('defaultLocale')

    @property
    def message(self):
        '''
        The system global message from the server.
        '''
        return self.update('message')

    @property
    def messageLocaleList(self):
        '''
        Provides the list of locales for which the server has localized messages.
        '''
        return self.update('messageLocaleList')

    @property
    def sessionList(self):
        '''
        The list of currently active sessions.
        '''
        return self.update('sessionList')

    @property
    def supportedLocaleList(self):
        '''
        Provides the list of locales that the server supports. Listing a locale ensures
        that some standardized information such as dates appear in the appropriate
        format. Other localized information, such as error messages, are
        displayed, if available. If localized information is not available, the
        message is returned using the system locale.
        '''
        return self.update('supportedLocaleList')


    def TerminateSession(self, sessionId):
        '''Log off and terminate the provided list of sessions.This method is only
        transactional for each session ID. The set of sessions are terminated
        sequentially, as specified in the list. If a failure occurs, for example,
        because of an unknown sessionID, the method aborts with an exception. When
        the method aborts, any sessions that have not yet been terminated are left
        in their unterminated state.

        :param sessionId: A list of sessions to terminate.

        '''
        
        return self.delegate("TerminateSession")(sessionId)
        

    def LoginExtensionByCertificate(self, extensionKey):
        '''Creates a special privileged session that includes the Sessions.ImpersonateUser
        privilege. Requires that the client connect over SSL and provide an X.509
        certificate for which they hold the private key. The certificate must
        match the certificate used in an earlier call to
        SetExtensionCertificate.NOTE: Verification of the received certificate
        (such as expiry, revocation, and trust chain) is not required for
        successful authentication using this method. If certificate verification
        is desired, use the LoginExtensionBySubjectName method instead.

        :param extensionKey: Key of extension that is logging in.


        :rtype: UserSession 

        '''
        
        return self.delegate("LoginExtensionByCertificate")(extensionKey)
        

    def AcquireLocalTicket(self, userName):
        '''Acquires a one-time ticket for mutual authentication between a server and
        client.The caller of this operation can use the user name and file content
        of the returned object as the userName and password arguments for login
        operation. The local ticket that is returned becomes invalid either after
        it is used or after a server-determined ticket expiration time passes.
        This operation can be used by servers and clients to avoid re-entering
        user credentials after authentication by the operating system has already
        happened.For example, service console utilities that connect to a host
        agent should not require users to re-enter their passwords every time the
        utilities run. Since the one-time password file is readable only by the
        given user, the identity of the one-time password user is protected by the
        operating system file permission.Only local clients are allowed to call
        this operation. Remote clients receive an InvalidRequest fault upon
        calling this operation.

        :param userName: User requesting one-time password.


        :rtype: SessionManagerLocalTicket 

        '''
        
        return self.delegate("AcquireLocalTicket")(userName)
        

    def AcquireCloneTicket(self):
        '''Acquire a session-specific ticket string which can be used to clone the current
        session. The caller of this operation can pass the ticket value to another
        entity on the client. The recipient can then call CloneSession with the
        ticket string on an unauthenticated session and avoid having to re-enter
        credentials.The ticket may only be used once and becomes invalid after
        use. The ticket is also invalidated when the corresponding session is
        closed or expires. The ticket is only valid on the server which issued
        it.This sequence of operations is conceptually similar to the
        functionality provided by AcquireLocalTicket, however the methods can be
        used by remote clients and do not require a shared filesystem for
        transport. See CloneSession

        :rtype: xsd:string 

        '''
        
        return self.delegate("AcquireCloneTicket")()
        

    def SetLocale(self):
        '''Sets the session locale.
        '''
        
        return self.delegate("SetLocale")()
        

    def LoginBySSPI(self, base64Token):
        '''Log on to the server using SSPI pass-through authentication.This method provides
        support for passing credentials of the calling process to the server
        without using a password, by leveraging the Windows Security Support
        Provider Interface (SSPI) library.If the function is not supported, this
        throws a NotSupported fault.The client first calls
        AcquireCredentialsHandle(). If Kerberos is used, this should include the
        desired credential to pass. The client then calls
        InitializeSecurityContext(). The resulting partially-formed context is
        passed in Base-64 encoded form to this method.If the context has been
        successfully formed, the server proceeds with login and behaves like
        Login. If further negotiation is needed, the server throws an
        SSPIChallenge fault with a challenge token, which the client should again
        pass to InitializeSecurityContext(), followed by calling this method
        again.For more information, see the MSDN documentation on SSPI.

        :param base64Token: The partially formed context returned from InitializeSecurityContext().


        :rtype: UserSession 

        '''
        
        return self.delegate("LoginBySSPI")(base64Token)
        

    def SessionIsActive(self, userName, sessionID):
        '''Validates that a currently-active session exists with the specified sessionID and
        userName associated with it. Returns true if session exists.

        :param userName: User name to validate.

        :param sessionID: Session ID to validate.


        :rtype: xsd:boolean 

        '''
        
        return self.delegate("SessionIsActive")(userName,sessionID)
        

    def ImpersonateUser(self, userName):
        '''Converts current session to impersonate the specified user. The current session
        will take on the identity and authorization level of the user. That user
        must have a currently-active session. If the given userName is an
        extension key and this key does not overlap with a user name of any
        currently-active session, it will take on the identity and authorization
        level of that extension provided the current session has the same
        authorization level of that extension.

        :param userName: The user or extension key to impersonate.


        :rtype: UserSession 

        '''
        
        return self.delegate("ImpersonateUser")(userName)
        

    def Logout(self):
        '''Log out and terminate the current session.
        '''
        
        return self.delegate("Logout")()
        

    def UpdateServiceMessage(self, message):
        '''Updates the system global message. If not blank, the message is immediately
        displayed to currently logged-on users. When set, the message is shown by
        new clients upon logging in.

        :param message: The message to send. Newline characters may be included.

        '''
        
        return self.delegate("UpdateServiceMessage")(message)
        

    def CloneSession(self):
        '''Clone the session specified by the clone ticket and associate it with the current
        connection. The current session will take on the identity and
        authorization level of the UserSession associated with the specified
        cloning ticket. See AcquireCloneTicket

        :rtype: UserSession 

        '''
        
        return self.delegate("CloneSession")()
        

    def Login(self, userName, password):
        '''Log on to the server. This method fails if the user name and password are
        incorrect, or if the user is valid but has no permissions granted.

        :param userName: The ID of the user who is logging on to the server.

        :param password: The password of the user who is logging on to the server.


        :rtype: UserSession 

        '''
        
        return self.delegate("Login")(userName,password)
        

    def LoginExtensionBySubjectName(self, extensionKey):
        '''Creates a special privileged session that includes the Sessions.ImpersonateUser
        privilege. Requires that the extension connected using SSL, with a
        certificate that has a subject name that matches the subject name
        registered for the extension.As of vSphere API 4.0, the NotFound fault is
        no longer thrown. Instead, InvalidLogin is thrown if the specified
        extension is not registered.

        :param extensionKey: Key of extension that is logging in.


        :rtype: UserSession 

        '''
        
        return self.delegate("LoginExtensionBySubjectName")(extensionKey)
        
