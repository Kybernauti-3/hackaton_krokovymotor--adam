from machine import Pin
import utime

pins = [
    Pin(0,Pin.OUT),#IN1
    Pin(1,Pin.OUT),#IN2
    Pin(2,Pin.OUT),#IN3
    Pin(3,Pin.OUT),#IN4
]
full_step_sequence = [
    [0,0,1,1],
    [0,1,1,0],
    [1,1,0,0],
    [1,0,0,1],
]

while True:
    for step in full_step_sequence:
        for i in range(len(pins)):
            pins[i].value(step[i])
            utime.sleep(0.003)
