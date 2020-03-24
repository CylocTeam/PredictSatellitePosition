from skyfield.api import Topos, load
from astropy.time import Time
import params
import Prediction
import pandas as pd
import pymap3d as pm

# Remember find SGP8 model without using any connection

# Create predition object for GPS satellites
prediction = Prediction.Prediction(path_TLE=params.TLE_GPS_URL)
print("TLE file time:"+str(prediction.get_TLE_file_time()))
# Set observation location and time
obs_datetime_str = '2020-03-23 08:15:27.243860'
obs_lon = 32.062930
obs_lat = 34.776593
prediction.set_observation_time(obs_datetime_str)
prediction.set_observation_location(obs_lon, obs_lat)
satellite_relative_to_obs = prediction.get_all_satellites_position_relative_to_obs_TLE()

pass
# # Define timescale for TLE files
# ts = load.timescale()
# # Define wanted date and user location
# t = ts.utc(2020, 3, 24, 11, 18, 7)
# obs_time = Time('2020-03-23 12:00:00')
# user_location = ""
# # Read TLE file
# stations_url = "https://www.celestrak.com/NORAD/elements/gps-ops.txt"
# satellites = load.tle(stations_url)
# satellite = satellites['GPS BIIF-8  (PRN 03)']
# print(satellite)
#
# days = t - satellite.epoch
# print('{:.3f} days away from epoch'.format(days))
#
# # Get satellite position using TLE
# geocentric = satellite.at(t)  # GCRS coordinates
# print(geocentric.position.km)
# subpoint = geocentric.subpoint()
# print('Latitude:', subpoint.latitude)
# print('Longitude:', subpoint.longitude)
# print('Elevation (m):', int(subpoint.elevation.m))
# observer_lon = 32.062930
# observer_lat = 34.776593
# bluffton = Topos('34.776593 N', '32.062930 W')
# difference = satellite - bluffton
# difference_at_t = difference.at(t)
# elev_tle, az_tle, distance_tle = difference_at_t.altaz()
# print(difference.at(t).position.km)


