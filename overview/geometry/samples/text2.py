import klayout.db as db

t = db.DText("KLAYOUT", db.DVector(1, 2))

print("Text location is: " + str(t.trans * db.Point()))
