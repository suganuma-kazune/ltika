def on_forever():
    pins.digital_write_pin(DigitalPin.P0, 1)
basic.forever(on_forever)
