from control_system import ControlSystem
from controller_impl import Controller, Thermometer, Heater


class UserInterface:
    def __init__(self):
        pass

    def discuss(self):
        print("Welcome to the Hello program")
        control_system = ControlSystem()
        control_system.set_temp(21)
        controller = Controller(0)
        heater = Heater(10, house=control_system)
        thermo = Thermometer(11, house=control_system)
        control_system.add_component(controller)
        control_system.add_component(heater,0)
        control_system.add_component(thermo,0)
        control_system.get_root()

        for t_step in range(20):
            control_system.run(1)
            if t_step==5:
                heater.malfunction(5)
            print("Step number :"+ str(t_step))
            print("temperature " + str(control_system.get_temp()))
