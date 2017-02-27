Tools of use:  SNAP / QGis / Orfeo toolbox / Gdal

* Load raster, single band
* RGB color combination
* Spectra / NDVI / optical thematic maps / radiometric indices
* Extracting / visualising Spectra 
* (Map projection)
* PCA
* Filtering, including spatial, convolution etc.

## Getting data
_Data for this tutorial is in the attached folder_

Attached we provide files obtained from Sentinel 2, 
which have been mosaiced and clipped to the area of 
interest and converted to multiband GeoTIFF format.

Additionally, the band values have been divided by 4095, to convert from
the range of brightness levels (0-4095) to brightness as a ratio (0-1).

The source data you can find on https://scihub.copernicus.eu/

The multispectral data is in the file **allBands01a.tif**
You can download it from Dropbox: https://www.dropbox.com/s/aizkdm22crh9ydx/allBands01a.tif.zip?dl=0
This file contains all bands available from Sentinel 2, with band 8A placed in band 9, 9 in 10, etc.

## Load raster (single band, RGB combination)
Copy this file into your work directory and uncompress ("extract here"). 
Open QGIS and start a new project, save to the work directory.
Drag and drop this file onto the screen. 
It should automatically display
<img src="illustrations/load.png" width="200"/>

### RGB
Right click on the layer in the layers panel and choose properties. 
Confirm that render type is Multiband color. Change blue to band 02, green to 03 and red to 04.
Set color enhancement ot stretch to Min/Max. Change min/max values to 0 for Min, and 1 for Max.
<img src="illustrations/ScreenshotRGB.png" alt="Drawing" style="width: 200px;"/>
Click Apply and OK. You should now see true colour RGB.
<img src="illustrations/TrueColourRGB01.png" alt="Drawing" style="width: 200px;"/>

### Singe band
Right click on the Layer in the Layers Panel, click duplicate, 
move the copied layer to the top, and rename to "singleband", click enable checkmark.
Right click on the Singleband layer in the layers panel and choose properties. 
Change render type to singleband pseudocolor, select band 11, interpolation linear color RdPu.
Load min/max values, use accuracy "Actual". Click classify.
In blending mode select "Overlay". Press Apply then OK.
You should now see high altitude clouds highlighted in purple. 
<img src="illustrations/cirrus-Clouds.png" alt="Drawing" style="width: 200px;"/>




