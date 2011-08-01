
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
    
    

    def RefreshDateTimeSystem(self):
        '''Refresh the DateTime related settings to pick up any changes that might have
        occurred.
        '''
        
        return self.delegate("RefreshDateTimeSystem")()
        

    def UpdateDateTime(self, dateTime):
        '''Update the date/time on the host. This method should be used with caution since
        network delays, execution delays can result in time skews.

        :param dateTime: DateTime to update the host to.

        '''
        
        return self.delegate("UpdateDateTime")(dateTime)
        

    def QueryAvailableTimeZones(self):
        '''Retrieves the list of available timezones on the host. The API works off the
        public domain 'tz' timezone database.

        :rtype: HostDateTimeSystemTimeZone[] 

        '''
        
        return self.delegate("QueryAvailableTimeZones")()
        

    def UpdateDateTimeConfig(self, config):
        '''Update the DateTime configuration of the host.

        :param config: The new DateTime configuration information.

        '''
        
        return self.delegate("UpdateDateTimeConfig")(config)
        

    def QueryDateTime(self):
        '''Get the current DateTime on the host.

        :rtype: xsd:dateTime 

        '''
        
        return self.delegate("QueryDateTime")()
        
