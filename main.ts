radio.onReceivedString(function (receivedString) {
    if (receivedString == "hi") {
        basic.showIcon(IconNames.SmallHeart)
    } else if (receivedString == "forward") {
        pins.servoWritePin(AnalogPin.P15, 180)
        pins.servoWritePin(AnalogPin.P16, 0)
        basic.showLeds(`
            . . # . .
            . # . # .
            # . . . #
            . . . . .
            . . . . .
            `)
    } else if (receivedString == "reverse") {
        pins.servoWritePin(AnalogPin.P15, 0)
        pins.servoWritePin(AnalogPin.P16, 180)
        basic.showLeds(`
            . . . . .
            . . . . .
            # . . . #
            . # . # .
            . . # . .
            `)
    } else if (receivedString == "stop") {
        basic.showIcon(IconNames.No)
        pins.servoWritePin(AnalogPin.P15, 88)
        pins.servoWritePin(AnalogPin.P16, 88)
        control.reset()
    } else if (receivedString == "left") {
        basic.showLeds(`
            . . # . .
            . # . . .
            # . . . .
            . # . . .
            . . # . .
            `)
        pins.servoWritePin(AnalogPin.P15, 90)
        pins.servoWritePin(AnalogPin.P16, 0)
    } else if (receivedString == "right") {
        basic.showLeds(`
            . . # . .
            . . . # .
            . . . . #
            . . . # .
            . . # . .
            `)
        pins.servoWritePin(AnalogPin.P15, 180)
        pins.servoWritePin(AnalogPin.P16, 90)
    }
})
basic.showIcon(IconNames.SmallHeart)
radio.setGroup(11)
