###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

temperature_in_celcius = int(input('Enter the temperature in Celcius :')) #nput of data

temperature_in_farenheit = (temperature_in_celcius * 9/5) + 32 #conversion to farenheit

temperature_in_kelvin = temperature_in_celcius + 273.15


print(f'Your given temperature in Celcius : {temperature_in_celcius}')
print(f'Converted temperature in Farenheit: {temperature_in_farenheit}') # print the results
print(f'Converted temperature in Kelvin : {temperature_in_kelvin} ')



