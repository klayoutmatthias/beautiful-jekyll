import klayout.db as db

p = db.DPolygon(db.DBox(1, 1, 5, 5))

hole_points = [
  db.DPoint(2, 2),
  db.DPoint(4, 4),
  db.DPoint(4, 2)
]

p.insert_hole(hole_points)
