import klayout.db as db

points = [
  db.DPoint(0, 0),
  db.DPoint(0, 5),
  db.DPoint(5, 5)
]

p = db.DPath(points, 2.0, 1.0, 1.0)
