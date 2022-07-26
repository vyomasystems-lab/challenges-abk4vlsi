# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestError

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
inp0 = 0b1
inp1 = 0b0
inp2 = 0b1
inp3 = 0b0
inp4 = 0b1
inp5 = 0b0
inp6 = 0b1
inp7 = 0b0
inp8 = 0b1
inp1 = 0b0
inp10 = 0b1
inp11 = 0b0
inp12 = 0b1
inp13 = 0b0
inp14 = 0b1
inp15 = 0b0
inp16 = 0b1
inp17 = 0b0
inp18 = 0b1
inp19 = 0b0
inp20 = 0b1
inp21 = 0b0
inp22 = 0b1
inp23 = 0b0
inp24 = 0b1
inp25 = 0b0
inp26 = 0b1
inp27 = 0b0
inp28 = 0b1
inp29 = 0b0
inp30 = 0b1
inp31 = 0b1
sel = 0
# input driving
dut.inp0.value = A
dut.sel.value = B
awaitTimer(2, units='ns')
expected = 0b0
if dut.out.value != expected:
    raise TestError("A={:0b}, sel={:04b}, expected {}, found {}".format(dut.inp0.value, dut.sel.value, expected, dut.out.value))

expected = 0b1
if dut.out.value != expected:
    raise TestError("A={:0b}, sel={:04b}, expected {}, found {}".format(dut.inp0.value, dut.sel.value, expected, dut.out.value))
