
import klayout.db as db

ly = db.Layout()
ly.read("my_layout.gds")

l1 = ly.layer(1, 0)

global_bbox = ly.top_cell().dbbox_per_layer(l1)
