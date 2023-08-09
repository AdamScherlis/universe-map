# universe-map
A log-log plot of everything in the universe

Every log-log plot of mass and radius (or energy and time, etc.) that I could find, and several I made myself, combined into one giant plot.

It spans about 60 orders of magnitude vertically and 120 horizontally. The three sides of the triangle are determined by the cosmic horizon, Schwarzschild radius, and Heisenberg uncertainty principle.

The plot itself is in **envelope.pdf**. It's the output of a somewhat convoluted CSV-Python-Mathematica-TeX pipeline.

Metadata (e.g. axes and units for each image) is contained in a few CSVs. 
A Python script does the math to put images in the right place, adds a few extra annotations, and writes out a TeX file. 
TeX does the actual rendering into a PDF. The Mathematica notebooks are for a couple of plots that I wanted and couldn't find.
