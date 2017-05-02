For this tutorial we use MicMac, available here: http://micmac.ensg.eu

Tutorial assumes the images were collected with a drone and contain 
camera information in exif tags comprehenisible for this software.

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
    
## Step 1.4: Combine all depth maps into a single point cloud:

    mm3d PIMs2Ply MicMac

_MicMac tools are still under development and can only take us this far.

_Further processing will be done in QGIS

# Stage 2: Converting point cloud to orthoimagery and DEM
This can be accomplised by conveting 3D point cloud to a 2D point feature class.

## Step 2.1: Convert PLY from Binary to ASCII format
Open Point Cloud produced in pervious step in meshlab.
Save it as .ply while unclicking checkbox "binary", while preserving vertex colour.
Open the file with command "less", you will see that the first 15 lines are text, the following are numbers. 

## Step 2.2: Remove the headers using command "tail"
Run

    tail -n +15 mesh03.ply >mesh04.ply

## Step 2.3: Convert to CSV:
Run

    sed 's/ /,/g' mesh04.ply > mesh04.csv
    
## Step 2.4: Import to QGIS:

Click on "Add Delimited Text Layer" button, and find your file.
Select first column (field_1) as X and second (field_2) as Y.





------------- Ok up to here
-----------------------------------

## Step 5: Define a normal to horizontal (for making orthogonal projection)

mm3d RepLocBascule ".*JPG" Ori-Orientation HORVy R-F1.xml PostPlan=_MasqFacade1

## Step 6: Create DSM, PIMs2MNT (doesn't work):





Convert point cloud to XYZ, use sed to convert to CSV:

    sed 's/ /,/g' mq.xyz > grid.csv

http://www.spatialguru.com/gdal-rasters-from-irregular-point-or-ascii-data/


mm3d Pims2MNT MicMac DoOrtho=1 Repere=R-F1.xml Pat=".*JPG"

gdal_grid -zfield field_3 -l grid grid.vrt newgrid.tif



## ? Step7: Create orthomosaic, Tawny??



