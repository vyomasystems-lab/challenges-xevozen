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
    cocotb.log.info('Input')
    cocotb.log.info('sel: '+str(sel))
    cocotb.log.info('inp12: '+str(inp12))
    cocotb.log.info('inp13: '+str(inp13))
    cocotb.log.info('Expected Output')
    await Timer(2, units='ns')
    cocotb.log.info('out: '+str(inp12))
    cocotb.log.info('Model Output')
    cocotb.log.info('out: '+str(dut.out.value))

    assert dut.out.value == inp12, f"Mux result is incorrect: {dut.out.value} != {inp12}"

    cocotb.log.info('##### CTB: Develop your test here ########')

@cocotb.test()
async def test_mux2(dut):
    """Test for mux2"""
    sel = 12
    inp30 = 1

    dut.sel.value = sel
    dut.inp12.value = inp30

    await Timer(2, units='ns')

    assert dut.out.value == inp30, f"Mux result is incorrect: {dut.out.value} != {inp30}"

    cocotb.log.info('##### CTB: Develop your test here ########')
