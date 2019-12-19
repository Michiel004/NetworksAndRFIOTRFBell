#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/lukas/Documents/NetRF/Project/rfproject/GNUradio_receiver/gr-module1/python
export PATH=/home/lukas/Documents/NetRF/Project/rfproject/GNUradio_receiver/gr-module1/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/lukas/Documents/NetRF/Project/rfproject/GNUradio_receiver/gr-module1/build/swig:$PYTHONPATH
/usr/bin/python2 /home/lukas/Documents/NetRF/Project/rfproject/GNUradio_receiver/gr-module1/python/qa_comparator_py_f.py 
