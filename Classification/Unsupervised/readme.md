# Use GRASS toolbox. 

## Step 1: Cluster spectral signatures
Choose i.cluster tool.

Set initial number of classes to 5.

Save output signature file as signature.sig

## Step 2: Classify raster by spectral signatures
Run i.maxlik

use the signature file created in Step 1. 

## Step 3: Edit style
Set symbology of the layer to "pseudocolor".
Add manual classes. Change colour of classes, change label of classes.

