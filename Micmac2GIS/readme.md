# This project explains how to convert Micmac point cloud (.ply) to TIFF DEM and Orthoimage using SAGA.

1. Export point cloud (PC) from meshlab to .ply with colours, without normals, without binary, remove header and replace commas with dots.

2. To convert PC to grids, import .ply into SAGA format, and do spline B interplolation by running these commands:
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
_This will produce grids from splines casted over PC's._

_You'll need to convert these to geotiffs to use in GIS_

3. First convert DEM grid to tiff (for Z coordinate)

```
saga_cmd io_gdal 2 -GRIDS splineZ.sgrd -FILE DEM.tif
```

4. Now create an RGB composite from RGB splines:
We can convert each of the splines to a separate tiff and recombine them using gdal
```
saga_cmd io_gdal 2 -GRIDS splineR.sgrd -FILE R.tif
saga_cmd io_gdal 2 -GRIDS splineG.sgrd -FILE G.tif
saga_cmd io_gdal 2 -GRIDS splineB.sgrd -FILE B.tif
gdal_merge.py -separate -o ortho.tif R.tif G.tif B.tif

```
_NOTE: Alternative approach is to use saga, but it doesn't quite work from the command line:_
```
saga_cmd grid_visualisation 3 -R_GRID splineR.sgrd -R_METHOD 0 -G_GRID splineG.sgrd -G_METHOD 0 -B_GRID splineB.sgrd -B_METHOD 0 -RGB ortho
saga_cmd io_gdal 2 -GRIDS ortho.sgrd -FILE ortho.tif
```
