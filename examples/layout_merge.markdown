---
layout: page
---

# Merge Layouts

This example demonstrates how to copy cell trees from one layout to another.
It takes three layouts - each with a single top cell - and arranges their 
top cells vertically from bottom to top.

It employs the `copy_tree` method of the `Cell` class. See the [Original documentation](https://www.klayout.de/doc-qt5/code/class_Cell.html#method36) 
for details.

{: .box-note }
**Note**: this example uses `_destroy` to free resources once they are no longer
required.

Code:

```python
{% include_relative layout_merge/layout_merge.py %}
```

Inputs (`A.gds`, `B.gds` and `C.gds`):

![Input](A.png)

[Download GDS](A.gds)

![Input](B.png)

[Download GDS](B.gds)

![Input](C.png)

[Download GDS](C.gds)

Result:

![Result](layout_merge.png)

Result (top level hierarchy only):

![Result](layout_merge_cells.png)

[Download GDS](layout_merge.gds)

