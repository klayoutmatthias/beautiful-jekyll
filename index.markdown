---
layout: page
---

![Nuts and Bolts](assets/img/nuts_and_bolts.jpg)

# The klayout Python Module

The *klayout* Python module is a side branch of the [KLayout](https://www.klayout.org) system. 
KLayout is a 2d viewer and editor for mask layouts used in chip manufacturing. It reads and writes
GDS, OASIS, CIF, DXF and other formats including Gerber PCB files. It is capable of handling 
large files on the multi-GB scale with literally billions of polygons. 

KLayout embeds a Ruby and Python interpreter and development environment. Scripting in KLayout
acts as a high-level access layer to the analysis and processing functionality. This layer provides
most of the relevant classes KLayout implements in C++. 

The *klayout* Python package available on PyPI offers a subset of this API packaged as a lean, dependency-free binary 
distribution. This subset includes:

  * Geometry database (```klayout.db``` submodule)
  * Utility classes (```klayout.tl``` submodule)
  * Report database classes (```klayout.rdb``` submodule)

{: .box-note}
**Note:** we'll focus on `klayout.db` here as this is by far the most important module.

Compared to KLayout's full functionality, the Python package lacks all user-interface related classes.
This avoids a dependency to the heavy Qt library and related license issues. Still the Python package 
allows generating, manipulating and analyzing layout files. If you need KLayout's full Python features
as an external Python package, consider using the Python package which comes with KLayout itself - e.g.
distributed with the Linux RPM or DEB packages. This package adds additional submodules like `klayout.lay`
for the user interface components.

  * [How to read the reference documentation](howtoreadtheref)
  * [API Overview](overview)
  * [Examples](examples)

## Sample

This simple example generates a small layout containing a single cell and some rectangles:

![Result](samples/basic.png)

[Download GDS file](samples/basic.gds)

Code:

```python
{% include_relative samples/basic.py %}
```

