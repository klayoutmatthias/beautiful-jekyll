---
layout: page
---

# Save Layout Options Example

This example demonstrates how to use `write` with options.

We read the output from the previous "Cheese" example and
write it to a new file.
In this case we will change the database unit and limit the
number of polygon vertexes to 4. This generates a pretty
blocky cheese:

Code:

```python
{% include_relative save_layout_options/save_layout_options.py %}
```

Input `cheese.gds`:

![Input](cheese.png)

[Download GDS](cheese.gds)

Result:

![Result](save_layout_options.png)

[Download GDS](save_layout_options.gds)

