# This will simulate the temperature and humidity adjustment in python
# Note that the app functions cannot be simulated right now

temp_low_hk_default = 68
temp_high_hk_default = 79
humidity_low_hk = 30
humidity_high_hk = 60

def reset():
        temp, humidity = startup()
        return temp, humidity

def startup():
        temp = [temp_low_hk_default,temp_high_hk_default]
        humidity = [humidity_low_hk,humidity_high_hk]
        return temp, humidity

def adjustable_temp_low(newtemp):
        temp[0] = newtemp
        return temp[0]

def adjustable_temp_high(newtemp):
        temp[1] = newtemp
        return temp[1]

# Load defaults
temp, humidity = startup()


