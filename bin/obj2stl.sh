#!/bin/bash
# converts a bic .obj file to an stl
# 
# Expects that vtk-polydata-to-stl.py is in the path

inputfile=$1
outputfile=$2

if [ -z "$inputfile" -o -z "$outputfile" ]; then
  echo "Usage: $0 <input.obj> <output.stl>"
  exit 1;
fi

tmpfile=$(mktemp)

bicobj2vtk $inputfile > $tmpfile
vtk-polydata-to-stl.py $tmpfile $outputfile
