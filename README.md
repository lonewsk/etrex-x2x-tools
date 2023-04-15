# etrex-x2x-tools

etrex-x2x-tools is a set of tools I created to make better use of my Garmin eTrex 32x.

## List of tools

* Prepare a GPX file: long tracks made with a lot of points will make Garmin freeze and eventually crash. This tool split the track into multiples files (each 8000 points max), then simplifies them into a 600 points file, using GPSBabel's algorithm. This ensure small files, which Garmin will handle at an acceptable speed, and the algorithm make a good job of keeping the track readable despite removing a lot of points.


