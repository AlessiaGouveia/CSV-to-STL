#!/usr/bin/env python3

import argparse
import pandas as pd
import numpy as np
from scipy.spatial import Delaunay


# ----------------------------
# Load x, y, z coordinates
# ----------------------------
def load_xyz_from_csv(file_path):
    try:
        df = pd.read_csv(file_path)

        # Ensure at least 3 columns
        if df.shape[1] < 3:
            raise ValueError("CSV file must have at least 3 columns (x, y, z).")

        # Drop rows with missing values
        missing_value_rows = df[df.isnull().any(axis=1)].index
        if len(missing_value_rows) > 0:
            print(f"Warning: Found {len(missing_value_rows)} rows with missing values. Removing these rows.")
            df.dropna(inplace=True)

        x = df.iloc[:, 0].values  # First column (x)
        y = df.iloc[:, 1].values  # Second column (y)
        z = df.iloc[:, 2].values  # Third column (z)
        return x, y, z

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at path {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error reading CSV file: {e}")


# ----------------------------
# Calculate normal vector
# ----------------------------
def calculate_normal(triangle):
    v1 = triangle[1] - triangle[0]
    v2 = triangle[2] - triangle[0]
    normal = np.cross(v1, v2)
    norm = np.linalg.norm(normal)
    if norm == 0:
        return np.array([0, 0, 0])  # Degenerate triangle
    return normal / norm


# ----------------------------
# Write STL helpers
# ----------------------------
def write_stl_triangle(file, v1, v2, v3, normal):
    file.write(f"  facet normal {normal[0]} {normal[1]} {normal[2]}\n")
    file.write("    outer loop\n")
    file.write(f"      vertex {v1[0]} {v1[1]} {v1[2]}\n")
    file.write(f"      vertex {v2[0]} {v2[1]} {v2[2]}\n")
    file.write(f"      vertex {v3[0]} {v3[1]} {v3[2]}\n")
    file.write("    endloop\n")
    file.write("  endfacet\n")


def write_stl_file(file_path, points, triangulation):
    with open(file_path, "w") as f:
        f.write("solid STL_from_CSV\n")
        for simplex in triangulation.simplices:
            triangle = points[simplex]
            normal = calculate_normal(triangle)
            write_stl_triangle(f, triangle[0], triangle[1], triangle[2], normal)
        f.write("endsolid STL_from_CSV\n")


# ----------------------------
# Main function
# ----------------------------
def main(input_csv, output_stl):
    # Load points
    x, y, z = load_xyz_from_csv(input_csv)
    points = np.column_stack((x, y, z))

    # Triangulate (based on x,y)
    points_2d = np.column_stack((x, y))
    try:
        tri = Delaunay(points_2d)
    except Exception as e:
        raise RuntimeError(f"Error during Delaunay triangulation: {e}")

    # Write STL
    try:
        write_stl_file(output_stl, points, tri)
        print(f"✅ STL file saved to {output_stl}")
    except Exception as e:
        raise RuntimeError(f"Error writing STL file: {e}")


# ----------------------------
# Entry point
# ----------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert CSV (x,y,z) points into an STL surface mesh.")
    parser.add_argument("input_csv", help="Path to input CSV file (with x,y,z columns).")
    parser.add_argument("output_stl", help="Path to output STL file.")
    args = parser.parse_args()

    main(args.input_csv, args.output_stl)
