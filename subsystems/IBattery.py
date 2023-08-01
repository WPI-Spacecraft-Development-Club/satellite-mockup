
class IBattery:
    """
    Battery class interface. Defines functions and handles any battery must implement/use in order to be used in the mockup.
    """
    sources = []
    sinks = []

    def update(self, deltaTimeSeconds: float = 1.0):
        raise NotImplementedError("Interface function")
    
    def connectPowerSource(self, source):
        self.sources.append(source)
    
    def connectPowerSink(self, sink):
        self.sinks.append(sink)
    
    def getCurrentStoredWattHours(self) -> float:
        raise NotImplementedError("Interface function")

    def getMaximumStoredWattHours(self) -> float:
        raise NotImplementedError("Interface function")