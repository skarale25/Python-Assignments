#! /usr/bin/env python3

# This assignment focuses on the design and  implementation testing of a Python
# program to display the wind chill temperature index under certain condition.

def calc_wct():
    """This function will calculate wind chill temparature"""
    air_temp = float(input("Enter air temperature: "))
    wind_speed = float(input("Enter wind speed: "))
    print("Air Temperature: %(temp)s" % {"temp": air_temp})
    print("Wind speed: %(speed)s"% {"speed": wind_speed})
    wct = 35.74 + 0.6215 * air_temp - 35.75 * wind_speed**0.16 \
          + 0.4275 * air_temp * wind_speed**0.16
    print("Wind Chill Temperature: %(wct)s"% {"wct": wct})

if __name__ == '__main__':
    calc_wct()
