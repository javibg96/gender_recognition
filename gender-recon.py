# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 16:53:51 2020

@author: JBLASCO
"""
import logging
import os

try:
    os.system('python src/detect_gender_webcam.py')
except:
    logging.exception("Error traceback")
