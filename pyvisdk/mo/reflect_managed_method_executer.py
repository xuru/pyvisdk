
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.managed_entity import ManagedEntity

import logging

log = logging.getLogger(__name__)

# This module is NOT auto-generated
# Inspired by decompiled Java classes from vCenter's internalvim25stubs.jar
# Unless states otherside, the methods and attributes were not used by esxcli,
# and thus not tested

class ReflectManagedMethodExecuter(ManagedEntity):
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.ReflectManagedMethodExecuter):
        super(ReflectManagedMethodExecuter, self).__init__(core, name=name, ref=ref, type=type)

    def executeSoap(self, moid, version, method, argument):
        return self.delegate("ExecuteSoap")(moid, version, method, argument)

    def fetchSoap(self, moid, version, prop):
        return self.delegate("FetchSoap")(moid, version, prop)
