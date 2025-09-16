---
layout: page
---

# Transformations

Affine transformations play an important role in KLayout's geometry API:

* To specify cell placements
* For transforming geometries from child cells into parent cells
* As operators for geometry manipulations
* For unit translations

Affine transformations describe geometrical modifications. A graphical object
can be rotated, mirrored or shifted using affine transformations. The transformation
object is basically the recipe to apply. Examples for transformations are:

* A rotation by 90 degree counterclockwise around the origin 0,0
* A shift by 10 µm to the right
* Mirroring at the x axis

Transformations are objects you can perform some computations with. This is very handy: For example, to 
transform a polygon with two different transformations consecutively, you don't need to execute the 
polygon transformation twice. Instead you multiply the transformations and only apply the resulting transformation
once to the polygon. This is usually much more efficient.

Transformation objects support three basic operations:

* Product: the product `a*b` of two transformations renders the transformation equivalent to applying b and then a.
* Inverse: the inverse of a transformation is the operation which will return an object to the original state after applying the forward transformation.
* Apply: in KLayout's API, a transformation is applied to an object using the star operator: `t*a` will apply transformation t to object a and render the transformed object.

Here is an example:

```python
{% include_relative samples/transformation.py %}
```

The rotated and shifted polygon is shown in blue while the original
is shown in red. The rotated-only polygon is shown in gray:

![Result](../samples/transformation.png)

[Download GDS file](../samples/transformation.gds)

## Simple Transformations

For the class references see [Trans class reference](https://www.klayout.org/doc-qt5/code/class_Trans.html)
and [DTrans class reference](https://www.klayout.org/doc-qt5/code/class_DTrans.html).

In many cases, simple transformations are used. Simple transformations feature (in this order):

* An optional mirroring at the x axis
* A rotation by a multiple of 90 degrees counter-clockwise
* A shift (translation)

There are basically eight possible rotation/mirror combinations plus the shift. KLayout uses a specific
notation for these eight variants, namely "r0", "r90", "r180", "r270", "m0", "m45", "m90" and "m135".
For an overview over the simple transformations see [Transformations in KLayout](https://www.klayout.org/doc-qt5/about/transformations.html).

Simple transformations come in two flavors: integer-unit transformations (`Trans` class) and micrometer-unit transformations (`DTrans` class).
The difference is that integer-unit transformations take shift vectors as integer x and y values while the 
micrometer-unit transformation takes floating-point values. Integer-unit transformations are used to transform
integer-unit objects (like `Polygon`) while micrometer-unit transformations are used to transform micrometer-unit
objects (like `DPolygon`).

```python
import klayout.db as db

# No argument gives the unit transformation
print("The unit transformation is " + str(db.DTrans()))

# A rotation by 90 degree counterclockwise followed by a 
# y displacement of 100 µm upwards.
t1 = db.DTrans(db.DTrans.R90, 0.0, 100.0)
print("t1 is: " + str(t1))

# "*" applies the transformation to a geometry object
box = db.DBox(0, 0, 10.0, 20.0)  # 10 µm wide, 20 µm tall
print("t1*" + str(box) + " is: " + str(t1 * box))

# Take the inverse of t1
t1inv = t1.inverted()
print("inverse(t1) is: " + str(t1inv))

# Product of two transformations a*b is the equivalent of
# appying b and then a
t2 = db.DTrans(100.0, 0.0)   # displacement to the right
print("t2 is: " + str(t2))
print("t2*t1 is: " + str(t2 * t1))

# The product is not commutable in general
print("t1*t2 is: " + str(t1 * t2))

# The product of a transformation and the inverse is 
# the unit transformation
print("t1inv*t1 is: " + str(t1inv * t1))
```

Produces:

```
The unit transformation is r0 0,0
t1 is: r90 0,100
t1*(0,0;10,20) is: (-20,100;0,110)
inverse(t1) is: r270 -100,0
t2 is: r0 100,0
t2*t1 is: r90 100,100
t1*t2 is: r90 0,200
t1inv*t1 is: r0 0,0
```

## Complex Transformations

For the class references see [ICplxTrans class reference](https://www.klayout.org/doc-qt5/code/class_ICplxTrans.html),
[DCplxTrans class reference](https://www.klayout.org/doc-qt5/code/class_DCplxTrans.html),
[CplxTrans class reference](https://www.klayout.org/doc-qt5/code/class_CplxTrans.html) and
[VCplxTrans class reference](https://www.klayout.org/doc-qt5/code/class_VCplxTrans.html).

While simple transformations are sufficient for many applications, KLayout also supports complex
transformations. Beyond simple transformations they offer:

* Separate input and output type versions - these can convert between integer- and micrometer-unit types
* Scaling - the coordinates are multiplied with a factor
* Any-angle rotations - the rotation angle can be any value between 0 and 360 degree

Complex transformations are implemented by the following classes:

* `ICplxTrans` a complex transformation between integer-unit types
* `DCplxTrans` a complex transformation between micrometer-unit types
* `CplxTrans` a complex transformation with integer-unit input and micrometer-unit output
* `VCplxTrans` a complex transformation with micrometer-unit output and integer-unit input

The inverse of a `CplxTrans` is a `VCplxTrans` and vice versa. Products of complex transformations
are permitted only if the output type of the right-side transformation is the same than the input
type of the left-side transformation.

Complex transformations can be used for cell instances. 

{: .box-warning}
**Warning**: Any-angle rotations and scaling implies generation of
offgrid geometries. Scaling also compromises the validity of physical design rules in the placed cells. 
Therefore complex transformations are often deprecated in VLSI layouts.


## Matrix Transformations

For the class references see [Matrix2d class reference](https://www.klayout.org/doc-qt5/code/class_Matrix2d.html) and
[Matrix3d class reference](https://www.klayout.org/doc-qt5/code/class_Matrix3d.html).

For special applications, KLayout offers even more generic matrix transformations: `Matrix2d` 
features a 2x2 rotation/scale/shear matrix and `Matrix3d` the full 3x3 matrix.

 * `Matrix2d` adds shear transformations
 * `Matrix3d` additionally adds perspective transformations - this is the most generic affine transformation in 2d space

{: .box-note}
**Note**: Both transformations come in micrometer-unit flavor only and cannot be used for cell instances.

In text books you will often see generic affine transformations in 2 dimensional space represented by a 3x3 matrix
using the "augmented matrix" (see for example [Affine Transformations on WikiPedia](https://en.wikipedia.org/wiki/Affine_transformation)).

This is how KLayout's two matrix transformations map to this picture:

`Matrix2d`:

|       |x  |y  |z  |
|-------|---|---|---|
|**x**  |m11|m12|dx |
|**y**  |m21|m22|dy |
|**z**  |0  |0  |1  |

`Matrix3d`:

|       |x  |y  |z  |
|-------|---|---|---|
|**x**  |m11|m12|m13|
|**y**  |m21|m22|m23|
|**z**  |m31|m32|m33|

