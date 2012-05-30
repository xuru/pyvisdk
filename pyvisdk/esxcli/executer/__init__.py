from xml.sax.saxutils import escape, unescape
from lxml import etree

SOAP_VERSION = "urn:vim25/5.0"

def marshall_response(vim, response):
    from suds.sax.parser import Parser
    from suds.bindings.document import Document
    parser = Parser()
    document = parser.parse(string=response)
    obj = document.getChildren()[0]
    binding = Document(vim.client.wsdl)
    unmarshaller = binding.unmarshaller()
    marshalled_obj = unmarshaller.process(obj, None)
    return vim._parse_object_content(marshalled_obj)

def unmarshall_object(vim, obj):
    from suds.mx import Content
    from suds.sax.parser import Parser
    from suds.bindings.document import Document
    binding = Document(vim.client.wsdl)
    marshaller = binding.marshaller()
    content = Content(obj.__class__.__name__, obj)
    marshalled_obj = marshaller.process(content)
    return str(marshalled_obj)

def get_xml_from_value(vim, key, value):
    from lxml import etree
    import types
    BASIC_TYPES = (types.BooleanType, types.FloatType, types.IntType,
                   types.LongType, types.StringType, types.UnicodeType)
    if isinstance(value, BASIC_TYPES):
        element = etree.Element(key)
        element.text = str(value)
        return etree.tostring(element)
    if isinstance(value, etree._Element):
        return etree.tostring(value)
    return unmarshall_object(vim, value)

def generate_arguments(vim, **kwargs):
    from pyvisdk.do.reflect_managed_method_executer_soap_argument import ReflectManagedMethodExecuterSoapArgument
    sorted_keys = kwargs.keys()
    sorted_keys.sort()
    sorted_kwargs = [(key, kwargs[key]) for key in sorted_keys]
    return [ReflectManagedMethodExecuterSoapArgument(vim, key, escape(get_xml_from_value(vim, key, value)))
            for key, value in sorted_kwargs if value is not None]

def _extract_response(response):
    """:param response: `ReflectManagedMethodExecuterSoapResult`"""
    return unescape(response.response).replace('<NONE>', 'None')

def _extract_fault(response):
    """:param response: `ReflectManagedMethodExecuterSoapResult`"""
    return unescape(response.fault.faultDetail)

def execute_soap(vim, host, moid, method, **kwargs):
    from suds import WebFault
    response = host.RetrieveManagedMethodExecuter().executeSoap(moid=moid, version=SOAP_VERSION, method=method,
                                                                argument=generate_arguments(vim, **kwargs))
    if response.response is None and response.fault.faultMsg is not None:
        fault = marshall_response(vim, response)
        fault.faultstring = response.faul.faultMsg
        raise WebFault(fault, response)
    return marshall_response(vim, response.response)
