from json import loads, dumps
from logging import getLogger
from infi.pyutils.lazy import cached_method, clear_cache
from pyvisdk import __version__

logger = getLogger(__name__)

from .errors import ExtensionAlreadyRegisteredException, ExtensionIsFullException, ExtensionNotRegisteredException
class TaskExtension(object):
    DESCRIPTION = "PyVISDK task facade extension"
    VERSION = __version__
    MAX_LENGTH = 255

    def __init__(self, client, key):
        super(TaskExtension, self).__init__()
        self._client = client
        self._managed_object = self._client.service_content.extensionManager
        self._key = key

    @cached_method
    def is_registered(self):
        return len(self._get_extensions_data_object()) > 0

    def register(self):
        if self.is_registered():
            raise ExtensionAlreadyRegisteredException()
        extension = self._new_extension()
        self._managed_object.RegisterExtension(extension)
        clear_cache(self)

    def is_task_registered(self, expected):
        return any([actual == expected for _, actual in self._get_tasks()])

    def get_task_id(self, task_name):
        if not self.is_registered():
            raise ExtensionNotRegisteredException()
        if not self.is_task_registered(task_name):
            raise KeyError(task_name)
        for task_tuple in self._get_tasks():
            if task_tuple[1] == task_name:
                return task_tuple[0]

    def add_task(self, task_name):
        task_id = str(hash(task_name))
        self._set_tasks([(task_id, task_name)] + self._get_tasks())
        clear_cache(self)

    @cached_method
    def _get_extensions_data_object(self):
        return [extension for extension in self._managed_object.extensionList
                if extension.key == self._key]

    @cached_method
    def _get_tasks(self):
        data_object = self._get_extensions_data_object()[0]
        return loads(data_object.description.summary or '[]')

    def _set_tasks(self, tasks):
        extension = self._get_extensions_data_object()[0]
        extension.description.summary = dumps(tasks)
        if len(extension.description.summary) > self.MAX_LENGTH:
            raise ExtensionIsFullException
        extension.taskList = [self._new_task_type_info(task_id) for task_id, _ in tasks]
        extension.resourceList = self._new_task_extension_resource_info(tasks)
        self._managed_object.UpdateExtension(extension)
        clear_cache(self)

    def _new_extension(self):
        from pyvisdk.do.extension import Extension
        from pyvisdk.do.description import Description
        description = Description(self._client, label=self.DESCRIPTION, summary='')
        return Extension(self._client, description=description, key=self._key,
                         lastHeartbeatTime=self._get_heartbeat(),
                         version=self.VERSION)

    def _get_heartbeat(self):
        return self._client.service_instance.CurrentTime()

    def _new_task_type_info(self, task_id):
        from pyvisdk.do.extension_task_type_info import ExtensionTaskTypeInfo
        return ExtensionTaskTypeInfo(self._client, task_id)

    def _new_task_extension_resource_info(self, tasks):
        from pyvisdk.do.extension_resource_info import ExtensionResourceInfo
        from pyvisdk.do.key_value import KeyValue
        data = [KeyValue(self._client, "{}.label".format(task_id), task_name) for task_id, task_name in tasks]
        return ExtensionResourceInfo(self._client, locale="en", module="task", data=data)
