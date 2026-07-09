from hub import light_matrix, port, sound
import runloop
import motor
import color_sensor

COLOR_RANGE = 5

DRIVE_MOTOR = port.A
STEERING_MOTOR = port.B

COLOR_SENSOR = port.C
COLOR_SENSOR_2 = port.D

STEERING_CENTER = 0
STEERING_LEFT = -90
STEERING_RIGHT = 90


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


async def lockSteeringCenter():
    """
    Locks Motor B to the default center rotation.
    """
    await motor.run_to_absolute_position(STEERING_MOTOR, STEERING_CENTER, 300)


async def turnRight(time_ms, speed):
    """
    Turns right using the steering motor.
    """
    await motor.run_to_absolute_position(STEERING_MOTOR, STEERING_RIGHT, 300)

    motor.run(DRIVE_MOTOR, speed)
    await runloop.sleep_ms(time_ms)
    motor.stop(DRIVE_MOTOR)

    await lockSteeringCenter()


async def turnLeft(time_ms, speed):
    """
    Turns left using the steering motor.
    """
    await motor.run_to_absolute_position(STEERING_MOTOR, STEERING_LEFT, 300)

    motor.run(DRIVE_MOTOR, speed)
    await runloop.sleep_ms(time_ms)
    motor.stop(DRIVE_MOTOR)

    await lockSteeringCenter()


async def moveForward(time_ms, speed):
    """
    Moves forward using Motor A.
    """
    await lockSteeringCenter()

    motor.run(DRIVE_MOTOR, speed)
    await runloop.sleep_ms(time_ms)
    motor.stop(DRIVE_MOTOR)


async def moveBackward(time_ms, speed):
    """
    Moves backward using Motor A.
    """
    await lockSteeringCenter()

    motor.run(DRIVE_MOTOR, -speed)
    await runloop.sleep_ms(time_ms)
    motor.stop(DRIVE_MOTOR)


async def main():
    print("Running program")
    await light_matrix.write("Hi!")

    # Lock the steering motor to the default center position before starting.
    await lockSteeringCenter()

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
            await moveForward(200, 200)

        await runloop.sleep_ms(100)


runloop.run(main())