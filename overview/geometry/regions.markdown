---
layout: page
---

# Regions

For original class documentation see [Region class reference](https://www.klayout.org/doc-qt5/code/class_Region.html).

Regions are basically collections of polygons. A simple application 
is to create a region object and insert polygons. Region objects support 
many geometrical operations such as sizing (enlargement, biasing), boolean 
operations (AND, NOT, XOR), merging (removing overlaps).

However, Region objects are much more powerful. They can be fed from a 
hierarchical layer. This enables operations on layouts. 
Regions support a hierarchical mode ("deep mode") that allows preserving
the hierarchy of the original layout as far as possible.

With this ability, Region objects are also the basis of KLayout's DRC (design rule check)
feature. All features available in DRC decks are mapped to Region methods.

I will discuss only the basic features here. The [original documentation](https://www.klayout.org/doc-qt5/programming/geometry_api.html#k_22) 
is the entry point for further explanations.

## Region Creation

Region objects can be filled with integer-unit polygons. When inserting
other graphic objects they are converted to polygons (note that we are
using the default database unit of 1 nm here):

```python
{% include_relative samples/region1.py %}
```

Gives:

![Result](../samples/region1.png)

Note that there are not micrometer-unit regions currently. A trick to convert
micrometer-units into integer-unit objects is a apply a complex transformation:

```python
{% include_relative samples/region2.py %}
```

Gives:

![Result](../samples/region2.png)

## Region Operations

"Sizing" (also called "biasing") is an operation that shifts the 
polygon edges by a certain distance. Positive values will shift 
outside, negative values inside. Before the edges are shifted, 
the polygons are merged:

```python
{% include_relative samples/region3.py %}
```

Gives (the original polygons are white):

![Result](../samples/region3.png)

Sizing can be anisotropic - in this case, the horizontal shift
can be different from the vertical shift:

```python
{% include_relative samples/region4.py %}
```

Gives (the original polygons are white):

![Result](../samples/region4.png)

The boolean "NOT" operation subtracts the second
region from the first. This operation is implemented
by the `-` operator:

```python
{% include_relative samples/region5.py %}
```

Gives (the result is white):

![Result](../samples/region5.png)

The boolean "AND" computes the intersection of two regions.
This operation is implemented by the `&` operator:

```python
{% include_relative samples/region6.py %}
```

Gives (the result is white):

![Result](../samples/region6.png)

The boolean "XOR" computes the intersection of two regions.
This operation is implemented by the `^` operator:

```python
{% include_relative samples/region7.py %}
```

Gives (the result is white):

![Result](../samples/region7.png)

The `+` operator joins two collections. `merge` (in place) or `merged` merges the polygons of
a region, i.e. it computes the envelopes or boolean "OR" of the polygons:

```python
{% include_relative samples/region8.py %}
```

Gives (the result is white):

![Result](../samples/region8.png)

## Regions from Layout Layers

You can pull polygons from a layout layer hierarchically and perform operations on it
([Download `my_layout.gds`](../samples/my_layout.gds)):

```python
{% include_relative samples/region9.py %}
```

Gives (the result are the white features):

![Result](../samples/region9.png)

[Download the GDS file](../samples/region9.gds)

