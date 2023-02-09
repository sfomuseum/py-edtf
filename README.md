# py-edtf

Python package wrapping the `sfomuseum/go-edtf` WASM (WASI) binary for parsing Library of Congress Extended DateTime Format (EDTF) strings.

## Documentation

Documentation is incomplete at this time.

## Install

```
$> pip3 install --upgrade -r requirements.txt .
```

## Example

```
import edtf.parser

p = edtf.parser.Parser()
d = p.parse("2022")

print(d["end"])
```

If successful `d` will be a JSON-representation of the [go-edtf.EDTFDate](https://pkg.go.dev/github.com/sfomuseum/go-edtf#EDTFDate) instance derived from the EDTF string being parsed. For example `print(d["end"])` would emit:

```
{'edtf': '2022', 'lower': {'approximate': 0, 'datetime': '2022-12-31T00:00:00Z', 'inclusivity': 0, 'open': False, 'precision': 64, 'timestamp': 1672444800, 'uncertain': 0, 'unknown': False, 'unspecified': 0, 'ymd': {'day': 31, 'month': 12, 'year': 2022}}, 'upper': {'approximate': 0, 'datetime': '2022-12-31T23:59:59Z', 'inclusivity': 0, 'open': False, 'precision': 64, 'timestamp': 1672531199, 'uncertain': 0, 'unknown': False, 'unspecified': 0, 'ymd': {'day': 31, 'month': 12, 'year': 2022}}}
```

If `p.parse` is passed invalid an EDTF string it will raise an exception.

## See also

* https://github.com/sfomuseum/go-edtf
* https://github.com/sfomuseum/go-edtf-wasm#wasi
