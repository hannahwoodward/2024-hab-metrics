import numpy as np
import regionmask
import xesmf


def mask_to_land(data):
    land_mask = regionmask.defined_regions.natural_earth_v5_0_0.land_110.mask(
        data
    )
    return data\
        .where(land_mask.notnull())\
        .compute()


def mask_to_ocean(data):
    land_mask = regionmask.defined_regions.natural_earth_v5_0_0.land_110.mask(
        data
    )
    return data\
        .where(land_mask.isnull())\
        .compute()


def regrid_data(
    data,
    grid,
    filename=None,
    method='bilinear',
    regrid_kwargs={}
):
    regrid = xesmf.Regridder(
        data,
        grid,
        method=method,
        **regrid_kwargs
    )

    data_regridded = regrid(data)

    filename != None and data_regridded.to_netcdf(filename)

    return data_regridded


def weighted(data, dim='lat'):
    weights = np.cos(np.deg2rad(data[dim]))
    weights.name = 'weights'

    return data.weighted(weights)