import klayout.db as db

points = [
  db.DPoint(1, 1),
  db.DPoint(1, 6),
  db.DPoint(5, 6),
  db.DPoint(5, 5),
  db.DPoint(2, 5),
  db.DPoint(2, 4),
  db.DPoint(3, 4),
  db.DPoint(3, 3),
  db.DPoint(2, 3),
  db.DPoint(2, 1)
]

p = db.DPolygon(points)
