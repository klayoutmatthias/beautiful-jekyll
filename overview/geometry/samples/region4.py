import klayout.db as db

region = db.Region()

region.insert(db.Box(0, 0, 3000, 4000))
region.insert(db.Box(2000, 0, 6000, 2000))

# "2" is the default cutoff mode. It is mandatory for
# anisotropic sizing.
sized_region = region.sized(0, 2000, 2)

