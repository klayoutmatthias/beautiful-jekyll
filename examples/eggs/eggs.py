import klayout.db as db
import math

ly = db.Layout()
ly.read("input.gds")

top_cell = ly.top_cell()

# input
l101 = ly.layer(101, 0)  # shapes
l100 = ly.layer(100, 0)  # "L" region

# output
l1 = ly.layer(1, 0)
l2 = ly.layer(2, 0)

# rectangular box region query -> goes to 1/0

box_region = db.DBox(30.0, 30.0, 45.0, 45.0)

box_iter = ly.top_cell().begin_shapes_rec_overlapping(l101, box_region)
while not box_iter.at_end():
  top_cell.shapes(l1).insert(box_iter.shape(), box_iter.trans())
  box_iter.next()

# irregular region query -> goes to 2/0

region = db.Region(top_cell.begin_shapes_rec(l100))

region_iter = db.RecursiveShapeIterator(ly, top_cell, l101, region)
while not region_iter.at_end():
  top_cell.shapes(l2).insert(region_iter.shape(), region_iter.trans())
  region_iter.next()

ly.write("eggs.gds")
