#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:28:20 2018

@author: hagan
"""

from astropy.io import fits
import os

def str2bool(v):
  return v.lower() in ("true")

def Write_TA_FITS(cv3Dir, preFileDir, outDir, frametime, subray):
    f1= fits.open(preFileDir)
    pipelineFile= fits.open(cv3Dir)

    hdu = f1[0]
    fitsdat=hdu.data
    primaryHeaderPipeline=pipelineFile[0].header

    primaryHeaderPipeline['FILENAME']=os.path.basename(outDir)
    primaryHeaderPipeline['TFRAME']=frametime
    primaryHeaderPipeline['NINT']= 1
    primaryHeaderPipeline['SUBARRAY']=subray
    (primaryHeaderPipeline['NAXIS3'],primaryHeaderPipeline['NAXIS2'],primaryHeaderPipeline['NAXIS1'])=fitsdat.shape
    primaryHeaderPipeline['NGROUP']=primaryHeaderPipeline['NAXIS3']
    primaryHeaderPipeline['INTTIME']=primaryHeaderPipeline['TFRAME']*primaryHeaderPipeline['NFRAME']*primaryHeaderPipeline['NGROUP']
    primaryHeaderPipeline['EXPTIME']=primaryHeaderPipeline['INTTIME']*primaryHeaderPipeline['NINT']
    primaryHeaderPipeline['NCOLS']=primaryHeaderPipeline['NAXIS1']
    primaryHeaderPipeline['NROWS']=primaryHeaderPipeline['NAXIS2']

    SCIext=fits.PrimaryHDU(data=fitsdat,header=primaryHeaderPipeline,uint='uint16')
    SCIext.scale('int16',bscale=1,bzero=32768)
    SCIext.header.insert(-3,('BSCALE', 1))
    SCIext.writeto(outDir)

import sys
if __name__ == '__main__':
    cv3Dir = sys.argv[1]
    preFileDir = sys.argv[2]
    outDir = sys.argv[3]
    frametime = float(sys.argv[4])
    subray=str2bool(sys.argv[5])
    Write_TA_FITS(cv3Dir, preFileDir, outDir, frametime, subray)



