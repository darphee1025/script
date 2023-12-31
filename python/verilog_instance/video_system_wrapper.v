/*************************************************************************
   > File Name: video_system_wrapper.v
   > Author: dafei.xiao
   > Mail: dafei.xiao@joulwatt.com
   > Created Time: Tue Jun 20 10:31:54 2023
 ************************************************************************/

`timescale 1 ps / 1 ps

module video_system_wrapper #(
    parameter UDLY = 1,
    parameter IDLE = 0
)
   (aclk_0,
    aresetn_0,
    camera_rstn,
    din_0,
    en_capture_0,
    href_0,
    locked_0,
    m_axis_video_0_tdata,
    m_axis_video_0_tlast,
    m_axis_video_0_tready,
    m_axis_video_0_tuser,
    m_axis_video_0_tvalid,
    overflow_0,
    pclk_0,
    s_axis_video_0_tdata,
    s_axis_video_0_tlast,
    s_axis_video_0_tready,
    s_axis_video_0_tuser,
    s_axis_video_0_tvalid,
    status_0,
    underflow_0,
    vga_clk,
    vid_io_out_0_active_video,
    vid_io_out_0_data,
    vid_io_out_0_field,
    vid_io_out_0_hblank,
    vid_io_out_0_hsync,
    vid_io_out_0_vblank,
    vid_io_out_0_vsync,
    vid_io_out_reset_0,
    vsync_0,
    vtc_ctrl_araddr,
    vtc_ctrl_arready,
    vtc_ctrl_arvalid,
    vtc_ctrl_awaddr,
    vtc_ctrl_awready,
    vtc_ctrl_awvalid,
    vtc_ctrl_bready,
    vtc_ctrl_bresp,
    vtc_ctrl_bvalid,
    vtc_ctrl_rdata,
    vtc_ctrl_rready,
    vtc_ctrl_rresp,
    vtc_ctrl_rvalid,
    vtc_ctrl_wdata,
    vtc_ctrl_wready,
    vtc_ctrl_wstrb,
    vtc_ctrl_wvalid);
  input aclk_0;
  input aresetn_0;
  output camera_rstn;
  input [7:0]din_0;
  input en_capture_0;
  input href_0;
  output locked_0;
  output [23:0]m_axis_video_0_tdata;
  output m_axis_video_0_tlast;
  input m_axis_video_0_tready;
  output m_axis_video_0_tuser;
  output m_axis_video_0_tvalid;
  output overflow_0;
  input pclk_0;
  input [23:0]s_axis_video_0_tdata;
  input s_axis_video_0_tlast;
  output s_axis_video_0_tready;
  input s_axis_video_0_tuser;
  input s_axis_video_0_tvalid;
  output [31:0]status_0;
  output underflow_0;
  input vga_clk;
  output vid_io_out_0_active_video;
  output [23:0]vid_io_out_0_data;
  output vid_io_out_0_field;
  output vid_io_out_0_hblank;
  output vid_io_out_0_hsync;
  output vid_io_out_0_vblank;
  output vid_io_out_0_vsync;
  input vid_io_out_reset_0;
  input vsync_0;
  input [8:0]vtc_ctrl_araddr;
  output vtc_ctrl_arready;
  input vtc_ctrl_arvalid;
  input [8:0]vtc_ctrl_awaddr;
  output vtc_ctrl_awready;
  input vtc_ctrl_awvalid;
  input vtc_ctrl_bready;
  output [1:0]vtc_ctrl_bresp;
  output vtc_ctrl_bvalid;
  output [31:0]vtc_ctrl_rdata;
  input vtc_ctrl_rready;
  output [1:0]vtc_ctrl_rresp;
  output vtc_ctrl_rvalid;
  input [31:0]vtc_ctrl_wdata;
  output vtc_ctrl_wready;
  input [3:0]vtc_ctrl_wstrb;
  input vtc_ctrl_wvalid;

  wire aclk_0;
  wire aresetn_0;
  wire camera_rstn;
  wire [7:0]din_0;
  wire en_capture_0;
  wire href_0;
  wire locked_0;
  wire [23:0]m_axis_video_0_tdata;
  wire m_axis_video_0_tlast;
  wire m_axis_video_0_tready;
  wire m_axis_video_0_tuser;
  wire m_axis_video_0_tvalid;
  wire overflow_0;
  wire pclk_0;
  wire [23:0]s_axis_video_0_tdata;
  wire s_axis_video_0_tlast;
  wire s_axis_video_0_tready;
  wire s_axis_video_0_tuser;
  wire s_axis_video_0_tvalid;
  wire [31:0]status_0;
  wire underflow_0;
  wire vga_clk;
  wire vid_io_out_0_active_video;
  wire [23:0]vid_io_out_0_data;
  wire vid_io_out_0_field;
  wire vid_io_out_0_hblank;
  wire vid_io_out_0_hsync;
  wire vid_io_out_0_vblank;
  wire vid_io_out_0_vsync;
  wire vid_io_out_reset_0;
  wire vsync_0;
  wire [8:0]vtc_ctrl_araddr;
  wire vtc_ctrl_arready;
  wire vtc_ctrl_arvalid;
  wire [8:0]vtc_ctrl_awaddr;
  wire vtc_ctrl_awready;
  wire vtc_ctrl_awvalid;
  wire vtc_ctrl_bready;
  wire [1:0]vtc_ctrl_bresp;
  wire vtc_ctrl_bvalid;
  wire [31:0]vtc_ctrl_rdata;
  wire vtc_ctrl_rready;
  wire [1:0]vtc_ctrl_rresp;
  wire vtc_ctrl_rvalid;
  wire [31:0]vtc_ctrl_wdata;
  wire vtc_ctrl_wready;
  wire [3:0]vtc_ctrl_wstrb;
  wire vtc_ctrl_wvalid;

  video_system video_system_i
       (.aclk_0(aclk_0),
        .aresetn_0(aresetn_0),
        .camera_rstn(camera_rstn),
        .din_0(din_0),
        .en_capture_0(en_capture_0),
        .href_0(href_0),
        .locked_0(locked_0),
        .m_axis_video_0_tdata(m_axis_video_0_tdata),
        .m_axis_video_0_tlast(m_axis_video_0_tlast),
        .m_axis_video_0_tready(m_axis_video_0_tready),
        .m_axis_video_0_tuser(m_axis_video_0_tuser),
        .m_axis_video_0_tvalid(m_axis_video_0_tvalid),
        .overflow_0(overflow_0),
        .pclk_0(pclk_0),
        .s_axis_video_0_tdata(s_axis_video_0_tdata),
        .s_axis_video_0_tlast(s_axis_video_0_tlast),
        .s_axis_video_0_tready(s_axis_video_0_tready),
        .s_axis_video_0_tuser(s_axis_video_0_tuser),
        .s_axis_video_0_tvalid(s_axis_video_0_tvalid),
        .status_0(status_0),
        .underflow_0(underflow_0),
        .vga_clk(vga_clk),
        .vid_io_out_0_active_video(vid_io_out_0_active_video),
        .vid_io_out_0_data(vid_io_out_0_data),
        .vid_io_out_0_field(vid_io_out_0_field),
        .vid_io_out_0_hblank(vid_io_out_0_hblank),
        .vid_io_out_0_hsync(vid_io_out_0_hsync),
        .vid_io_out_0_vblank(vid_io_out_0_vblank),
        .vid_io_out_0_vsync(vid_io_out_0_vsync),
        .vid_io_out_reset_0(vid_io_out_reset_0),
        .vsync_0(vsync_0),
        .vtc_ctrl_araddr(vtc_ctrl_araddr),
        .vtc_ctrl_arready(vtc_ctrl_arready),
        .vtc_ctrl_arvalid(vtc_ctrl_arvalid),
        .vtc_ctrl_awaddr(vtc_ctrl_awaddr),
        .vtc_ctrl_awready(vtc_ctrl_awready),
        .vtc_ctrl_awvalid(vtc_ctrl_awvalid),
        .vtc_ctrl_bready(vtc_ctrl_bready),
        .vtc_ctrl_bresp(vtc_ctrl_bresp),
        .vtc_ctrl_bvalid(vtc_ctrl_bvalid),
        .vtc_ctrl_rdata(vtc_ctrl_rdata),
        .vtc_ctrl_rready(vtc_ctrl_rready),
        .vtc_ctrl_rresp(vtc_ctrl_rresp),
        .vtc_ctrl_rvalid(vtc_ctrl_rvalid),
        .vtc_ctrl_wdata(vtc_ctrl_wdata),
        .vtc_ctrl_wready(vtc_ctrl_wready),
        .vtc_ctrl_wstrb(vtc_ctrl_wstrb),
        .vtc_ctrl_wvalid(vtc_ctrl_wvalid));
endmodule

video_system_wrapper.v
