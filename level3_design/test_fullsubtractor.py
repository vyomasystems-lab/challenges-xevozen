# See LICENSE.cocotb for details
# See LICENSE.vyoma for details

# Simple tests for an adder module
import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def subtractor_test(dut):
    A = 1
    B = 0
    Bin = 1
    
    # input driving
    dut.A.value = A
    dut.B.value = B
    dut.Bin.value = Bin
    cocotb.log.info('INPUT')
    cocotb.log.info('A: '+str(A))
    cocotb.log.info('B: '+str(B))
    cocotb.log.info('Bin: '+str(Bin))
    await Timer(2, units='ns')
    exD = (dut.A.value^dut.B.value)^dut.Bin.value
    exBout = int((dut.Bin.value and (not((dut.A.value)^(dut.B.value)))) or (~(dut.A.value) and dut.B.value))
    cocotb.log.info('EXPECTED OUTPUT')
    cocotb.log.info('D: '+str(exD))
    cocotb.log.info('Bout: '+str(exBout))
    cocotb.log.info('OUTPUT')
    cocotb.log.info('D: '+str(dut.D.value))
    cocotb.log.info('Bout: '+str(dut.Bout.value))

    print(dut.D.value)
    print(dut.Bout.value)
    assert (dut.D.value == exD) and (dut.Bout.value==exBout) , f"FullSubtractor result is incorrect: {dut.D.value} != {exD} or {dut.Bout.value} != {exBout}"
    #assert 1