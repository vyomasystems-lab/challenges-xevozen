# Level 2 Design - Full Subtractor Design Verification
-------
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![Verification Environment](/assets/)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Full Subtractor Design Under Test which takes in 1-bit inputs *A*, *B*, *Bin* and sets 1-bit outputs *D* and *Bout* according to instruction.

The values are assigned to the input port using 
```
	dut.A.value = 1/0
	dut.B.value = 1/0
	dut.Bin.value = 1/0
```

The assert statement is used for comparing the Full Subtractor's output to the expected value.

The following error is seen:
```
assert (dut.D.value == (dut.A.value^dut.B.value)^dut.Bin.value) and (dut.Bout.value == (dut.Bin.value and (not(dut.A.value))) or (not(dut.A.value) and dut.B.value)) , f"FullSubtractor result is incorrect: {dut.D.value} != {(dut.A.value^dut.B.value)^dut.Bin.value} or {dut.Bout.value} != {dut.Bin.value and (~(dut.A.value)) or (~dut.A.value and dut.B.value)}"
```
## Test Scenario 1
- Test Inputs: A = 1,	B = 1,	Bin = 1
- Expected Output: D = 1, Bout = 1
- Observed Output: D = 0, Bout = 1

Output mismatches for the above inputs proving that there is a design bug

### Design Bug
Based on the above test input and analysing the design, we see the following

```
	xor_gate u6(q, r, Bout);	====> BUG
```
For the multiplexer design, the logic should be 
```
	or_gate u6(q, r, Bout);
```
instead of 
```
	xor_gate u6(q, r, Bout);
``` 
as in the design code.

## Verification Strategy
We can study the design code to identify any commonly occuring fault. We found that for Inputs: A = 1,	B = 1,	Bin = 1 wrong output is coming. If we make state transition diagram we can get the fault. We can brute force each input combination to find the combination which is having fault for complex designs.

## Is the verification complete ?
Ofcourse **NO**. There can be many input combination for which output fails to produce correct output. There is no design which is 100% bug free. We can only take best action to test and prevent that. All types of test is not possible in this type of testing. There can be many hidden bugs which will only come into picture after hardware implementation and can be very tricky to reproduce and debug them.