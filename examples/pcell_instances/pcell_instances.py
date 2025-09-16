import klayout.db as db

# This will enable the Basic library
import klayout.lib

ly = db.Layout()
top_cell = ly.create_cell("TOP")
layer = ly.layer(1, 0)

# The parameter names are specific for the 
parameters = {
  "layer": db.LayerInfo(1, 0),
  "text": "KLAYOUT",
  "mag": 10.0
}

cell = ly.create_cell("TEXT", "Basic", parameters)

top_cell.insert(db.CellInstArray(cell.cell_index(), db.DTrans()))

ly.write("pcell_instances.gds")
