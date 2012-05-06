
from infi.pyutils.lazy import cached_method
from pyvisdk.do.traversal_spec import TraversalSpec
from pyvisdk.do.selection_spec import SelectionSpec
from pyvisdk.do.wait_options import WaitOptions
from logging import getLogger
from re import match, findall
from bunch import Bunch

logger = getLogger(__name__)

INITIAL_VERSION = ''
NESTED_PROPERTY_PATTERN = r'(?P<name>.*)\["(?P<key>.*)"\]'

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
                getattr(self, '_propertiesList', []), getattr(self, '_version', repr('')))
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
        wait_options = WaitOptions(self._vim, maxWaitSeconds=time_in_seconds)
        logger.debug("Checking for updates on property collector {!r}".format(self))
        update = property_collector.WaitForUpdatesEx(truncated_version or self._version,
                                                     wait_options)
        logger.debug("There is {} pending update".format('no' if update is None else 'indeed an'))
        return update

    def _refToString(self, ref):
        return "{}:{}".format(ref._type, ref.value)

    def _mergeObjectUpdateIntoCache__enter(self, key, objectUpdate):
        # Rebuild the properties dict
        properties = {propertyChange.name:propertyChange.val
                      for propertyChange in filter(lambda propertyChange:propertyChange.op in ['add', 'assign'],
                                                   objectUpdate.changeSet)}
        logger.debug("Replacing cache for key {}with a dictionary of the following keys {}".format(key, properties.keys()))
        self._result[key] = properties

    def _mergeObjectUpdateIntoCache__leave(self, key, objectUpdate=None):
        # the object no longer exists, we drop it from the result dictionary
        logger.debug("Removing key {} from cache".format(key))
        _ = self._result.pop(key, None)

    def _get_list_to_be_merged(self, object_to_update, property_path, stop_before_last=False):
        list_to_update = []
        while len(property_path) > (1 if stop_before_last else 0):
            matched = match(NESTED_PROPERTY_PATTERN, property_path[0])
            if matched:
                list_to_update = getattr(object_to_update, matched.group('name'))
                object_to_update = filter(lambda item: item.key == matched.group('key'), list_to_update)[:1]
                object_to_update = object_to_update.pop() if object_to_update else None
            else:
                object_to_update = getattr(object_to_update, property_path[0])
            _ = property_path.pop(0)
        return list_to_update, object_to_update

    def _split_property_path(self, key):
        return findall(r"[A-Za-z]*\[[^\]]+\]", key)

    def _get_list_and_object_to_update(self, property_dict, key, value, stop_before_last=False):
        key_to_update = filter(lambda prefix: key.startswith(prefix), property_dict.keys())[0]
        key = key.replace(key_to_update, '')
        object_to_update = Bunch(property_dict)
        property_path = self._split_property_path(key)
        if property_path[0].startswith('['):
            property_path[0] = "{}{}".format(key_to_update, property_path[0])
        else:
            property_path.insert(0, key_to_update)
        list_to_update, object_to_update = self._get_list_to_be_merged(object_to_update, property_path, stop_before_last)
        return list_to_update, object_to_update

    def _mergePropertyChange__add(self, property_dict, key, value):
        # http://vijava.sourceforge.net/vSphereAPIDoc/ver5/ReferenceGuide/vmodl.query.PropertyCollector.Change.html
        list_to_update, object_to_update = self._get_list_and_object_to_update(property_dict, key, value)
        logger.debug("Appending {}".format(value.__class__))
        list_to_update.insert(-1, value)

    def _mergePropertyChange__assign(self, property_dict, key, value):
        # http://vijava.sourceforge.net/vSphereAPIDoc/ver5/ReferenceGuide/vmodl.query.PropertyCollector.Change.html
        list_to_update, object_to_update = self._get_list_and_object_to_update(property_dict, key, value, True)
        key = key.split('.')[-1]
        logger.debug("Assigning {} to {}".format(value.__class__, key))
        setattr(object_to_update, key, value)

    def _mergePropertyChange__remove(self, property_dict, key, value):
        # http://vijava.sourceforge.net/vSphereAPIDoc/ver5/ReferenceGuide/vmodl.query.PropertyCollector.Change.html
        list_to_update, object_to_update = self._get_list_and_object_to_update(property_dict, key, value)
        for index in range(len(list_to_update)):
            value = list_to_update[index]
            if value.key == object_to_update.key:
                break
        logger.debug("Removing {}".format(value.__class__))
        list_to_update.remove(value)

    def _mergeObjectUpdateIntoCache__modify(self, key, objectUpdate):
        # http://vijava.sourceforge.net/vSphereAPIDoc/ver5/ReferenceGuide/vmodl.query.PropertyCollector.ObjectUpdate.html
        # http://vijava.sourceforge.net/vSphereAPIDoc/ver5/ReferenceGuide/vmodl.query.PropertyCollector.Change.html
        # http://vijava.sourceforge.net/vSphereAPIDoc/ver5/ReferenceGuide/vmodl.query.PropertyCollector.MissingProperty.html
        properties = self._result[key]
        logger.debug("Modifying cache for key {}".format(key))
        updatemethods = dict(add=self._mergePropertyChange__add,
                             assign=self._mergePropertyChange__assign,
                             remove=self._mergePropertyChange__remove,
                             indirectRemove=self._mergePropertyChange__remove)
        for propertyChange in objectUpdate.changeSet:
            logger.debug("Modifying property {}, operation {}".format(propertyChange.name, propertyChange.op))
            updatemethods[propertyChange.op](properties, propertyChange.name, propertyChange.val)
        for missingSet in objectUpdate.missingSet:
            logger.debug("Removing from cache a property that has gone missing{}".format(missingSet.path))
            self._mergePropertyChange__remove(properties, missingSet.path, None)

    def _mergeObjectUpdateIntoCache(self, objectUpdate):
        # http://vijava.sourceforge.net/vSphereAPIDoc/ver5/ReferenceGuide/vmodl.query.PropertyCollector.ObjectUpdate.html
        updateMethods = dict(enter=self._mergeObjectUpdateIntoCache__enter,
                             leave=self._mergeObjectUpdateIntoCache__leave,
                             modify=self._mergeObjectUpdateIntoCache__modify)
        key = self._refToString(objectUpdate.obj.ref)
        logger.debug("Update kind {} on cache key {}".format(objectUpdate.kind, key))
        updateMethods[objectUpdate.kind](key, objectUpdate)

    def _mergeChangesIntoCache(self, update):
        # http://vijava.sourceforge.net/vSphereAPIDoc/ver5/ReferenceGuide/vmodl.query.PropertyCollector.UpdateSet.html
        # http://vijava.sourceforge.net/vSphereAPIDoc/ver5/ReferenceGuide/vmodl.query.PropertyCollector.FilterUpdate.html
        filterSet = update.filterSet[0]
        for key in map(lambda missingObject: self._refToString(missingObject.obj), filterSet.missingSet):
            logger.debug("Removing key {} from cache because it is missing in the filterSet".format(key))
            _ = self._result.pop(key, None)
        for objectUpdate in filterSet.objectSet:
            self._mergeObjectUpdateIntoCache(objectUpdate)
        if update.truncated:
            self._mergeChangesIntoCache(self._getChanges(0, update.version))
        else:
            self._version = update.version
            logger.debug("Cache is updated for version {}".format(self._version))

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
