---
layout: page
---

# Clip

This example clips a rectangular region taken from layer 100/0 and saves this clip
as a new layout. The clip is generated in-place which means that no new 
cells need to be generated if cells are entirely inside the clip box.

This example demonstrates:

* How to use `clip` from the Layout object (see [original documentation of `clip`](https://www.klayout.de/doc-qt5/code/class_Layout.html#method33)).
* Saving cells to layout files using `write` of the Cell object.

Note that the clip is done hierarchically - i.e. preserving the original hierarchy where
possible. With this particular example (a layer from a SRAM) this is much more efficient than
a flat clip using a boolean operation.

{: .box-note }
**Note**: This sample can easily be extended to provide a clip at multiple boxes at once.
Use [`multi_clip`](https://www.klayout.de/doc-qt5/code/class_Layout.html#method98)
instead of `clip` and collect the clip boxes from layer 100/0 instead of taking the
bounding box.

Code:

```python
{% include_relative clip/clip.py %}
```

Input `input.gds` (the white box is on layer 100/0):

![Input](input.png)

[Download GDS](input.gds)

Result (a cutout from the original layout):

![Result](clip.png)

[Download GDS](clip.gds)

