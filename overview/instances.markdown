---
layout: page
---

# Instances

For the reference documentation see [CellInstArray Class Reference](https://www.klayout.org/doc-qt5/code/class_CellInstArray.html) and
[DCellInstArray Class Reference](https://www.klayout.org/doc-qt5/code/class_DCellInstArray.html).

For the Instance object reference see [Instance Class Reference](https://www.klayout.org/doc-qt5/code/class_Instance.html).

Instances (or "references") correspond to AREF and SREF objects in GDS. Instances "place" another cell inside a cell.
When looking at a layout, an instance appears as a copy of the instantiated cell. This copy can be shifted, rotated or mirrored.
Instances are used to generate bigger cells from smaller components. A typical application is to place
instances of logic gates to form functional blocks.

Instance objects describe such cell placements with the following attributes:

* A reference to the cell placed. In KLayout this is a cell index.
* The transformation to apply. This is a simple or complex transformation object (see [Transformations](transformations)).
* Optionally a regular array specification. An instance with an array specification corresponds to an AREF element in GDS.

KLayout's API uses two (actually three) classes to represent instances:

* `CellInstArray` and `DCellInstArray` are the input objects. These are the objects inserted into a cell to create an instance.
* `Instance` is the object by which you retrieve instances from the database. `Instance` objects are directly 
  connected to instances in the database and manipulating them changes the instance inside the database.

{: .box-note }
**Note**: although the classes are called CellInstArray, the do not necessarily represent arrays. 
Single instances are also represented by CellInstArray objects.

Here is an example for creating instances:

```python
{% include_relative samples/instances.py %}
```

![Result](../samples/instances.png)

[Download GDS file](../samples/instances.gds)

Instances can use complex transformations which enables any-angle rotations
and cell scaling. A mentioned earlier such instances may be deprecated however in 
some applications.

Array instances are made from two step vectors (`a` and `b`) and two array dimensions (`na` and `nb`).
The array expands to `na*nb` instances with additional displacements

```
d = i * a + j * b

with

i = 0 .. na-1
j = 0 .. nb-1
```

{: .box-warning }
**Warning:** other systems reading your layout files may require that a and b are orthogonal vectors and are oriented along the x 
and y axis respectively.

KLayout does not impose such a restriction and supports skew arrays as well.

