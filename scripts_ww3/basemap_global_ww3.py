# hs ww3 global #



from mpl_toolkits.basemap import Basemap, cm
import netCDF4
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio


hs_global = netCDF4.Dataset('/home/rafael/Desktop/ww3.201606_hs.nc','r')

# campo = range[1,20]
hs_global_2 = hs_global.variables['hs'][120,:,:]

m = Basemap(projection='mill', llcrnrlat=-71, llcrnrlon=-360, urcrnrlat=71, urcrnrlon=0, resolution='c')

m.drawcoastlines()
m.drawstates()

m.imshow(hs_global_2, cm.GMT_haxby)
plt.title('Altura significativa de ondas - Grade global')
plt.colorbar()
plt.show() 

