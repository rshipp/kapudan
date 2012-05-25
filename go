#!/bin/bash
rm -rf build
mkdir build
cp -R data help po src ui about.py setup.py build/
cd build
./setup.py build
python build/kaptan.py
cd ..
rm -rf build
