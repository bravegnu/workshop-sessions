#!/usr/bin/python
import time
from pwm import PWM

buzz = PWM("2")
buzz.export_channel()

melody = ["379218", "379218", "100000", "379218",
          "100000", "477782", "379218", "100000",
          "318878", "100000", "100000", "100000",
          "637754", "100000", "100000", "100000",
          "477782", "100000", "100000", "637754",
          "100000", "100000", "75814",  "100000",
          "100000", "568182" "100000", "506072",
          "100000", "536192", "568182", "100000",
          "637754", "379218", "379218", 
          "284092", "100000", "35792", "318878",
          "100000", "379218", "100000", "477782",
          "100000", "379218", "100000", "477782",
          "425712", "506072", "100000", "100000",
          "379218", "379218", "100000", "379218",
          "100000", "477782", "379218", "100000",
          "318878", "100000", "100000", "100000",
          "637754", "100000", "100000", "100000",
          "284092", "100000", "35792", "318878",
          "100000", "379218", "100000", "477782",
          "100000", "379218", "100000", "477782",
          "425712", "506072", "100000", "100000",
          ]

note = [0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        
        0.111, 0.111, 0.111,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        
        0.111, 0.111, 0.111,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,]

loop = 0
while loop in range(1):
    count = 0
    for count in range(18):
        buzz.set_period_ns(melody[count])
        duty = int(melody[count])/2
        duty = str(int(duty))
        buzz.set_dutycycle_ns(duty)
        buzz.start()
        time.sleep(note[count])
        buzz.stop()
        time.sleep(note[count])
        count += 1
    loop += 1

buzz.unexport_channel()