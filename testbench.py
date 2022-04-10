import cocotb
from cocotb.triggers import Timer
from cocotb.triggers import RisingEdge
from cocotb.clock import Clock

@cocotb.test()




def my_first_test(dut):
    c = dut.clk
    feed = dut.feedback
    out = dut.out
    r = dut.rst
    #dut.feedback = ~(dut.out[3] ^ dut.out[2]);
    cocotb.fork(Clock(c, 10).start())
    
    r <= 1
    yield Timer(1, "ns")
    
    r <= 0
    yield Timer(1, "ns")
    #yield Timer(250)
    
    print("begin")
    
    
    
    
    
    
    
@cocotb.test()
def my_second_test(dut):
    c = dut.clk
    out = dut.out
    r = dut.rst
    #r <= 1
    #cocotb.fork(Clock(c, ).start())
    
    for i in range(1):
        feed = dut.feedback.value
        outer = dut.out.value
        #print(outer.binstr)
        #feed = ~(outer[3] ^ outer[2])
        
        r <= 1
        
        yield Timer(250)
        
        r <= 0
        #200
        yield Timer(250)
        #outer = (outer[2:0],feed)
    
    
    
    
    