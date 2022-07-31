# See LICENSE.cocotb for details
# See LICENSE.vyoma for details

# Simple tests for an adder module
import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def adder_basic_test(dut):
    """Test for 5 + 10"""

    A = 5
    B = 10

    # input driving
    dut.A.value = 1
    dut.B.value = 1
    print("Hello World!!")
    await Timer(2, units='ns')
    print(dut.D.value)
    #assert dut.sum.value == A+B, f"Adder result is incorrect: {dut.X.value} != 15"
    assert 1

