---
layout: page
---

# Hierarchical Gratings

This implementation of the gratings example uses
cells and instances. First, the gratings are generated using
array instances. Second, every grating is placed inside
a separate cell and the stacking is achieved by placing
these cells.

{: .box-note }
**Note**: With this approach you can create huge gratings very
efficiently.

Code:

```python
{% include_relative gratings_hierarchical/gratings_hierarchical.py %}
```

Result:

![Result](gratings_hierarchical.png)

The top-level-only hierarchy view shows the cells:

![Result Top Level](gratings_hierarchical_cells.png)

[Download GDS](gratings_hierarchical.gds)

