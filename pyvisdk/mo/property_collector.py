
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PropertyCollector(BaseEntity):
    '''The PropertyCollector managed object retrieves and detects changes to the
        properties of other managed objects. The RetrievePropertiesEx method
        provides one-time property retrieval. The WaitForUpdatesEx method provides
        incremental change detection and supports both polling and
        notification.For change detection a client creates one or more filters to
        specify the subset of managed objects in which the client is interested.
        Filters keep per-session state to track incremental changes. Because this
        state is per-session:
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.PropertyCollector):
        # MUST define these
        super(PropertyCollector, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def filter(self):
        '''The filters that this PropertyCollector uses to determine the list of properties
        for which it detects incremental changes.
        '''
        return self.update('filter')


    def CancelRetrievePropertiesEx(self, token):
        '''Discards remaining results from a retrieval started by RetrievePropertiesEx on the
        same session on the same PropertyCollector.

        :param token: the token returned in the previous RetrieveResult returned on the same session by
        the same PropertyCollector.

        '''
        
        return self.delegate("CancelRetrievePropertiesEx")(token)
        

    def CancelWaitForUpdates(self):
        '''Attempts to cancel outstanding calls to WaitForUpdates or WaitForUpdatesEx in the
        current session. If an update calculation is in process this method has no
        effect. If an update calculation is not in process any waiting calls
        complete quickly and report a RequestCanceled fault.
        '''
        
        return self.delegate("CancelWaitForUpdates")()
        

    def CheckForUpdates(self, version):
        '''Deprecated. As of vSphere API 4.1, use WaitForUpdatesEx with a maxWaitSeconds of
        0. Checks for updates on properties specified by the union of all current
        filters. If no updates are pending, this method returns null.

        :param version: The data version currently known to the client. The value must be either * the
        special initial version (an empty string) * a data version returned from
        CheckForUpdates or WaitForUpdates by the same PropertyCollector on the
        same session. * a non-truncated data version returned from
        WaitForUpdatesEx by the same PropertyCollector on the same session.


        :rtype: UpdateSet 

        '''
        
        return self.delegate("CheckForUpdates")(version)
        

    def ContinueRetrievePropertiesEx(self, token):
        '''Retrieves additional results from a retrieval started by RetrievePropertiesEx on
        the same session on the same PropertyCollector.

        :param token: the token returned in the previous RetrieveResult returned on the same session by
        the same PropertyCollector.


        :rtype: RetrieveResult 

        '''
        
        return self.delegate("ContinueRetrievePropertiesEx")(token)
        

    def CreateFilter(self, spec, partialUpdates):
        '''Creates a new filter for the given set of managed objects.

        :param spec: The specifications for the filter.

        :param partialUpdates: Flag to specify whether a change to a nested property should report only the
        nested change or the entire specified property value. If the value is
        true, a change should report only the nested property. If the value is
        false, a change should report the enclosing property named in the filter.


        :rtype: ManagedObjectReference to a PropertyFilter 

        '''
        
        return self.delegate("CreateFilter")(spec,partialUpdates)
        

    def CreatePropertyCollector(self):
        '''Creates a new session-specific PropertyCollector that can be used to retrieve
        property updates independent of any other PropertyCollector. The newly
        created PropertyCollector is not tied to the creating PropertyCollector in
        any way and exists until it is destroyed by a call to
        DestroyPropertyCollector or until the session on which the
        PropertyCollector was created is closed. This is in contrast to the
        default PropertyCollector, which always exists, but still has session-
        specific data such as filters and unfinished update calculations that are
        discarded when the associated session is closed.A new PropertyCollector
        can be useful when multiple modules or even multiple clients that share
        the same session need to create their own PropertyFilter objects and
        process updates independently. They may also be useful to allow important
        updates to be seen on one PropertyCollector while a large update is being
        calculated on another. The underlying issue that this addresses is that
        any call to WaitForUpdates, CheckForUpdates, or WaitForUpdatesEx does
        updates on all the filters created on a given PropertyCollector on a given
        session.A more subtle use of multiple PropertyCollector objects is implied
        by the fact that the returned version value for the various updates
        calculations is strongly ordered. The only way this can make sense is that
        two different versions calculated on the same PropertyCollector on the
        same session cannot ever be created in parallel. This means that multiple
        calls to WaitForUpdates, CheckForUpdates, or WaitForUpdatesEx made to the
        same PropertyCollector on the same session on different threads of the
        same client, or even on different clients that share the same session are
        still handled on the server serially. Use of different PropertyCollector
        instances allows the server to handle these calculations in
        parallel.Typically a service that supports the PropertyCollector managed
        object type will automatically create a default PropertyCollector and
        provide some way to obtain a reference to this PropertyCollector. If not,
        it will have to provide some service-specific way to create the a
        PropertyCollector.

        :rtype: ManagedObjectReference to a PropertyCollector 

        '''
        
        return self.delegate("CreatePropertyCollector")()
        

    def DestroyPropertyCollector(self):
        '''Destroys this PropertyCollector.A PropertyCollector that was created by
        CreatePropertyCollector is automatically destroyed when the session on
        which it was created is closed. This method can be used to destroy them
        explicitly.An automatically created PropertyCollector provided by a
        service is not session specific and may not be destroyed.
        '''
        
        return self.delegate("DestroyPropertyCollector")()
        

    def RetrieveProperties(self, specSet):
        '''Deprecated. As of vSphere API 4.1, use RetrievePropertiesEx. Retrieves the
        specified properties of the specified managed objects.

        :param specSet: Specifies the properties to retrieve.


        :rtype: ObjectContent[] 

        '''
        
        return self.delegate("RetrieveProperties")(specSet)
        

    def RetrievePropertiesEx(self, specSet, options):
        '''Retrieves the specified properties of the specified managed objects.This method is
        similar to creating the filters, receiving the property values, and
        destroying the filters. The main difference is that the output blends the
        results from all the filters and reports a given managed object at most
        once no matter how many filters apply.The filter creation step can throw
        all of the same faults as CreateFilter.

        :param specSet: Specifies the properties to retrieve.

        :param options: Additional method options. If omitted, equivalent to an options argument with no
        fields set.


        :rtype: RetrieveResult 

        '''
        
        return self.delegate("RetrievePropertiesEx")(specSet,options)
        

    def WaitForUpdates(self, version):
        '''Deprecated. As of vSphere API 4.1, use WaitForUpdatesEx. Calculate the set of
        updates for each existing filter in the session, returning when at least
        one filter has updates.

        :param version: The data version currently known to the client. The value must be either * the
        special initial version (an empty string) * a data version returned from
        CheckForUpdates or WaitForUpdates by the same PropertyCollector on the
        same session * a non-truncated data version returned from WaitForUpdatesEx
        by the same PropertyCollector on the same session.


        :rtype: UpdateSet 

        '''
        
        return self.delegate("WaitForUpdates")(version)
        

    def WaitForUpdatesEx(self, version, options):
        '''Calculate the set of updates for each existing filter in the
        session.WaitForUpdatesEx may return only partial update calculations. See
        truncated for a more detailed explanation. WaitForUpdatesEx may also
        return null after a timeout, either as requested by maxWaitSeconds or due
        to PropertyCollector policy.If an application uses waitForUpdatesEx it is
        strongly recommended that it not make concurrent calls to WaitForUpdates,
        CheckForUpdates, or WaitForUpdatesEx in the same session. Concurrent calls
        may cause suspended change calculations to be discarded.

        :param version: The data version currently known to the client. The value must be either * the
        special initial data version (an empty string), * a data version returned
        from CheckForUpdates or WaitForUpdates * a non-truncated data version
        returned from WaitForUpdatesEx * a truncated data version returned from
        the last call to WaitForUpdatesEx with no intervening calls to
        WaitForUpdates or CheckForUpdates.

        :param options: Additional options controlling the change calculation. If omitted, equivalent to
        an options argument with no fields set.


        :rtype: UpdateSet 

        '''
        
        return self.delegate("WaitForUpdatesEx")(version,options)
        
