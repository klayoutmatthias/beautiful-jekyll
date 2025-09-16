---
layout: page
---

# Polygons

For original class documentation see [Polygon class reference](https://www.klayout.org/doc-qt5/code/class_Polygon.html) and
[DPolygon class reference](https://www.klayout.org/doc-qt5/code/class_DPolygon.html).

{: .box-note }
**Note**: you may be looking for something beyond the polygon. When you 
need boolean operations, the polygon is not the right place to look for.
Boolean operations and many higher-level functions are implemented in the 
[`Region`](../regions) class which is a _collection_ of polygons.

Polygons are closed contours of points (vertexes) and can contain a number of holes.
The outer contour is called the "hull" of the polygon. Holes itself are also 
closed contours of points.

GDS polygons cannot have holes, so basically these polygons cannot be written to GDS.
Instead they are converted to simple polygons first (see below). In GDS also the number
of points is usually limited, while in the API it is not. When writing a huge polygon to GDS,
the polygon may be split into smaller parts if the vertex limit is exceeded.
So eventually it is safe to use polygon objects - the GDS writer will take care of
properly handling the special cases.

{: .box-warning }
**Warning**: avoid generating polygons which are self-intersecting - e.g. the 
"8" shape. Also avoid overlapping holes or holes which are not entirely inside the hull. 
Such polygons may be rendered differently on other systems. You can 
normalize polygons by "merging" them. The [Region class](../region) implements
a merging algorithm for single or multiple polygons.

Having said that, here are the basic features of the `Polygon` and `DPolygon` classes:

* The default constructor creates an empty polygon. `polygon.empty()` tells us if the polygon is empty.
* A polygon without holes can be created from an array of `Point` or `DPoint` objects.
* Holes can be inserted into polygons with `polygon.insert_hole(..)`. The argument is an array of points.
* Boxes can be converted to polygons using the constructor with the box argument.
* Ellipses or circle (approximations) can be generated with the `ellipse` class method.
* The edges (lines connecting two points) can be iterated with `each_edge`.
* The points of the hull can be iterated with `each_point_hull`.
* The points of a hole can be iterated with `each_point_hole`.

The hull and hole contours of the polygons are oriented in a specific way: 
The hull is oriented clockwise while the holes are oriented counterclockwise.
The points passed to the constructor of `insert_hole` do no need to be compatible
with this orientation - the polygon will take care of correcting the orientation
if necessary.

When a polygon is constructed, collinear points (points on an edge) or returning edges (zero degree spikes)
are removed from hull or hole contours. This can be avoided by passing `True` to the `raw` flag which is 
available for some methods taking point arrays.

The empty polygon a s special case which does not have any points. Non-empty polygons
need to have at least three points.

Creating a polygon from a box:

```python
{% include_relative samples/polygon1.py %}
```

Gives:

![Result](../samples/polygon1.png)

Creating an ellipse (approximated by 32 points):

```python
{% include_relative samples/polygon2.py %}
```

Gives:

![Result](../samples/polygon2.png)

Creating a polygon from a list of points:

```python
{% include_relative samples/polygon3.py %}
```

Gives:

![Result](../samples/polygon3.png)

Creating a polygon with a hole:

```python
{% include_relative samples/polygon4.py %}
```

Note that the cut line has been inserted when the polygon was written to a GDS file.
It is not there initially:

![Result](../samples/polygon4.png)


# Simple Polygons

For original class documentation see [SimplePolygon class reference](https://www.klayout.org/doc-qt5/code/class_SimplePolygon.html) and
[DSimplePolygon class reference](https://www.klayout.org/doc-qt5/code/class_DSimplePolygon.html).

In short, simple polygons are polygons without holes.

Simple polygons are the database objects generated when reading GDS files. Simple polygons can be converted easily 
to generic polygons and back. When a polygon with holes is converted to a simple polygon, the holes
are connected to the hull through cut lines:

```python
import klayout.db as db

simple_polygon = db.DSimplePolygon(...)

# conversion of simple polygon to a polygon
polygon = db.DPolygon(simple_polygon)

# conversion of polygon to a simple polygon
simple_polygon = polygon.to_simple_polygon()
```

In most Python applications, simple polygons will hardly provide any performance or memory benefits, so
simple polygons are not further discussed here.

