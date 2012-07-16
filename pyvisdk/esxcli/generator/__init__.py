from infi.pyutils.lazy import cached_method
from xml.sax.saxutils import escape, unescape
from ..base import Base
from os.path import abspath, dirname, join, pardir, exists
from os import makedirs

DATA_MODULES_DIR = abspath(join(dirname(__file__), pardir, pardir, 'do'))
HANDLERS_DIR = abspath(join(dirname(__file__), pardir, 'handlers'))

DATA_OBJECT_TYPES_TEMPLATE = """

from ..thirdparty import Enum

DataObjectTypes = Enum(*[
    {%- for name in types %}
    "{{ name }}",
    {%- endfor %}
    ])
"""

HANLDERS_IMPORT_METHOD = """
def import_handler(name):
    from pyvisdk.utils import camel_to_under
    from brownie.importing import import_string
    return import_string('{}.ha_cli_handler_{}.{}'.format(__name__, camel_to_under(name), name))
"""

HANDLER_MODULE_TEMPLATE = """
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class {{ class_name }}(Base):
    '''
    {{ class_doc }}
    '''
    moid = {{ moid }}
    
    {%- for method in methods %}
    def {{ method.name }}({{ method.formatted_args }}):
        '''
        {{ method.doc }}
        {%- for kwarg in method.kwargs %}
        :param {{ kwarg.name }}: {{ kwarg.doc }}
        {%- endfor %}
        :returns: {{ method.returns_doc }}
        '''
        return execute_soap(self._client, self._host, self.moid, {{ method.wsdl_name_repr }},
                            {%- for kwarg in method.kwargs %}
                            {{ kwarg.name }}={{ kwarg.name }}, 
                            {%- endfor %}
                            )
            
    {%- endfor %}   
"""

DATA_OBJECT_TEMPLATE = """
import logging
from pyvisdk.exceptions import InvalidArgumentError

# This module is NOT auto-generated
# Inspired by decompiled Java classes from vCenter's internalvim25stubs.jar
# Unless states otherside, the methods and attributes were not used by esxcli,
# and thus not tested

log = logging.getLogger(__name__)

def {{ name }}(vim, *args, **kwargs):
    obj = vim.client.factory.create('ns0:{{ name }}')

    # do some validation checking...
    if (len(args) + len(kwargs)) < {{ required_args_size }}:
        raise IndexError('Expected at least {{ required_args_size+1 }} arguments got: %d' % len(args))

    required = [ {{ required_args|join(', ') }} ]
    optional = [ {{ optional_args|join(', ') }} ]

    for name, arg in zip(required + optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
"""


class Generator(Base):
    @cached_method
    def _get_managed_object_instances(self):
        """:returns: `DynamicTypeMgrMoInstance`"""
        HANDLER_PREFIX = "ha-cli-handler"
        return [item for item in self._get_dynamic_type_manager().DynamicTypeMgrQueryMoInstances(None)
                if item.id.startswith(HANDLER_PREFIX)]

    @cached_method
    def _get_types(self):
        """:returns: `DynamicTypeMgrAllTypeInfo`"""
        return self._get_dynamic_type_manager().DynamicTypeMgrQueryTypeInfo(None)

    @cached_method
    def _get_dynamic_type_manager(self):
        return self._host.RetrieveDynamicTypeManager()

    def _create_schema(self):
        from lxml.builder import ElementMaker
        from lxml import etree
        kwargs = {'targetNamespace': "urn:vim25",
                  'nsmap': {None: "http://www.w3.org/2001/XMLSchema",
                            'vim25':"urn:vim25",
                            'xsd':"http://www.w3.org/2001/XMLSchema",
                            'reflect':"urn:reflect"},
                  'elementFormDefault':"qualified"}
        schema = etree.Element("schema", **kwargs)
        schema.append(etree.Element("include", schemaLocation="core-types.xsd"))
        schema.append(etree.Element("include", schemaLocation="vim-types.xsd"))
        return schema

    def _fix_base(self, base):
        return base.replace("vmodl", "vim25").replace('.', ':')

    def _fix_type(self, data_type):
        BASIC_DATA_TYPES = ["string", "boolean", "long", "int", "dateTime", "short", "float" "anyType"]
        for basic_type in BASIC_DATA_TYPES:
            if data_type.startswith(basic_type):
                return "xsd:{}".format(basic_type)
        type_name = data_type.replace('[]', '')
        matching_cli_type = filter(lambda item: item.name == type_name, self._get_types().dataTypeInfo)
        if matching_cli_type:
            return "vim25:{}".format(matching_cli_type[0].wsdlName)
        return "vim25:{}".format(type_name.replace('vim.', ''))

    def _add_property_to_element(self, parent, property):
        """:param property: `DynamicTypeMgrPropertyTypeInfo`"""
        from lxml import etree
        kwargs = dict(name=property.name,
                      type=self._fix_type(property.type),
                      minOccurs="0")
        if '[]' in property.type:
            kwargs.update(dict(maxOccurs="unbounded"))
        parent.append(etree.Element("element", **kwargs))

    def _add_data_object(self, schema, data_object):
        from lxml import etree
        complex_type = etree.Element("complexType", name=data_object.wsdlName)
        complex_content = etree.Element("complexContent")
        extension = etree.Element("extension", base=self._fix_base(data_object.base[0]))
        sequence = etree.Element("sequence")
        for element in data_object.property:
            self._add_property_to_element(sequence, element)
        extension.append(sequence)
        complex_content.append(extension)
        complex_type.append(complex_content)
        schema.append(complex_type)

    @cached_method
    def generate_xsd(self):
        from lxml import etree
        schema = self._create_schema()
        for data_object in self._get_types().dataTypeInfo:
            self._add_data_object(schema, data_object)
        return schema

    def generate_xsd_to_file(self):
        from pyvisdk.client import WSDL_DIR
        from os.path import join
        from lxml import etree
        with open(join(WSDL_DIR, 'cli-types.xsd'), 'w') as fd:
            fd.write(etree.tostring(self.generate_xsd(), pretty_print=True, xml_declaration=True, encoding='UTF-8'))

    def _get_cli_info_for_motype(self, motype):
        """:returns:`VimCLIInfoInfo`"""
        from lxml import etree
        from ..executer import execute_soap
        CLI_INFO_ID = "ha-dynamic-type-manager-local-cli-cliinfo"
        CLI_FETCH_METHOD_NAME = "vim.CLIInfo.FetchCLIInfo"
        element = etree.Element("typeName")
        element.text = motype
        return execute_soap(self._client, self._host, CLI_INFO_ID, CLI_FETCH_METHOD_NAME, typeName=element)

    @cached_method
    def _get_managed_types_dict(self):
        """:returns: `DynamicTypeMgrManagedTypeInfo`"""
        return {item.name:{method.name:method for method in item.method}
                for item in self._get_types().managedTypeInfo}

    @cached_method
    def _get_handler_names_dict(self):
        return {item.moType:item.id for item in self._get_managed_object_instances()}

    def _prepare_method_parameters(self, param_type_info_list, cli_info_param_dict):
        """:param param_type_info_list: `DynamicTypeMgrParamTypeInfo`
        :param cli_info_param_dict: `VimCLIInfoParam`"""
        from bunch import Bunch
        return [Bunch(name=param_type_info.name,
                      doc="{}, {}".format(param_type_info.type,
                                          cli_info_param_dict.get(param_type_info.name).help),
                      )
                for param_type_info in param_type_info_list]

    def prepare_method_formatted_arugments(self, param_type_info_list, cli_info_param_dict):
        """:param param_type_info_list: `DynamicTypeMgrParamTypeInfo`
        :param cli_info_param_dict: `VimCLIInfoParam`"""
        def is_optional(param_type_info):
            return any([annotation.name == 'optional' for annotation in param_type_info.annotation])

        def formatter(param_type_info):
            return "{}={}".format(param_type_info.name, 'None') if is_optional(param_type_info) else \
                    param_type_info.name

        return ', '.join(['self'] + map(formatter, filter(lambda item: not is_optional(item), param_type_info_list) +
                                        filter(lambda item: is_optional(item), param_type_info_list)))

    def _prepate_methods(self, managed_type_name, methods_dict, cli_info, handler_name):
        from bunch import Bunch
        methods_in_cli_info = {}
        for method in cli_info.method:
            methods_in_cli_info[method.name] = Bunch(parameters={param.name: param for param in method.param},
                                                     return_value=method.ret,
                                                     help=method.help)
        methods = []
        for method in methods_dict.values():
            kwargs = self._prepare_method_parameters(method.paramTypeInfo,
                                                     methods_in_cli_info.get(method.name)['parameters'])
            formatted_args = self.prepare_method_formatted_arugments(method.paramTypeInfo,
                                                                     methods_in_cli_info.get(method.name)['parameters'])
            returns_doc = ', '.join([return_type_info.type for return_type_info in method.returnTypeInfo])
            methods.append(Bunch(name=method.name,
                                 wsdl_name_repr=repr(".".join([managed_type_name, method.name.capitalize()])),
                                 doc=methods_in_cli_info.get(method.name).help,
                                 returns_doc=returns_doc,
                                 kwargs=kwargs,
                                 formatted_args=formatted_args))
        return methods

    def _render_handler_module(self, managed_type_name, methods_dict, cli_info, handler_name):
        """ Render handle module 
        
        :param managed_type_name: string
        :param methods_dict: {name:`DynamicTypeMgrMethodTypeInfo`}
        :param cli_info: `VimCLIInfoInfo`
        :param handler_name: string
        """
        from jinja2 import Template
        template = Template(HANDLER_MODULE_TEMPLATE)
        methods = self._prepate_methods(managed_type_name, methods_dict, cli_info, handler_name)
        kwargs = dict(class_name=''.join([item.capitalize() for item in cli_info.name.split('.')]),
                      moid=repr(handler_name),
                      class_doc=cli_info.help,
                      methods=methods)
        return template.render(**kwargs)

    def _get_filename_for_handler_module(self, handler_name):
        return join(HANDLERS_DIR, '{}.py'.format(handler_name.replace('-', '_').lower()))

    def _write_handler_module_to_disk(self, handler_name, content):
        with open(self._get_filename_for_handler_module(handler_name), 'w') as fd:
            fd.write(content)

    @cached_method
    def generate_cli_handlers(self):
        methods_by_managed_types = self._get_managed_types_dict()
        handler_names = self._get_handler_names_dict()
        handlers = {}
        for managed_type_name, methods_dict in methods_by_managed_types.items():
            handler_name = handler_names.get(managed_type_name)
            if handler_name is None:
                continue
            cli_info = self._get_cli_info_for_motype(managed_type_name)
            content = self._render_handler_module(managed_type_name, methods_dict, cli_info, handler_name)
            handlers[handler_name] = content
        return handlers

    def save_cli_handlers_to_disk(self):
        if not exists(HANDLERS_DIR):
            makedirs(HANDLERS_DIR)
        with open(join(HANDLERS_DIR, '__init__.py'), 'w') as fd:
            fd.write(HANLDERS_IMPORT_METHOD)
        for name, content in self.generate_cli_handlers().items():
            self._write_handler_module_to_disk(name, content)

    @cached_method
    def generate_data_type_modules(self):
        from jinja2  import Template
        template = Template(DATA_OBJECT_TEMPLATE)
        data_type_modules = {}
        for data_object in self._get_types().dataTypeInfo:
            name = data_object.wsdlName
            required_args = [] # TODO what is required
            optional_args = [repr(property.name) for property in data_object.property]
            content = template.render(name=name, required_args=required_args,
                                      optional_args=optional_args,
                                      required_args_size=len(required_args))
            data_type_modules[name] = content
        return data_type_modules

    def _write_data_object_types_file(self):
        from pyvisdk.base import data_object_types
        from jinja2  import Template
        template = Template(DATA_OBJECT_TYPES_TEMPLATE)
        originals = set(data_object_types.DataObjectTypes.keys())
        additions = set(self.generate_data_type_modules().keys())
        types = list(originals.union(additions))
        types.sort()
        with open(str(data_object_types.__file__).replace('.pyc', '.py'), 'w') as fd:
            fd.write(template.render(types=types))

    def save_data_modules_to_disk(self):
        from pyvisdk.utils import camel_to_under
        self._write_data_object_types_file()
        for name, content in self.generate_data_type_modules().items():
            with open(join(DATA_MODULES_DIR, '{}.py'.format(camel_to_under(name))), 'w') as fd:
                fd.write(content)
