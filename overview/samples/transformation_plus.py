ly = db.Layout()
tc = ly.create_cell("TOP")
l1 = ly.layer(1, 0)
l2 = ly.layer(2, 0)
l101 = ly.layer(101, 0)

tc.shapes(l1).insert(poly)
tc.shapes(l2).insert(transformed_poly)
tc.shapes(l101).insert(rotated_poly)

ly.write("transformation.gds")
