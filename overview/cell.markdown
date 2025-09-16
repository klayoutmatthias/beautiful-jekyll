---
layout: page
---

# Cells

For the reference documentation see [Cell Class Reference](https://www.klayout.org/doc-qt5/code/class_Cell.html).

Cells are STRUCTs in GDS terminology. Cells for the basic building blocks of layouts. Cells can be "placed" in 
other cells by creating "instances". Instances are basically references to other cells. A cell which is placed inside 
another cell becomes a "child cell" of the other cell. The other cell will become the "parent" of the child cell.

Cell placement can involve transformations like movement (translation), rotation, mirroring and even magnification/shrinking.

{: .box-warning }
**Warning**: cell scaling is deprecated in many GDS applications.

A cell is created using `create_cell` from Layout:

```python
import klayout.db as db

ly = db.Layout()

top_cell = ly.create_cell("TOP")

# ... 
```

A cell has a unique name. If the given name is present already, KLayout will assign a new unique name.
You can obtain and change a cell's name using the "name" property.

{: .box-warning }
**Caution**: renaming a cell is a way to break the uniqueness requirement.

```python
import klayout.db as db

ly = db.Layout()

top_cell = ly.create_cell("TOP")

print("Cell name is: " + top_cell.name)
top_cell.name = "NEW_TOP"
print("Cell name now is: " + top_cell.name)
```

In the klayout package, a cell is currently addressed in two ways: by a Cell object reference 
and by a cell index. `create_cell` will return a Cell object. Some functions however, need the 
cell index. The cell index is an integer value addressing the cell. The integer value is a lean and
safe way of addressing the cell as it can be checked for validity and is not subject to lifetime
management issues. However, it's a legacy concept and cell references and indexes may be harmonized
in the future.

You can obtain the cell index from a Cell object using the `cell_index` method:

```python
import klayout.db as db

ly = db.Layout()

top_cell = ly.create_cell("TOP")

print("Cell index of top cell is: " + str(top_cell.cell_index()))
```

Vice versa, the "cell" method from Layout gives the Cell reference from a cell index:

```python
import klayout.db as db

ly = db.Layout()

top_cell_index = ly.create_cell("TOP").cell_index()

top_cell = ly.cell(top_cell_index)

# ...
```

{: .box-warning }
**Caution**: don't assume the cell index will take a certain value. The value of the cell index is an implementation detail and
may change in other KLayout versions.

## Finding and Iterating Cells 

Once you have read a layout file, you can find a cell by name using Layout's `cell` method. This method will
return `None` if the cell cannot be found:

```python
import klayout.db as db

ly = db.Layout()
ly.read("my_layout.gds")

cell_top = ly.cell("TOP")
if cell_top is None:
  print("Cell 'TOP' not found")
```

Cells in Layouts form hierarchy trees. Cells not having children are called "leaf cells", cells not having parents are called "top cells".
In most valid GDS files, there is a single top cell only and all other cells are placed inside the top cell - either directly
or indirectly.

If there is a single top cell, you can obtain the top cell as a `Cell` object using Layout's `top_cell` method:

```python
import klayout.db as db

ly = db.Layout()
ly.read("my_layout.gds")

top_cell = ly.top_cell()
print("Name of top cell is: " + top_cell.name)
```

The `top_cell` method will fail if there are multiple top cells. In this case, you can use `top_cells` to get a array with all 
top cells.

Here are some more features of the Layout class:
 * Iterate all cells with [`each_cell`](https://www.klayout.org/doc-qt5/code/class_Layout.html#method54)
 * Iterate all cells in bottom-up order (children before parents) with [`each_cell_bottom_up`](https://www.klayout.org/doc-qt5/code/class_Layout.html#method55). This iterator delivers *cell indexes*.
 * Iterate all cells in top-down order (parents before children) with [`each_cell_top_down`](https://www.klayout.org/doc-qt5/code/class_Layout.html#method55). This iterator delivers *cell indexes*.

## The Cell Bounding Box

A cell has a global and layer specific bounding box. The layer specific bounding box is the box enclosing all shapes on this layer plus
all shapes from child cells on this layer. The global bounding box is the envelope of all layer specific bounding boxes.

A bounding box maybe empty indicating there are not shapes on that specific layer or the cell is empty of geometrical
objects in case of the global bounding box. This also includes emptyness of child cells.

{: .box-note }
**Note**: for the bounding box computation, labels are considered point-like objects. The text strings do not contribute to 
the bounding box.

The global bounding box is obtained with the `bbox` method. The layer specific bounding box is
obtained with `bbox_per_layer`. Both methods are available as micrometer-unit variants with the "d" prefix:

Global bounding box example ([Download `my_layout.gds`](../samples/my_layout.gds)):
```python
{% include_relative samples/cell_global_bbox.py %}
```

Which renders the white box:

![Output](../samples/cell_global_bbox.png)

Per-layer bounding box example ([Download `my_layout.gds`](../samples/my_layout.gds)):
```python
{% include_relative samples/cell_layer_bbox.py %}
```

Which renders the white box (layer 1/0 is the red one):

![Output](../samples/cell_layer_bbox.png)

