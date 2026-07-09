from hub import light_matrix, port, sound
import runloop
import motor
import color_sensor
import motor_pair

COLOR_RANGE = 5

LEFT_MOTOR = port.A
RIGHT_MOTOR = port.B
COLOR_SENSOR = port.C
COLOR_SENSOR_2 = port.D


def inColor(r, g, b, color_range, sensor_port) -> bool:
    """
    Returns True if the color sensor is reading close to the given RGB values.
    r, g, and b should be 0-255 values.
    """
    detected = color_sensor.rgbi(sensor_port)

    # Change this if your raw sensor values max out higher or lower
    max_value = 1024

    detected_r = int((detected[0] / max_value) * 255)
    detected_g = int((detected[1] / max_value) * 255)
    detected_b = int((detected[2] / max_value) * 255)
    print("Detected colors: ", detected_r, detected_g, detected_b)
    return (
        abs(detected_r - r) <= color_range and
        abs(detected_g - g) <= color_range and
        abs(detected_b - b) <= color_range
    )

async def turnRight(time_ms, speed):
    """
    Turns right using the motor pair.
    """
    motor_pair.pair(motor_pair.PAIR_1, LEFT_MOTOR, RIGHT_MOTOR)
    motor_pair.move(motor_pair.PAIR_1, 100, velocity=speed)
    await runloop.sleep_ms(time_ms)
    motor_pair.stop(motor_pair.PAIR_1)


async def turnLeft(time_ms, speed):
    """
    Turns left using the motor pair.
    """
    motor_pair.pair(motor_pair.PAIR_1, LEFT_MOTOR, RIGHT_MOTOR)
    motor_pair.move(motor_pair.PAIR_1, -100, velocity=speed)
    await runloop.sleep_ms(time_ms)
    motor_pair.stop(motor_pair.PAIR_1)


async def moveForward(time_ms, speed):
    """
    Moves forward using the motor pair.
    """
    motor_pair.pair(motor_pair.PAIR_1, LEFT_MOTOR, RIGHT_MOTOR)
    motor_pair.move(motor_pair.PAIR_1, 0, velocity=speed)
    await runloop.sleep_ms(time_ms)
    motor_pair.stop(motor_pair.PAIR_1)


async def moveBackward(time_ms, speed):
    """
    Moves backward using the motor pair.
    """
    motor_pair.pair(motor_pair.PAIR_1, LEFT_MOTOR, RIGHT_MOTOR)
    motor_pair.move(motor_pair.PAIR_1, 0, velocity=-speed)
    await runloop.sleep_ms(time_ms)
    motor_pair.stop(motor_pair.PAIR_1)

async def main():
    print("Running program")
    await light_matrix.write("Hi!")

    while True:
        #print(color_sensor.rgbi(COLOR_SENSOR))

        if inColor(0, 0, 20, COLOR_RANGE, COLOR_SENSOR):
            print("BORDER detected! Turning 180 around.")
            await turnLeft(900, 500)
            await runloop.sleep_ms(1000)

        elif (inColor(100, 25, 60, COLOR_RANGE, COLOR_SENSOR) or inColor(100, 25, 60, COLOR_RANGE, COLOR_SENSOR_2)):
            sound.beep(600, 500, 100)
            print("RED Mine detected! Turning left.")
            await turnLeft(400, 500)
            await runloop.sleep_ms(1000)

        elif (inColor(150, 150, 100, COLOR_RANGE, COLOR_SENSOR) or inColor(150, 150, 100, COLOR_RANGE, COLOR_SENSOR_2)):
            print("YELLOW mine detected. Turning right!")
            await turnRight(400, 500)
            await runloop.sleep_ms(1000)


        elif (inColor(150, 150, 130, COLOR_RANGE, COLOR_SENSOR) or inColor(150, 150, 130, COLOR_RANGE, COLOR_SENSOR_2)):
            print("BEIGE mine detected! Turning left!")
            await turnLeft(400, 500)
            await runloop.sleep_ms(1000)

        elif (inColor(100, 60, 50, COLOR_RANGE, COLOR_SENSOR) or inColor(100, 60, 50, COLOR_RANGE, COLOR_SENSOR_2)):
            print("ORANGE mine detected! Turning right!")
            await turnRight(400, 500)
            await runloop.sleep_ms(1000)

        else:
            print("No colors detected! Moving slowly forward!")
            await moveForward(100, 200)

        await runloop.sleep_ms(100)


runloop.run(main())