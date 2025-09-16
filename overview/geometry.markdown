---
layout: page
---

# Geometry Classes

The KLayout API provides some basic geometrical objects. These objects are used
independently from the layout database. 

Graphic objects such as boxes or polygons can be inserted into the database
on layers. On retrieval, the primary object is `Shape` which is 
a representative for an opaque object actually stored in the database. `Shape`  
represents different types of graphic objects. `Shape` also adds additional attributes
such as user properties. `Shape` can also return back the graphic object
if necessary. See [Shapes](../shapes) for details.

KLayout's documentation refers to the graphic objects as the "working objects"
because usually those are the objects which are easier to deal with.

* [Points and Vectors](pointsandvectors)
* [Boxes](boxes)
* [Polygons](polygons)
* [Paths](paths)
* [Texts](texts)
* [Regions](regions)

