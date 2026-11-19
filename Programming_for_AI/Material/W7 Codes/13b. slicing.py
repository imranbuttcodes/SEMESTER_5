#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 03:08:25 2026

@author: awais
"""

from numpy import dtype
import numpy as np


# --- Diagnostic Filter (Masking) ---
def find_anomalies(data, threshold):
    # Boolean Masking
    # mask = data > threshold
    # print(mask)
    return data[np.array([0,1,0,1,0], dtype=bool)]

heart_rates = np.array([72, 110, 65, 140, 80])
tachycardia = find_anomalies(heart_rates, 100)
print(f"Anomalous Heart Rates: {tachycardia}") # [110 140]

