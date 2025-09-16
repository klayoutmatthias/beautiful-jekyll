import klayout.db as db

# This will enable the Basic library
import klayout.lib

lib = db.Library.library_by_name("Basic")

types = {
  db.PCellParameterDeclaration.TypeBoolean: "bool",
  db.PCellParameterDeclaration.TypeDouble:  "double",
  db.PCellParameterDeclaration.TypeInt:     "int",
  db.PCellParameterDeclaration.TypeLayer:   "layer",
  db.PCellParameterDeclaration.TypeList:    "list",
  db.PCellParameterDeclaration.TypeNone:    "none",
  db.PCellParameterDeclaration.TypeShape:   "shape",
  db.PCellParameterDeclaration.TypeString:  "string"
}

for pcell_name in lib.layout().pcell_names():

  print("--------------------------------------")
  print("PCell parameters for '" + pcell_name + "':")

  pcell_decl = lib.layout().pcell_declaration(pcell_name)

  for param in pcell_decl.get_parameters():
    print("  name: " + param.name + ", hidden: " + str(param.hidden) + ", type: " + types[param.type] + ", description: " + param.description)

