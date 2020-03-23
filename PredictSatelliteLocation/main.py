from skyfield.api import Topos, load
import ephem
from astropy import units as u
from astropy import coordinates as coord
from astropy.time import Time
import pymap3d as pm

# Remember find SGP8 model without using any connection

# Define timescale for TLE files
ts = load.timescale()
# Define wanted date and user location
t = ts.utc(2020, 3, 24, 11, 18, 7)
obs_time = Time('2020-03-23 12:00:00')
user_location = ""
# Read TLE file
stations_url = "https://www.celestrak.com/NORAD/elements/gps-ops.txt"
satellites = load.tle(stations_url)
satellite = satellites['GPS BIIF-8  (PRN 03)']
print(satellite)

days = t - satellite.epoch
print('{:.3f} days away from epoch'.format(days))

# Get satellite position using TLE
geocentric = satellite.at(t)  # GCRS coordinates
print(geocentric.position.km)
subpoint = geocentric.subpoint()
print('Latitude:', subpoint.latitude)
print('Longitude:', subpoint.longitude)
print('Elevation (m):', int(subpoint.elevation.m))
observer_lon = 32.062930
observer_lat = 34.776593
bluffton = Topos('34.776593 N', '32.062930 W')
difference = satellite - bluffton
difference_at_t = difference.at(t)
elev_tle, az_tle, distance_tle = difference_at_t.altaz()
print(difference.at(t).position.km)
pass
# cartrep = coord.CartesianRepresentation(x=geocentric.position.km[0],
#                                         y=geocentric.position.km[1],
#                                         z=geocentric.position.km[2],
#                                         unit=u.km)
# gcrs = coord.GCRS(cartrep, obstime=obs_time)
# itrs = gcrs.transform_to(coord.ITRS(obstime=obs_time))
# # loc = coord.EarthLocation(*itrs.cartesian)
#
# # az, el, range = pm.geodetic2aer(geocentric.position.km[1], geocentric.position.km[0], geocentric.position.km[2], observer_lat, observer_lon, 0)
# # print(loc.lat, loc.lon, loc.height)
# tle_file = ""

# sat = "GPS BIIR-2  (PRN 13)"
# line1 = "1 24876C 97035A   20084.70201389 -.00000000  00000-0  00000-0 0   841"
# line2 = "2 24876  55.4535 187.4631 0039305  63.3714 311.8540  2.00565462    13"
# satellite = ephem.readtle(sat, line1, line2)
# obs = ephem.Observer()
# obs.lat = ''  # latitude of the observation point in string
# obs.lon = ''  # longitude of the observation point in string
#
#
# # Try read tle using ephem
# f = open(stations_url, "rw+")
