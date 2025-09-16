---
layout: page
---

# How to Read the Reference Documentation

KLayout's reference documentation ([KLayout Class Index](https://www.klayout.de/doc-qt5/code/index.html)) is the 
auto-generated API documentation and lists all classes and methods available. In the documents here you will 
find many references into this documentation.

Although Python is supported well in KLayout's API, the primary scripting language in KLayout is Ruby. 
The documentation uses Ruby syntax and terminology, but as the methods and classes are basically implemented in C++, the
documentation refers to C++ concepts as well.

I will try to explain some concepts to make it easier to understand the reference documentation. More
details can be found in [Notation used in the Ruby API documentation](https://www.klayout.de/doc-qt5/about/rba_notation.html)
and [Using Python](https://www.klayout.de/doc-qt5/programming/python.html) from the KLayout application
documentation. Most Ruby concepts directly translate to Python, so the Ruby explanations apply to Python as
well.

When you navigate to a class documentation - for example: [Layout Class Reference](https://www.klayout.de/doc-qt5/code/class_Layout.html) - you
will look at the basic data sheet of the class: 
The Module the class is implemented in (here: "db" which translates to `klayout.db`), a brief
and often a more detailed description.

Below that you find a list of the various methods. The descriptions use C++ slang and Python programmers are
not necessarily familiar with that. In addition, Python and Ruby are very similar, but not fully compatible.
Some concepts are added by the system in a generic way and need explanation. Here are some notes:

  * A "constructor" corresponds to the `__init__(self)` method. C++ has overloading, so multiple 
    different ways may exist how an object is initialized. KLayout will pick the best match und
    complain if the match is ambiguous. The Ruby way of creating an object is "new", hence the
    constructors are named "new". "new" is actually also available as a class method, so an alternative way to 
    create a Layout object is `klayout.db.Layout.new()`. This way, there is support for constructors
    which are named differently than "new" as well.

  * Factory methods: some methods create new objects. Such methods are called "factory methods" and will return
    a new, independent object. For example, Layout's `dup` method will return an exact copy of the Layout
    it is called on. You will see "new Layout ptr" as the return value which means that this method
    returns a new Layout object.

  * `nil` value: `nil` is Ruby for `None`. In C++ this is called a null pointer.
  
  * 'true' and 'false' in Ruby are the equivalent to 'True' and 'False' in Python.

  * Most classes have some internal methods which usually start with an underscore (e.g. `_destroy`). 
    You should not need them often, but sometimes they are useful. `_destroy` for example will immediately
    free the resources of an object and not only after the reference went out of scope. This allows
    for some memory optimization in some cases.

  * "const" is a concept inherited from C++. An object reference can be "const" (constant). In 
    this case, it is only allowed to call methods declared as "const". Such methods will not alter the 
    object. Such a reference eventually is read-only. 

  * "static method" is C++ speak for "class method".

  * Some methods are properties Python. The Ruby notation for this is the getter/setter pair. For 
    example, Layout's database unit getter is `dbu` and the setter is `dbu=`. When there is such a pair, 
    it is made available as a property in Python. In the documentation, this is mentioned as 
    "Python specific notes: The object exposes a readable attribute 'dbu'. This is the getter." or
    "... This is the setter.".

  * Pointers, references and return by value: C++ differentiates between pointers to objects, references to objects and
    objects copied by value. For most "heavy" objects, references are used. This means that the 
    actual object lives inside another object (the "container" or "aggregation") and client code will 
    refer to this object. So modifying the object directly manipulates the container collection of objects.
    Pointers (denoted as "ptr" in the documentation) are special forms of references. They can become null pointers (`None` in Python).
    For example, Layout's `cell` method can return a cell reference from a cell name. This is a pointer,
    as the return value can be `None` if there is no cell with that name.
    Lightweight objects are often returned by value, which means they will be made independent copies.
    Manipulating them does not have any other effect than changing exactly this one object. 
    For example, Layout's `get_info` method will return a copy of a `LayerInfo` object for a specific layer. 
    In order to change the layer information, you have to modify the returned object and set it using 
    `set_info`.

  * Iterators: some methods deliver iterators which can be used in a `for x in ...` loop to 
    generate all objects from a sequence. These methods are marked with "iter". For example,
    Layout's `each_cell` returns a cell iterators. The values delivered by this iterator
    are Cell references. 

  * Scalar data types: "double" is C++ for "float", "unsigned .." is the unsigned version
    of some integer type. "int" is a 32 bit integer, "long" is a 64 bit integer. "bool" is a boolean
    value (`True` or `False`). "string" is a unicode string.

  * Variants: some methods return variant values which means the return type is not fully specified
    and can basically any type. Usually variants are only used in "either something of type X or None"
    mode. For example, Layout's `find_layer` method will return a variant that is either a layer handle
    or `None` if the given layer does not exist.

  * Arrays: if a method returns or takes an array of objects, the notation indicates this with a "[]" suffix. For example
    Layout's `layer_indexes` returns an array of all layer indexes, which reads as "unsigned int[]" in the
    documentations.

  * Predicates: in Ruby, predicates (method or attributes with boolean value) are traditionally are written with a "?" suffix. 
    For example, Layout's `is_editable?` is a such a predicate. In Python, the question mark cannot be part
    of the method name, so it is not present.

  * Operators: Ruby allows operator overloading similar to Python, but the Ruby way to doing so is to 
    define a method with the operator name, e.g. `+(other)` is equivalent to Python's `__add__(self, other)`.
    Ruby does not have a way of overloading the in-place versions such as `+=`, so there are no such operators
    available in Python as well.

  * In Python, brackets are mandatory for method calls: while Ruby allows skipping the brackets for method calls without 
    arguments, Python needs them. For example, the Layout's `clear` method in Ruby can be called as `layout.clear` 
    while in Python it has to be written as `layout.clear()`. It's a common mistake to skip the brackets - in
    this case, the method will not be called. Instead, only a method reference will be created but no code
    will be executed.

  * Constants start with an upper-case letter always in Ruby.
  
