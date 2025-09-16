import klayout.db as db

ly_file = db.Layout()
ly_file.read("my_layout.gds")

l1 = ly_file.layer(1, 0)
r1 = db.Region(ly_file.top_cell().begin_shapes_rec(l1))

l2 = ly_file.layer(2, 0)
r2 = db.Region(ly_file.top_cell().begin_shapes_rec(l2))

# Note: the database unit is 1 nm, so 300 corresponds to 0.3 µm
result = r1.sized(300) + r2.sized(-300)

