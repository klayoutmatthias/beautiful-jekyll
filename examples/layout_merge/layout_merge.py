import klayout.db as db
import math

ly = db.Layout()
top_cell = ly.create_cell("TOP")

spacing = 1.0
y = 0.0

for file in [ "A.gds", "B.gds", "C.gds" ]:

  ly_import = db.Layout()
  ly_import.read(file)
  imported_top_cell = ly_import.top_cell()

  target_cell = ly.create_cell(imported_top_cell.name)
  target_cell.copy_tree(imported_top_cell)

  # frees the resources of the imported layout
  ly_import._destroy()

  inst = db.DCellInstArray(target_cell.cell_index(), db.DTrans(db.DVector(0, y)))
  top_cell.insert(inst)

  y += target_cell.dbbox().height() + spacing

ly.write("layout_merge.gds")
