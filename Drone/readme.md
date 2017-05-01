For this tutorial we use MicMac, available here: http://micmac.ensg.eu

Tutorial assumes the images were collected with a drone and contain 
camera information in exif tags comprehenisible for this software.

## Step1:
Using a set of drone collected images, begin by calculating tie points.
Tie points are matching regions on different photos. 
These allow for determening position of the cameras in the next step

Run

mm3d Tapioca All ".*JPG" 1000

The matching will be done on all images at a scale 1000 (size of image 1000 px, for full resolution use -1). 



