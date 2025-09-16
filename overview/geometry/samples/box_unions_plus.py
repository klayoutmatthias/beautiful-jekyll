
ly = db.Layout()
tc = ly.create_cell("TOP")
l1 = ly.layer(1, 0)
l2 = ly.layer(2, 0)
l100 = ly.layer(100, 0)

tc.shapes(l1).insert(b1)
tc.shapes(l2).insert(b2)
tc.shapes(l100).insert(b12)

ly.write("box_unions.gds")
