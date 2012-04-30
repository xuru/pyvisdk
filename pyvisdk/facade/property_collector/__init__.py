
from infi.pyutils.lazy import cached_method
from pyvisdk.do.traversal_spec import TraversalSpec
from pyvisdk.do.selection_spec import SelectionSpec
from pyvisdk.do.wait_options import WaitOptions

INITIAL_VERSION = ''

class CachedPropertyCollector(object):
    """
    Facade for using PropertyCollectors to fetch a list of properties from all instances of a specific object_type
    
    :param vim: :py:class:`Vim` instance
    :param managedObjectTypeName: A name of managed object type, e.g. HostSystem
    :param propertiesList: A list of properties to fetch, can be nested, e.g. config.storageDevice
    """
    def __init__(self, vim, managedObjectTypeName, propertiesList):
        super(CachedPropertyCollector, self).__init__()
        self._vim = vim
        self._managedObjectTypeName = managedObjectTypeName
        self._propertiesList = propertiesList
        self._version = INITIAL_VERSION
        self._result = {}

    def __repr__(self):
        args = (self.__class__.__name__, getattr(self, '_managedObjectTypeName', None),
                getattr(self, '_propertiesList', []), getattr(self, '', repr('')))
        return "<{}: objectType={!r}, properties={!r}, version={}>".format(*args)

    def _guessTraversalSpecName(self, managed_object_type_name, property_name):
        """:returns: A guessable name of a TraversalSpec being used in this facade"""
        name = "{}.{}".format(managed_object_type_name, property_name)
        return name

    def _createTraversalSpec(self, managed_object_type_name, property_name, next_selector_names=[]):
        """:returns: a TravelSpec object whose name is '{managed_object_type_name}.{property_name}'"""
        return TraversalSpec(self._vim, name=self._guessTraversalSpecName(managed_object_type_name, property_name),
                             type=managed_object_type_name, path=property_name,
                             selectSet=[SelectionSpec(self._vim, name=name) for name in next_selector_names])

    @cached_method
    def _getContainerView(self):
        kwargs = dict(container=self._vim.root, type=[self._managedObjectTypeName], recursive=True)
        return self._vim.service_content.viewManager.CreateContainerView(**kwargs)

    @cached_method
    def _getObjectSet(self):
        from pyvisdk.do.object_spec import ObjectSpec
        return ObjectSpec(self._vim, obj=self._getContainerView().ref,
                          selectSet=self._getSelectSet())

    @cached_method
    def _getPropSet(self):
        from pyvisdk.do.property_spec import PropertySpec
        return [PropertySpec(self._vim, type=self._managedObjectTypeName, pathSet=self._propertiesList)]

    @cached_method
    def _getPropertyCollector(self):
        property_collector = self._vim.service_content.propertyCollector.CreatePropertyCollector()
        property_collector.CreateFilter(self._getPropertyFilterSpec(), partialUpdates=True)
        return property_collector

    @cached_method
    def _getPropertyFilterSpec(self):
        # http://vijava.sourceforge.net/vSphereAPIDoc/ver5/ReferenceGuide/vmodl.query.PropertyCollector.FilterSpec.html
        from pyvisdk.do.property_filter_spec import PropertyFilterSpec
        return PropertyFilterSpec(self._vim, propSet=self._getPropSet(),
                                  objectSet=[self._getObjectSet()])

    @cached_method
    def _getSelectSet(self):
        """This method returns a SelectSet that travels the entire heirarchy.
        If you want to go over heirarchy in a more efficient way, overload this method"""
        select_set = list(self._vim._buildFullTraversal())
        select_set.append(self._createTraversalSpec("ContainerView", 'container',
                          [select.name for select in select_set]))
        return select_set

    def _getChanges(self, time_in_seconds=0, truncated_version=None):
        # http://vijava.sourceforge.net/vSphereAPIDoc/ver5/ReferenceGuide/vmodl.query.PropertyCollector.html#waitForUpdatesEx
        property_collector = self._getPropertyCollector()
        update = property_collector.WaitForUpdatesEx(truncated_version or self._version ,
                                                     WaitOptions(self._vim, maxWaitSeconds=time_in_seconds))
        return update

    def _refToString(self, ref):
        return "{}.{}".format(ref._type, ref.value)

    def _mergeObjectUpdateIntoCache__enter(self, objectUpdate):
        # Rebuild the properties dict
        properties = {propertyChange.name:propertyChange.val
                      for propertyChange in filter(lambda propertyChange:propertyChange.op in ['add', 'assign'],
                                                   objectUpdate.changeSet)}
        self._result[self._refToString(objectUpdate.obj)] = properties

    def _mergeObjectUpdateIntoCache__leave(self, objectUpdate):
        # the object no longer exists, we drop it from the result dictionary
        _ = self._result.pop(self._refToString(objectUpdate.obj), None)

    def _mergeObjectUpdateIntoCache__modify(self, objectUpdate, properties, propertyChange):
        properties = self._result[self._refToString(objectUpdate.obj)]
        for propertyChange in objectUpdate.changeSet:
            if propertyChange.op in ['add', 'assign']:
                properties[propertyChange.name] = propertyChange.val
            else:
                _ = properties.pop(propertyChange.name, None)
        for missingSet in objectUpdate.missingSet:
                _ = properties.pop(missingSet.path, None)

    def _mergeObjectUpdateIntoCache(self, objectUpdate):
        # http://vijava.sourceforge.net/vSphereAPIDoc/ver5/ReferenceGuide/vmodl.query.PropertyCollector.Change.html
        updateMethods = dict(enter=self._mergeObjectUpdateIntoCache__enter,
                             leave=self._mergeObjectUpdateIntoCache__leave,
                             modify=self._mergeObjectUpdateIntoCache__modify)
        updateMethods[objectUpdate.kind](objectUpdate)

    def _mergeChangesIntoCache(self, update):
        # http://vijava.sourceforge.net/vSphereAPIDoc/ver5/ReferenceGuide/vmodl.query.PropertyCollector.UpdateSet.html
        # http://vijava.sourceforge.net/vSphereAPIDoc/ver5/ReferenceGuide/vmodl.query.PropertyCollector.FilterUpdate.html
        filterSet = update.filterSet[0]
        for key in map(lambda missingObject: self._refToString(missingObject.obj), filterSet.missingSet):
            _ = self._result.pop(key, None)
        for objectUpdate in filterSet.objectSet:
            self._mergeObjectUpdateIntoCache(objectUpdate)
        if update.truncated:
            self._mergeChangesIntoCache(self._getChanges(0, update.version))
        else:
            self._version = update.version

    def checkForUpdates(self):
        """:returns: True if the cached data is not up to date"""
        return self.waitForUpdates(0)

    def getProperties(self):
        """This method checks first if there are changes in the server.
        If there are, the changes are merged into the cache and then returned from the cache.
        If there are not, the data is returned from the cache.
        :rtype: a dictionary with MoRefs as keys, and propertyName=propertyValue dictionary as values"""

        update = self._getChanges()
        if update is not None:
            self._mergeChangesIntoCache(update)
        return self.getPropertiesFromCache()

    def getPropertiesFromCache(self):
        """:returns: the cached properties immediately from the cache.
        :rtype: a dictionary with MoRefs as keys, and propertyName=propertyValue dictionary as values"""
        return self._result

    def waitForUpdates(self, time_in_seconds):
        """This method is blocking a maximum time of time_in_seconds, depending if there are changes on the server.
        This method does not update the cache with the changes, if there are any.
        :returns: True if there are updates on the server, False if there are not."""
        update = self._getChanges(time_in_seconds)
        return update is not None

class HostSystemCachedPropertyCollector(CachedPropertyCollector):
    """
    Facade for fetching host attributes by using a faster traversal (e.g no need to traverse inside HostSystem) 
    """

    def __init__(self, vim, hostProperties):
        super(HostSystemCachedPropertyCollector, self).__init__(vim, 'HostSystem', hostProperties)

    @cached_method
    def _getSelectSet(self):
        #TODO docstring
        select_set = list()
        select_set.append(self._createTraversalSpec("ClusterComputeResource", 'host'))
        select_set.append(self._createTraversalSpec("ComputeResource", 'host'))
        select_set.append(self._createTraversalSpec("Datacenter", 'hostFolder',
                          ['Folder.childEntity']))
        select_set.append(self._createTraversalSpec("Folder", 'childEntity',
                          ['Datacenter.hostFolder', 'ClusterComputeResource.host', 'ComputeResource.host']))
        select_set.append(self._createTraversalSpec("ContainerView", 'container',
                          [select.name for select in select_set]))
        return select_set
