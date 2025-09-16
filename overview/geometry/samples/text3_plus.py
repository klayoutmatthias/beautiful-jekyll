
ly = db.Layout()
tc = ly.create_cell("TOP")
l1 = ly.layer(1, 0)
l2 = ly.layer(2, 0)
l100 = ly.layer(100, 0)

for t in texts:
  tc.shapes(l1).insert(t)

for t in texts:
  p = t.trans * db.DPoint()
  tc.shapes(l100).insert(db.DBox(p, p))

ly.write("text3.gds")
