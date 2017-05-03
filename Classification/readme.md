This tutorial will discuss Supervised and Unsupervised classification.
For this work We will be using the Semi-Automatic Classification Plugin (https://fromgistors.blogspot.com/p/semi-automatic-classification-plugin.html) in QGIS.

Install dependencies:
sudo apt-get install qgis python-matplotlib python-scipy

Then start QGIS and install Plugin


# Part I: Supervised Classification
Consists of:
* Training Stage
* Classification Stage
* Output Stage

### Step 0: Get image
On virtual machine the file we are using (Chad) is located in the directory

    /home/u64b/Desktop/data/landsat/LC08_L1TP_158044_20170309_20170309_01_RT/

## Create new training input file




### Preprocessing

Go to "Preprocessing", Landsat, choose directory containing Landsat bands, add them

Switch to band set, to band set definition add bands 2,3,4,5,6,7 and choose quick wavelength settings to Landsat 8OLI, close dialog. In RGB= type 3-2-1, which sets it to visible, or 4-3-2, which sets it to IR pseudocolour. Temporary virtual raster band_set.vrt will be created


### Training
Now let's classify water, farmland, sand and rock. We will create 4 training classes one for each.

Use ROI, Activate ROI pointer

Begin by selecting representative region, then click somewhere on the ocean near the shore, but your ROI will probably be very small, so increase Distance which by default is 0.02, to something greater, just try different values until satisfactory result. For me a good value seems to be around 2000. Once happy with the result go to classification dock and add "save temporary ROI to training input".

Now do the same for vegetation (which is very visible in IR). You may have to merge several ROI to get satisfactory result.

Do the same for sand dune fields in the southeast.

Repeat for rocks in the middle of the coverage. Pick separately dark rock and light rock, assigning each to a same MC ID (Macroclasses).

### Classification
Keep default settings for Classification algorithm, don't bother with Macroclasses, these are for cases when you want to select more than one type of rock or vegetation, etc.

### Output 
Go to Classification output and click run. Choose a file name to save.
