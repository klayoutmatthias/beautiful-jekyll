---
layout: page
---

# Shapes

For the original documentation see [Shapes Class Reference](https://www.klayout.org/doc-qt5/code/class_Shapes.html).

Cells carry the geometrical shapes. Geometrical shapes are:

  * Boxes (Rectangles)
  * Polygons
  * Paths (Lines with a certain width tracing a sequence of points)
  * Labels (Text strings placed at a specific location)

A cell object carries one list of geometrical objects per logical layer. This list 
as represented by the `Shapes` class. To get the Shapes object for a specific layer handle,
use the Cell's `shapes` method. Once obtained, the Shapes object can be manipulated to 
add or remove shapes.

```python
import klayout.db as db

ly = db.Layout()

top_cell = ly.create_cell("TOP")
layer1 = ly.layer(1, 0)

shapes1 = top_cell.shapes(layer1)

shapes1.insert(db.DBox(0, 0, 1.0, 1.0))

ly.write("sample.gds")
```

## The Shape Class

The original documentation of the Shape class is found here: [Shape class reference](https://www.klayout.org/doc-qt5/code/class_Shape.html)

When you retrieve shapes from a `Shapes` container, you will receive `Shape` objects. These objects are generic 
shapes and can represent boxes, polygons, paths or texts. You can ask the Shape for the kind of shape it is and convert 
to the plain geometrical object:

```python
import klayout.db as db

ly = db.Layout()
ly.read("my_layout.gds")

top_cell = ly.top_cell()
layer1 = ly.layer(1, 0)

for shape in top_cell.shapes(layer1).each():

  if shape.is_polygon():
    print("Polygon: " + str(shape.dpolygon))
  elif shape.is_path():
    print("Path: " + str(shape.dpath))
  elif shape.is_text():
    print("Text: " + str(shape.dtext))
  elif shape.is_box():
    print("Box: " + str(shape.dbox))
```

Assigning Shape properties will change the shape in the database. The following example will
substitute all polygons by their bounding boxes:

```python
import klayout.db as db

# NOTE: manipulations are safe only in editable mode
ly = db.Layout(True)
ly.read("my_layout.gds")

top_cell = ly.top_cell()
layer1 = ly.layer(1, 0)

for shape in top_cell.shapes(layer1).each():
  if shape.is_polygon():
    shape.dbox = shape.dpolygon.bbox
```

{: .box-note }
**Note**: the layout is opened in 'editable' mode. Without this, manipulating
shapes while iterating them is not safe.

## More things you can do with Shapes

* Iterate over all shapes with [`each`](https://www.klayout.org/doc-qt5/code/class_Shapes.html#method23). You can specify a selector that allows iterating over specific types of shapes only.
* Efficient region lookups with [`each_touching`](https://www.klayout.org/doc-qt5/code/class_Shapes.html#method29) and [`each_overlapping`](https://www.klayout.org/doc-qt5/code/class_Shapes.html#method25).
* Modify single shapes or the whole collecting with an affine transformation with [`transform`](https://www.klayout.org/doc-qt5/code/class_Shapes.html#method136).

