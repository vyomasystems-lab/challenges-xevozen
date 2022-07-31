# Level 2 Design - Bit Manipulator Coprocessor Design Verification
-------
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![Verification Environment](/assets/lvl2-1.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Bit Manipulator Coprocessor Design Under Test which takes in 32-bit inputs *mav_putvalue_instr*, *mav_putvalue_src1*, *mav_putvalue_src2*, *mav_putvalue_src3* and sets 33-bit output *mav_putvalue* according to instruction.

The values are assigned to the input port using 
```
dut.mav_putvalue_instr.value = 01000000000100000110000010110011 // Sample Instruction
```

The print statement is used for showing the state at which model is failing, comparing the Bit Manipulator Coprocessor's output to the expected value.

The following error is seen:
```
	--ANDN 1
	Binary Function: 01000000000100000111000010110011
	Input 1: 00111011100111101000010011111011
	Input 2: 01101000110000100010111011111011
	Input 3: 00000100110010001000000101011010
	Expected Output: 0x26390001
	Output Got: 0x510409f7
	FAILED!!!
```
## Test Scenario 1
--ANDN 1
- Binary Function: 01000000000100000111000010110011
- Input 1: 00111011100111101000010011111011
- Input 2: 01101000110000100010111011111011
- Input 3: 00000100110010001000000101011010
- Expected Output: 0x26390001
- Output Got: 0x510409f7

Output mismatches for the above inputs proving that there is a design bug.

### Design Bug
Based on test bench output, we got that ``ANDN 1`` instruction is not producing expected output.

## Verification Strategy
We can study the design code to identify any commonly occuring fault. We can brute force each input combination to find the combination which is having fault for complex designs. If we look closely at the test bench script we can get idea of brut forcing. At first list of instructions needs to be made, if the list is too long, we need to find a pattern in them. Some portions of the instructions are fixed so that can be fixed for the whole test thus reducing time significantly. If we just change parts of instruction such a way that it covers all instructions we can find mmajor bugs. Input combination also needs to be shuffled to test properly, that's why we used random number generator to give random outputs.

## Is the verification complete ?
Ofcourse **NO**. There is no design which is 100% bug free. We can only take best action to test and prevent that. All types of test is not possible in this type of testing. There can be many hidden bugs which will only come into picture after hardware implementation and can be very tricky to reproduce and debug them.