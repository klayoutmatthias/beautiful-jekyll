import klayout.db as db

# Note we use integer-unit paths here

points = [
  db.Point(0, 0),
  db.Point(0, 5),
  db.Point(5, 5)
]

p = db.Path(points, 3)
