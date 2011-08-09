
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DiagnosticManagerLogHeader(DynamicData):
    '''A header that is returned with a set of log entries. This header describes where
        entries are located in the log file. Log files typically grow dynamically,
        so indexes based on line numbers may become inaccurate.
    '''
    
    def __init__(self, lineEnd, lineStart, lineText):
        # MUST define these
        super(DiagnosticManagerLogHeader, self).__init__()
    
        self.data['lineEnd'] = lineEnd
        self.data['lineStart'] = lineStart
        self.data['lineText'] = lineText
    
    
    @property
    def lineEnd(self):
        '''The last line of this log segment.
        '''
        return self.data['lineEnd']

    @property
    def lineStart(self):
        '''The first line of this log segment.
        '''
        return self.data['lineStart']

    @property
    def lineText(self):
        '''Log entries, listed by line, for this log segment.
        '''
        return self.data['lineText']

