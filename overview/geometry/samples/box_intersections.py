import klayout.db as db

b1 = db.DBox(2, 4, 6, 8)
b2 = db.DBox(4, 6, 8, 10)

b12 = b1 & b2
