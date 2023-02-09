import json
from wasmer import engine, Store, Module, Instance, wasi
from wasmer_compiler_cranelift import Compiler
import importlib.resources as importlib_resources
from edtf.output import OutputGrabber

class Parser:

    def __init__(self) :
        
        pkg = importlib_resources.files("edtf")
        pkg_data_file = pkg / "wasi" / "parse.wasm"
        wasm_bytes = pkg_data_file.read_bytes()
        
        store = Store(engine.JIT(Compiler))
        
        module = Module(store, wasm_bytes)
        
        wasi_version = wasi.get_version(module, strict=True)
        
        self.store = store
        self.module = module
        self.version = wasi_version
    
    def parse(self, edtf_str) :

        wasi_env = wasi.StateBuilder('main').  \
            argument(edtf_str). \
            finalize()
        
        import_object = wasi_env.generate_import_object(self.store, self.version)
        instance = Instance(self.module, import_object)
        
        out = OutputGrabber()
        
        with out:
            instance.exports._start()
            
        result = out.capturedtext.strip()

        try:
            return json.loads(result)
        except:
            raise Exception(result)
    
