import edtf.parser
import json

edtf_str = "2004-06-XX/2004-07-03"

p = edtf.parser.Parser()
d = p.parse(edtf_str)

assert d["end"]["lower"]["timestamp"] == 1088812800

d = p.parse("{1667,1668,1670..1672}")

assert d["start"]["upper"]["timestamp"] == -9530179201
