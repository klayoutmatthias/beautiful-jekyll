---
layout: page
---

# Paths

For original class documentation see [Path class reference](https://www.klayout.org/doc-qt5/code/class_Path.html) and
[DPath class reference](https://www.klayout.org/doc-qt5/code/class_DPath.html).

{: .box-note }
**A note of caution**: you'll see a lot of warnings in this section. 
Path rendering lacks standardization in GDS and OASIS too.
Only simple paths are guaranteed to render the same geometry in all systems.
It's easy to create paths that look differently in different systems.
In case of doubt, consider converting your paths to polygons.

Paths are lines along a series of points with a given width. The path ends can be configured
to be flat, square or something between. The path ends can be round as well. 

{: .box-warning }
**Warning**: round-ended paths
are deprecated in many applications.

Paths are build from a sequence of points and take a width and optionally path end configuration
parameters. By default a flush-ended path is created:

```python
{% include_relative samples/path1.py %}
```

Gives

![Result](../samples/path1.png)

Paths can easily be configured in ways that introduce interpretation ambiguities.
Other systems may read such paths differently (see below for some examples).
If you need to be sure that paths
are read the same way by other systems, you can convert them to polygons:

```
{% include_relative samples/path_to_polygon.py %}
```

Gives

![Result](../samples/path_to_polygon.png)

The ends are configured using two additional parameters: the start and
end extension. The extension is added to the front and end of the path. 
To create a square-ended path, pass half the width to begin and end extensions:

```python
{% include_relative samples/path2.py %}
```

Gives

![Result](../samples/path2.png)

Arbitrary extensions can be specified. Even negative extensions are possible. 

{: .box-warning }
**Warning**:
the results of negative extensions may be undefined on other systems.

```python
{% include_relative samples/path3.py %}
```

Gives

![Result](../samples/path3.png)

Round ends can be specified by adding one additional boolean parameter: `True` gives
a round-ended path. Extensions can be combined with the round-mode flag, basically giving
elliptic ends. Specifying half the width for begin and end extensions gives circular ends.
Contrary to popular expectation, the corners of the path itself are not
rounded.

{: .box-warning }
**Warning**:
only round-ended paths with circular ends are supported in GDS.
In OASIS, round-ended paths are replaced by flat-ended ones and two circles at the
ends.

```python
{% include_relative samples/path4.py %}
```

Gives

![Result](../samples/path4.png)

A special case is a single-point path with round ends. Formally such a path allows
defining circles in GDS. It is translated into a single circle object in OASIS.

{: .box-warning }
**Warning**:
in GDS, such paths may not be read properly by other systems.

```python
{% include_relative samples/path5.py %}
```

Gives

![Result](../samples/path5.png)

Acute corners will be clipped. 

{: .box-warning }
**Warning**:
other system reading such a path may apply a different clipping.

```python
{% include_relative samples/path6.py %}
```

Gives

![Result](../samples/path6.png)

Short start and end segments are handled by KLayout in a specific way. 

{: .box-warning }
**Warning**:
other systems my render such paths differently.

```python
{% include_relative samples/path7.py %}
```

Gives

![Result](../samples/path7.png)

Paths can be configured to have a width that is an odd multiple of the
database unit. This will create path outlines which are not on the database
unit grid. Such paths cannot be translated exactly to polygons. 

{: .box-warning }
**Warning**:
such paths cannot be written to OASIS.

```python
{% include_relative samples/path8.py %}
```

Gives

![Result](../samples/path8.png)
