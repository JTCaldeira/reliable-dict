import os

from cffi import FFI


HEADER_FILE_NAME = "reliabledict.h"
SOURCE_FILE_NAME = "reliabledict.c"

ffi = FFI()

header = open(HEADER_FILE_NAME, "rt").read()
source = open(SOURCE_FILE_NAME, "rt").read()

ffi.set_source("reliabledict.reliabledict", header + source)

ffi.cdef(header)


if __name__ == "__main__":
	ffi.compile()
	print("henlo worlmd")

