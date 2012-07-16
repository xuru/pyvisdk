'''
Created on Mar 8, 2011

@author: eplaster
'''
import suds.sax, logging, types

from pyvisdk.base.managed_object_types import ManagedObjectTypes

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

class ManagedObjectReference(suds.sudsobject.Property):
    """Custom class to replace the suds generated class, which lacks _type."""
    def __init__(self, _type, value):
        suds.sudsobject.Property.__init__(self, value)
        self._type = _type

class TaskDelegate(object):
    """ delegates to the real method, and waits for the task to complete"""

    def __init__(self, cls, name):
        """ Initializes the delagate with the method to proxy """
        self.__target = getattr(cls.service, name)
        self.name = name
        self.cls = cls

    def __call__(self, *args, **kwargs):
        """ calls original method """
        log.debug("Calling %s" % self.__target.method.name)
        if len(args):
            _list = []
            for x in list(args):
                if x.__class__.__name__ in ManagedObjectTypes:
                    _list.append(x.ref)
                else:
                    _list.append(x)
            _list.insert(0, self.cls.ref)
            args = _list
        else:
            args = (self.cls.ref,)
        rv = self.__target(*args, **kwargs)
        if self.name[-5:] == '_Task' and self.cls.core.wait_for_task:
            log.debug("Waiting for task to Complete")
            self.cls.core.waitForTask(rv)
        if self.__target.method.name in ["RetrieveProperties", "RetrievePropertiesEx"]:
            return rv
        else:
            return self.cls.core._parse_object_content(rv)

    def _return_value(self, rv):
        if isinstance(rv, list):
            return [self._return_value(x) for x in rv]
        if 'suds.sudsobject' in str(rv.__class__):
            new_obj = eval("pyvisdk.do.%s()" % rv.__class__.__name__)
            for attr in dir(rv):
                if attr[0] != '_':
                    if isinstance(attr, suds.sax.text.Text):
                        new_obj.data[str(attr)] = str(eval('rv.%s' % attr))
                    elif 'suds.sudsobject' in str(eval('rv.%s' % attr)):
                        new_obj.data[str(attr)] = self._return_value(eval('rv.%s' % attr))
                    else:
                        new_obj.data[str(attr)] = eval("rv.%s" % attr)
            return new_obj
        else:
            return rv


class BaseEntity(object):
    def __init__(self, core, name=None, ref=None, type=None):
        self.core = core
        self._name = name
        self.ref = ref
        self._type = type

        self.client = core.client
        self.service = core.client.service

        if self.ref:
            self.ref = ManagedObjectReference(self._type, self.ref.value)

            # we have a ref, AND we don't already have a name, we can get the name from it...
            if not self._name:
                self._name = self.ref.value
        else:
            if name:
                self.ref = self.core.getDecendentsByName(self._name)

    @property
    def name(self):
        '''List of custom field definitions that are valid for the object's type. The fields
        are sorted by name.
        '''
        return self.update('name')

    @name.setter
    def name(self, name):
        self._name = name

    def update(self, prop):
        if type(prop) == types.ListType:
            for x in prop:
                self.update(x)

        data = self.core.getObjectProperties(self.ref, prop, parent=self)
        if isinstance(data, list) and len(data) == 1:
            data = data[0]
        return data

    def getDecendants(self, type=getattr(ManagedObjectTypes, "ManagedEntity")):
        return self.core.getContentsRecursively(_type=type, root=self)

    def delegate(self, name):
        log.debug("Delegating %s" % name)
        return TaskDelegate(self, name)











