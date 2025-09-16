
l100 = ly.layer(100, 0)
ly.top_cell().shapes(l100).insert(global_bbox)

ly.write("cell_global_bbox.gds")

