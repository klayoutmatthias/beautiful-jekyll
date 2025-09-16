import klayout.db as db

points = [
  db.DPoint(0, 0),
  db.DPoint(10, 0),
  db.DPoint(10, 2)
]

p = db.DPath(points, 10.0)
