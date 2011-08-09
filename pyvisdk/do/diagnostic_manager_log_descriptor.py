
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DiagnosticManagerLogDescriptor(DynamicData):
    '''Describes a log file that is available on a server.
    '''
    
    def __init__(self, creator, fileName, format, info, key, mimeType):
        # MUST define these
        super(DiagnosticManagerLogDescriptor, self).__init__()
    
        self.data['creator'] = creator
        self.data['fileName'] = fileName
        self.data['format'] = format
        self.data['info'] = info
        self.data['key'] = key
        self.data['mimeType'] = mimeType
    
    
    @property
    def creator(self):
        '''The application that generated the log file. For more information on currently
        supported creators, see DiagnosticManagerLogCreator.
        '''
        return self.data['creator']

    @property
    def fileName(self):
        '''The filename of the log.
        '''
        return self.data['fileName']

    @property
    def format(self):
        '''Describes the format of the log file. For more information on currently supported
        formats, see DiagnosticManagerLogFormat.
        '''
        return self.data['format']

    @property
    def info(self):
        '''Localized description of log file.
        '''
        return self.data['info']

    @property
    def key(self):
        '''A key to identify the log file for browsing and download operations.
        '''
        return self.data['key']

    @property
    def mimeType(self):
        '''Describes the mime-type of the returned file. Typical mime-types include: *
        text/plain - for a plain log file
        '''
        return self.data['mimeType']

