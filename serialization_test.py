###############################################################################
#######     TITLE "Project Envirocam "      ########
#######     SUBTITLE "COPYRIGHT 2015 BRK BRANDS, INC., FIRST ALERT"    ########
###############################################################################
#######     MODEL:         AC10-500 DC10-500                           ########
###############################################################################
#######     PROJECT:       ONELINK WiFi Smoke and CO Alarm              #######
#######     FILENAME:      serialization_test.py                        #######
#######     DATE:          10/19/2016                                   #######
#######     FILE VERSION:  VERSION 1.0                                  #######
#######     AUTHOR:        MOBIN ANANDWALA                              #######
#######     COMPANY:       BRK BRANDS, INC., FIRST ALERT, INC.          #######
#######                    3901 LIBERTY STREET ROAD                     #######
#######                    AURORA, IL 60504-8122                        #######
###############################################################################
#######     HISTORY:       10/19/2016 FIRST RELEASE                    #######
#######                     10/20/2016 ADDED WIFI CREDENTIALS          #######
###############################################################################

import uuid
import os

model = 'ENVIROCAM-500'
#print('Model is ' + model)
serialNumber = str(uuid.uuid4()).translate(None, ''.join('-')).upper()
#print('Serial Number is ' + serialNumber)
cryptoKey = os.urandom(16).encode('hex').upper()
#print('Cryptokey is ' + cryptoKey)
accessToken = os.urandom(16).encode('hex').upper()
#print('Access token is ' + accessToken)
Wifi_ssid = raw_input('Enter the ssid of the wifi network that you will be using for serialization: ')
#print(Wifi_ssid)
Wifi_pw = raw_input('Enter the password of the wifi network that you will be using for serialization: ')
#print(Wifi_pw)

with open('./test_result.txt','wb') as result_file:
    result_file.write('Model: ' + model + '\n')
    result_file.write('Serial Number: ' + serialNumber + '\n')
    result_file.write('Cryptokey: ' + cryptoKey + '\n')
    result_file.write('Access token: ' + accessToken + '\n')
    result_file.write('WiFi SSID: ' + Wifi_ssid + '\n')
    result_file.write('WiFi Password: ' + Wifi_pw + '\n')
    result_file.close()

# Readback the file and print it here
with open('./test_result.txt', 'r') as result_file:
    flashed_model = result_file.readline().replace('\n','')
    print('Flashed Model is: ' + flashed_model)
    flashed_serial = result_file.readline().replace('\n','')
    print('Flashed serial number is:' + flashed_serial)
    flashed_cryptokey = result_file.readline().replace('\n','')
    print('Flashed cryptokey is: ' + flashed_cryptokey)
    flashed_accesstoken = result_file.readline().replace('\n','')
    print('Flashed access token is: ' + flashed_accesstoken)
    flashed_WiFi_SSID = result_file.readline().replace('\n','')
    print('Flashed WiFI SSID is: ' + flashed_WiFi_SSID)
    flashed_WiFi_PW = result_file.readline().replace('\n','')
    print('Flashed WiFI PW is: ' + flashed_WiFi_PW)
    result_file.close()


    


