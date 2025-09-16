
# Boxes

For original class documentation see [Box class reference](https://www.klayout.org/doc-qt5/code/class_Box.html),
[DBox class reference](https://www.klayout.org/doc-qt5/code/class_DBox.html).

Boxes are rectangles aligned at the x and y axes. Boxes are given by 
four coordinates: left, bottom, right and top coordinate. Boxes can 
specified also by two points: the first is the lower-left corner, the second
the upper-right corner. 

{: .box-note }
**Note**: Coordinates and points do not need to be in the right
order - KLayout will swap the coordinates if required.

As derived attributes, a box has a width and height and a center point.

As a special case, boxes can be empty:

* `box.empty()` can be used to check if a box is empty
* Empty boxes don't participate in unions (`+` operator)
* The intersection (`&` operator) returns an empty box if the boxes do not intersect or one of the inputs is an empty box
* Width, height and center of empty boxes are undefined
* The area of an empty box is 0

Boxes with a width or height of zero are called degenerated as they represent 
lines or an single point. The area of such boxes is 0. Still they represent valid border cases.

An empty box is created by the default constructor:
```python
import klayout.db as db

empty = db.DBox()
print("empty is " + str(empty))
print("empty.empty() is " + str(empty.empty()))
```

Output:
```
empty is ()
empty.empty() is True
```

The `&` operator implements the intersection:
```python
{% include_relative samples/box_intersections.py %}
```

Output (`b1` is red, `b2` is blue, the intersection is white):

![Result](../samples/box_intersections.png)

The `+` operator implements the union (envelope):
```python
{% include_relative samples/box_unions.py %}
```

Output (`b1` is red, `b2` is blue, the union is white):

![Result](../samples/box_unions.png)



