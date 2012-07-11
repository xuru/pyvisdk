
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PropertyCollector(BaseEntity):
    '''The PropertyCollector managed object retrieves and detects changes to the
    properties of other managed objects. The RetrievePropertiesEx method provides
    one-time property retrieval. The WaitForUpdatesEx method provides incremental
    change detection and supports both polling and notification.For change
    detection a client creates one or more filters to specify the subset of managed
    objects in which the client is interested. Filters keep per-session state to
    track incremental changes. Because this state is per-session:* A session cannot
    share its PropertyCollector filters with other sessions * two different clients
    can share the same session, and so can share the same filters, but this is not
    recommended * When a session terminates, the associated PropertyCollector
    filters are automatically destroyed.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.PropertyCollector):
        super(PropertyCollector, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def filter(self):
        '''The filters that this PropertyCollector uses to determine the list of
        properties for which it detects incremental changes.'''
        return self.update('filter')

    
    
    def CancelRetrievePropertiesEx(self, token):
        '''Discards remaining results from a retrieval started by RetrievePropertiesEx on
        the same session on the same PropertyCollector.
        
        :param token: the token returned in the previous RetrieveResult returned on the same session by the same PropertyCollector.
        
        '''
        return self.delegate("CancelRetrievePropertiesEx")(token)
    
    def CancelWaitForUpdates(self):
        '''Attempts to cancel outstanding calls to WaitForUpdates or WaitForUpdatesEx in
        the current session. If an update calculation is in process this method has no
        effect. If an update calculation is not in process any waiting calls complete
        quickly and report a RequestCanceled fault.
        
        '''
        return self.delegate("CancelWaitForUpdates")()
    
    def CheckForUpdates(self, version=None):
        '''<b>Deprecated.</b> <i>As of vSphere API 4.1, use WaitForUpdatesEx with a
        maxWaitSeconds of 0.</i> Checks for updates on properties specified by the
        union of all current filters. If no updates are pending, this method returns
        null.
        
        :param version: The data version currently known to the client. The value must be either * the special initial version (an empty string) * a data version returned from CheckForUpdates or WaitForUpdates by the same PropertyCollector on the same session. * a non-truncated data version returned from WaitForUpdatesEx by the same PropertyCollector on the same session.
        
        '''
        return self.delegate("CheckForUpdates")(version)
    
    def ContinueRetrievePropertiesEx(self, token):
        '''Retrieves additional results from a retrieval started by RetrievePropertiesEx
        on the same session on the same PropertyCollector.
        
        :param token: the token returned in the previous RetrieveResult returned on the same session by the same PropertyCollector.
        
        '''
        return self.delegate("ContinueRetrievePropertiesEx")(token)
    
    def CreateFilter(self, spec, partialUpdates):
        '''Creates a new filter for the given set of managed objects.
        
        :param spec: The specifications for the filter.
        
        :param partialUpdates: Flag to specify whether a change to a nested property should report only the nested change or the entire specified property value. If the value is true, a change should report only the nested property. If the value is false, a change should report the enclosing property named in the filter.
        
        '''
        return self.delegate("CreateFilter")(spec, partialUpdates)
    
    def CreatePropertyCollector(self):
        '''Creates a new session-specific PropertyCollector that can be used to retrieve
        property updates independent of any other PropertyCollector. The newly created
        PropertyCollector is not tied to the creating PropertyCollector in any way and
        exists until it is destroyed by a call to DestroyPropertyCollector or until the
        session on which the PropertyCollector was created is closed. This is in
        contrast to the default PropertyCollector, which always exists, but still has
        session-specific data such as filters and unfinished update calculations that
        are discarded when the associated session is closed.Creates a new session-
        specific PropertyCollector that can be used to retrieve property updates
        independent of any other PropertyCollector. The newly created PropertyCollector
        is not tied to the creating PropertyCollector in any way and exists until it is
        destroyed by a call to DestroyPropertyCollector or until the session on which
        the PropertyCollector was created is closed. This is in contrast to the default
        PropertyCollector, which always exists, but still has session-specific data
        such as filters and unfinished update calculations that are discarded when the
        associated session is closed.Creates a new session-specific PropertyCollector
        that can be used to retrieve property updates independent of any other
        PropertyCollector. The newly created PropertyCollector is not tied to the
        creating PropertyCollector in any way and exists until it is destroyed by a
        call to DestroyPropertyCollector or until the session on which the
        PropertyCollector was created is closed. This is in contrast to the default
        PropertyCollector, which always exists, but still has session-specific data
        such as filters and unfinished update calculations that are discarded when the
        associated session is closed.Creates a new session-specific PropertyCollector
        that can be used to retrieve property updates independent of any other
        PropertyCollector. The newly created PropertyCollector is not tied to the
        creating PropertyCollector in any way and exists until it is destroyed by a
        call to DestroyPropertyCollector or until the session on which the
        PropertyCollector was created is closed. This is in contrast to the default
        PropertyCollector, which always exists, but still has session-specific data
        such as filters and unfinished update calculations that are discarded when the
        associated session is closed.
        
        '''
        return self.delegate("CreatePropertyCollector")()
    
    def DestroyPropertyCollector(self):
        '''Destroys this PropertyCollector.Destroys this PropertyCollector.Destroys this
        PropertyCollector.
        
        '''
        return self.delegate("DestroyPropertyCollector")()
    
    def RetrieveProperties(self, specSet):
        '''<b>Deprecated.</b> <i>As of vSphere API 4.1, use RetrievePropertiesEx.</i>
        Retrieves the specified properties of the specified managed objects.
        
        :param specSet: Specifies the properties to retrieve.
        
        '''
        return self.delegate("RetrieveProperties")(specSet)
    
    def RetrievePropertiesEx(self, specSet, options):
        '''Retrieves the specified properties of the specified managed objects.Retrieves
        the specified properties of the specified managed objects.Retrieves the
        specified properties of the specified managed objects.
        
        :param specSet: Specifies the properties to retrieve.
        
        :param options: Additional method options. If omitted, equivalent to an options argument with no fields set.
        
        '''
        return self.delegate("RetrievePropertiesEx")(specSet, options)
    
    def WaitForUpdates(self, version=None):
        '''<b>Deprecated.</b> <i>As of vSphere API 4.1, use WaitForUpdatesEx.</i>
        Calculate the set of updates for each existing filter in the session, returning
        when at least one filter has updates.
        
        :param version: The data version currently known to the client. The value must be either * the special initial version (an empty string) * a data version returned from CheckForUpdates or WaitForUpdates by the same PropertyCollector on the same session * a non-truncated data version returned from WaitForUpdatesEx by the same PropertyCollector on the same session.
        
        '''
        return self.delegate("WaitForUpdates")(version)
    
    def WaitForUpdatesEx(self, version=None, options=None):
        '''Calculate the set of updates for each existing filter in the session.Calculate
        the set of updates for each existing filter in the session.Calculate the set of
        updates for each existing filter in the session.
        
        :param version: The data version currently known to the client. The value must be either * the special initial data version (an empty string), * a data version returned from CheckForUpdates or WaitForUpdates * a non-truncated data version returned from WaitForUpdatesEx * a truncated data version returned from the last call to WaitForUpdatesEx with no intervening calls to WaitForUpdates or CheckForUpdates.
        
        :param options: Additional options controlling the change calculation. If omitted, equivalent to an options argument with no fields set.
        
        '''
        return self.delegate("WaitForUpdatesEx")(version, options)