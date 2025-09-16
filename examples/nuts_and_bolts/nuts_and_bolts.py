import klayout.db as db
import random
import math

ly = db.Layout()
top_cell = ly.create_cell("TOP")
layer = ly.layer(1, 0)

# Produce a cell for the nuts

nut = ly.create_cell("NUT")

t = db.CplxTrans(ly.dbu).inverted()
r = db.Region(t * db.DPolygon.ellipse(db.DBox(-1.0, -1.0, 1.0, 1.0), 6))
r -= db.Region(t * db.DPolygon.ellipse(db.DBox(-0.6, -0.6, 0.6, 0.6), 32))
nut.shapes(layer).insert(r)

# Produce a cell for the bolts

bolt = ly.create_cell("BOLT")

points = [
  db.DPoint(-1.0, -5.0),
  db.DPoint(-1.0, -4.0),
  db.DPoint(-0.5, -4.0),
  db.DPoint(-0.5, 5.0),
  db.DPoint(0.5, 5.0),
  db.DPoint(0.5, -4.0),
  db.DPoint(1.0, -4.0),
  db.DPoint(1.0, -5.0)
]
bolt.shapes(layer).insert(db.DPolygon(points))

# Random placements with scaling and arbitrary rotations

for i in range(0, 50):

  cell_name = [ "NUT", "BOLT" ][math.floor(2.0 * random.random())]
  cell = ly.cell(cell_name)

  x = random.random() * 100.0
  y = random.random() * 100.0
  scale = random.random() * 1.0 + 0.5
  angle = random.random() * 360.0
  mirror = False

  t = db.ICplxTrans(scale, angle, mirror, x, y)

  top_cell.insert(db.DCellInstArray(cell.cell_index(), t))

ly.write("nuts_and_bolts.gds")
