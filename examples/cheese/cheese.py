import klayout.db as db
import math

ly = db.Layout()
ly.read("input.gds")

top_cell = ly.top_cell()

l1 = ly.layer(1, 0)
l2 = ly.layer(2, 0)

r1 = db.Region(top_cell.begin_shapes_rec(l1))
r2 = db.Region(top_cell.begin_shapes_rec(l2))

cheese = r1 - r2

l100 = ly.layer(100, 0)
top_cell.shapes(l100).insert(r2)

# Note: as r2 links to l2 (copy on write), we must 
# not clear these layers before using r2.
ly.clear_layer(l1)
ly.clear_layer(l2)

top_cell.shapes(l1).insert(cheese)

ly.write("cheese.gds")
