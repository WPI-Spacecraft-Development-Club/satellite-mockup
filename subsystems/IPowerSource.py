
class IPowerSource:

    def update(self, deltaTimeSeconds: float = 1.0):
        raise NotImplementedError("Interface function")
    
    def popGeneratedWattHours(self) -> float:
        raise NotImplementedError("Interface function")
    
    def getCurrentGeneratedWatts(self) -> float:
        raise NotImplementedError("Interface function")

    def getTotalGeneratedWattHours(self) -> float:
        raise NotImplementedError("Interface function")