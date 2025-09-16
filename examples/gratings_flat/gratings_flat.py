import klayout.db as db
import math

ly = db.Layout()
top_cell = ly.create_cell("TOP")
layer = ly.layer(1, 0)

width = 1.0
height = 10.0
length = 100.0

y = 0.0

for pitch in [ 2.0, 2.5, 3.0 ]:

  n = math.floor(length / pitch)

  for i in range(0, n):

    pt = db.DPoint(i * pitch, y)
    box = db.DBox(pt, pt + db.DVector(width, height))

    top_cell.shapes(layer).insert(box)

  y += height * 1.5

ly.write("gratings_flat.gds")
