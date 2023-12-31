module reg_rw #(
    parameter BITS_W    = 1'b1,
    parameter DEFAULT_V = 1'b0
) (
    input                       clk  ,
    input                       rst_n,
    input                       w_en , //1: to write
    input   [BITS_W-1:0]        w_dat, //write dat
    output  reg [BITS_W-1:0]    dout//1: to write
);

//reg     [BITS_W-1:0]    dout;
always@(posedge clk or negedge rst_n) begin
    if (~rst_n)
        dout <= DEFAULT_V;
    else begin
        if(w_en)
            dout <= w_dat;
        else;
    end
end
endmodule
