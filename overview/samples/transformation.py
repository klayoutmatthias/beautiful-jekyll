import klayout.db as db

poly = db.DPolygon([ 
  db.DPoint(0, 0), db.DPoint(0, 5), db.DPoint(4, 5), db.DPoint(4, 4),
  db.DPoint(1, 4), db.DPoint(1, 3), db.DPoint(3, 3), db.DPoint(3, 2),
  db.DPoint(1, 2), db.DPoint(1, 0)
])

# rotate by 90 degree counterclockwise

t1 = db.DTrans.R90

rotated_poly = t1 * poly

# rotate by 90 degree counterclockwise and shift by 10 µm to the right
# and 5 µm up

t2 = db.DTrans(db.DTrans.R90, 10.0, 5.0)

transformed_poly = t2 * poly
