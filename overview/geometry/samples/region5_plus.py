
ly = db.Layout()
tc = ly.create_cell("TOP")
l1 = ly.layer(1, 0)
l2 = ly.layer(2, 0)
l101 = ly.layer(101, 0)
l100 = ly.layer(100, 0)

tc.shapes(l1).insert(r1)
tc.shapes(l2).insert(r2)
tc.shapes(l101).insert(result)
tc.shapes(l100).insert(result)

ly.write("region5.gds")
