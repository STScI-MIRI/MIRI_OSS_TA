- This script generates 3 products for a given configuration, where a configuration consists of 3 inputs: readout type, subarray, and number of integrations. The three products include a FITS file (for OSS to test), a .png file (for reference), and a README.txt file (provides more information on the FITS file)
- Size and location of ROIs are taken from the the MIRI SIAF excel file: MIRI_SIAF.xml, which currently is taken from here: https://github.com/spacetelescope/pysiaf/tree/master/pysiaf/prd_data/JWST/PRDOPSSOC-H-015/SIAFXML
- All {X,Y} locations are given using the SIAF pixel location scheme - note this coordinate system is the same as the one used in DS9.
- Delivered_FITS_File generated from CV3 FITS file MIRM107-E-6021041029_1_493_SE_2016-01-21T04h22m18.fits, hereafter referred to as Origin_FITS_File, located in /ifs/jwst/wit/miri/pipelinetests/testdata/
- Origin_FITS_File has FAST readout pattern, and has 5 integrations, each with 20 groups
- For each image in the final FITS product, every 5th column of the image contains reference pixels (this is the main task of this script, properly inserting the reference pixels into every fifth column of the image)
- Any point source that is injected to a region of interest (ROI) is a copy and pasted 3x3 cut out of a CV3 point source in Origin_FITS_File, whose center pixel is located at {X,Y} = {701, 451} in Origin_FITS_File. 

An example input configuration:
{readout, subarray, int_number} = {"FASTGRPAVG16","MASK1065",4}. An example of the resulting README.txt for this config would look like this:

README for MIR4QPM_FASTGRPAVG16_MASKnnnn_4.fits, hereafter referred to as Delivered_FITS_File.
- Size and location of ROIs are taken from the the MIRI SIAF excel file: MIRI_SIAF.xml
- All {X,Y} locations are given using the SIAF pixel location scheme - note this coordinate system is the same as the one used in DS9.
- Delivered_FITS_File generated from CV3 FITS file MIRM107-E-6021041029_1_493_SE_2016-01-21T04h22m18.fits, hereafter referred to as Origin_FITS_File,  located in /ifs/jwst/wit/miri/pipelinetests/testdata/
- Delivered_FITS_File is for use in testing READOUT = FASTGRPAVG16
- Origin_FITS_File has FAST readout pattern
- Delivered_FITS_File has NGROUP = 64
- After averaging, Delivered_FITS_File would have NGROUP = 4 for READOUT = FASTGRPAVG16
- For each image in Delivered_FITS_File, every 5th column of the image contains reference pixels
- 8 ROI locations for this subarray, with 1 point source located in each ROI.
- Each point source in Delivered_FITS_File is a copy and pasted 3x3 cut out of a CV3 point source in Origin_FITS_File, whose center pixel is located at {X,Y} = {701, 451} in Origin_FITS_File. 
- For each image in Delivered_FITS_File, the center pixel for the injected point source(s) are located at:
{X,Y}= {77, 174}
{X,Y}= {221, 171}
{X,Y}= {72, 61}
{X,Y}= {213, 56}
{X,Y}= {131, 129}
{X,Y}= {170, 124}
{X,Y}= {127, 99}
{X,Y}= {167, 97}
- Without the reference columns, the point sources' center pixels are located at the following locations on the FULL array (these numbers are obtained by multiplying the x-values in the numbers above by 0.8):
{X,Y}= {62, 174}
{X,Y}= {177, 171}
{X,Y}= {58, 61}
{X,Y}= {171, 56}
{X,Y}= {105, 129}
{X,Y}= {136, 124}
{X,Y}= {102, 99}
{X,Y}= {134, 97}
- Within the ROI, the point sources' center pixels are located at the following locations:
MIRIM_TA1065_UL -> {25, 25}    MIRIM_TA1140_UL -> {24, 28}    MIRIM_TA1550_UL -> {24, 25}
MIRIM_TA1065_UR -> {25, 25}    MIRIM_TA1140_UR -> {27, 28}    MIRIM_TA1550_UR -> {27, 33}
MIRIM_TA1065_LL -> {25, 25}    MIRIM_TA1140_LL -> {25, 29}    MIRIM_TA1550_LL -> {22, 25}
MIRIM_TA1065_LR -> {25, 25}    MIRIM_TA1140_LR -> {25, 28}    MIRIM_TA1550_LR -> {25, 27}
MIRIM_TA1065_CUL -> {9, 7}    MIRIM_TA1140_CUL -> {9, 11}    MIRIM_TA1550_CUL -> {7, 11}
MIRIM_TA1065_CUR -> {9, 5}    MIRIM_TA1140_CUR -> {7, 7}    MIRIM_TA1550_CUR -> {11, 10}
MIRIM_TA1065_CLL -> {9, 8}    MIRIM_TA1140_CLL -> {9, 11}    MIRIM_TA1550_CLL -> {6, 9}
MIRIM_TA1065_CLR -> {9, 8}    MIRIM_TA1140_CLR -> {9, 11}    MIRIM_TA1550_CLR -> {9, 10}
- Origin_FITS_File contains 5 integrations with 20 groups each. 
- Delivered_FITS_File made with the last NGROUP groups of the last integration of the Origin_FITS_File. If NGROUP > the number of frames contained in the last integration of Origin_FITS_File, then extra data was made (taken from Origin_FITS_File) to extend the integration.  
- Only the following FITS keywords are accounted for in the Delivered_FITS_File: 'FILENAME', 'READOUT', 'NGROUP', 'TFRAME', 'NINT', 'SUBARRAY', 'NAXIS', 'NAXIS1', 'NAXIS2', 'NAXIS3', 'INTTIME', 'EXPTIME', 'NCOLS', 'NROWS', 'BSCALE', 'BZERO', 'BITPIX'. All other keywords were directly inherited from Origin_FITS_File and have not been verified to be correct.


Delivery made by J. Brendan Hagan for OSS target acquisition testing.
Delivery Date: Mon 2 Nov 2020
