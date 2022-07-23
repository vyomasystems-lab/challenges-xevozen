# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    sel = 12
    inp12 = 1
    inp13 = 0

    dut.sel.value = sel
    dut.inp12.value = inp12

    await Timer(2, units='ns')

    assert dut.out.value == 1, f"Adder result is incorrect: {dut.X.value} != 15"

    cocotb.log.info('##### CTB: Develop your test here ########')
