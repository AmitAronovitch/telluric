import os
import numpy as np
from affine import Affine
from rasterio.crs import CRS
from telluric import GeoRaster2


def test_recursion(tmp_path):
    raster = GeoRaster2(image=np.ones([10, 10], dtype=np.uint8), crs=CRS(), affine=Affine.identity())
    filename = os.fspath(tmp_path / 'raster1.tif')
    raster.save(filename)
    # Load a raster from file
    raster = GeoRaster2.open(filename)
    raster2 = raster.copy_with()
    print('---->', raster2.crs, raster2.affine)
