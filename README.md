# shp2rnet

Convert an ESRI shapefile (.shp, sbx, .dbf) into an "rnet" file.

Requires [networkx](https://networkx.github.io)
Requires [gdal](https://pypi.python.org/pypi/GDAL)

To get both:
`pip install networkx gdal`

The rnet (road-network) file format is space separated columns, looks like this:
```
edge_id from_id to_id from_lng from_lat to_lng to_lat
```

The `edge_id` is automatically generated.

Why? Because sometimes graphs come in shapefiles, that is difficult to
plot w gnuplot, but with the rnet file, it is very easy. Example:
```
plot 'output.rnet' using 4:5:($6-$4):($7-$5) w vectors nohead lt rgb 'black' lw 1
```

Example:
```
shp2rnet edges.shp -o "output.rnet"
```
