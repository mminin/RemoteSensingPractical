For this tutorial we use MicMac, available here: http://micmac.ensg.eu

Tutorial assumes the images were collected with a drone and contain 
camera information in exif tags comprehenisible for this software.

Sample data can be found here: https://www.dropbox.com/s/6pl4dj98emzqyxn/data.zip?dl=0

# Stage 1: Generating Point Cloud

## Step 1.1: Find matching points (tie points), "Tapioca"
Using a set of drone collected images, begin by calculating tie points.
Tie points are matching regions on different photos. 
These allow for determening position of the cameras in the next step

Run

    mm3d Tapioca All ".*JPG" 1000

The matching will be done on all images at a scale 1000 (size of image 1000 px, for full resolution use -1). 

## Step 1.2: Compute camera orientations, "Tapas"
Next we compute positions and directions of cameras relative to each other.
These orientations are in arbitrary, purely relative coordinate frame.
The only required paramenters are the Camera Calibration mode (distorsion model) and input images.
For Classic Lens use RadialBasic.

Run

    mm3d Tapas RadialBasic ".*JPG" Out=Orientation

## Step 1.3: Compute depth map for each image, "PIMs"
Now we can compute how far the image was from the camera when it was taken using the
camera orinetations from the previous step

    mm3d PIMs MicMac ".*JPG" Ori-Orientation
    
## Step 1.4: Combine all depth maps into a single point cloud,"PIMs2Ply":

    mm3d PIMs2Ply MicMac

_MicMac tools are still under development and can only take us this far._

_Further processing will be done in QGIS and meshlab_

# Stage 2: Producing DEM 
(after http://www.spatialguru.com/gdal-rasters-from-irregular-point-or-ascii-data/)

## Step 2.1: Turn mesh into CSV:
This step is best done with meshlab.
Open point cloud in meshlab.
Click on Filters > Point Set > Surface Reconstruction: Poisson
Click Apply
Click File > Save Mesh As
and save as grid.xyz
Convert to CSV using:

    sed 's/ /,/g' grid.xyz > grid.csv

## Step 2.2: Make virtual raster to trick gdal into accepting it:
Create virtual header grid.vrt containing:
    
    <OGRVRTDataSource>
    <OGRVRTLayer name="grid">
    <SrcDataSource>grid.csv</SrcDataSource>
    <GeometryType>wkbPoint</GeometryType>
    <LayerSRS>WGS84</LayerSRS>
    <GeometryField separator=" " encoding="PointFromColumns" x="field_1" y="field_2" z="field_3"/>
    </OGRVRTLayer>
    </OGRVRTDataSource>

## Step 2.3: Convert to tiff using gdal:

    gdal_grid -zfield field_3 -l grid grid.vrt newgrid.tif

# Stage 3: Converting point cloud to orthoimagery
This can be accomplised by conveting 3D point cloud to a 2D point feature class.

## Step 3.1: Convert PLY from Binary to ASCII format
Open Point Cloud produced in pervious step in meshlab.
Save it as .ply while unclicking checkbox "binary", while preserving vertex colour.
Open the file with command "less", you will see that the first 15 lines are text, the following are numbers. 

## Step 3.2: Remove the headers using command "tail"
Run

    tail -n +15 mesh03.ply >mesh04.ply

## Step 3.3: Convert to CSV:
_Note: If your file was written out with commas instead of dots as a decimal symbol (check it with "less"), you might want to run_

    sed 's/,/\./g' mesh04.ply > mesh04a.ply
_(Whether you'll need to do it or not will probably depend on the settings of your locale - American vs Europe)

Run

    sed 's/ /,/g' mesh04.ply > mesh04.csv

    
## Step 3.4: Import to QGIS:

Click on "Add Delimited Text Layer" button, and find your file.
Select first column (field_1) as X and second (field_2) as Y.
Save it in SpatiaLite format (this indexes the table, otherwise interpolation will not be possible).

## Step 3.5: Interpolate:
Use Raster > Analysis > Grid (Interpolation)...

Choosing Z Field 4, 5, then 6, setting Algorithm to "Inverse distance to a power" and "Max points" to 10.
This step may take a few moments. This will produce orthorectified rasters for different channels. 
Combine them to get RGB image.
