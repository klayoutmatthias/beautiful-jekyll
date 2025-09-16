import klayout.db as db

ly = db.Layout()

# Creates a cell called "F" with some polygon

f_cell = ly.create_cell("F")

poly = db.DPolygon([ 
  db.DPoint(0, 0), db.DPoint(0, 5), db.DPoint(4, 5), db.DPoint(4, 4),
  db.DPoint(1, 4), db.DPoint(1, 3), db.DPoint(3, 3), db.DPoint(3, 2),
  db.DPoint(1, 2), db.DPoint(1, 0)
])

l1 = ly.layer(1, 0)
f_cell.shapes(l1).insert(poly)

# Place this cell two times in a new cell TOP

top_cell = ly.create_cell("TOP")

# The first placement is a single instance
i1 = db.DCellInstArray(f_cell.cell_index(), db.DTrans.R90)
top_cell.insert(i1)

# The second placement is a 2x3 array instance
i2 = db.DCellInstArray(
  f_cell.cell_index(),                  # cell reference
  db.DTrans(db.DTrans.M90, 10.0, 5.0),  # basic transformation
  db.DVector(0, 6),                     # a
  db.DVector(5, 0),                     # b
  2,                                    # na
  3                                     # nb
)
top_cell.insert(i2)

ly.write("instances.gds")
