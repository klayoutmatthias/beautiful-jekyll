---
layout: page
---

# Texts

For original class documentation see [Text class reference](https://www.klayout.org/doc-qt5/code/class_Text.html) and
[DText class reference](https://www.klayout.org/doc-qt5/code/class_DText.html).

Text objects are basically points with a string attached to it.
Texts can have an orientation, hence the location is specified by
a simple transformation rather than a single point.

Texts have a variety of attributes such as fonts and text size and
text justification settings.

{: .box-warning }
**Warning**: OASIS does not support text orientations, fonts information or
text justification.

KLayout itself does not display texts with a specific font. Instead
all texts are shown with the same font which can be configured 
globally. 

{: .box-note }
**Note:** with the 'Default' font selected, KLayout will not display
text sizes or texts rotated. Use one of the other fonts to enable display
of scaled or rotated texts (use File/Setup, Display/Texts page).

Note that the text is only considered a point-like object. The
extensions of the label are not considered in the text's bounding 
box. This is important for example for region queries.

```python
{% include_relative samples/text1.py %}
```

Gives

![Result](../samples/text1.png)

To get the text position, apply the text transformation to 
the origin point:

```python
{% include_relative samples/text2.py %}
```

Gives

```
Text location is: 1,2
```

The alignment attributes `halign` and `valign` control how the text is 
placed relative to it's location:

```python
{% include_relative samples/text3.py %}
```

Gives

![Result](../samples/text3.png)

