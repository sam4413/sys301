# LEGO type:standard slot:0 autostart
# The above line allows VS Code Lego Spike Extension to upload and run code.

# region Imports
from math import *
import sys

from hub import battery
from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import equal_to, greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, not_equal_to
# endregion

# region Initialization
my_hub = PrimeHub()
distance_sensor = DistanceSensor('C')
right_sensor = ColorSensor('F')
left_sensor = ColorSensor('B')
wheels = MotorPair('A', 'E')
wheels.set_motor_rotation(20)
matrix = LightMatrix()
# endregion

# region Functions


def check_battery():
    BATTERY_OK = '\033[32m'
    BATTERY_LOW = '\033[31m'
    ENDC = '\033[0m'
    VOLTAGE_THRESHOLD = 8000  # Threshold for battery level

    # Battery voltage printout in console for monitoring charge
    if battery.voltage() < VOLTAGE_THRESHOLD:
        print(BATTERY_LOW + "battery voltage is too low: " + str(battery.voltage()) +
              " \n ----------------------------- \n >>>> please charge robot <<<< \n ----------------------------- \n"
              + ENDC)
    else:
        print(BATTERY_OK + "battery voltage: " + str(battery.voltage()) + ENDC)


def print_module_objects_and_attributes(module_name):
    """Print hidden Spike APIs given a module name.

    Usage:
        `print_module_objects_and_attributes('hub')`
    Args:
        module_name (string): i.e. 'hub' or 'spike'
    """
    module = __import__(module_name)
    print("Module: ", module_name)
    objects = dir(module)

    for obj_name in objects:
        obj = getattr(module, obj_name)
        attributes = dir(obj)

        print("Object: ", obj_name)
        for attribute in attributes:
            print("- ", attribute)
        print()


def end_program():
    """Gracefully end the program without any traceback messages.
    """
    try:
        # Code that may raise SystemExit
        sys.exit(0)
    except SystemExit:
        # Handle the SystemExit exception without propagating it
        pass

# endregion

# region Main



def main():

    def getColorInfo(port: int) -> list:
        """
        Get the current color sensor and return a list of ints of R, G, and B as well as ambient light and reflected light in a single list.
        """
        sensor = ColorSensor(port)
        return list(list(sensor.get_rgb_intensity()), sensor.get_ambient_light(), sensor.get_reflected_light())
    
    def inColor(r, g, b, range, port: int) -> bool:
        """
        Returns a boolean given the r, g, and b values on if the color sensor is reading the given values.
        The Range variable is used to give a bit of wiggle room in these values.
        """
        return True
    
    def 

    # ----------------  Put your code logic here  -----------------
    try:
        matrix.show_image("YES")
        wheels.move(5)
        print('distance=%d' % distance_sensor.get_distance_cm())
    except Exception:
        matrix.show_image("SAD")
        print("Error occured!!!!!!!!")
    
    

# endregion


# region DO NOT EDIT ANYTHING HERE
print("\n\nStarting... ")
check_battery()
timer = Timer()
main()
print("Ended program. Elapsed time: " + str(timer.now()))
end_program()
# endregion
