# -*- coding: utf-8 -*-
"""
dicom2nifti

@author: abrys
"""

from .settings import disable_validate_sliceincrement, \
    disable_validate_orientation, \
    disable_validate_orthogonal, \
    disable_validate_slicecount, \
    enable_validate_orientation, \
    enable_validate_orthogonal, \
    enable_validate_slicecount, \
    enable_validate_sliceincrement
from .convert_dicom import dicom_series_to_nifti
from .convert_dir import convert_directory