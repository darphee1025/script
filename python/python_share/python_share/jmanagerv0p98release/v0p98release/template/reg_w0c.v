module reg_w0c #(
    parameter BITS_W    = 1'b1
) (
    input                       clk  ,
    input                       rst_n,
    input   [BITS_W-1:0]        trig , //1: to set reg , this is level sensitive
    input                       w_en , //1: to write
    input                       clr , //1: to write 0,
    input   [BITS_W-1:0]        w_dat, //write dat
    output  reg [BITS_W-1:0]    dout//1: to write
);

//reg     [BITS_W-1:0]    dout;
always@(posedge clk or negedge rst_n) begin
    if (~rst_n)
        dout <= 1'b0;
    else begin
        if(|trig)
            dout <= trig | dout ;
        else if(w_en)
            //dout <= {~w_dat} & dout ;
            dout <= w_dat & dout ;
        else if(clr)
            dout <= 1'b0;
    	else;
    end
end
endmodule
