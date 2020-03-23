import numpy as np
from skyfield.api import Topos, load
import params

class Prediction:
    def __init__(self, path_TLE = None, path_RINEX=None):
        self.tle_satellites = load.tle(path_TLE)
        self.rinex_satelltes = ""
        self.obs_time = None
        self.obs_lon = None
        self.obs_lat = None

    def set_observation_time(self, time_str):
        """
        set_observation_time - sets observation time
        """

    def get_TLE_file_time(self):
        pass
    def predict_satellite_position_TLE(self, path_TLE_):
        pass
    def get_satellite_position(self, satellite_TLE_name):
        satellite = self.tle_satellites[satellite_TLE_name]