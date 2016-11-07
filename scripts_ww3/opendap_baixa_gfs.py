from pydap.client import open_url
import numpy as np
from netCDF4 import Dataset

#acessar os dados por opendap no servidor
u_component = open_url('http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs20160616/gfs_0p25_1hr_00z')['ugrd10m']
v_component = open_url('http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs20160616/gfs_0p25_1hr_00z')['vgrd10m']
tempo = open_url('http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs20160616/gfs_0p25_1hr_00z')['time'][0:121:3]
lats = open_url('http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs20160616/gfs_0p25_1hr_00z')['lat'][:]
lons = open_url('http://nomads.ncep.noaa.gov:80/dods/gfs_0p25_1hr/gfs20160616/gfs_0p25_1hr_00z')['lon'][:]

ugrd_10m = u_component.array[0:121:3,:,:]
vgrd_10m = v_component.array[0:121:3,:,:]

# criando arquivo netcdf
dataset = Dataset('/home/piatam8/Desktop/rafael_ondas/wavewatch3/resultados_gfs/arquivo_criado/dap_wind.nc', 'w', format='NETCDF3_CLASSIC')

# criando dimensoes
lat = dataset.createDimension('latitude', lats.size)
lon = dataset.createDimension('longitude', lons.size)
time = dataset.createDimension('time', tempo.size)

# criando variaveis
latitudes = dataset.createVariable('latitude', "f8", ('latitude',))
longitudes = dataset.createVariable('longitude', "f8", ('longitude',))
times = dataset.createVariable('time', "f8", ('time',))

# criando as variaveis U e V em 3D
u_wnd10m_component = dataset.createVariable('u_wnd10m_component', "f4", ('time', 'latitude', 'longitude'))
v_wnd10m_component = dataset.createVariable('v_wnd10m_component', "f4", ('time', 'latitude', 'longitude'))

# global attributes     
dataset.description = 'NCEP/NOAA - GFS WIND - 0.25 degree'

# variable attributes
latitudes.units = 'degree_north'
longitudes.units = 'degree_east'
times.units = 'days since 0000-12-30 00:00:0.0'

# adicionando dados 
latitudes[:] = lats
longitudes[:] = lons
u_wnd10m_component[:] = ugrd_10m[:]
v_wnd10m_component[:] = vgrd_10m[:]
times[:] = tempo
dataset.close()