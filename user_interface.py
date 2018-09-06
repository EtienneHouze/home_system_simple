from control_system import ControlSystem
from controller_impl import Controller


class UserInterface:
     def __init__(self):
         pass

     def discuss(self):
         print("Welcome to the Hello program")
         control_system = ControlSystem()
         control_system.set_temp(23)
         controller = Controller()
         control_system.add_component(controller)
