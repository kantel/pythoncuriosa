#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 20:34:00 2020

@author: admin
"""

import matplotlib.pyplot as plt

import cartopy.crs as ccrs
from cartopy.io.img_tiles import OSM

imagery = OSM()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection=imagery.crs)
ax.set_extent([13.0, 13.8, 52.0, 52.4], ccrs.PlateCarree())

ax.add_image(imagery, 14)

plt.show()