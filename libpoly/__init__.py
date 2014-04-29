# The MIT License (MIT)
#
# Copyright (c) 2014 Samuel Lucidi
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

__version__ = "0.1.0-56c157633b"

import cffi

libpoly_header = open('poly.h').read()

ffi = cffi.FFI()
ffi.cdef(libpoly_header)

# look in the typical places for
# libpoly.so
__libpoly = ffi.dlopen('libpoly.so')

Sine = __libpoly.poly_sine
Square = __libpoly.poly_square
Saw = __libpoly.poly_saw
Triangle = __libpoly.poly_triangle
Sample = __libpoly.poly_sample
LoopSample = __libpoly.poly_loopsample

def init(bitdepth, channels, bitrate, max_generators, filename=None):
	if filename is None:
		filename = ffi.NULL
	return __libpoly.poly_init(bitdepth, channels, bitrate, max_generators, filename)

def shutdown():
	__libpoly.poly_shutdown()

def start():
	return __libpoly.poly_start()

def stop():
	__libpoly.poly_stop()

def get_init(index):
	return __libpoly.poly_get_init(index)

def get_wavetype(index):
	return __libpoly.poly_get_wavetype(index)

def get_amplitude(index):
	return __libpoly.poly_get_amplitude(index)

def get_L_amp(index):
	return __libpoly.poly_get_L_amp(index)

def get_R_amp(index):
	return __libpoly.poly_get_R_amp(index)

def get_freq(index):
	return __libpoly.poly_get_freq(index)

def get_phrase(index):
	return __libpoly.poly_get_phrase(index)

def get_duty(index):
	return __libpoly.poly_get_duty(index)

def get_sample_bitdepth(index):
	return __libpoly.poly_get_sample_bitdepth(index)

def get_sample_length(index):
	return __libpoly.poly_get_sample_length(index)

def get_sample(index):
	return __libpoly.poly_get_sample(index)

def mute(index):
	__libpoly.poly_mute(index)

def unmute(index):
	__libpoly.poly_unmute(index)

def set_wavetype(index, wavetype):
	__libpoly.poly_set_wavetype(index, wavetype)

def set_amplitude(index, amplitude):
	__libpoly.poly_set_amplitude(index, amplitude)

def set_L_amp(index, L_amp):
	__libpoly.poly_set_L_ampl(index, L_amp)

def set_R_amp(index, R_amp):
	__libpoly.poly_set_R_ampl(index, R_amp)

def bump_freq(index, freq):
	__libpoly.poly_bump_freq(index, freq)

def set_freq(index, freq):
	__libpoly.poly_set_freq(index, freq)

def set_phase(index, phase):
	__libpoly.poly_set_phase(index, phase)

def set_duty(index, duty):
	__libpoly.poly_set_duty(index, duty)

def set_sample_bitdepth(index, sample_bitdepth):
	__libpoly.poly_set_sample_bitdepth(index, sample_bitdepth)

def set_sample_length(index, sample_length):
	__libpoly.poly_set_sample_length(index, sample_length)

def set_sample(index, sample):
	__libpoly.poly_set_sample(index, sample)

def init_generator(index, wavetype, amplitude, freq):
	__libpoly.poly_init_generator(index, wavetype, amplitude, freq)
