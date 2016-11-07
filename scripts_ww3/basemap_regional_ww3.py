	

from mpl_toolkits.basemap import Basemap, cm
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio

hs_reg = sio.loadmat('hs_reg.mat')
hs_regional_2 = hs_reg['hs_regional_2']

m = Basemap(projection='mill', llcrnrlat=-66.0, llcrnrlon=-68.0, urcrnrlat=-5.0, urcrnrlon=-3.1, resolution='l')
																				
m.drawcoastlines()
m.drawstates()
m.imshow(hs_regional_2, cm.GMT_haxby)


plt.title('Altura significativa de ondas - Grade regional')
plt.colorbar()
plt.show() 