import klayout.db as db
import math

ly = db.Layout()
ly.read("input.gds")

clip_layer = ly.layer(100, 0)

# Note that we use "bbox" to get the integer-unit bounding box
clip_box = ly.top_cell().bbox_per_layer(clip_layer)

# The clip method only takes integer-unit clip boxes so far.
# It takes and returns cell indexes.
clip_cell_index = ly.clip(ly.top_cell().cell_index(), clip_box)

clip_cell = ly.cell(clip_cell_index)
clip_cell.name = "CLIP"

clip_cell.write("clip.gds")
