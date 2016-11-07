import pygrib 
import matplotlib.pyplot as plt
import numpy as np
from netCDF4 import Dataset

#opening .grib file
grib_file = 'gfs.t12z.pgrb2.1p00.f000'
grbs = pygrib.open(grib_file)

#select U-V 10m components, lat e lon
U_grd10m = grbs.select(name='10 metre U wind component')[0]
V_grd10m = grbs.select(name='10 metre V wind component')[0]
lat_f, lon_f = U_grd10m.latlons()
lat_f = lat_f[::-1] #inverse lat
lon_f = lon_f[::-1] #inverse lon

#extracting U-V components values
U_grd10m_field = U_grd10m.values
V_grd10m_field = V_grd10m.values
U_grd10m_field = U_grd10m_field[::-1] # inverse U array 
V_grd10m_field = V_grd10m_field[::-1] # inverse V rray 

# junta variaveis em 3D
U_component = np.stack((U_grd10m_field, V_grd10m_field), axis=0)


# criando arquivo netcdf
dataset = Dataset('wnd_gfs.nc', 'w', format='NETCDF4_CLASSIC')

# criando dimensoes
lat = dataset.createDimension('lat', 181) 
lon = dataset.createDimension('lon', 360)
time = dataset.createDimension('time', 2)

# criando variaveis
latitudes = dataset.createVariable('latitude', np.float32, ('lat', 'lon'))
longitudes = dataset.createVariable('longitude', np.float32, ('lat', 'lon'))
times = dataset.createVariable('time', np.float64, ('time',))

# criando a variavel U em 3D
u_wnd10m_component = dataset.createVariable('u_wnd10m_component', np.float32, ('time', 'lat', 'lon'))

# global attributes	
dataset.description = 'NCEP/NOAA - GFS WIND'

# variable attributes
latitudes.units = 'degree_north'
longitudes.units = 'degree_east'
times.units = 'hours'

# adicionando dados 
lats = np.arange(-90,91)
lons = np.arange(0,360)
lons, lats = np.meshgrid(lons, lats)
latitudes[:] = lats
longitudes[:] = lons 
u_wnd10m_component[:] = U_component

dataset.close()