---
layout: page
---

# Eggs (Region Queries)

The example demonstrates how to retrieve shapes from 
a certain region. The first case uses a fixed box, the 
second a non-rectangular region taken from layer 100/0.
Input comes from layer 101/0.

The query descends into the hierarchy rendering a 
flat copy of the shapes while iterating.

The core feature is the `RecursiveShapeIterator`. 
See here for the [original documentation](https://www.klayout.de/doc-qt5/code/class_RecursiveShapeIterator.html).

Code:

```python
{% include_relative eggs/eggs.py %}
```

Input (layer 1 is red, layer 100 white, layer 101 is gray):

![Result](input.png)

[Download GDS](input.gds)

Result (the box query is red, the complex region query is blue):

![Result](eggs.png)

[Download GDS](eggs.gds)

