

import pygrib 
import matplotlib.pyplot as plt
from netCDF4 import Dataset

#opening .grib file
wind_file = 'gfs.t00z.pgrb2.1p00.f000'
grbs = pygrib.open(wind_file)

#selecting all U-V components
U_grd10m = grbs.select(name='10 metre U wind component')[0]
V_grd10m = grbs.select(name='10 metre V wind component')[0]
lat, lon = U_grd10m.latlons()

#extracting U-V components values
U_grd10m_field = U_grd10m.values
V_grd10m_field = V_grd10m.values

#plotting wind field
#plt.quiver(lon, lat, U_grd10m_field, V_grd10m_field)
plt.pcolor(lon, lat, U_grd10m_field)
plt.show()
