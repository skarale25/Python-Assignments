#! /usr/bin/env python3

# This assignment focuses on the design and implementation of a Python program
# to display information about the energy released by earthquakes in joules
# and in tons of exploded TNT.


def calc_energy():
    try:
        richter_scale = float(input("Enter the richter scale for earthquake: "))
        # new string formatting method
        print("Richter Scale value: %(richter)s" % {"richter": richter_scale})

        energy_joules = 10**((1.5 * richter_scale)+4.8)
        print("Energy equivalence in joules:" + str(energy_joules))

        TNT = energy_joules / 4.184 * 10**9
        print("Energy equivalence in Tones of TNT:" + str( TNT))

    except NameError:
        print "Invalid input type. Please enter input of type float."

    except Exception as e:
        print e


if __name__ == '__main__':
    calc_energy()
