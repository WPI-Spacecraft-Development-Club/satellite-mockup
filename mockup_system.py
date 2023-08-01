
from subsystems.solarpanels import SolarPanels
from subsystems.battery import BatteryBank

class MockupSystem:
    """
    The MockupSystem is a container class for different Subsystems, which are interconnected modules.
    These modules may be part of the satellite, or they may represent an element of the environment.
    This class provides a structure for these modules so they can be reliably found and accessed.
    It also provides an easy way to pull data and call functions, creating a useful developer interface.
    """

    subsystems = {}
    uptimeSeconds = 0

    def __init__(self):
        self.subsystems["solarpanels"] = SolarPanels()
        self.subsystems["batterybank"] = BatteryBank()
        self.subsystems["batterybank"].sources.append(self.subsystems["solarpanels"])

    def update(self, deltaTimeSeconds: float = 1.0):
        for subsystem in self.subsystems.keys():
            self.subsystems[subsystem].update(deltaTimeSeconds)
        self.uptimeSeconds += deltaTimeSeconds


if __name__ == "__main__":
    system = MockupSystem()
    for i in range(100):
        for j in range(3600):
            system.update() # 1s update interval
        print("Current battery level: ", end="")
        print(system.subsystems["batterybank"].currentStoredWattHours, end="")
        print(" watt hours.")
        print("Uptime: " + str(system.uptimeSeconds) + " seconds.")
        print()