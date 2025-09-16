
import klayout.db as db

ly = db.Layout()
ly.read("my_layout.gds")

global_bbox = ly.top_cell().dbbox()
