
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDateTimeSystem(BaseEntity):
    '''This managed object provides for NTP and date/time related configuration on a
        host. Information regarding the running status of the NTP daemon and
        functionality to start and stop the daemon is provided by the
        HostServiceSystem object.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostDateTimeSystem):
        # MUST define these
        super(HostDateTimeSystem, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def dateTimeInfo(self):
        '''The DateTime configuration of the host.
        '''
        return self.update('dateTimeInfo')


    def QueryAvailableTimeZones(self, config):
        '''Retrieves the list of available timezones on the host. The API works off the
        public domain 'tz' timezone database.

        :param config: The new DateTime configuration information.

        '''
        
        return self.delegate("QueryAvailableTimeZones")(config)
        

    def QueryDateTime(self, config):
        '''Get the current DateTime on the host.

        :param config: The new DateTime configuration information.

        '''
        
        return self.delegate("QueryDateTime")(config)
        

    def RefreshDateTimeSystem(self, config):
        '''Refresh the DateTime related settings to pick up any changes that might have
        occurred.

        :param config: The new DateTime configuration information.

        '''
        
        return self.delegate("RefreshDateTimeSystem")(config)
        

    def UpdateDateTime(self, config):
        '''Update the date/time on the host. This method should be used with caution since
        network delays, execution delays can result in time skews.

        :param config: The new DateTime configuration information.

        '''
        
        return self.delegate("UpdateDateTime")(config)
        

    def UpdateDateTimeConfig(self, config):
        '''Update the DateTime configuration of the host.

        :param config: The new DateTime configuration information.

        '''
        
        return self.delegate("UpdateDateTimeConfig")(config)
        
