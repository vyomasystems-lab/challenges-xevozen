// See LICENSE.vyoma for more details
module or_gate(a0, b0, c0);

input a0, b0;

output c0;

assign c0 = a0 | b0;

endmodule


module xor_gate(a1, b1, c1);

input a1, b1;

output c1;

assign c1 = a1 ^ b1;

endmodule


module and_gate(a2, b2, c2);

input a2, b2;

output c2;

assign c2 = a2 | b2;

endmodule


module not_gate(a3, b3);

input a3;

output b3;

assign b3 = ~ a3;

endmodule


module half_subtractor(a4, b4, c4, d4);

input a4, b4;

output c4, d4;

wire x;

xor_gate u1(a4, b4, c4);

and_gate u2(x, b4, d4);

not_gate u3(a4, x);

endmodule


module fullsubtractor(A, B, Bin, D, Bout);

input A, B, Bin;

output D, Bout;

wire p, q, r;

half_subtractor u4(A, B, p, q);

half_subtractor u5(p, Bin, D, r);

or_gate u6(q, r, Bout);

endmodule : fullsubtractor