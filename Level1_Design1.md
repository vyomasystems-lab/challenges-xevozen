# Level 1 Design 1 - Mutiplexer Design Verification
-------
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![Verification Environment](/assets/lvl1-1.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Mux Design Under Test which takes in 5-bit input *sel* and individual 31 - 1-bit lines to pass input to output selecting based on *sel* and gives 1-bit output *out*.

The values are assigned to the input port using 
```
dut.sel.value = 12
dut.inp[x].value = 1
```

The assert statement is used for comparing the Multiplexer's outut to the expected value.

The following error is seen:
```
assert dut.out.value == inp[x], f"Mux result is incorrect: {dut.out.value} != {inp[x]}"
```
## Test Scenario 1
- Test Inputs: sel = 12,	inp12 = 1,	inp13 = 0
- Expected Output: out = 1
- Observed Output in the DUT dut.out = 0

Output mismatches for the above inputs proving that there is a design bug

### Design Bug
Based on the above test input and analysing the design, we see the following

```
	5'b01010: out = inp10;
	5'b01011: out = inp11;
	5'b01101: out = inp12;   ====> BUG
	5'b01101: out = inp13;
	5'b01110: out = inp14;
```
For the multiplexer design, the logic should be ``5'b01100: out = inp12;`` instead of ``5'b01101: out = inp12;`` as in the design code.

### Design Fix
Updating the design and re-running the test makes the test pass.
Updated design files is attached in level1_design1_fixed/mux.v .

## Test Scenario 2
- Test Inputs: sel = 12,	inp30 = 1
- Expected Output: out = 1
- Observed Output in the DUT dut.out = 0

Output mismatches for the above inputs proving that there is a design bug

### Design Bug
Based on the above test input and analysing the design, we see the following

```
	5'b11100: out = inp28;
	5'b11101: out = inp29;
							====> BUG
	default: out = 0;
```
For the multiplexer design, the logic should be ``5'b11110: out = inp30;`` which is missing in the design code.

### Design Fix
Updating the design and re-running the test makes the test pass.
Updated design files is attached in level1_design1_fixed/mux.v .


## Verification Strategy
Since, the design file is relatively easy and simple we can study the design code to identify any commonly occuring fault. We found that for sel 12 there is no switch case so missing output. Another bug was that inp30 was not defined in switch. We can brute force each input combination to find the combination which is having fault for complex designs.

## Is the verification complete ?
Ofcourse **NO**. There is no design which is 100% bug free. We can only take best action to test and prevent that. All types of test is not possible in this type of testing. There can be many hidden bugs which will only come into picture after hardware implementation and can be very tricky to reproduce and debug them.