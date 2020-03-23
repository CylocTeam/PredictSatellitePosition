import numpy as np
from skyfield.api import Topos, load
import params
import pandas as pd


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
        # all satellites in the tle file are with the same epoch
        # therefore we use the first
        first_sat = self.tle_satellites_names.iloc[0]
        satellite = self.tle_load_satellites[first_sat]

    def predict_satellite_position_TLE(self, path_TLE_):
        pass

    def get_satellite_position(self, satellite_TLE_name):
        satellite = self.tle_file[satellite_TLE_name]
