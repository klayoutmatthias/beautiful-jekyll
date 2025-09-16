import klayout.db as db

dbu = 0.001

t = db.CplxTrans(dbu).inverted()

r = db.Region()

r.insert(t * db.DBox(0.0, 3.0, 1.0, 4.0))

points = [
  db.DPoint(0.0, 1.0), db.DPoint(3.0, 1.0), db.DPoint(3.0, 4.0)
]
r.insert(t * db.DPath(points, 2.0))
