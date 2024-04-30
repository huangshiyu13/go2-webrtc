# from go2_webrtc import ROBOT_CMD

from wasmtime import Config, Engine, Store, Module, Instance, Func, FuncType, ValType
import ctypes

config = Config()
store = Store(Engine(config))
file_path = "/Users/huangshiyu/Downloads/hsy/Task/robotics/github/go2-webrtc/python/go2_webrtc/libvoxel.wasm"
module = Module.from_file(store.engine, file_path)

a_callback_type = FuncType([ValType.i32()], [ValType.i32()])
b_callback_type = FuncType([ValType.i32(), ValType.i32(), ValType.i32()], [])

def copy_memory_region(t, n, a):
    copy_within(t, n, n + a)

def adjust_memory_size(t):
    return len(HEAPU8)

a = Func(store, a_callback_type, adjust_memory_size)
b = Func(store, b_callback_type, copy_memory_region)
instance = Instance(store, module, [a, b])
wasm_memory = instance.exports(store)["c"]
buffer = wasm_memory.data_ptr(store)
buffer_ptr = int.from_bytes(buffer, "little")
memory_size = wasm_memory.data_len(store)
HEAPU8 = (ctypes.c_uint8 * memory_size).from_address(buffer_ptr)

def copy_within(target, start, end):
    # Copy the sublist for the specified range [start:end]
    sublist = HEAPU8[start:end]

    # Replace elements in the list starting from index 'target'
    for i in range(len(sublist)):
        if target + i < len(HEAPU8):
            HEAPU8[target + i] = sublist[i]

a = Func(store, a_callback_type, adjust_memory_size)
b = Func(store, b_callback_type, copy_memory_region)
malloc = instance.exports(store)["f"]
# input = malloc(store, 61440)
input = malloc(store, 1)
