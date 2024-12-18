#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 18 2024
MLBZ - Mathias Labz
@author: Mathias Boyer
"""
# coding=utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

num_slices = 12 #slice radians of graph to simulate clock positions

def graph_by_tag(df, tag):
    df = df[df['tag'] == tag]
    scores = df['score'] + 0.5  # offset scores to fit graph better by +.5
    slice_indices = df['radian']  # 'radian' represents slice indices (0 to 15)

    # Convert slice indices to angles in radians
    radians = slice_indices * (2 * np.pi / num_slices)

    # Create the radial plot
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

    # Define the angles for the slices
    theta = np.linspace(0, 2 * np.pi, num_slices + 1)

    # Plot the slices
    for i in range(num_slices):
        ax.plot([theta[i], theta[i]], [0, 11], color='blue')

    # Plot the data points from the CSV
    ax.scatter(radians, scores, color='red', s=50, label='CSV Data Points')

    # Set 0 degrees at the top and direction clockwise
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)

    # Add customizations
    ax.set_ylim(11, 0)  # Correct y-limits to simulate target score layout
    ax.set_yticks(range(0, 12))  # Tick marks for the radial values
    ax.set_title(f"Radial Plot with Estimated Shot Data Points from {tag}", va='bottom')

    # Show the plot
    plt.show()

def main():
    print("Usage: this should be used as an imported module unless testing. Exiting...")
    sys.exit(0)


if __name__ == "__main__":
    if main():
        sys.exit(0)
    else:
        sys.exit(1)




