import pywapi
import string

google_result = pywapi.get_weather_from_google('10001')
yahoo_result = pywapi.get_weather_from_yahoo('10001')
noaa_result = pywapi.get_weather_from_noaa('KCLL')

#print ("Google says: It is " + (google_result['current_conditions']['condition']) + " and " + google_result['current_conditions']['temp_c'] + "C now in New York.\n\n")

#print ("Yahoo says: It is " + (yahoo_result['condition']['text']) + " and " + yahoo_result['condition']['temp'] + "C now in New York.\n\n")

print ("NOAA says: It is " + (noaa_result['weather']) + " and " + noaa_result['temp_f'] + "F in College Station.\n")
