import klayout.db as db
import math

ly = db.Layout()
ly.read("nuts_and_bolts.gds")

# arguments are: levels (-1: all), remove orphan cells
ly.top_cell().flatten(-1, True)

ly.write("flatten.gds")
