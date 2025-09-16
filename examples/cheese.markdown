---
layout: page
---

# Cheese

This example demonstrates how to read and manipulate a layout
with boolean operations between two layers.

The input layout contains the outline on layer 1/0, the cheese holes
on layer 2/0.

Code:

```python
{% include_relative cheese/cheese.py %}
```

Input `input.gds` (layer 1 is red, layer 2 is blue):

![Input](input.png)

[Download GDS](input.gds)

Result (boolean result in red, holes shown in white):

![Result](cheese.png)

[Download GDS](cheese.gds)

