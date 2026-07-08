from math import *
import sys

import hub
def main():
    #matrix.show_image("HAPPY")
    hub.light_matrix.write('Hello, World!')
    #print("Main loop called")
    #print(getColorInfo(4))

    """
    if (inColor(255, 255,0, 10, 4)):
        print("Inside the color!!")
    #wheels.move(5)
    """
    #print('distance=%d' % distance_sensor.get_distance_cm())

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
    
    def isMine(port: int) -> bool:
        """
        Returns true if the color that was detected is a Mine sticky note, meaning a mine color. Emits true if so.
        """
        return True

    # ----------------  Put your code logic here  -----------------
   
    
    

# endregion


# region DO NOT EDIT ANYTHING HERE
print("\n\nStarting... ")
check_battery()
timer = Timer()
main()
print("Ended program. Elapsed time: " + str(timer.now()))
end_program()
# endregion
