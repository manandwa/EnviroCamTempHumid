# Mobin Anandwala
# Date: 10/31/2016
# Script Title: Envriocam_temp_humidity_10312016.py
# Purpose: Simulate adjustable temperature settings in Onelink app
# Changelog: Script revised to include user input


## Load defaults
# Homekit temperature defaults are as follows 68 to 79 F (20 to 26 C)
# Homekit humidity defaults are as follows (30% to 60% RH)

# Convert this into a dictionary with both F and C readings for temperature
hk_defaults = {'temp_low': 68,'temp_low_C': 20, 'temp_high': 79, 'temp_high_C': 26, 'humid_low': 30, 'humid_high': 60}

def temp_reset():
        temp = [hk_defaults['temp_low'],hk_defaults['temp_high']]
        return temp

def startup():
        temp = [hk_defaults['temp_low'],hk_defaults['temp_high']]
        humidity = [hk_defaults['humid_low'],hk_defaults['humid_high']]
        return temp, humidity

def adjustable_temp_low(newtemp):
        temp[0] = newtemp
        return temp[0]

def adjustable_temp_high(newtemp):
        temp[1] = newtemp
        return temp[1]

# Load defaults
temp, humidity = startup()

# Ask user to set lower bound
newtemp_low = int(raw_input('Please enter a minimum for the temperature: '))
if newtemp_low < 30:
    print('Too Low!')
else:
    temp[0] = adjustable_temp_low(newtemp_low)
    print('New temperature lower bound is: ' + str(temp[0]))

# Ask user to set upper bound
newtemp_high = int(raw_input('Please enter a maximum for the temperature: '))
if newtemp_low > 90:
    print('Too High')
else:
    temp[1] = adjustable_temp_high(newtemp_high)
    print('New temperature upper bound is: ' + str(temp[1]))

defaults_return = raw_input('Do you wish to return to default temperature Yes\No?')
if defaults_return == 'Yes' or defaults_return == 'Y' or defaults_return == 'yes' or defaults_return == 'y':
    temp = temp_reset()
    print('Temperature returned to homekit defaults')
elif defaults_return == 'No' or defaults_return == 'N' or defaults_return == 'no' or defaults_return == 'n':
    print('Temperature settings not reset')
else:
    print('Invalid Input!!')
