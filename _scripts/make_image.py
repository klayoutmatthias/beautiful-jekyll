
import pya

mw = pya.Application.instance().main_window()

cv = mw.load_layout(input, 0)
ly = cv.layout()
cell = cv.cell
view = mw.current_view()
view.clear_layers()
view.select_cell(0, cell.cell_index())

lp = pya.LayerProperties()
lp.fill_color = lp.frame_color = 0xffffff
lp.source_layer = 0
lp.source_datatype = 0
lp.dither_pattern = 5
lp.width = 0
lp.name = "TXT"
view.insert_layer(view.end_layers(), lp)

lp = pya.LayerProperties()
lp.fill_color = lp.frame_color = 0xff8080
lp.source_layer = 1
lp.source_datatype = 0
lp.dither_pattern = 5
lp.name = "IN1"
view.insert_layer(view.end_layers(), lp)

lp = pya.LayerProperties()
lp.fill_color = lp.frame_color = 0x8080ff
lp.source_layer = 2
lp.source_datatype = 0
lp.dither_pattern = 9
lp.name = "IN2"
view.insert_layer(view.end_layers(), lp)

lp = pya.LayerProperties()
lp.fill_color = lp.frame_color = 0x404040
lp.source_layer = 101
lp.source_datatype = 0
lp.width = 0
lp.dither_pattern = 0
lp.transparent = True
lp.name = "OUT_POLY"
view.insert_layer(view.end_layers(), lp)

lp = pya.LayerProperties()
lp.fill_color = lp.frame_color = 0xffffff
lp.source_layer = 100
lp.source_datatype = 0
lp.dither_pattern = 1
lp.width = 3
lp.name = "OUT"
view.insert_layer(view.end_layers(), lp)

box = cell.dbbox()
e = max(box.height() * 0.1, 3.0)
ey = max(e, box.width() * 0.5 - box.height())
ex = max(e, box.height() * 0.5 - box.width())
box.enlarge(ex, ey)

t = pya.DText(input, box.left + 1.0, box.top - 0.5)
t.valign = 0
t.font = 0
t.size = 0.2 / ly.dbu
cell.shapes(ly.layer(0, 0)).insert(t)

view.zoom_box(box)
view.max_hier()

h = 700
w = box.width() * h / box.height()
if w > 700:
  w = 700
  h = box.height() * w / box.width()

view.update_content()
print("Producing " + output + " ..")
view.save_image_with_options(output, w, h, 3, 3, 1/3.0, pya.DBox(), False)

view.max_hier_levels = 1
view.update_content()
output_cells = output.replace(".png", "_cells.png")
print("Producing " + output_cells + " ..")
view.save_image_with_options(output_cells, w, h, 3, 3, 1/3.0, pya.DBox(), False)

