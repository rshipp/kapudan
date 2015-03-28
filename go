#!/bin/bash
rm -rf build
mkdir build
cp -R data help po src ui setup.py build/
cd build
./setup.py build
python3 build/kapudan.py
cd ..
rm -rf build
