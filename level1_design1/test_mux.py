# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
inp0 = 1
inp1 = 0
inp2 = 1
inp3 = 0
inp4 = 1
inp5 = 0
inp6 = 1
inp7 = 0
inp8 = 1
inp1 = 0
inp10 = 1
inp11 = 0
inp12 = 1
inp13 = 0
inp14 = 1
inp15 = 0
inp16 = 1
inp17 = 0
inp18 = 1
inp19 = 0
inp20 = 1
inp21 = 0
inp22 = 1
inp23 = 0
inp24 = 1
inp25 = 0
inp26 = 1
inp27 = 0
inp28 = 1
inp29 = 0
inp30 = 1
inp31 = 1
sel = 0
    # input driving
    dut.inp0.value = inp0
    dut.sel.value = sel
    await Timer(2, units='ns')
    assert dut.out.value == mux0, f"Mux result is incorrect: {dut.X.value} != 1"
@cocotb.test()
async def mux_randomised_test(dut):
    """Test for adding 2 random numbers multiple times"""
   for i in range(5):
        inp0 = random.randint(0, 15)
        sel = random.randint(0, 15)
        dut.inp0.value = inp0
        dut.sel.value = sel
        await Timer(2, units='ns')
       dut._log.info(f'inp0={inp0:05} sel={sel:05} model={mux0:05} DUT={int(dut.out.value):05}')
        assert dut.out.value == mux0, "Randomised test failed with: {inp0} {sel} = {out}".format(
            inp0=dut.inp0.value, sel=dut.sel.value, out=dut.out.value)
