
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNumericSensorInfo(DynamicData):
    '''Base class for numeric sensor information.
    '''
    
    def __init__(self, baseUnits, currentReading, healthState, name, rateUnits, sensorType, unitModifier):
        # MUST define these
        super(HostNumericSensorInfo, self).__init__()
    
        self.data['baseUnits'] = baseUnits
        self.data['currentReading'] = currentReading
        self.data['healthState'] = healthState
        self.data['name'] = name
        self.data['rateUnits'] = rateUnits
        self.data['sensorType'] = sensorType
        self.data['unitModifier'] = unitModifier
    
    
    @property
    def baseUnits(self):
        '''The base units in which the sensor reading is specified. If rateUnits is set the
        units of the current reading is further qualified by the rateUnits.
        '''
        return self.data['baseUnits']

    @property
    def currentReading(self):
        '''The current reading of the element indicated by the sensor. The actual sensor
        reading is obtained by multiplying the current reading by the scale
        factor.
        '''
        return self.data['currentReading']

    @property
    def healthState(self):
        '''The health state of the of the element indicated by the sensor. This property is
        populated only for sensors that support threshold settings.
        '''
        return self.data['healthState']

    @property
    def name(self):
        '''The name of the physical element associated with the sensor
        '''
        return self.data['name']

    @property
    def rateUnits(self):
        '''The rate units in which the sensor reading is specified. For example if the
        baseUnits is Volts and the rateUnits is per second the value returned by
        the sensor are in Volts/second.
        '''
        return self.data['rateUnits']

    @property
    def sensorType(self):
        '''The type of the sensor. If the sensor type is set to Other the sensor name can be
        used to further identify the type of sensor. The sensor units can also be
        used to further implicitly determine the type of the sensor.
        '''
        return self.data['sensorType']

    @property
    def unitModifier(self):
        '''The unit multiplier for the values returned by the sensor. All values returned by
        the sensor are current reading * 10 raised to the power of the
        UnitModifier.
        '''
        return self.data['unitModifier']

