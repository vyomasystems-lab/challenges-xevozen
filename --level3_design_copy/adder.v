// See LICENSE.vyoma for more details

module adder(a, b, sum);

  input [3:0] a, b;
  output reg [4:0] sum;

  always @(a or b) 
  begin
    sum = a + b;
  end

endmodule : adder
