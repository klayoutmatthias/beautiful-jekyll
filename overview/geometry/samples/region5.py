import klayout.db as db

r1 = db.Region()
r1.insert(db.Box(0, 0, 3000, 4000))

r2 = db.Region()
r2.insert(db.Box(1000, 1000, 6000, 2000))

result = r1 - r2
