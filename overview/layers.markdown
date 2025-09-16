---
layout: page
---

# Layers

Unlike plain GDS, the layout object specifies layers globally, not individually for each shape.
The layer specification (number, datatype and name for formats which support that) is 
managed inside the Layout object. 

Before you can create shapes on a layer, you have to register your layer in the Layout object.
You will receive a handle which you then use to address the layer when you create shapes.

```python
import klayout.db as db

ly = db.Layout()

# creates a GDS layer with layer 1, datatype 0
layer1 = ly.layer(1, 0)

# layer 2/0 with additional name:
layer2 = ly.layer(2, 0, "Poly")

# pure named layer for CIF, DXF etc.
# NOTE: this layer will not be written to GDS or OASIS
layer_m1 = ly.layer("Metal1")

# anonymous layer for intermediate results
layer_anonymous = ly.layer()
```

To get the information for a layer handle use `get_info`:

```python
import klayout.db as db

ly = db.Layout()

layer1 = ly.layer(1, 0)

print("Layer handle " + str(layer1) + " refers to " + str(ly.get_info(layer1)))
```


