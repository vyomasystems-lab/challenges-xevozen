# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

import time

from model_mkbitmanip import *

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 




# Sample Test
@cocotb.test()
def run_test(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1
    count = 1
    passed = 0
    failed = 0
    for func7seed in range(64):
        for func3seed in range(8):
            for func1seed in range(2):
                if(count%100==0):
                    time.sleep(1)
                # print("Test: "+str(count)+ " ", end='')
                count = count + 1
                func7gen = bin(func7seed)
                func7gen=func7gen[2:].zfill(6)
                func3gen = bin(func3seed)
                func3gen=func3gen[2:].zfill(3)
                # print(func7gen)
                # print(func3gen)
                binaryFunc = "0"+func7gen+"0000100000"+func3gen+"000010"+str(func1seed)+"10011"
                # print(binaryFunc)
                # print(hex(int(binaryFunc, 2)))
                inp1 = bin(random.randint(0, 4294967295))[2:]
                inp2 = bin(random.randint(0, 4294967295))[2:]
                inp3 = bin(random.randint(0, 4294967295))[2:]
                inp1=inp1.zfill(32)
                inp2=inp2.zfill(32)
                inp3=inp3.zfill(32)
                # print(inp1)
                # print(inp2)
                # print(inp3)
                ######### CTB : Modify the test to expose the bug #############
                # input transaction
                mav_putvalue_src1 = int(inp1, 2)
                mav_putvalue_src2 = int(inp2, 2)
                mav_putvalue_src3 = int(inp3, 2)
                mav_putvalue_instr = int(binaryFunc, 2)
                # 401070B3
                # expected output from the model
                expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)
                # driving the input transaction
                dut.mav_putvalue_src1.value = mav_putvalue_src1
                dut.mav_putvalue_src2.value = mav_putvalue_src2
                dut.mav_putvalue_src3.value = mav_putvalue_src3
                dut.EN_mav_putvalue.value = 1
                dut.mav_putvalue_instr.value = mav_putvalue_instr
                yield Timer(1) 
                # obtaining the output
                dut_output = dut.mav_putvalue.value
                if(expected_mav_putvalue==0):
                    # print("found")
                    dut_output = 0
                if(hex(dut_output) != hex(expected_mav_putvalue)):
                    failed = failed + 1
                    print("Binary Function: "+binaryFunc)
                    print("Input 1: "+ inp1)
                    print("Input 2: "+ inp2)
                    print("Input 3: "+ inp3)
                    print("Expected Output: "+str(hex(expected_mav_putvalue)))
                    print("Output Got: "+str(hex(dut_output)))
                    print("FAILED!!!")
                    time.sleep(10)
                else:
                    passed = passed + 1
                    # print("PASSED!!!")
                # print()
                # cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
                # cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
                # print("Test END")
                
    print("Passed: "+str(passed))
    print("Failed: "+str(failed))
    print("Total: "+str(count))
    print("-------------------------------------")
    binaryFunc = "0100000 0000100000 110 00001 0110011"
    # 01000000000100000110000010110011

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x5
    mav_putvalue_src3 = 0x5
    mav_putvalue_instr = 0x401060B3
    # 401070B3
    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # dut_output = expected_mav_putvalue

    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message












# # Sample Test
# @cocotb.test()
# def run_test(dut):

#     # clock
#     cocotb.fork(clock_gen(dut.CLK))

#     # reset
#     dut.RST_N.value <= 0
#     yield Timer(10) 
#     dut.RST_N.value <= 1


#     ######### CTB : Modify the test to expose the bug #############
#     # input transaction
#     mav_putvalue_src1 = 0x5
#     mav_putvalue_src2 = 0x0
#     mav_putvalue_src3 = 0x0
#     mav_putvalue_instr = 0x101010B3
#     # 401070B3
#     # expected output from the model
#     expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

#     # driving the input transaction
#     dut.mav_putvalue_src1.value = mav_putvalue_src1
#     dut.mav_putvalue_src2.value = mav_putvalue_src2
#     dut.mav_putvalue_src3.value = mav_putvalue_src3
#     dut.EN_mav_putvalue.value = 1
#     dut.mav_putvalue_instr.value = mav_putvalue_instr
  
#     yield Timer(1) 

#     # obtaining the output
#     dut_output = dut.mav_putvalue.value

#     cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
#     cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
#     # dut_output = expected_mav_putvalue

#     # comparison
#     error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
#     assert dut_output == expected_mav_putvalue, error_message
