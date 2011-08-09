
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class EventDescriptionEventDetail(DynamicData):
    '''Each Event object provides an automatic event message string through its
        fullFormattedMessage property. However, you can use the EventDetail
        object's properties to format an event message string that is appropriate
        when viewed from a specific context. The variable information (vm.name,
        and so on) is derived from the Event object's event arguments
        (VmEventArgument, and so on).
    '''
    
    def __init__(self, category, description, formatOnComputeResource, formatOnDatacenter, formatOnHost, formatOnVm, fullFormat, key, longDescription):
        # MUST define these
        super(EventDescriptionEventDetail, self).__init__()
    
        self.data['category'] = category
        self.data['description'] = description
        self.data['formatOnComputeResource'] = formatOnComputeResource
        self.data['formatOnDatacenter'] = formatOnDatacenter
        self.data['formatOnHost'] = formatOnHost
        self.data['formatOnVm'] = formatOnVm
        self.data['fullFormat'] = fullFormat
        self.data['key'] = key
        self.data['longDescription'] = longDescription
    
    
    @property
    def category(self):
        '''A category of events.
        '''
        return self.data['category']

    @property
    def description(self):
        '''A string that is a short human-parseable description of the event.
        '''
        return self.data['description']

    @property
    def formatOnComputeResource(self):
        '''A string that is appropriate in the context of a specific cluster. For example, a
        powering on event in this context produces the following string:
        '''
        return self.data['formatOnComputeResource']

    @property
    def formatOnDatacenter(self):
        '''A string that is appropriate in the context of a specific Datacenter. For example,
        a renaming event in this context produces the following string:
        '''
        return self.data['formatOnDatacenter']

    @property
    def formatOnHost(self):
        '''A string that is appropriate in the context of a specific Host. For example, a
        powering on event in this context produces the following string:
        '''
        return self.data['formatOnHost']

    @property
    def formatOnVm(self):
        '''A string that is appropriate for the context of a specific virtual machine. For
        example, a powering on event in this context produces the following
        string:
        '''
        return self.data['formatOnVm']

    @property
    def fullFormat(self):
        '''A string whose context is not entity-specific. For example, a powering on event
        produces the following string:
        '''
        return self.data['fullFormat']

    @property
    def key(self):
        '''Type of event being described.
        '''
        return self.data['key']

    @property
    def longDescription(self):
        '''A detailed description of the event. It includes common causes and actions to
        remediate them. It may also include links to kb articles and other
        diagnostic information. For example, the BadUserNameSessionEvent may
        produce the following string:
        '''
        return self.data['longDescription']

