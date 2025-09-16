import klayout.db as db
import math

ly = db.Layout()
top_cell = ly.create_cell("TOP")
l1 = ly.layer(1, 0)
l2 = ly.layer(2, 0)

mag = 10.0

# uses the default font
gen = db.TextGenerator.default_generator()
region = gen.text("0123456789", ly.dbu, mag)

top_cell.shapes(l1).insert(region)

# uses a new generator with a custom font
gen = db.TextGenerator()
gen.load_from_file("7seg_font.gds")
region = gen.text("0123456789", ly.dbu, mag)

top_cell.shapes(l2).insert(region, db.DTrans(db.DVector(0, 10.0)))

ly.write("glyphs.gds")
