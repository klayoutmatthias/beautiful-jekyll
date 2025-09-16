
# The Layout Object

For the original documentation refer to [The Database API](https://www.klayout.org/doc-qt5/programming/database_api.html) and 
[Layout Class Reference](https://www.klayout.org/doc-qt5/code/class_Layout.html).

The `Layout` object is the most important and central object in KLayout's database API.
A Layout object basically represents a GDS, OASIS or other format file.

To create a Layout object from a file use "read":

```python
import klayout.db as db

ly = db.Layout()
ly.read("my_layout.gds")
```

In layout-generating applications, a Layout object will usually be created from scratch and then written
to a file with "write":

```python
import klayout.db as db

ly = db.Layout()

# ... add layers, cells, instances, shapes

ly.write("generated_layout.gds")
```

## Database Unit

The database unit is a very basic concept in GDS and many other formats. 

GDS stores coordinates as integer multiples of some basic unit - the database unit. This
is the fundamental resolution of a GDS file. Unless you use scaled instances (which I do 
not recommend). The database unit should not be too small as GDS is employing 32 bit
coordinates - this limits the total physical dimension you can map with a given database
unit. The default database unit of 1 nm is usually a good compromise.

The database unit is given in micrometers and read or written with the Layout's "dbu" property:

```python
import klayout.db as db

ly = db.Layout()
print("Current DBU is: " + str(ly.dbu))
ly.dbu = 0.00025
print("New DBU is: " + str(ly.dbu))
```

## Micrometer and Integer Units

The klayout module offers two representations for many objects: in micrometer coordinates and in integer-unit
coordinates. The latter coordinates need to be multiplied by the layout's database unit to obtain
micrometer units.

In most cases, there is a duality. Here are some examples:

| Object/Method         | Micrometer units      | Integer units        |
|-----------------------|-----------------------|----------------------|
|Rectangle              | `DBox` class          | `Box` class          |
|Polygon                | `DPolygon` class      | `Polygon` class      |
|Path                   | `DPath` class         | `Path` class         |
|Label                  | `DText` class         | `Text` class         |
|Regions (polygon sets) | *not available*       | `Region` class       |
|Cell placement         | `DCellInstArray` class| `CellInstArray` class|
|Cell bounding box      | `Cell.dbbox` method   | `Cell.bbox` method   |
|Simple transformation  | `DTrans` class        | `Trans` class        |
|Complex transformation | `DCplxTrans` class    | `ICplxTrans` class   |

## Editable and Non-Editable mode

By default, layouts are created in non-editable mode. This does not mean that
a layout cannot be manipulated, but non-editable mode has some consequences:

* When reading OASIS files, shapes are stored as shape arrays. Hence memory requirements are typically less
* Adding objects to a layout is safe. **Manipulating existing layouts is not.** Manipulations may fail and 
  in some cases, the application may crash.

Editable-mode layouts are less efficient in terms of memory footprint and are more safe in general when
it comes to manipulations of existing objects.

To create a layout in editable mode use:

```python
import klayout.db as db

ly_editable = db.Layout(True)
ly_editable.read("my_layout.gds")

# ...
```

