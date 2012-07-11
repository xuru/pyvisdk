
def import_handler(name):
    from pyvisdk.utils import camel_to_under
    from brownie.importing import import_string
    return import_string('{}.ha_cli_handler_{}.{}'.format(__name__, camel_to_under(name), name))
