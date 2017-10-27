#This project explains how to convert Micmac point cloud (.ply) to TIFF DEM and Orthoimage using SAGA.

1. Export point cloud (PC) from meshlab to .ply with colours, without normals, without binary, remove header and replace commas with dots.

2. To convert PC to grids, import .ply into SAGA format, and do spline B interplolation by runnig these commands:
```
saga_cmd io_shapes 16 -POINTS OutputZ -FILE input.ply -ZFIELD 3 -FIELDSEP 1
saga_cmd io_shapes 16 -POINTS OutputR -FILE input.ply -ZFIELD 4 -FIELDSEP 1
saga_cmd io_shapes 16 -POINTS OutputG -FILE input.ply -ZFIELD 5 -FIELDSEP 1
saga_cmd io_shapes 16 -POINTS OutputB -FILE input.ply -ZFIELD 6 -FIELDSEP 1

saga_cmd grid_spline 4 -SHAPES OutputZ.spc -TARGET_OUT_GRID splineZ -FIELD 3
saga_cmd grid_spline 4 -SHAPES OutputR.spc -TARGET_OUT_GRID splineR -FIELD 4
saga_cmd grid_spline 4 -SHAPES OutputG.spc -TARGET_OUT_GRID splineG -FIELD 5
saga_cmd grid_spline 4 -SHAPES OutputB.spc -TARGET_OUT_GRID splineB -FIELD 6
```
_This will produce grids from splines casted over PC's_
_You'll need to convert these to geotiffs to use in GIS_

3. 
