from .IBattery import IBattery
from .IPowerSource import IPowerSource

class BatteryBank(IBattery):

    # TODO: update the following battery characteristics to match a little more closely with potential options

    nominalVoltage = 1.2 # volts
    maxStoredWattHours = 35 # milliamp hours
    chargingEfficiency = 0.8 # percent

    currentStoredWattHours = 0

    def __init__(self):
        pass

    def update(self, deltaTimeSeconds: float = 1.0):
        # TODO: take power output into account
        totalInputWatts = 0 # in watts
        for source in self.sources:
            source: IPowerSource
            totalInputWatts += source.getCurrentGeneratedWatts()
        
        totalInputWattHours = totalInputWatts * (deltaTimeSeconds / 3600) # input in watts * time in hours
        maxInputWatts = totalInputWattHours * self.chargingEfficiency

        self.currentStoredWattHours = min(self.currentStoredWattHours + maxInputWatts, self.maxStoredWattHours)
    
    def getCurrentStoredWattHours(self):
        return self.currentStoredWattHours
    
    def getMaximumStoredWattHours(self):
        return self.maxStoredWattHours