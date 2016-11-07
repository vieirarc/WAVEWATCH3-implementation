import pygrib 
import numpy as np
from netCDF4 import Dataset
from os import listdir


u_wind = {}
v_wind = {}
diretorio = '/home/rafael/Documentos/lamce/wavewatch3/resultados_gfs/arquivos_grib'

for file in listdir(diretorio):
	grbs = pygrib.open(file)
	U_grd10m = grbs.select(name='10 metre U wind component')[0]
	V_grd10m = grbs.select(name='10 metre V wind component')[0]
	U_grd10m_field = U_grd10m.values
	V_grd10m_field = V_grd10m.values
	u_wind["u_grd10m_{0}".format(file[22:24])] = U_grd10m_field[::-1] # inverse U array 
	v_wind["v_grd10m_{0}".format(file[22:24])]= V_grd10m_field[::-1] # inverse V array
    

u_component = np.stack((u_wind['u_grd10m_00'], u_wind['u_grd10m_03'], u_wind['u_grd10m_06'], u_wind['u_grd10m_09'], \
	u_wind['u_grd10m_12'], u_wind['u_grd10m_15'], u_wind['u_grd10m_18'], u_wind['u_grd10m_21']), axis=0)

v_component = np.stack((v_wind['v_grd10m_00'], v_wind['v_grd10m_03'], v_wind['v_grd10m_06'], v_wind['v_grd10m_09'], \
	v_wind['v_grd10m_12'], v_wind['v_grd10m_15'], v_wind['v_grd10m_18'], v_wind['v_grd10m_21']), axis=0)


# criando arquivo netcdf
dataset = Dataset('/home/rafael/Documentos/lamce/wavewatch3/resultados_gfs/arquivo_criado/wnd_gfs.nc', 'w', format='NETCDF3_CLASSIC')

# criando dimensoes
lat = dataset.createDimension('lat', 181) 
lon = dataset.createDimension('lon', 360)
time = dataset.createDimension('time', 8)

# criando variaveis
latitudes = dataset.createVariable('latitude', np.float32, ('lat',))
longitudes = dataset.createVariable('longitude', np.float32, ('lon',))
times = dataset.createVariable('time', np.float64, ('time',))

# criando as variaveis U e V em 3D
u_wnd10m_component = dataset.createVariable('u_wnd10m_component', np.float32, ('time', 'lat', 'lon'))
v_wnd10m_component = dataset.createVariable('v_wnd10m_component', np.float32, ('time', 'lat', 'lon'))

# global attributes	
dataset.description = 'NCEP/NOAA - GFS WIND'

# variable attributes
latitudes.units = 'degree_north'
longitudes.units = 'degree_east'
times.units = 'hours'

# adicionando dados 
lats = np.arange(-90,91)
lons = np.arange(0,360)
#lons, lats = np.meshgrid(lons, lats)
latitudes[:] = lats
longitudes[:] = lons 
u_wnd10m_component[:] = u_component
v_wnd10m_component[:] = v_component

dataset.close()