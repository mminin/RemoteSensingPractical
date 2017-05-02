For this tutorial we use MicMac, available here: http://micmac.ensg.eu

Tutorial assumes the images were collected with a drone and contain 
camera information in exif tags comprehenisible for this software.

## Step 1: Find matching points (tie points), "Tapioca"
Using a set of drone collected images, begin by calculating tie points.
Tie points are matching regions on different photos. 
These allow for determening position of the cameras in the next step

Run

    mm3d Tapioca All ".*JPG" 1000

The matching will be done on all images at a scale 1000 (size of image 1000 px, for full resolution use -1). 

## Step 2: Compute camera orientations, "Tapas"
Next we compute positions and directions of cameras relative to each other.
These orientations are in arbitrary, purely relative coordinate frame.
The only required paramenters are the Camera Calibration mode (distorsion model) and input images.
For Classic Lens use RadialBasic.

Run

    mm3d Tapas RadialBasic ".*JPG" Out=Orientation


## Step 3: Compute depth map for each image, "PIMs"
  
    mm3d PIMs MicMac ".*JPG" Ori-Orientation
    
## Step 4: Combine multiple depth maps into a single point cloud:

    mm3d PIMs2Ply MicMac

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



