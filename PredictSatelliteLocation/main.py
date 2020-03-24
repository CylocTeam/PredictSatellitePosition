import params
import Prediction

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


