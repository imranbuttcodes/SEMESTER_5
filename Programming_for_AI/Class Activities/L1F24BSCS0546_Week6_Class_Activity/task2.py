from os import PRIO_PGRP
from abc import ABC, abstractmethod
class Component:
    @abstractmethod
    def startup(self):
        pass

class PowerDevice(Component):
    def startup(self):
        print("Power Grid Connected")
    

class NetworkDevice(Component):
    def startup(self):
        print("NetworkDevice Grid Connected")

class SmartLift(PowerDevice, NetworkDevice):
    def startup(self):
        print("SmartLift Grid Connected")


lift = SmartLift()

print(SmartLift.mro())
