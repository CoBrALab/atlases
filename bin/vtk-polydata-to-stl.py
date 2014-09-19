#!/usr/bin/env python
# from https://gist.githubusercontent.com/thewtex/8263132/raw/079eca1603ed750d1707516ef51eed33e4934b44/vtk-unstructuredgrid-to-stl.py
"""Convert PolyData in .vtk files to STL files."""

import sys
import vtk

if len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print('Usage: vtk-polydata-to-stl.py <input.vtk> <output.stl>')
    sys.exit(1)

reader = vtk.vtkPolyDataReader()
reader.SetFileName(sys.argv[1])

surface_filter = vtk.vtkDataSetSurfaceFilter()
surface_filter.SetInputConnection(reader.GetOutputPort())

triangle_filter = vtk.vtkTriangleFilter()
triangle_filter.SetInputConnection(surface_filter.GetOutputPort())

writer = vtk.vtkSTLWriter()
writer.SetFileName(sys.argv[2])
writer.SetInputConnection(triangle_filter.GetOutputPort())
writer.SetFileTypeToBinary()
writer.Write()
