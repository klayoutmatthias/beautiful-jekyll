import klayout.db as db

r = db.Region()

r.insert(db.Box(0, 3000, 1000, 4000))

points = [
  db.Point(0, 1000), db.Point(3000, 1000), db.Point(3000, 4000)
]
r.insert(db.Path(points, 2000))
