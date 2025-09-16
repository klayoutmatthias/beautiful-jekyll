import klayout.db as db

points = [
  db.DPoint(0, 0),
  db.DPoint(0, 5),
  db.DPoint(5, 5)
]

path = db.DPath(points, 2.0)
poly = path.polygon()
