import klayout.db as db

points = [
  db.DPoint(0, 0),
  db.DPoint(2, 5),
  db.DPoint(4, 0)
]

p = db.DPath(points, 2.0)
