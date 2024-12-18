#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 18 2024
MLBZ - Mathias Labz
@author: Mathias Boyer
"""
# coding=utf-8

import pandas as pd
import sys
import graphShots as gshot

def main():
    df = pd.read_csv('shot_log.csv')  # Ensure the file exists in the working directory
    tag = input('Enter filter tag: ')
    gshot.graph_by_tag(df, tag)

if __name__ == "__main__":
    if main():
        sys.exit(0)
    else:
        sys.exit(1)