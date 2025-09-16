
ly = db.Layout()
tc = ly.create_cell("TOP")
l1 = ly.layer(1, 0)
l2 = ly.layer(2, 0)
l100 = ly.layer(100, 0)

tc.shapes(l1).insert(poly)

ly.write("path_to_polygon.gds")
