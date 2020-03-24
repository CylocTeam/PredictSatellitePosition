from skyfield.api import Topos, load
from datetime import datetime
import pandas as pd
import numpy as np
import params


class Prediction:
    def __init__(self, path_TLE=None, path_RINEX=None):
        self.tle_load_satellites = load.tle(path_TLE)
        self.tle_satellites_names = pd.read_csv(params.GPS_TLE_NAMES_PATH, header=None)[0]
        self.rinex_satelltes = ""
        self.obs_time = None
        self.obs_lon = None
        self.obs_lat = None

    def set_observation_time(self, obs_datetime_str):
        """
        set_observation_time - sets observation utc time
        Inputs:
            obs_datetime_str - string of observation utc time in the following format
                                '%Y-%m-%d %H:%M:%S.%f' for example  '2018-06-29 08:15:27.243860' or
                                '%Y-%m-%d %H:%M:%S' for example  '2018-06-29 08:15:27'
        """
        ts = load.timescale()
        try:
            date_time_obj = datetime.strptime(obs_datetime_str, '%Y-%m-%d %H:%M:%S.%f')
            t = ts.utc(date_time_obj.year, date_time_obj.month, date_time_obj.day, date_time_obj.hour,
                       date_time_obj.minute, date_time_obj.second, np.int(date_time_obj.microsecond/1000))
        except Exception as c:
            date_time_obj = datetime.strptime(obs_datetime_str, '%Y-%m-%d %H:%M:%S')
            t = ts.utc(date_time_obj.year, date_time_obj.month, date_time_obj.day, date_time_obj.hour,
                       date_time_obj.minute, date_time_obj.second)
            self.obs_time = t

    def get_TLE_file_time(self):
        """
        get_TLE_file_time returns the utc time of the tle file in datetime format
        """
        # all satellites in the tle file are with the same epoch
        # therefore we use the first
        first_sat = self.tle_satellites_names.iloc[0]
        satellite = self.tle_load_satellites[first_sat]
        tle_time_vec = satellite.epoch.utc

        self.tle_time = datetime(tle_time_vec[0], tle_time_vec[1], tle_time_vec[2],
                                 tle_time_vec[3], tle_time_vec[4], np.int(np.floor(tle_time_vec[5])),
                                 np.int(np.mod(tle_time_vec[5], 1) * 1000))
        return self.tle_time

    def set_observation_location(self, obs_lon, obs_lat):
        self.obs_lon = obs_lon
        self.obs_lat = obs_lat

    def predict_satellite_position_TLE(self, path_TLE_):
        pass

    def get_satellite_position_TLE(self, satellite_TLE_name):
        satellite = self.tle_file[satellite_TLE_name]
        if self.obs_time is None:
            print('Please set observation time, your observation time is none')
            return
        geocentric = satellite.at(self.obs_time)
        satellite_position_tle = geocentric.subpoint()
        return satellite_position_tle