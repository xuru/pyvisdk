'''
Created on Mar 8, 2011

@author: eplaster
'''
from pyvisdk import consts
from pyvisdk.consts import ManagedObjectReference
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

class ManagedEntity(object):
    def __init__(self, core, props, name=None, ref=None):
        self.core = core
        self.client = core.client
        self.service = core.client.service
        self.type = consts.ManagedEntity
        self.props = ["configIssue", "configStatus", "name", "parent"] + props
        if ref:
            self.ref = ManagedObjectReference(consts.ManagedEntity, ref.value)
        self.name = name
        
        self.parent = None
        self.issues = None
        self.status = None
        
    def parse(self):
        for prop in self.props:
            data = self.core.getDynamicProperty(self.ref, prop)
            self.update(data)
        
    def update(self, propset):
        for name, value in propset.items():
            try:
                if name == "name":
                    log.debug("[%s] %s" % (name, value.__class__.__name__))
                    self.name = value
            
                elif name == "parent":
                    log.debug("[%s] %s" % (name, value.__class__.__name__))
                    self.parent = value
            
                elif name == "configIssue":
                    log.debug("[%s] %s" % (name, value.__class__.__name__))
                    self.issues = value
            
                elif name == "configStatus":
                    log.debug("[%s] %s" % (name, value.__class__.__name__))
                    self.status = value
            except AttributeError, e:
                log.warning("[WARNING] [%s] %s" %  (name, e))
