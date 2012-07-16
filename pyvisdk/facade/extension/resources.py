
from UserDict import DictMixin
from infi.pyutils.lazy import clear_cache, cached_method
from cjson import encode, decode

MANAGED_OBJECT_REFERENCE = "Folder:group-d1"

class ExtensionResourceDict(object, DictMixin):
    """
    The problem with vSphere is that is does not expose extension's resources.
    For this purpose we have this dict on top of a custom field at the root folder
    """
    def __init__(self, client, field_name):
        super(ExtensionResourceDict, self).__init__()
        self._client = client
        self._field_name = field_name
        self._managed_object = self._client.getManagedObjectByReference(MANAGED_OBJECT_REFERENCE)
        self._manager = self._client.service_content.customFieldsManager
        if not self._is_custom_field_installed():
            self._install_custom_field()

    def keys(self):
        return self._get_dict().keys()

    def __getitem__(self, key):
        return self._get_dict()[key]

    def __setitem__(self, key, value):
        dictionary = self._get_dict()
        dictionary[key] = value
        self._set_dict(dictionary)

    def __delitem__(self, key):
        dictionary = self._get_dict()
        dictionary.__delitem__(key)
        self._set_dict(dictionary)

    def _get_dict(self):
        return decode(self._get_json_string())

    def _set_dict(self, dictionary):
        self._set_json_string(encode(dictionary))

    @cached_method
    def _is_custom_field_installed(self):
        return any([field.name == self._field_name for field in self._manager.field])

    def _install_custom_field(self):
        self._manager.AddCustomFieldDef(name=self._field_name, moType="Folder", fieldDefPolicy=None, fieldPolicy=None)
        clear_cache(self)

    @cached_method
    def _get_custom_field_key(self):
        return [field for field in self._manager.field if field.name == self._field_name][0].key

    @cached_method
    def _get_json_string(self):
        item = [item for item in self._managed_object.customValue if item.key == self._get_custom_field_key()]
        return encode({}) if not item else item[0].value

    def _set_json_string(self, json):
        self._manager.SetField(entity=self._managed_object, key=self._get_custom_field_key(), value=json)
        clear_cache(self)

class ExtensionResourceFactory(object):
    @classmethod
    def get_dict(cls, client, extension_key):
        return ExtensionResourceDict(client, extension_key)
