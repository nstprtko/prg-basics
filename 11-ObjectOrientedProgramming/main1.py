from thermometer import Thermometer
import random

def main():
    my_thermometer = Thermometer()
    my_thermometer.turn_on()
    temperature = round(random.uniform(34, 42),1)
    my_thermometer.measure(temperature)
    my_thermometer.turn_off()


if __name__ =='__main__':
    main()