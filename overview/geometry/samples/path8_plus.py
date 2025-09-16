
ly = db.Layout()
ly.dbu = 1.0
tc = ly.create_cell("TOP")
l1 = ly.layer(1, 0)
l2 = ly.layer(2, 0)
l100 = ly.layer(100, 0)

tc.shapes(l1).insert(p)

for x in range(-3, 8):
  for y in range(-2, 9):
    tc.shapes(l100).insert(db.DBox(x, y, x, y))

ly.write("path8.gds")
