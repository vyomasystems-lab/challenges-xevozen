# Level 1 Design 2 - 1011 Sequence Detector Design Verification
-------
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![Verification Environment](/assets/lvl1-2.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the 1011 Sequence Detector Design Under Test which takes in 1-bit input *inp_bit*, *clk* and *reset* lines and sets 1-bit output *seq_seen* to 1 according to input sequence.

The values are assigned to the input port using 
```
dut.inp_bit.value = 1/0
```

The assert statement is used for comparing the 1011 Sequence Detector's outut to the expected value.

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

### Design Fix
Updating the design and re-running the test makes the test pass.
Updated design files is attached in level1_design2_fixed/seq_detect_1011.v .

## Test Scenario 2
- Test Inputs: inp_bit = 101011,	clk = 10uS period clock,	reset = 1-0
- Expected Output: out = 1		====> 1 time 1011 detected
- Observed Output in the dut.out = 0	====> 0 time 1011 detected

Output mismatches for the above inputs proving that there is a design bug

### Design Bug
Based on the above test input and analysing the design, we see the following

```
	SEQ_101:
	begin
	if(inp_bit == 1)
	  next_state = SEQ_1011;
	else
	  next_state = IDLE;	====> BUG, If input 0 it's going to IDLE in next state
	end
```
For the multiplexer design, the logic should be 
```
	next_state = SEQ_10;
```
instead of 
```
	next_state = IDLE;
``` 
as in the design code.

## Test Scenario 3
- Test Inputs: inp_bit = 11011,	clk = 10uS period clock,	reset = 1-0
- Expected Output: out = 1		====> 1 time 1011 detected
- Observed Output in the dut.out = 0	====> 0 time 1011 detected

Output mismatches for the above inputs proving that there is a design bug

### Design Bug
Based on the above test input and analysing the design, we see the following

```
	SEQ_1:
	begin
	if(inp_bit == 1)
	  next_state = IDLE;	====> BUG, If input 1 it's going to IDLE in next state
	else
	  next_state = SEQ_10;
	end
```
For the multiplexer design, the logic should be 
```
	next_state = SEQ_1;
```
instead of 
```
	next_state = IDLE;
``` 
as in the design code.

### Design Fix
Updating the design and re-running the test makes the test pass.
Updated design files is attached in level1_design2_fixed/seq_detect_1011.v .


## Verification Strategy
We can study the design code to identify any commonly occuring fault. We found that for sequence 10111011, 101011, 11011 wrong output is coming. If we make state transition diagram we can get the fault. We can brute force each input combination to find the combination which is having fault for complex designs.

## Is the verification complete ?
Ofcourse **NO**. There is no design which is 100% bug free. We can only take best action to test and prevent that. All types of test is not possible in this type of testing. There can be many hidden bugs which will only come into picture after hardware implementation and can be very tricky to reproduce and debug them.