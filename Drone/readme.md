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



------- Scratch workspace below ----

    mm3d CenterBascule ".*JPG" Ori-Orientation Ori-Orientation All-RTL
    
    

## Step3: Sparse point clouds:
Now we can calculate sparce clouds for every orientation

    mm3d C3DC Forest
because Ground is not implemented yet


## Step4: Orthomosaic, "Tawny"

Must first run

      mm3d CenterBascule "R.*.JPG" All-Rel Nav-adjusted-RTL All-RTL
      mm3d ChgSysCo  "R.*JPG" All-RTL SysCoRTL.xml@SysCoBL72_EPSG31370.xml All-BL72
      mm3d Malt Ortho "R.*JPG" All-BL72 DirMEC=MEC DefCor=0 AffineLast=1 Regul=0.005 HrOr=0 LrOr=0 ZoomF=1
      
      mm3d Malt Ortho ".*JPG" All-RTL DirMEC=MEC DefCor=0 AffineLast=1 Regul=0.005 HrOr=0 LrOr=0 ZoomF=1
      mm3d 
      mm3d Malt Ortho ".*JPG"

To generate DSM,

Afterwards must run 

      mm3d Tawny Ortho-MEC



