#given an Ames Stereo Pipeline "*-PC.tif" file subset this code produces a delimited text fitted to ingest into SAGA
import rasterio
import numpy as np
name="input-PC.tif"
src=rasterio.open(name)
zdat=src.read_band(1)
xdat=src.read_band(2)
ydat=src.read_band(3)
datsize=xdat.size
q=list(zip(xdat.reshape(datsize),ydat.reshape(datsize),zdat.reshape(datsize)))

import csv
with open('out.ply', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for qq in q:
        spamwriter.writerow([str(qqq) for qqq in qq])

