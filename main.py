def on_received_string(receivedString):
    if receivedString == "hi":
        basic.show_icon(IconNames.SMALL_HEART)
        servos.P0.run(50)
    elif receivedString == "forward":
        pins.servo_write_pin(AnalogPin.P15, 180)
        pins.servo_write_pin(AnalogPin.P16, 0)
        basic.show_leds("""
            . . # . .
            . # . # .
            # . . . #
            . . . . .
            . . . . .
            """)
    elif receivedString == "reverse":
        pins.servo_write_pin(AnalogPin.P15, 0)
        pins.servo_write_pin(AnalogPin.P16, 180)
        basic.show_leds("""
            . . . . .
            . . . . .
            # . . . #
            . # . # .
            . . # . .
            """)
    elif receivedString == "stop":
        basic.show_icon(IconNames.NO)
        pins.servo_write_pin(AnalogPin.P15, 88)
        pins.servo_write_pin(AnalogPin.P16, 88)
    elif receivedString == "left":
        basic.show_leds("""
            . . # . .
            . # . . .
            # . . . .
            . # . . .
            . . # . .
            """)
        pins.servo_write_pin(AnalogPin.P15, 90)
        pins.servo_write_pin(AnalogPin.P16, 0)
    elif receivedString == "right":
        basic.show_leds("""
            . . # . .
            . . . # .
            . . . . #
            . . . # .
            . . # . .
            """)
        pins.servo_write_pin(AnalogPin.P15, 180)
        pins.servo_write_pin(AnalogPin.P16, 90)
radio.on_received_string(on_received_string)

basic.show_icon(IconNames.SMALL_HEART)
radio.set_group(11)