
from subsystems.solarpanels import SolarPanels


class MockupSystem:
    """
    The MockupSystem is a container class for different Subsystems, which are interconnected modules.
    These modules may be part of the satellite, or they may represent an element of the environment.
    This class provides a structure for these modules so they can be reliably found and accessed.
    It also provides an easy way to pull data and call functions, creating a useful developer interface.
    """

    subsystems = {}

    def __init__(self):
        self.subsystems["solarpanels"] = SolarPanels()
        pass

    def update(self, deltaTimeSeconds: float = 1.0):
        for subsystem in self.subsystems.keys():
            subsystem.update(deltaTimeSeconds)

