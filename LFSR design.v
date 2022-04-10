// Code your design here
`timescale 1ns / 1ps
module lfsr (out, clk, rst);

  output reg [3:0] out;
  input [3:0] in;
  input clk, rst;

  wire feedback;
  

  assign feedback = (out[3] ^ out[2]);
  //in ^= feedback;
  
  

  always @(posedge clk, posedge rst)
  begin
    if (rst)
      out = 4'b1;
    else
      
      out = {out[2:0],feedback};
      
  end
initial 
  begin
    $dumpfile("dump.vcd");
    $dumpvars(1, lfsr);
    
    #1000 $finish;
  end
endmodule