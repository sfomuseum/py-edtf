import edtf.parser
import sys
import json

if __name__ == "__main__":

    edtf_str = sys.argv[1]

    p = edtf.parser.Parser()
    d = p.parse(edtf_str)
    print(json.dumps(d))
