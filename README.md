# CSV to STL Converter

## Why?
Working with 3D point data often starts in simple CSV files containing sets of (x, y, z) coordinates. While this tabular format is easy to generate and analyse, it’s not suitable for visualising shapes or models. This project was created to bridge that gap — converting raw coordinate data into a 3D mesh that can be opened in any STL-compatible viewer or CAD software. This makes it much easier to see and work with 3D structures instead of interpreting rows of numbers.

## What?
This tool takes a three-column CSV file (representing x, y, z coordinates) and generates a triangulated 3D surface mesh in STL format. The STL file can then be used for:

- Visual inspection of 3D datasets
- Import into CAD or 3D modeling software
- 3D printing experiments

# How does it work?
