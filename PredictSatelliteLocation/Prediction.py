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
        self.obs_datetime = None
        self.obs_lon = None
        self.obs_lat = None
        self.satellites_position_tle = pd.DataFrame(columns=['satellite', 'elevation', 'azimuth', 'time'])

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
                       date_time_obj.minute, date_time_obj.second + date_time_obj.microsecond / 1e6)
        except Exception as c:
            date_time_obj = datetime.strptime(obs_datetime_str, '%Y-%m-%d %H:%M:%S')
            t = ts.utc(date_time_obj.year, date_time_obj.month, date_time_obj.day, date_time_obj.hour,
                       date_time_obj.minute, date_time_obj.second)
        self.obs_time = t
        self.obs_datetime = date_time_obj

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

    def get_all_satellites_position_relative_to_obs_TLE(self):

        if self.obs_time is None:
            print('Please set observation time, your observation time is none')
            return
        if self.obs_lon is None:
            print('Please set observation location, your observation lon and lat are none')
            return
        obs_position = Topos(np.str(self.obs_lat) + ' N', np.str(self.obs_lon) + ' W')
        for current_satellite in self.tle_satellites_names:
            current_satellite_position = self.get_satellite_position_TLE(current_satellite)
            if not current_satellite_position is None:
                difference = current_satellite_position - obs_position
                difference_at_obs_time = difference.at(self.obs_time)
                elev_tle, az_tle, distance_tle = difference_at_obs_time.altaz()
                current_row = {'satellite': current_satellite, 'elevation': np.float(elev_tle.degrees),
                               'azimuth': np.float(az_tle.degrees), 'time': str(self.obs_datetime)}
                self.satellites_position_tle = self.satellites_position_tle.append(current_row, ignore_index=True)
        return self.satellites_position_tle

    def get_satellite_position_TLE(self, satellite_TLE_name):
        try:
            satellite = self.tle_load_satellites[satellite_TLE_name]
        except Exception as c:
            print('satellite:'+satellite_TLE_name+'is not in the TLE file')
            return
        if self.obs_time is None:
            print('Please set observation time, your observation time is none')
            return
        geocentric = satellite.at(self.obs_time)
        satellite_position_tle = geocentric.subpoint()
        return satellite_position_tle
