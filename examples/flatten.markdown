---
layout: page
---

# Flatten

When a cell is "flattened", all child cells are resolved and the shapes
are propagated into the parent cell. 
See [`flatten` documentation](https://www.klayout.de/doc-qt5/code/class_Cell.html#method71) for details 
about this feature.

{: .box-note }
**Note**: this operation is potentially expensive. Depending on the
hierarchical organization, this may create a large number of shapes 
even from few cells.

Code:

```python
{% include_relative flatten/flatten.py %}
```

Input `nuts_and_bolts.gds`:

![Input](nuts_and_bolts.png)

[Download GDS](nuts_and_bolts.gds)

Result (looks the same, but actually is flat):

![Result](flatten.png)

[Download GDS](flatten.gds)

