import klayout.db as db

region = db.Region()

region.insert(db.Box(0, 0, 3000, 4000))
region.insert(db.Box(2000, 0, 6000, 2000))

sized_region = region.sized(1000)

