import klayout.db as db
import math

ly = db.Layout()
ly.read("cheese.gds")

options = db.SaveLayoutOptions()
options.dbu = 0.01                 # change database unit
options.gds2_max_vertex_count = 4  # fragment layout

ly.write("save_layout_options.gds", options)
