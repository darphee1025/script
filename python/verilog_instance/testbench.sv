module wrapper();
reg   [1-1:0] aclk_0;
reg   [1-1:0] aresetn_0;
wire  [1-1:0] camera_rstn;
reg   [8-1:0] din_0;
reg   [1-1:0] en_capture_0;
reg   [1-1:0] href_0;
wire  [1-1:0] locked_0;
wire  [24-1:0] m_axis_video_0_tdata;
wire  [1-1:0] m_axis_video_0_tlast;
reg   [1-1:0] m_axis_video_0_tready;
wire  [1-1:0] m_axis_video_0_tuser;
wire  [1-1:0] m_axis_video_0_tvalid;
wire  [1-1:0] overflow_0;
reg   [1-1:0] pclk_0;
reg   [24-1:0] s_axis_video_0_tdata;
reg   [1-1:0] s_axis_video_0_tlast;
wire  [1-1:0] s_axis_video_0_tready;
reg   [1-1:0] s_axis_video_0_tuser;
reg   [1-1:0] s_axis_video_0_tvalid;
wire  [32-1:0] status_0;
wire  [1-1:0] underflow_0;
reg   [1-1:0] vga_clk;
wire  [1-1:0] vid_io_out_0_active_video;
wire  [24-1:0] vid_io_out_0_data;
wire  [1-1:0] vid_io_out_0_field;
wire  [1-1:0] vid_io_out_0_hblank;
wire  [1-1:0] vid_io_out_0_hsync;
wire  [1-1:0] vid_io_out_0_vblank;
wire  [1-1:0] vid_io_out_0_vsync;
reg   [1-1:0] vid_io_out_reset_0;
reg   [1-1:0] vsync_0;
reg   [9-1:0] vtc_ctrl_araddr;
wire  [1-1:0] vtc_ctrl_arready;
reg   [1-1:0] vtc_ctrl_arvalid;
reg   [9-1:0] vtc_ctrl_awaddr;
wire  [1-1:0] vtc_ctrl_awready;
reg   [1-1:0] vtc_ctrl_awvalid;
reg   [1-1:0] vtc_ctrl_bready;
wire  [2-1:0] vtc_ctrl_bresp;
wire  [1-1:0] vtc_ctrl_bvalid;
wire  [32-1:0] vtc_ctrl_rdata;
reg   [1-1:0] vtc_ctrl_rready;
wire  [2-1:0] vtc_ctrl_rresp;
wire  [1-1:0] vtc_ctrl_rvalid;
reg   [32-1:0] vtc_ctrl_wdata;
wire  [1-1:0] vtc_ctrl_wready;
reg   [4-1:0] vtc_ctrl_wstrb;
reg   [1-1:0] vtc_ctrl_wvalid;


video_system_wrapper inst_name
(
.aclk_0                        (aclk_0)                      ,//input          width:1
.aresetn_0                     (aresetn_0)                   ,//input          width:1
.camera_rstn                   (camera_rstn)                 ,//output         width:1
.din_0                         (din_0)                       ,//input          width:8
.en_capture_0                  (en_capture_0)                ,//input          width:1
.href_0                        (href_0)                      ,//input          width:1
.locked_0                      (locked_0)                    ,//output         width:1
.m_axis_video_0_tdata          (m_axis_video_0_tdata)        ,//output         width:24
.m_axis_video_0_tlast          (m_axis_video_0_tlast)        ,//output         width:1
.m_axis_video_0_tready         (m_axis_video_0_tready)       ,//input          width:1
.m_axis_video_0_tuser          (m_axis_video_0_tuser)        ,//output         width:1
.m_axis_video_0_tvalid         (m_axis_video_0_tvalid)       ,//output         width:1
.overflow_0                    (overflow_0)                  ,//output         width:1
.pclk_0                        (pclk_0)                      ,//input          width:1
.s_axis_video_0_tdata          (s_axis_video_0_tdata)        ,//input          width:24
.s_axis_video_0_tlast          (s_axis_video_0_tlast)        ,//input          width:1
.s_axis_video_0_tready         (s_axis_video_0_tready)       ,//output         width:1
.s_axis_video_0_tuser          (s_axis_video_0_tuser)        ,//input          width:1
.s_axis_video_0_tvalid         (s_axis_video_0_tvalid)       ,//input          width:1
.status_0                      (status_0)                    ,//output         width:32
.underflow_0                   (underflow_0)                 ,//output         width:1
.vga_clk                       (vga_clk)                     ,//input          width:1
.vid_io_out_0_active_video     (vid_io_out_0_active_video)   ,//output         width:1
.vid_io_out_0_data             (vid_io_out_0_data)           ,//output         width:24
.vid_io_out_0_field            (vid_io_out_0_field)          ,//output         width:1
.vid_io_out_0_hblank           (vid_io_out_0_hblank)         ,//output         width:1
.vid_io_out_0_hsync            (vid_io_out_0_hsync)          ,//output         width:1
.vid_io_out_0_vblank           (vid_io_out_0_vblank)         ,//output         width:1
.vid_io_out_0_vsync            (vid_io_out_0_vsync)          ,//output         width:1
.vid_io_out_reset_0            (vid_io_out_reset_0)          ,//input          width:1
.vsync_0                       (vsync_0)                     ,//input          width:1
.vtc_ctrl_araddr               (vtc_ctrl_araddr)             ,//input          width:9
.vtc_ctrl_arready              (vtc_ctrl_arready)            ,//output         width:1
.vtc_ctrl_arvalid              (vtc_ctrl_arvalid)            ,//input          width:1
.vtc_ctrl_awaddr               (vtc_ctrl_awaddr)             ,//input          width:9
.vtc_ctrl_awready              (vtc_ctrl_awready)            ,//output         width:1
.vtc_ctrl_awvalid              (vtc_ctrl_awvalid)            ,//input          width:1
.vtc_ctrl_bready               (vtc_ctrl_bready)             ,//input          width:1
.vtc_ctrl_bresp                (vtc_ctrl_bresp)              ,//output         width:2
.vtc_ctrl_bvalid               (vtc_ctrl_bvalid)             ,//output         width:1
.vtc_ctrl_rdata                (vtc_ctrl_rdata)              ,//output         width:32
.vtc_ctrl_rready               (vtc_ctrl_rready)             ,//input          width:1
.vtc_ctrl_rresp                (vtc_ctrl_rresp)              ,//output         width:2
.vtc_ctrl_rvalid               (vtc_ctrl_rvalid)             ,//output         width:1
.vtc_ctrl_wdata                (vtc_ctrl_wdata)              ,//input          width:32
.vtc_ctrl_wready               (vtc_ctrl_wready)             ,//output         width:1
.vtc_ctrl_wstrb                (vtc_ctrl_wstrb)              ,//input          width:4
.vtc_ctrl_wvalid               (vtc_ctrl_wvalid)             //input          width:1
);
endmodule

