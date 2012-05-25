#!/bin/bash
rm -rf build
mkdir build
cp -R data help po src ui about.py AUTHORS COPYING README setup.py TODO build/
cd build

./setup.py build
python build/kaptan.py
