
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.managed_entity import ManagedEntity

import logging

log = logging.getLogger(__name__)

# This module is NOT auto-generated
# Inspired by decompiled Java classes from vCenter's internalvim25stubs.jar
# Unless states otherside, the methods and attributes were not used by esxcli,
# and thus not tested

class InternalDynamicTypeManager(ManagedEntity):
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.InternalDynamicTypeManager):
        super(InternalDynamicTypeManager, self).__init__(core, name=name, ref=ref, type=type)

    def DynamicTypeMgrQueryTypeInfo(self, filterSpec):
        return self.delegate("DynamicTypeMgrQueryTypeInfo")(filterSpec)

    def DynamicTypeMgrQueryMoInstances(self, filterSpec):
        return self.delegate("DynamicTypeMgrQueryMoInstances")(filterSpec)
