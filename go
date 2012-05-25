#!/bin/bash
rm -rf build
mkdir build
cp -R data help po src ui about.py AUTHORS COPYING README setup.py TODO build/
cd build
sed -i 's/pykde4uic/pykdeuic4/g' setup.py
sed -i 's/import pardus.*//g' src/kaptan/screens/scrSmolt.py
sed -i 's/import smolt//g' src/kaptan/screens/scrSmolt.py
sed -i 's/import pardus.*//g; s/from pardus.*//g' src/kaptan/screens/scrKeyboard.py

./setup.py build
python build/kaptan.py
