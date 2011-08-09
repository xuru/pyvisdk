import logging

log = logging.getLogger(__name__)

class BaseData(object):
    '''
    classdocs
    '''

    def __init__(self, *args, **argv):
        '''
        Constructor
        '''
        self.data = {}