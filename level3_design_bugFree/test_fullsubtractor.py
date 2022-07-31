# See LICENSE.cocotb for details
# See LICENSE.vyoma for details

# Simple tests for an adder module
import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def subtractor_test(dut):
    A = 0
    B = 1
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
    cocotb.log.info('EXPECTED OUTPUT')
    cocotb.log.info('D: '+str((dut.A.value^dut.B.value)^dut.Bin.value))
    cocotb.log.info('Bout: '+str((dut.Bin.value and (~(dut.A.value))) or (~dut.A.value and dut.B.value)))
    cocotb.log.info('OUTPUT')
    cocotb.log.info('D: '+str(dut.D.value))
    cocotb.log.info('Bout: '+str(dut.Bout.value))
    assert (dut.D.value == (dut.A.value^dut.B.value)^dut.Bin.value) and (dut.Bout.value == (dut.Bin.value and (~(dut.A.value))) or (~dut.A.value and dut.B.value)) , f"FullSubtractor result is incorrect: {dut.D.value} != {(dut.A.value^dut.B.value)^dut.Bin.value} or {dut.Bout.value} != {dut.Bin.value and (~(dut.A.value)) or (~dut.A.value and dut.B.value)}"
    #assert 1
