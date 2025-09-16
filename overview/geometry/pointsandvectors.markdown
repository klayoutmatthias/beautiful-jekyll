---
layout: page
---

# Points and Vectors

For original class documentation see [Point class reference](https://www.klayout.org/doc-qt5/code/class_Point.html),
[DPoint class reference](https://www.klayout.org/doc-qt5/code/class_DPoint.html),
[Vector class reference](https://www.klayout.org/doc-qt5/code/class_Vector.html) and
[DVector class reference](https://www.klayout.org/doc-qt5/code/class_DVector.html).

Unlike other systems, KLayout differentiates between vectors and points. This is some important 
concept that helps avoiding some mistakes. But it is important to understand the idea. It is a basic
concept of KLayout's geometry API.

Points are fixed coordinates in a 2 dimensions coordinate space. Vectors connect points. Technically,
a vector is made from the difference of the coordinates of two points.

Vectors and points are simple pairs of a x and a y value.
The respective classes are `Vector` or `DVector` for vectors and `Point` and `DPoint` for points.

Points and vectors arithmetically behave this way:

* `point - point` gives a vector
* `point + vector` or `Point - Vector` gives a point
* `vector + vector` or `vector - vector` gives a vector

For convenience, points can be added although formally this is not within the framework.

The main difference between points and vectors is their behavior in transformations:
on applying a transformation, the displacement is not applied to vectors while it is applied to points. 

{: .box-note }
**Rationale**: if t is a transformation and
p1 and p2 are points, then `t * (p2 - p1)` should be `t * p2 - t * p1`. In this case, the displacement
cancels out and only the rotation / mirror is applied. In KLayout's framework `p2 - p1` renders a vector 
and to a vector, only the rotation/mirror part is applied. The result of `t * (p2 - p1)` and `t * p2 - t * p1` is identical.

In KLayout's API, points play a role mainly for defining the vertexes of polygons or the segments
of a path. Vectors are used for example as displacements for transformations and as arguments in 
various operations.

The default point is the origin:
```python
import klayout.db as db

p0 = db.DPoint()

print("p0 is " + str(p0))
```

Output:
```
p0 is 0,0
```

Adding a vector to a point shifts it:
```python
import klayout.db as db

p1 = db.DPoint(1.0, 2.0)
v = db.DVector(1, 1)

print("p1+" + str(v) + " is " + str(p1 + v))
```

Output:
```
p1+1,1 is 2,3
```

The difference of two points gives a vector:
```python
import klayout.db as db

p1 = db.DPoint(1.0, 2.0)
print("p1 is " + str(p1))
p2 = db.DPoint(-2.0, 5.0)
print("p2 is " + str(p2))

v12 = p2 - p1
print("v12=p2-p1 is " + str(v12) + " (class " + type(v).__name__ + ")")
```

Output:
```
p1 is 1,2
p2 is -2,5
v12=p2-p1 is -3,3 (class DVector)
```

The displacement is not applied to vectors, so distribution
of the product renders the same result:
```python
import klayout.db as db

p1 = db.DPoint(1.0, 2.0)
print("p1 is " + str(p1))
p2 = db.DPoint(-2.0, 5.0)
print("p2 is " + str(p2))

t = db.DTrans(db.DTrans.R90, 1.0, 2.0) 
print("t is " + str(t))
print("t*(p2-p1) is " + str(t * (p2 - p1)))
print("t*p2-t*p1 is " + str(t * p2 - t * p1))
```

Output:
```
p1 is 1,2
p2 is -2,5
t is r90 1,2
t*(p2-p1) is -3,-3
t*p2-t*p1 is -3,-3
```


