# Level 2 Design - Bit Manipulator Coprocessor Design Verification
-------
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![Verification Environment](/assets/)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Bit Manipulator Coprocessor Design Under Test which takes in 32-bit inputs *mav_putvalue_instr*, *mav_putvalue_src1*, *mav_putvalue_src2*, *mav_putvalue_src3* and sets 33-bit output *mav_putvalue* according to instruction.

The values are assigned to the input port using 
```
dut.mav_putvalue_instr.value = 1/0
```

The assert statement is used for comparing the Bit Manipulator Coprocessor's output to the expected value.

The following error is seen:
```
assert dut.seq_seen.value == 1, f"Seq Detector result is incorrect: {dut.seq_seen.value} != {1}"
```
## Test Scenario 1
- Test Inputs: inp_bit = 10111011,	clk = 10uS period clock,	reset = 1-0
- Expected Output: out = 11		====> 2 times 1011 detected
- Observed Output in the dut.out = 10	====> 1 time 1011 detected

Output mismatches for the above inputs proving that there is a design bug

### Design Bug
Based on the above test input and analysing the design, we see the following

```
	SEQ_1011:
	begin
		next_state = IDLE;	====> BUG, irrespective of input it's going to IDLE in next state
	end
```
For the multiplexer design, the logic should be 
```
	if(inp_bit == 1)
	  next_state = SEQ_1;
	else
	  next_state = IDLE;
```
instead of 
```
	next_state = IDLE;
``` 
as in the design code.

## Verification Strategy
We can study the design code to identify any commonly occuring fault. We found that for sequence 10111011, 101011, 11011 wrong output is coming. If we make state transition diagram we can get the fault. We can brute force each input combination to find the combination which is having fault for complex designs.

## Is the verification complete ?
Ofcourse **NO**. There is no design which is 100% bug free. We can only take best action to test and prevent that. All types of test is not possible in this type of testing. There can be many hidden bugs which will only come into picture after hardware implementation and can be very tricky to reproduce and debug them.