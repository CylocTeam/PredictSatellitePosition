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

    def set_observation_time(self, time_str):
        """
        set_observation_time - sets observation time
        time str
        """

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

    def predict_satellite_position_TLE(self, path_TLE_):
        pass

    def get_satellite_position(self, satellite_TLE_name):
        satellite = self.tle_file[satellite_TLE_name]
