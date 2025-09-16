import klayout.db as db

t1 = db.DText("ALIGN 0,0", db.DVector(0, 0))
t1.halign = 0  # left
t1.valign = 0  # top

t2 = db.DText("ALIGN 1,0", db.DVector(0, 1))
t2.halign = 1  # center
t2.valign = 0  # top

t3 = db.DText("ALIGN 2,0", db.DVector(0, 2))
t3.halign = 2  # right
t3.valign = 0  # top

t4 = db.DText("ALIGN 1,0", db.DVector(0, 3))
t4.halign = 1  # center
t4.valign = 0  # top

t5 = db.DText("ALIGN 1,1", db.DVector(0, 4))
t5.halign = 1  # center
t5.valign = 1  # center

t6 = db.DText("ALIGN 1,2", db.DVector(0, 5))
t6.halign = 1  # center
t6.valign = 2  # bottom

texts = [ t1, t2, t3, t4, t5, t6 ]
