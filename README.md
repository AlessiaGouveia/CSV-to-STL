# CSV to STL Converter

## Why?
Working with 3D point data often starts in simple CSV files containing sets of (x, y, z) coordinates. While this tabular format is easy to generate and analyse, it’s not suitable for visualising shapes or models. This project was created to bridge that gap — converting raw coordinate data into a 3D mesh that can be opened in any STL-compatible viewer or CAD software. This makes it much easier to see and work with 3D structures instead of interpreting rows of numbers.

## What?
This tool takes a three-column CSV file (representing x, y, z coordinates) and generates a triangulated 3D surface mesh in STL format. The STL file can then be used for:

- Visual inspection of 3D datasets
- Import into CAD or 3D modeling software
- 3D printing experiments

## How?
### 1. Clone this repository

```bash
git clone https://github.com/AlessiaGouveia/CSV-to-STL.git
cd CSV-to-STL
```

### 2. Install dependencies
Make sure you have Python 3.x installed, then install the required libraries:

```bash
pip install -r requirements.txt
```
### 3. Run the script
Provide your own CSV file (with three columns: x,y,z) and specify an output STL filename:

```bash
python csv_to_stl.py input.csv output.stl
```

### 4. View the result 
Open the generated output.stl in any 3D viewer or CAD software.

## Example

An example CSV file (example.csv) is included in this repository so you can test quickly.

#### Run the script:

```bash
python csv_to_stl.py example.csv example.stl
```


