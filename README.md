# egldockertest

This repository is part of my attempts to debug my failure run an OpenGL ELG surfaceless program on GPU compute when running in GPU hosts Runpod and Replicate. I'm publishing this to use as a reference for the various people I'm asking for help. :) Apologies if I use OpenGL terminology incorrectly here, I'm pretty new to this.

The overall status is:

- ✅ When running directly on my host machine (Linux with 3090) with no display, the program successfully runs on headlessly on GPU.
- ✅ When running inside a docker container on my machine, the program successfully runs on headlessly on GPU.
- ✅ When following Runpod and Replicate's documentation to test locally, the program successfully runs on headlessly on GPU.
- ❌ When deployed to Replicate, the program falls back to using software rendering (CPU).
- ❌ When deployed to Runpod, the program falls back to using software rendering (CPU).

A minimal testcase is simply to run the utility `eglinfo` (provided by package `mesa-utils`), whose output describes whether the system can run egl workloads successfully.
The output of `eglinfo` is notably different in the working and failing scenarios.

So, something about way the GPU is exposed to the docker container is different on my system versus on the GPU hosts. However, at this stage I don't know what that could be, or whether it is fixable. Any help welcome!


- The docker image I'm testing with is available here: https://hub.docker.com/repository/docker/rewbs/egldockertest/general
- The deployed Replicate API is public: https://replicate.com/rewbs/egldockertest


## Example outputs

Note how the in the good cases, the info for `Device platform:` and `GBM platform:` look healthy, but not in the failing cases.

### Host (good case)

```
-➜  egldockertest git:(main) ✗ eglinfo

EGL client extensions string:
    EGL_EXT_platform_base EGL_EXT_device_base EGL_EXT_device_enumeration
    EGL_EXT_device_query EGL_KHR_client_get_all_proc_addresses
    EGL_EXT_client_extensions EGL_KHR_debug EGL_KHR_platform_x11
    EGL_EXT_platform_x11 EGL_EXT_platform_device
    EGL_MESA_platform_surfaceless EGL_EXT_explicit_device
    EGL_KHR_platform_wayland EGL_EXT_platform_wayland
    EGL_KHR_platform_gbm EGL_MESA_platform_gbm EGL_EXT_platform_xcb

GBM platform:
EGL API version: 1.5
EGL vendor string: NVIDIA
EGL version string: 1.5
EGL client APIs: OpenGL_ES OpenGL
EGL extensions string:
    EGL_ANDROID_native_fence_sync EGL_EXT_buffer_age EGL_EXT_client_sync
    EGL_EXT_create_context_robustness EGL_EXT_image_dma_buf_import
    EGL_EXT_image_dma_buf_import_modifiers EGL_MESA_image_dma_buf_export
    EGL_EXT_output_base EGL_EXT_output_drm EGL_EXT_protected_content
    EGL_EXT_stream_consumer_egloutput EGL_EXT_stream_acquire_mode
    EGL_EXT_sync_reuse EGL_IMG_context_priority EGL_KHR_config_attribs
    EGL_KHR_create_context_no_error EGL_KHR_context_flush_control
    EGL_KHR_create_context EGL_KHR_fence_sync
    EGL_KHR_get_all_proc_addresses EGL_KHR_partial_update
    EGL_KHR_swap_buffers_with_damage EGL_KHR_no_config_context
    EGL_KHR_gl_colorspace EGL_KHR_gl_renderbuffer_image
    EGL_KHR_gl_texture_2D_image EGL_KHR_gl_texture_3D_image
    EGL_KHR_gl_texture_cubemap_image EGL_KHR_image EGL_KHR_image_base
    EGL_KHR_reusable_sync EGL_KHR_stream EGL_KHR_stream_attrib
    EGL_KHR_stream_consumer_gltexture EGL_KHR_stream_cross_process_fd
    EGL_KHR_stream_fifo EGL_KHR_stream_producer_eglsurface
    EGL_KHR_surfaceless_context EGL_KHR_wait_sync EGL_NV_nvrm_fence_sync
    EGL_NV_quadruple_buffer EGL_NV_stream_consumer_eglimage
    EGL_NV_stream_cross_display EGL_NV_stream_cross_object
    EGL_NV_stream_cross_process EGL_NV_stream_cross_system
    EGL_NV_stream_dma EGL_NV_stream_flush EGL_NV_stream_metadata
    EGL_NV_stream_remote EGL_NV_stream_reset EGL_NV_stream_socket
    EGL_NV_stream_socket_inet EGL_NV_stream_socket_unix
    EGL_NV_stream_sync EGL_NV_stream_fifo_next
    EGL_NV_stream_fifo_synchronous EGL_NV_stream_consumer_gltexture_yuv
    EGL_NV_stream_attrib EGL_NV_stream_origin EGL_NV_system_time
    EGL_NV_output_drm_flip_event EGL_NV_triple_buffer
    EGL_NV_robustness_video_memory_purge EGL_WL_bind_wayland_display
    EGL_WL_wayland_eglstream
Configurations:
     bf lv colorbuffer dp st  ms    vis   cav bi  renderable  supported
  id sz  l  r  g  b  a th cl ns b    id   eat nd gl es es2 vg surfaces
---------------------------------------------------------------------
0x01 32  0  8  8  8  8 24  8  0 0 0x34325241--         y  y  y     win,pb,str
0x02 32  0  8  8  8  8 24  0  0 0 0x34325241--         y  y  y     win,pb,str
0x03 32  0  8  8  8  8  0  8  0 0 0x34325241--         y  y  y     win,pb,str
0x04 32  0  8  8  8  8  0  0  0 0 0x34325241--         y  y  y     win,pb,str
0x05 32  0  8  8  8  8 24  8  2 1 0x34325241--         y  y  y     win,pb,str
0x06 32  0  8  8  8  8 24  0  2 1 0x34325241--         y  y  y     win,pb,str
0x07 32  0  8  8  8  8  0  8  2 1 0x34325241--         y  y  y     win,pb,str
0x08 32  0  8  8  8  8  0  0  2 1 0x34325241--         y  y  y     win,pb,str
0x09 32  0  8  8  8  8 24  8  4 1 0x34325241--         y  y  y     win,pb,str
0x0a 32  0  8  8  8  8 24  8  4 1 0x34325241--         y  y  y     win,pb,str
0x0b 32  0  8  8  8  8 24  0  4 1 0x34325241--         y  y  y     win,pb,str
0x0c 32  0  8  8  8  8 24  0  4 1 0x34325241--         y  y  y     win,pb,str
0x0d 32  0  8  8  8  8  0  8  4 1 0x34325241--         y  y  y     win,pb,str
0x0e 32  0  8  8  8  8  0  8  4 1 0x34325241--         y  y  y     win,pb,str
0x0f 32  0  8  8  8  8  0  0  4 1 0x34325241--         y  y  y     win,pb,str
0x10 32  0  8  8  8  8  0  0  4 1 0x34325241--         y  y  y     win,pb,str
0x11 32  0  8  8  8  8 24  8  8 1 0x34325241--         y  y  y     win,pb,str
0x12 32  0  8  8  8  8 24  0  8 1 0x34325241--         y  y  y     win,pb,str
0x13 32  0  8  8  8  8  0  8  8 1 0x34325241--         y  y  y     win,pb,str
0x14 32  0  8  8  8  8  0  0  8 1 0x34325241--         y  y  y     win,pb,str
0x15 24  0  8  8  8  0 24  8  0 0 0x34325258--         y  y  y     win,pb,str
0x16 24  0  8  8  8  0 24  0  0 0 0x34325258--         y  y  y     win,pb,str
0x17 24  0  8  8  8  0  0  8  0 0 0x34325258--         y  y  y     win,pb,str
0x18 24  0  8  8  8  0  0  0  0 0 0x34325258--         y  y  y     win,pb,str
0x19 24  0  8  8  8  0 24  8  2 1 0x34325258--         y  y  y     win,pb,str
0x1a 24  0  8  8  8  0 24  0  2 1 0x34325258--         y  y  y     win,pb,str
0x1b 24  0  8  8  8  0  0  8  2 1 0x34325258--         y  y  y     win,pb,str
0x1c 24  0  8  8  8  0  0  0  2 1 0x34325258--         y  y  y     win,pb,str
0x1d 24  0  8  8  8  0 24  8  4 1 0x34325258--         y  y  y     win,pb,str
0x1e 24  0  8  8  8  0 24  8  4 1 0x34325258--         y  y  y     win,pb,str
0x1f 24  0  8  8  8  0 24  0  4 1 0x34325258--         y  y  y     win,pb,str
0x20 24  0  8  8  8  0 24  0  4 1 0x34325258--         y  y  y     win,pb,str
0x21 24  0  8  8  8  0  0  8  4 1 0x34325258--         y  y  y     win,pb,str
0x22 24  0  8  8  8  0  0  8  4 1 0x34325258--         y  y  y     win,pb,str
0x23 24  0  8  8  8  0  0  0  4 1 0x34325258--         y  y  y     win,pb,str
0x24 24  0  8  8  8  0  0  0  4 1 0x34325258--         y  y  y     win,pb,str
0x25 24  0  8  8  8  0 24  8  8 1 0x34325258--         y  y  y     win,pb,str
0x26 24  0  8  8  8  0 24  0  8 1 0x34325258--         y  y  y     win,pb,str
0x27 24  0  8  8  8  0  0  8  8 1 0x34325258--         y  y  y     win,pb,str
0x28 24  0  8  8  8  0  0  0  8 1 0x34325258--         y  y  y     win,pb,str
0x29 16  0  5  6  5  0 24  8  0 0 0x36314752--         y  y  y     win,pb,str
0x2a 16  0  5  6  5  0 24  0  0 0 0x36314752--         y  y  y     win,pb,str
0x2b 16  0  5  6  5  0 16  0  0 0 0x36314752--         y  y  y     win,pb,str
0x2c 16  0  5  6  5  0  0  8  0 0 0x36314752--         y  y  y     win,pb,str
0x2d 16  0  5  6  5  0  0  0  0 0 0x36314752--         y  y  y     win,pb,str
0x2e 16  0  5  6  5  0 24  8  2 1 0x36314752--         y  y  y     win,pb,str
0x2f 16  0  5  6  5  0 24  0  2 1 0x36314752--         y  y  y     win,pb,str
0x30 16  0  5  6  5  0 16  0  2 1 0x36314752--         y  y  y     win,pb,str
0x31 16  0  5  6  5  0  0  8  2 1 0x36314752--         y  y  y     win,pb,str
0x32 16  0  5  6  5  0  0  0  2 1 0x36314752--         y  y  y     win,pb,str
0x33 16  0  5  6  5  0 24  8  4 1 0x36314752--         y  y  y     win,pb,str
0x34 16  0  5  6  5  0 24  8  4 1 0x36314752--         y  y  y     win,pb,str
0x35 16  0  5  6  5  0 24  0  4 1 0x36314752--         y  y  y     win,pb,str
0x36 16  0  5  6  5  0 24  0  4 1 0x36314752--         y  y  y     win,pb,str
0x37 16  0  5  6  5  0 16  0  4 1 0x36314752--         y  y  y     win,pb,str
0x38 16  0  5  6  5  0 16  0  4 1 0x36314752--         y  y  y     win,pb,str
0x39 16  0  5  6  5  0  0  8  4 1 0x36314752--         y  y  y     win,pb,str
0x3a 16  0  5  6  5  0  0  8  4 1 0x36314752--         y  y  y     win,pb,str
0x3b 16  0  5  6  5  0  0  0  4 1 0x36314752--         y  y  y     win,pb,str
0x3c 16  0  5  6  5  0  0  0  4 1 0x36314752--         y  y  y     win,pb,str
0x3d 16  0  5  6  5  0 24  8  8 1 0x36314752--         y  y  y     win,pb,str
0x3e 16  0  5  6  5  0 24  0  8 1 0x36314752--         y  y  y     win,pb,str
0x3f 16  0  5  6  5  0 16  0  8 1 0x36314752--         y  y  y     win,pb,str
0x40 16  0  5  6  5  0  0  8  8 1 0x36314752--         y  y  y     win,pb,str
0x41 16  0  5  6  5  0  0  0  8 1 0x36314752--         y  y  y     win,pb,str

Wayland platform:
eglinfo: eglInitialize failed

X11 platform:
eglinfo: eglInitialize failed

Device platform:
EGL API version: 1.5
EGL vendor string: NVIDIA
EGL version string: 1.5
EGL client APIs: OpenGL_ES OpenGL
EGL extensions string:
    EGL_ANDROID_native_fence_sync EGL_EXT_buffer_age EGL_EXT_client_sync
    EGL_EXT_create_context_robustness EGL_EXT_image_dma_buf_import
    EGL_EXT_image_dma_buf_import_modifiers EGL_MESA_image_dma_buf_export
    EGL_EXT_output_base EGL_EXT_output_drm EGL_EXT_protected_content
    EGL_EXT_stream_consumer_egloutput EGL_EXT_stream_acquire_mode
    EGL_EXT_sync_reuse EGL_IMG_context_priority EGL_KHR_config_attribs
    EGL_KHR_create_context_no_error EGL_KHR_context_flush_control
    EGL_KHR_create_context EGL_KHR_fence_sync
    EGL_KHR_get_all_proc_addresses EGL_KHR_partial_update
    EGL_KHR_swap_buffers_with_damage EGL_KHR_no_config_context
    EGL_KHR_gl_colorspace EGL_KHR_gl_renderbuffer_image
    EGL_KHR_gl_texture_2D_image EGL_KHR_gl_texture_3D_image
    EGL_KHR_gl_texture_cubemap_image EGL_KHR_image EGL_KHR_image_base
    EGL_KHR_reusable_sync EGL_KHR_stream EGL_KHR_stream_attrib
    EGL_KHR_stream_consumer_gltexture EGL_KHR_stream_cross_process_fd
    EGL_KHR_stream_fifo EGL_KHR_stream_producer_eglsurface
    EGL_KHR_surfaceless_context EGL_KHR_wait_sync EGL_NV_nvrm_fence_sync
    EGL_NV_quadruple_buffer EGL_NV_stream_consumer_eglimage
    EGL_NV_stream_cross_display EGL_NV_stream_cross_object
    EGL_NV_stream_cross_process EGL_NV_stream_cross_system
    EGL_NV_stream_dma EGL_NV_stream_flush EGL_NV_stream_metadata
    EGL_NV_stream_remote EGL_NV_stream_reset EGL_NV_stream_socket
    EGL_NV_stream_socket_inet EGL_NV_stream_socket_unix
    EGL_NV_stream_sync EGL_NV_stream_fifo_next
    EGL_NV_stream_fifo_synchronous EGL_NV_stream_consumer_gltexture_yuv
    EGL_NV_stream_attrib EGL_NV_stream_origin EGL_NV_system_time
    EGL_NV_output_drm_flip_event EGL_NV_triple_buffer
    EGL_NV_robustness_video_memory_purge EGL_WL_bind_wayland_display
    EGL_WL_wayland_eglstream
Configurations:
     bf lv colorbuffer dp st  ms    vis   cav bi  renderable  supported
  id sz  l  r  g  b  a th cl ns b    id   eat nd gl es es2 vg surfaces
---------------------------------------------------------------------
0x01 32  0  8  8  8  8 24  8  0 0 0x00--         y  y  y     pb,str
0x02 32  0  8  8  8  8 24  0  0 0 0x00--         y  y  y     pb,str
0x03 32  0  8  8  8  8  0  8  0 0 0x00--         y  y  y     pb,str
0x04 32  0  8  8  8  8  0  0  0 0 0x00--         y  y  y     pb,str
0x05 32  0  8  8  8  8 24  8  2 1 0x00--         y  y  y     pb,str
0x06 32  0  8  8  8  8 24  0  2 1 0x00--         y  y  y     pb,str
0x07 32  0  8  8  8  8  0  8  2 1 0x00--         y  y  y     pb,str
0x08 32  0  8  8  8  8  0  0  2 1 0x00--         y  y  y     pb,str
0x09 32  0  8  8  8  8 24  8  4 1 0x00--         y  y  y     pb,str
0x0a 32  0  8  8  8  8 24  8  4 1 0x00--         y  y  y     pb,str
0x0b 32  0  8  8  8  8 24  0  4 1 0x00--         y  y  y     pb,str
0x0c 32  0  8  8  8  8 24  0  4 1 0x00--         y  y  y     pb,str
0x0d 32  0  8  8  8  8  0  8  4 1 0x00--         y  y  y     pb,str
0x0e 32  0  8  8  8  8  0  8  4 1 0x00--         y  y  y     pb,str
0x0f 32  0  8  8  8  8  0  0  4 1 0x00--         y  y  y     pb,str
0x10 32  0  8  8  8  8  0  0  4 1 0x00--         y  y  y     pb,str
0x11 32  0  8  8  8  8 24  8  8 1 0x00--         y  y  y     pb,str
0x12 32  0  8  8  8  8 24  0  8 1 0x00--         y  y  y     pb,str
0x13 32  0  8  8  8  8  0  8  8 1 0x00--         y  y  y     pb,str
0x14 32  0  8  8  8  8  0  0  8 1 0x00--         y  y  y     pb,str
0x15 24  0  8  8  8  0 24  8  0 0 0x00--         y  y  y     pb,str
0x16 24  0  8  8  8  0 24  0  0 0 0x00--         y  y  y     pb,str
0x17 24  0  8  8  8  0  0  8  0 0 0x00--         y  y  y     pb,str
0x18 24  0  8  8  8  0  0  0  0 0 0x00--         y  y  y     pb,str
0x19 24  0  8  8  8  0 24  8  2 1 0x00--         y  y  y     pb,str
0x1a 24  0  8  8  8  0 24  0  2 1 0x00--         y  y  y     pb,str
0x1b 24  0  8  8  8  0  0  8  2 1 0x00--         y  y  y     pb,str
0x1c 24  0  8  8  8  0  0  0  2 1 0x00--         y  y  y     pb,str
0x1d 24  0  8  8  8  0 24  8  4 1 0x00--         y  y  y     pb,str
0x1e 24  0  8  8  8  0 24  8  4 1 0x00--         y  y  y     pb,str
0x1f 24  0  8  8  8  0 24  0  4 1 0x00--         y  y  y     pb,str
0x20 24  0  8  8  8  0 24  0  4 1 0x00--         y  y  y     pb,str
0x21 24  0  8  8  8  0  0  8  4 1 0x00--         y  y  y     pb,str
0x22 24  0  8  8  8  0  0  8  4 1 0x00--         y  y  y     pb,str
0x23 24  0  8  8  8  0  0  0  4 1 0x00--         y  y  y     pb,str
0x24 24  0  8  8  8  0  0  0  4 1 0x00--         y  y  y     pb,str
0x25 24  0  8  8  8  0 24  8  8 1 0x00--         y  y  y     pb,str
0x26 24  0  8  8  8  0 24  0  8 1 0x00--         y  y  y     pb,str
0x27 24  0  8  8  8  0  0  8  8 1 0x00--         y  y  y     pb,str
0x28 24  0  8  8  8  0  0  0  8 1 0x00--         y  y  y     pb,str
0x29 16  0  5  6  5  0 24  8  0 0 0x00--         y  y  y     pb,str
0x2a 16  0  5  6  5  0 24  0  0 0 0x00--         y  y  y     pb,str
0x2b 16  0  5  6  5  0 16  0  0 0 0x00--         y  y  y     pb,str
0x2c 16  0  5  6  5  0  0  8  0 0 0x00--         y  y  y     pb,str
0x2d 16  0  5  6  5  0  0  0  0 0 0x00--         y  y  y     pb,str
0x2e 16  0  5  6  5  0 24  8  2 1 0x00--         y  y  y     pb,str
0x2f 16  0  5  6  5  0 24  0  2 1 0x00--         y  y  y     pb,str
0x30 16  0  5  6  5  0 16  0  2 1 0x00--         y  y  y     pb,str
0x31 16  0  5  6  5  0  0  8  2 1 0x00--         y  y  y     pb,str
0x32 16  0  5  6  5  0  0  0  2 1 0x00--         y  y  y     pb,str
0x33 16  0  5  6  5  0 24  8  4 1 0x00--         y  y  y     pb,str
0x34 16  0  5  6  5  0 24  8  4 1 0x00--         y  y  y     pb,str
0x35 16  0  5  6  5  0 24  0  4 1 0x00--         y  y  y     pb,str
0x36 16  0  5  6  5  0 24  0  4 1 0x00--         y  y  y     pb,str
0x37 16  0  5  6  5  0 16  0  4 1 0x00--         y  y  y     pb,str
0x38 16  0  5  6  5  0 16  0  4 1 0x00--         y  y  y     pb,str
0x39 16  0  5  6  5  0  0  8  4 1 0x00--         y  y  y     pb,str
0x3a 16  0  5  6  5  0  0  8  4 1 0x00--         y  y  y     pb,str
0x3b 16  0  5  6  5  0  0  0  4 1 0x00--         y  y  y     pb,str
0x3c 16  0  5  6  5  0  0  0  4 1 0x00--         y  y  y     pb,str
0x3d 16  0  5  6  5  0 24  8  8 1 0x00--         y  y  y     pb,str
0x3e 16  0  5  6  5  0 24  0  8 1 0x00--         y  y  y     pb,str
0x3f 16  0  5  6  5  0 16  0  8 1 0x00--         y  y  y     pb,str
0x40 16  0  5  6  5  0  0  8  8 1 0x00--         y  y  y     pb,str
0x41 16  0  5  6  5  0  0  0  8 1 0x00--         y  y  y     pb,str
```



### Docker (good case)

```
-➜  egldockertest git:(main) ✗ sudo docker build . -t egldockertest:0.0.0 && sudo docker run -it --gpus all --rm -it --entrypoint eglinfo egldockertest:0.0.0
[+] Building 1.0s (10/10) FINISHED                                                                                                                                                                                     docker:default
 => [internal] load build definition from Dockerfile                                                                                                                                                                             0.0s
 => => transferring dockerfile: 582B                                                                                                                                                                                             0.0s
 => [internal] load metadata for docker.io/nvidia/cuda:12.3.2-cudnn9-devel-ubuntu22.04                                                                                                                                           0.8s
 => [internal] load .dockerignore                                                                                                                                                                                                0.0s
 => => transferring context: 2B                                                                                                                                                                                                  0.0s
 => [1/5] FROM docker.io/nvidia/cuda:12.3.2-cudnn9-devel-ubuntu22.04@sha256:fb1ad20f2552f5b3aafb2c9c478ed57da95e2bb027d15218d7a55b3a0e4b4413                                                                                     0.0s
 => [internal] load build context                                                                                                                                                                                                0.0s
 => => transferring context: 37B                                                                                                                                                                                                 0.0s
 => CACHED [2/5] RUN apt-get update &&      apt-get install --no-install-recommends -y         mesa-utils         python3         python3-pip      && rm -rf /var/lib/apt/lists/*                                                0.0s
 => CACHED [3/5] COPY ./requirements.txt /requirements.txt                                                                                                                                                                       0.0s
 => CACHED [4/5] RUN pip install --no-cache-dir -r /requirements.txt                                                                                                                                                             0.0s
 => CACHED [5/5] WORKDIR /app                                                                                                                                                                                                    0.0s
 => exporting to image                                                                                                                                                                                                           0.0s
 => => exporting layers                                                                                                                                                                                                          0.0s
 => => writing image sha256:79bbe52213695787ee8dcd0a857e07879205f00863fe507abfc2cc245539c25d                                                                                                                                     0.0s
 => => naming to docker.io/library/egldockertest:0.0.0                                                                                                                                                                           0.0s
EGL client extensions string:
    EGL_EXT_platform_base EGL_EXT_device_base EGL_EXT_device_enumeration
    EGL_EXT_device_query EGL_KHR_client_get_all_proc_addresses
    EGL_EXT_client_extensions EGL_KHR_debug EGL_KHR_platform_x11
    EGL_EXT_platform_x11 EGL_EXT_platform_device
    EGL_MESA_platform_surfaceless EGL_EXT_explicit_device
    EGL_KHR_platform_gbm EGL_MESA_platform_gbm EGL_EXT_platform_wayland
    EGL_KHR_platform_wayland EGL_EXT_platform_xcb

GBM platform:
EGL API version: 1.5
EGL vendor string: NVIDIA
EGL version string: 1.5
EGL client APIs: OpenGL_ES OpenGL
EGL extensions string:
    EGL_ANDROID_native_fence_sync EGL_EXT_buffer_age EGL_EXT_client_sync
    EGL_EXT_create_context_robustness EGL_EXT_image_dma_buf_import
    EGL_EXT_image_dma_buf_import_modifiers EGL_MESA_image_dma_buf_export
    EGL_EXT_output_base EGL_EXT_output_drm EGL_EXT_protected_content
    EGL_EXT_stream_consumer_egloutput EGL_EXT_stream_acquire_mode
    EGL_EXT_sync_reuse EGL_IMG_context_priority EGL_KHR_config_attribs
    EGL_KHR_create_context_no_error EGL_KHR_context_flush_control
    EGL_KHR_create_context EGL_KHR_fence_sync
    EGL_KHR_get_all_proc_addresses EGL_KHR_partial_update
    EGL_KHR_swap_buffers_with_damage EGL_KHR_no_config_context
    EGL_KHR_gl_colorspace EGL_KHR_gl_renderbuffer_image
    EGL_KHR_gl_texture_2D_image EGL_KHR_gl_texture_3D_image
    EGL_KHR_gl_texture_cubemap_image EGL_KHR_image EGL_KHR_image_base
    EGL_KHR_reusable_sync EGL_KHR_stream EGL_KHR_stream_attrib
    EGL_KHR_stream_consumer_gltexture EGL_KHR_stream_cross_process_fd
    EGL_KHR_stream_fifo EGL_KHR_stream_producer_eglsurface
    EGL_KHR_surfaceless_context EGL_KHR_wait_sync EGL_NV_nvrm_fence_sync
    EGL_NV_quadruple_buffer EGL_NV_stream_consumer_eglimage
    EGL_NV_stream_cross_display EGL_NV_stream_cross_object
    EGL_NV_stream_cross_process EGL_NV_stream_cross_system
    EGL_NV_stream_dma EGL_NV_stream_flush EGL_NV_stream_metadata
    EGL_NV_stream_remote EGL_NV_stream_reset EGL_NV_stream_socket
    EGL_NV_stream_socket_inet EGL_NV_stream_socket_unix
    EGL_NV_stream_sync EGL_NV_stream_fifo_next
    EGL_NV_stream_fifo_synchronous EGL_NV_stream_consumer_gltexture_yuv
    EGL_NV_stream_attrib EGL_NV_stream_origin EGL_NV_system_time
    EGL_NV_output_drm_flip_event EGL_NV_triple_buffer
    EGL_NV_robustness_video_memory_purge
Configurations:
     bf lv colorbuffer dp st  ms    vis   cav bi  renderable  supported
  id sz  l  r  g  b  a th cl ns b    id   eat nd gl es es2 vg surfaces
---------------------------------------------------------------------
0x01 32  0  8  8  8  8 24  8  0 0 0x34325241--         y  y  y     win,pb,str
0x02 32  0  8  8  8  8 24  0  0 0 0x34325241--         y  y  y     win,pb,str
0x03 32  0  8  8  8  8  0  8  0 0 0x34325241--         y  y  y     win,pb,str
0x04 32  0  8  8  8  8  0  0  0 0 0x34325241--         y  y  y     win,pb,str
0x05 32  0  8  8  8  8 24  8  2 1 0x34325241--         y  y  y     win,pb,str
0x06 32  0  8  8  8  8 24  0  2 1 0x34325241--         y  y  y     win,pb,str
0x07 32  0  8  8  8  8  0  8  2 1 0x34325241--         y  y  y     win,pb,str
0x08 32  0  8  8  8  8  0  0  2 1 0x34325241--         y  y  y     win,pb,str
0x09 32  0  8  8  8  8 24  8  4 1 0x34325241--         y  y  y     win,pb,str
0x0a 32  0  8  8  8  8 24  8  4 1 0x34325241--         y  y  y     win,pb,str
0x0b 32  0  8  8  8  8 24  0  4 1 0x34325241--         y  y  y     win,pb,str
0x0c 32  0  8  8  8  8 24  0  4 1 0x34325241--         y  y  y     win,pb,str
0x0d 32  0  8  8  8  8  0  8  4 1 0x34325241--         y  y  y     win,pb,str
0x0e 32  0  8  8  8  8  0  8  4 1 0x34325241--         y  y  y     win,pb,str
0x0f 32  0  8  8  8  8  0  0  4 1 0x34325241--         y  y  y     win,pb,str
0x10 32  0  8  8  8  8  0  0  4 1 0x34325241--         y  y  y     win,pb,str
0x11 32  0  8  8  8  8 24  8  8 1 0x34325241--         y  y  y     win,pb,str
0x12 32  0  8  8  8  8 24  0  8 1 0x34325241--         y  y  y     win,pb,str
0x13 32  0  8  8  8  8  0  8  8 1 0x34325241--         y  y  y     win,pb,str
0x14 32  0  8  8  8  8  0  0  8 1 0x34325241--         y  y  y     win,pb,str
0x15 24  0  8  8  8  0 24  8  0 0 0x34325258--         y  y  y     win,pb,str
0x16 24  0  8  8  8  0 24  0  0 0 0x34325258--         y  y  y     win,pb,str
0x17 24  0  8  8  8  0  0  8  0 0 0x34325258--         y  y  y     win,pb,str
0x18 24  0  8  8  8  0  0  0  0 0 0x34325258--         y  y  y     win,pb,str
0x19 24  0  8  8  8  0 24  8  2 1 0x34325258--         y  y  y     win,pb,str
0x1a 24  0  8  8  8  0 24  0  2 1 0x34325258--         y  y  y     win,pb,str
0x1b 24  0  8  8  8  0  0  8  2 1 0x34325258--         y  y  y     win,pb,str
0x1c 24  0  8  8  8  0  0  0  2 1 0x34325258--         y  y  y     win,pb,str
0x1d 24  0  8  8  8  0 24  8  4 1 0x34325258--         y  y  y     win,pb,str
0x1e 24  0  8  8  8  0 24  8  4 1 0x34325258--         y  y  y     win,pb,str
0x1f 24  0  8  8  8  0 24  0  4 1 0x34325258--         y  y  y     win,pb,str
0x20 24  0  8  8  8  0 24  0  4 1 0x34325258--         y  y  y     win,pb,str
0x21 24  0  8  8  8  0  0  8  4 1 0x34325258--         y  y  y     win,pb,str
0x22 24  0  8  8  8  0  0  8  4 1 0x34325258--         y  y  y     win,pb,str
0x23 24  0  8  8  8  0  0  0  4 1 0x34325258--         y  y  y     win,pb,str
0x24 24  0  8  8  8  0  0  0  4 1 0x34325258--         y  y  y     win,pb,str
0x25 24  0  8  8  8  0 24  8  8 1 0x34325258--         y  y  y     win,pb,str
0x26 24  0  8  8  8  0 24  0  8 1 0x34325258--         y  y  y     win,pb,str
0x27 24  0  8  8  8  0  0  8  8 1 0x34325258--         y  y  y     win,pb,str
0x28 24  0  8  8  8  0  0  0  8 1 0x34325258--         y  y  y     win,pb,str
0x29 16  0  5  6  5  0 24  8  0 0 0x36314752--         y  y  y     win,pb,str
0x2a 16  0  5  6  5  0 24  0  0 0 0x36314752--         y  y  y     win,pb,str
0x2b 16  0  5  6  5  0 16  0  0 0 0x36314752--         y  y  y     win,pb,str
0x2c 16  0  5  6  5  0  0  8  0 0 0x36314752--         y  y  y     win,pb,str
0x2d 16  0  5  6  5  0  0  0  0 0 0x36314752--         y  y  y     win,pb,str
0x2e 16  0  5  6  5  0 24  8  2 1 0x36314752--         y  y  y     win,pb,str
0x2f 16  0  5  6  5  0 24  0  2 1 0x36314752--         y  y  y     win,pb,str
0x30 16  0  5  6  5  0 16  0  2 1 0x36314752--         y  y  y     win,pb,str
0x31 16  0  5  6  5  0  0  8  2 1 0x36314752--         y  y  y     win,pb,str
0x32 16  0  5  6  5  0  0  0  2 1 0x36314752--         y  y  y     win,pb,str
0x33 16  0  5  6  5  0 24  8  4 1 0x36314752--         y  y  y     win,pb,str
0x34 16  0  5  6  5  0 24  8  4 1 0x36314752--         y  y  y     win,pb,str
0x35 16  0  5  6  5  0 24  0  4 1 0x36314752--         y  y  y     win,pb,str
0x36 16  0  5  6  5  0 24  0  4 1 0x36314752--         y  y  y     win,pb,str
0x37 16  0  5  6  5  0 16  0  4 1 0x36314752--         y  y  y     win,pb,str
0x38 16  0  5  6  5  0 16  0  4 1 0x36314752--         y  y  y     win,pb,str
0x39 16  0  5  6  5  0  0  8  4 1 0x36314752--         y  y  y     win,pb,str
0x3a 16  0  5  6  5  0  0  8  4 1 0x36314752--         y  y  y     win,pb,str
0x3b 16  0  5  6  5  0  0  0  4 1 0x36314752--         y  y  y     win,pb,str
0x3c 16  0  5  6  5  0  0  0  4 1 0x36314752--         y  y  y     win,pb,str
0x3d 16  0  5  6  5  0 24  8  8 1 0x36314752--         y  y  y     win,pb,str
0x3e 16  0  5  6  5  0 24  0  8 1 0x36314752--         y  y  y     win,pb,str
0x3f 16  0  5  6  5  0 16  0  8 1 0x36314752--         y  y  y     win,pb,str
0x40 16  0  5  6  5  0  0  8  8 1 0x36314752--         y  y  y     win,pb,str
0x41 16  0  5  6  5  0  0  0  8 1 0x36314752--         y  y  y     win,pb,str

Wayland platform:
error: XDG_RUNTIME_DIR not set in the environment.
error: XDG_RUNTIME_DIR not set in the environment.
eglinfo: eglInitialize failed

X11 platform:
eglinfo: eglInitialize failed

Device platform:
EGL API version: 1.5
EGL vendor string: NVIDIA
EGL version string: 1.5
EGL client APIs: OpenGL_ES OpenGL
EGL extensions string:
    EGL_ANDROID_native_fence_sync EGL_EXT_buffer_age EGL_EXT_client_sync
    EGL_EXT_create_context_robustness EGL_EXT_image_dma_buf_import
    EGL_EXT_image_dma_buf_import_modifiers EGL_MESA_image_dma_buf_export
    EGL_EXT_output_base EGL_EXT_output_drm EGL_EXT_protected_content
    EGL_EXT_stream_consumer_egloutput EGL_EXT_stream_acquire_mode
    EGL_EXT_sync_reuse EGL_IMG_context_priority EGL_KHR_config_attribs
    EGL_KHR_create_context_no_error EGL_KHR_context_flush_control
    EGL_KHR_create_context EGL_KHR_fence_sync
    EGL_KHR_get_all_proc_addresses EGL_KHR_partial_update
    EGL_KHR_swap_buffers_with_damage EGL_KHR_no_config_context
    EGL_KHR_gl_colorspace EGL_KHR_gl_renderbuffer_image
    EGL_KHR_gl_texture_2D_image EGL_KHR_gl_texture_3D_image
    EGL_KHR_gl_texture_cubemap_image EGL_KHR_image EGL_KHR_image_base
    EGL_KHR_reusable_sync EGL_KHR_stream EGL_KHR_stream_attrib
    EGL_KHR_stream_consumer_gltexture EGL_KHR_stream_cross_process_fd
    EGL_KHR_stream_fifo EGL_KHR_stream_producer_eglsurface
    EGL_KHR_surfaceless_context EGL_KHR_wait_sync EGL_NV_nvrm_fence_sync
    EGL_NV_quadruple_buffer EGL_NV_stream_consumer_eglimage
    EGL_NV_stream_cross_display EGL_NV_stream_cross_object
    EGL_NV_stream_cross_process EGL_NV_stream_cross_system
    EGL_NV_stream_dma EGL_NV_stream_flush EGL_NV_stream_metadata
    EGL_NV_stream_remote EGL_NV_stream_reset EGL_NV_stream_socket
    EGL_NV_stream_socket_inet EGL_NV_stream_socket_unix
    EGL_NV_stream_sync EGL_NV_stream_fifo_next
    EGL_NV_stream_fifo_synchronous EGL_NV_stream_consumer_gltexture_yuv
    EGL_NV_stream_attrib EGL_NV_stream_origin EGL_NV_system_time
    EGL_NV_output_drm_flip_event EGL_NV_triple_buffer
    EGL_NV_robustness_video_memory_purge
Configurations:
     bf lv colorbuffer dp st  ms    vis   cav bi  renderable  supported
  id sz  l  r  g  b  a th cl ns b    id   eat nd gl es es2 vg surfaces
---------------------------------------------------------------------
0x01 32  0  8  8  8  8 24  8  0 0 0x00--         y  y  y     pb,str
0x02 32  0  8  8  8  8 24  0  0 0 0x00--         y  y  y     pb,str
0x03 32  0  8  8  8  8  0  8  0 0 0x00--         y  y  y     pb,str
0x04 32  0  8  8  8  8  0  0  0 0 0x00--         y  y  y     pb,str
0x05 32  0  8  8  8  8 24  8  2 1 0x00--         y  y  y     pb,str
0x06 32  0  8  8  8  8 24  0  2 1 0x00--         y  y  y     pb,str
0x07 32  0  8  8  8  8  0  8  2 1 0x00--         y  y  y     pb,str
0x08 32  0  8  8  8  8  0  0  2 1 0x00--         y  y  y     pb,str
0x09 32  0  8  8  8  8 24  8  4 1 0x00--         y  y  y     pb,str
0x0a 32  0  8  8  8  8 24  8  4 1 0x00--         y  y  y     pb,str
0x0b 32  0  8  8  8  8 24  0  4 1 0x00--         y  y  y     pb,str
0x0c 32  0  8  8  8  8 24  0  4 1 0x00--         y  y  y     pb,str
0x0d 32  0  8  8  8  8  0  8  4 1 0x00--         y  y  y     pb,str
0x0e 32  0  8  8  8  8  0  8  4 1 0x00--         y  y  y     pb,str
0x0f 32  0  8  8  8  8  0  0  4 1 0x00--         y  y  y     pb,str
0x10 32  0  8  8  8  8  0  0  4 1 0x00--         y  y  y     pb,str
0x11 32  0  8  8  8  8 24  8  8 1 0x00--         y  y  y     pb,str
0x12 32  0  8  8  8  8 24  0  8 1 0x00--         y  y  y     pb,str
0x13 32  0  8  8  8  8  0  8  8 1 0x00--         y  y  y     pb,str
0x14 32  0  8  8  8  8  0  0  8 1 0x00--         y  y  y     pb,str
0x15 24  0  8  8  8  0 24  8  0 0 0x00--         y  y  y     pb,str
0x16 24  0  8  8  8  0 24  0  0 0 0x00--         y  y  y     pb,str
0x17 24  0  8  8  8  0  0  8  0 0 0x00--         y  y  y     pb,str
0x18 24  0  8  8  8  0  0  0  0 0 0x00--         y  y  y     pb,str
0x19 24  0  8  8  8  0 24  8  2 1 0x00--         y  y  y     pb,str
0x1a 24  0  8  8  8  0 24  0  2 1 0x00--         y  y  y     pb,str
0x1b 24  0  8  8  8  0  0  8  2 1 0x00--         y  y  y     pb,str
0x1c 24  0  8  8  8  0  0  0  2 1 0x00--         y  y  y     pb,str
0x1d 24  0  8  8  8  0 24  8  4 1 0x00--         y  y  y     pb,str
0x1e 24  0  8  8  8  0 24  8  4 1 0x00--         y  y  y     pb,str
0x1f 24  0  8  8  8  0 24  0  4 1 0x00--         y  y  y     pb,str
0x20 24  0  8  8  8  0 24  0  4 1 0x00--         y  y  y     pb,str
0x21 24  0  8  8  8  0  0  8  4 1 0x00--         y  y  y     pb,str
0x22 24  0  8  8  8  0  0  8  4 1 0x00--         y  y  y     pb,str
0x23 24  0  8  8  8  0  0  0  4 1 0x00--         y  y  y     pb,str
0x24 24  0  8  8  8  0  0  0  4 1 0x00--         y  y  y     pb,str
0x25 24  0  8  8  8  0 24  8  8 1 0x00--         y  y  y     pb,str
0x26 24  0  8  8  8  0 24  0  8 1 0x00--         y  y  y     pb,str
0x27 24  0  8  8  8  0  0  8  8 1 0x00--         y  y  y     pb,str
0x28 24  0  8  8  8  0  0  0  8 1 0x00--         y  y  y     pb,str
0x29 16  0  5  6  5  0 24  8  0 0 0x00--         y  y  y     pb,str
0x2a 16  0  5  6  5  0 24  0  0 0 0x00--         y  y  y     pb,str
0x2b 16  0  5  6  5  0 16  0  0 0 0x00--         y  y  y     pb,str
0x2c 16  0  5  6  5  0  0  8  0 0 0x00--         y  y  y     pb,str
0x2d 16  0  5  6  5  0  0  0  0 0 0x00--         y  y  y     pb,str
0x2e 16  0  5  6  5  0 24  8  2 1 0x00--         y  y  y     pb,str
0x2f 16  0  5  6  5  0 24  0  2 1 0x00--         y  y  y     pb,str
0x30 16  0  5  6  5  0 16  0  2 1 0x00--         y  y  y     pb,str
0x31 16  0  5  6  5  0  0  8  2 1 0x00--         y  y  y     pb,str
0x32 16  0  5  6  5  0  0  0  2 1 0x00--         y  y  y     pb,str
0x33 16  0  5  6  5  0 24  8  4 1 0x00--         y  y  y     pb,str
0x34 16  0  5  6  5  0 24  8  4 1 0x00--         y  y  y     pb,str
0x35 16  0  5  6  5  0 24  0  4 1 0x00--         y  y  y     pb,str
0x36 16  0  5  6  5  0 24  0  4 1 0x00--         y  y  y     pb,str
0x37 16  0  5  6  5  0 16  0  4 1 0x00--         y  y  y     pb,str
0x38 16  0  5  6  5  0 16  0  4 1 0x00--         y  y  y     pb,str
0x39 16  0  5  6  5  0  0  8  4 1 0x00--         y  y  y     pb,str
0x3a 16  0  5  6  5  0  0  8  4 1 0x00--         y  y  y     pb,str
0x3b 16  0  5  6  5  0  0  0  4 1 0x00--         y  y  y     pb,str
0x3c 16  0  5  6  5  0  0  0  4 1 0x00--         y  y  y     pb,str
0x3d 16  0  5  6  5  0 24  8  8 1 0x00--         y  y  y     pb,str
0x3e 16  0  5  6  5  0 24  0  8 1 0x00--         y  y  y     pb,str
0x3f 16  0  5  6  5  0 16  0  8 1 0x00--         y  y  y     pb,str
0x40 16  0  5  6  5  0  0  8  8 1 0x00--         y  y  y     pb,str
0x41 16  0  5  6  5  0  0  0  8 1 0x00--         y  y  y     pb,str
```


### Local testing with runpod (good case)

```
(base) (pseye)-➜  egldockertest git:(main) ✗ sudo docker build . -t egldockertest:0.0.0 && sudo docker run -it --gpus all --rm -it --entrypoint bash egldockertest:0.0.0
[+] Building 2.0s (12/12) FINISHED                                                                                                                                                                                     docker:default
 => [internal] load build definition from Dockerfile                                                                                                                                                                             0.0s
 => => transferring dockerfile: 592B                                                                                                                                                                                             0.0s
 => [internal] load metadata for docker.io/nvidia/cuda:12.3.2-cudnn9-devel-ubuntu22.04                                                                                                                                           1.6s
 => [auth] nvidia/cuda:pull token for registry-1.docker.io                                                                                                                                                                       0.0s
 => [internal] load .dockerignore                                                                                                                                                                                                0.0s
 => => transferring context: 2B                                                                                                                                                                                                  0.0s
 => [1/6] FROM docker.io/nvidia/cuda:12.3.2-cudnn9-devel-ubuntu22.04@sha256:fb1ad20f2552f5b3aafb2c9c478ed57da95e2bb027d15218d7a55b3a0e4b4413                                                                                     0.0s
 => [internal] load build context                                                                                                                                                                                                0.0s
 => => transferring context: 67B                                                                                                                                                                                                 0.0s
 => CACHED [2/6] RUN apt-get update &&      apt-get install --no-install-recommends -y         mesa-utils         python3         python3-pip      && rm -rf /var/lib/apt/lists/*                                                0.0s
 => CACHED [3/6] COPY ./requirements.txt /requirements.txt                                                                                                                                                                       0.0s
 => CACHED [4/6] RUN pip install --no-cache-dir -r /requirements.txt                                                                                                                                                             0.0s
 => CACHED [5/6] WORKDIR /app                                                                                                                                                                                                    0.0s
 => [6/6] COPY ./handler.py /app/handler.py                                                                                                                                                                                      0.1s
 => exporting to image                                                                                                                                                                                                           0.1s
 => => exporting layers                                                                                                                                                                                                          0.1s
 => => writing image sha256:1d72bcef25c05d983a031aad7aca2b9653b8df4c1288b702f0da5657551dc146                                                                                                                                     0.0s
 => => naming to docker.io/library/egldockertest:0.0.0                                                                                                                                                                           0.0s
root@5da9acc94b1d:/app# python3 handler.py --test-input '{"input":{}}'
--- Starting Serverless Worker |  Version 1.6.2 ---
WARN   | test_input.json not found, exiting.
root@5da9acc94b1d:/app# python3 handler.py --test-input '{"input":{"dummy":{}}}'
--- Starting Serverless Worker |  Version 1.6.2 ---
WARN   | test_input.json not found, exiting.
root@5da9acc94b1d:/app# python3 handler.py --test_input '{"input": {}}'
--- Starting Serverless Worker |  Version 1.6.2 ---
INFO   | test_input set, using test_input as job input.
DEBUG  | Retrieved local job: {'input': {}, 'id': 'local_test'}
INFO   | local_test | Started.
STDOUT: EGL client extensions string:
    EGL_EXT_platform_base EGL_EXT_device_base EGL_EXT_device_enumeration
    EGL_EXT_device_query EGL_KHR_client_get_all_proc_addresses
    EGL_EXT_client_extensions EGL_KHR_debug EGL_KHR_platform_x11
    EGL_EXT_platform_x11 EGL_EXT_platform_device
    EGL_MESA_platform_surfaceless EGL_EXT_explicit_device
    EGL_KHR_platform_gbm EGL_MESA_platform_gbm EGL_EXT_platform_wayland
    EGL_KHR_platform_wayland EGL_EXT_platform_xcb

GBM platform:
EGL API version: 1.5
EGL vendor string: NVIDIA
EGL version string: 1.5
EGL client APIs: OpenGL_ES OpenGL
EGL extensions string:
    EGL_ANDROID_native_fence_sync EGL_EXT_buffer_age EGL_EXT_client_sync
    EGL_EXT_create_context_robustness EGL_EXT_image_dma_buf_import
    EGL_EXT_image_dma_buf_import_modifiers EGL_MESA_image_dma_buf_export
    EGL_EXT_output_base EGL_EXT_output_drm EGL_EXT_protected_content
    EGL_EXT_stream_consumer_egloutput EGL_EXT_stream_acquire_mode
    EGL_EXT_sync_reuse EGL_IMG_context_priority EGL_KHR_config_attribs
    EGL_KHR_create_context_no_error EGL_KHR_context_flush_control
    EGL_KHR_create_context EGL_KHR_fence_sync
    EGL_KHR_get_all_proc_addresses EGL_KHR_partial_update
    EGL_KHR_swap_buffers_with_damage EGL_KHR_no_config_context
    EGL_KHR_gl_colorspace EGL_KHR_gl_renderbuffer_image
    EGL_KHR_gl_texture_2D_image EGL_KHR_gl_texture_3D_image
    EGL_KHR_gl_texture_cubemap_image EGL_KHR_image EGL_KHR_image_base
    EGL_KHR_reusable_sync EGL_KHR_stream EGL_KHR_stream_attrib
    EGL_KHR_stream_consumer_gltexture EGL_KHR_stream_cross_process_fd
    EGL_KHR_stream_fifo EGL_KHR_stream_producer_eglsurface
    EGL_KHR_surfaceless_context EGL_KHR_wait_sync EGL_NV_nvrm_fence_sync
    EGL_NV_quadruple_buffer EGL_NV_stream_consumer_eglimage
    EGL_NV_stream_cross_display EGL_NV_stream_cross_object
    EGL_NV_stream_cross_process EGL_NV_stream_cross_system
    EGL_NV_stream_dma EGL_NV_stream_flush EGL_NV_stream_metadata
    EGL_NV_stream_remote EGL_NV_stream_reset EGL_NV_stream_socket
    EGL_NV_stream_socket_inet EGL_NV_stream_socket_unix
    EGL_NV_stream_sync EGL_NV_stream_fifo_next
    EGL_NV_stream_fifo_synchronous EGL_NV_stream_consumer_gltexture_yuv
    EGL_NV_stream_attrib EGL_NV_stream_origin EGL_NV_system_time
    EGL_NV_output_drm_flip_event EGL_NV_triple_buffer
    EGL_NV_robustness_video_memory_purge
Configurations:
     bf lv colorbuffer dp st  ms    vis   cav bi  renderable  supported
  id sz  l  r  g  b  a th cl ns b    id   eat nd gl es es2 vg surfaces
---------------------------------------------------------------------
0x01 32  0  8  8  8  8 24  8  0 0 0x34325241--         y  y  y     win,pb,str
0x02 32  0  8  8  8  8 24  0  0 0 0x34325241--         y  y  y     win,pb,str
0x03 32  0  8  8  8  8  0  8  0 0 0x34325241--         y  y  y     win,pb,str
0x04 32  0  8  8  8  8  0  0  0 0 0x34325241--         y  y  y     win,pb,str
0x05 32  0  8  8  8  8 24  8  2 1 0x34325241--         y  y  y     win,pb,str
0x06 32  0  8  8  8  8 24  0  2 1 0x34325241--         y  y  y     win,pb,str
0x07 32  0  8  8  8  8  0  8  2 1 0x34325241--         y  y  y     win,pb,str
0x08 32  0  8  8  8  8  0  0  2 1 0x34325241--         y  y  y     win,pb,str
0x09 32  0  8  8  8  8 24  8  4 1 0x34325241--         y  y  y     win,pb,str
0x0a 32  0  8  8  8  8 24  8  4 1 0x34325241--         y  y  y     win,pb,str
0x0b 32  0  8  8  8  8 24  0  4 1 0x34325241--         y  y  y     win,pb,str
0x0c 32  0  8  8  8  8 24  0  4 1 0x34325241--         y  y  y     win,pb,str
0x0d 32  0  8  8  8  8  0  8  4 1 0x34325241--         y  y  y     win,pb,str
0x0e 32  0  8  8  8  8  0  8  4 1 0x34325241--         y  y  y     win,pb,str
0x0f 32  0  8  8  8  8  0  0  4 1 0x34325241--         y  y  y     win,pb,str
0x10 32  0  8  8  8  8  0  0  4 1 0x34325241--         y  y  y     win,pb,str
0x11 32  0  8  8  8  8 24  8  8 1 0x34325241--         y  y  y     win,pb,str
0x12 32  0  8  8  8  8 24  0  8 1 0x34325241--         y  y  y     win,pb,str
0x13 32  0  8  8  8  8  0  8  8 1 0x34325241--         y  y  y     win,pb,str
0x14 32  0  8  8  8  8  0  0  8 1 0x34325241--         y  y  y     win,pb,str
0x15 24  0  8  8  8  0 24  8  0 0 0x34325258--         y  y  y     win,pb,str
0x16 24  0  8  8  8  0 24  0  0 0 0x34325258--         y  y  y     win,pb,str
0x17 24  0  8  8  8  0  0  8  0 0 0x34325258--         y  y  y     win,pb,str
0x18 24  0  8  8  8  0  0  0  0 0 0x34325258--         y  y  y     win,pb,str
0x19 24  0  8  8  8  0 24  8  2 1 0x34325258--         y  y  y     win,pb,str
0x1a 24  0  8  8  8  0 24  0  2 1 0x34325258--         y  y  y     win,pb,str
0x1b 24  0  8  8  8  0  0  8  2 1 0x34325258--         y  y  y     win,pb,str
0x1c 24  0  8  8  8  0  0  0  2 1 0x34325258--         y  y  y     win,pb,str
0x1d 24  0  8  8  8  0 24  8  4 1 0x34325258--         y  y  y     win,pb,str
0x1e 24  0  8  8  8  0 24  8  4 1 0x34325258--         y  y  y     win,pb,str
0x1f 24  0  8  8  8  0 24  0  4 1 0x34325258--         y  y  y     win,pb,str
0x20 24  0  8  8  8  0 24  0  4 1 0x34325258--         y  y  y     win,pb,str
0x21 24  0  8  8  8  0  0  8  4 1 0x34325258--         y  y  y     win,pb,str
0x22 24  0  8  8  8  0  0  8  4 1 0x34325258--         y  y  y     win,pb,str
0x23 24  0  8  8  8  0  0  0  4 1 0x34325258--         y  y  y     win,pb,str
0x24 24  0  8  8  8  0  0  0  4 1 0x34325258--         y  y  y     win,pb,str
0x25 24  0  8  8  8  0 24  8  8 1 0x34325258--         y  y  y     win,pb,str
0x26 24  0  8  8  8  0 24  0  8 1 0x34325258--         y  y  y     win,pb,str
0x27 24  0  8  8  8  0  0  8  8 1 0x34325258--         y  y  y     win,pb,str
0x28 24  0  8  8  8  0  0  0  8 1 0x34325258--         y  y  y     win,pb,str
0x29 16  0  5  6  5  0 24  8  0 0 0x36314752--         y  y  y     win,pb,str
0x2a 16  0  5  6  5  0 24  0  0 0 0x36314752--         y  y  y     win,pb,str
0x2b 16  0  5  6  5  0 16  0  0 0 0x36314752--         y  y  y     win,pb,str
0x2c 16  0  5  6  5  0  0  8  0 0 0x36314752--         y  y  y     win,pb,str
0x2d 16  0  5  6  5  0  0  0  0 0 0x36314752--         y  y  y     win,pb,str
0x2e 16  0  5  6  5  0 24  8  2 1 0x36314752--         y  y  y     win,pb,str
0x2f 16  0  5  6  5  0 24  0  2 1 0x36314752--         y  y  y     win,pb,str
0x30 16  0  5  6  5  0 16  0  2 1 0x36314752--         y  y  y     win,pb,str
0x31 16  0  5  6  5  0  0  8  2 1 0x36314752--         y  y  y     win,pb,str
0x32 16  0  5  6  5  0  0  0  2 1 0x36314752--         y  y  y     win,pb,str
0x33 16  0  5  6  5  0 24  8  4 1 0x36314752--         y  y  y     win,pb,str
0x34 16  0  5  6  5  0 24  8  4 1 0x36314752--         y  y  y     win,pb,str
0x35 16  0  5  6  5  0 24  0  4 1 0x36314752--         y  y  y     win,pb,str
0x36 16  0  5  6  5  0 24  0  4 1 0x36314752--         y  y  y     win,pb,str
0x37 16  0  5  6  5  0 16  0  4 1 0x36314752--         y  y  y     win,pb,str
0x38 16  0  5  6  5  0 16  0  4 1 0x36314752--         y  y  y     win,pb,str
0x39 16  0  5  6  5  0  0  8  4 1 0x36314752--         y  y  y     win,pb,str
0x3a 16  0  5  6  5  0  0  8  4 1 0x36314752--         y  y  y     win,pb,str
0x3b 16  0  5  6  5  0  0  0  4 1 0x36314752--         y  y  y     win,pb,str
0x3c 16  0  5  6  5  0  0  0  4 1 0x36314752--         y  y  y     win,pb,str
0x3d 16  0  5  6  5  0 24  8  8 1 0x36314752--         y  y  y     win,pb,str
0x3e 16  0  5  6  5  0 24  0  8 1 0x36314752--         y  y  y     win,pb,str
0x3f 16  0  5  6  5  0 16  0  8 1 0x36314752--         y  y  y     win,pb,str
0x40 16  0  5  6  5  0  0  8  8 1 0x36314752--         y  y  y     win,pb,str
0x41 16  0  5  6  5  0  0  0  8 1 0x36314752--         y  y  y     win,pb,str

Wayland platform:
eglinfo: eglInitialize failed

X11 platform:
eglinfo: eglInitialize failed

Device platform:
EGL API version: 1.5
EGL vendor string: NVIDIA
EGL version string: 1.5
EGL client APIs: OpenGL_ES OpenGL
EGL extensions string:
    EGL_ANDROID_native_fence_sync EGL_EXT_buffer_age EGL_EXT_client_sync
    EGL_EXT_create_context_robustness EGL_EXT_image_dma_buf_import
    EGL_EXT_image_dma_buf_import_modifiers EGL_MESA_image_dma_buf_export
    EGL_EXT_output_base EGL_EXT_output_drm EGL_EXT_protected_content
    EGL_EXT_stream_consumer_egloutput EGL_EXT_stream_acquire_mode
    EGL_EXT_sync_reuse EGL_IMG_context_priority EGL_KHR_config_attribs
    EGL_KHR_create_context_no_error EGL_KHR_context_flush_control
    EGL_KHR_create_context EGL_KHR_fence_sync
    EGL_KHR_get_all_proc_addresses EGL_KHR_partial_update
    EGL_KHR_swap_buffers_with_damage EGL_KHR_no_config_context
    EGL_KHR_gl_colorspace EGL_KHR_gl_renderbuffer_image
    EGL_KHR_gl_texture_2D_image EGL_KHR_gl_texture_3D_image
    EGL_KHR_gl_texture_cubemap_image EGL_KHR_image EGL_KHR_image_base
    EGL_KHR_reusable_sync EGL_KHR_stream EGL_KHR_stream_attrib
    EGL_KHR_stream_consumer_gltexture EGL_KHR_stream_cross_process_fd
    EGL_KHR_stream_fifo EGL_KHR_stream_producer_eglsurface
    EGL_KHR_surfaceless_context EGL_KHR_wait_sync EGL_NV_nvrm_fence_sync
    EGL_NV_quadruple_buffer EGL_NV_stream_consumer_eglimage
    EGL_NV_stream_cross_display EGL_NV_stream_cross_object
    EGL_NV_stream_cross_process EGL_NV_stream_cross_system
    EGL_NV_stream_dma EGL_NV_stream_flush EGL_NV_stream_metadata
    EGL_NV_stream_remote EGL_NV_stream_reset EGL_NV_stream_socket
    EGL_NV_stream_socket_inet EGL_NV_stream_socket_unix
    EGL_NV_stream_sync EGL_NV_stream_fifo_next
    EGL_NV_stream_fifo_synchronous EGL_NV_stream_consumer_gltexture_yuv
    EGL_NV_stream_attrib EGL_NV_stream_origin EGL_NV_system_time
    EGL_NV_output_drm_flip_event EGL_NV_triple_buffer
    EGL_NV_robustness_video_memory_purge
Configurations:
     bf lv colorbuffer dp st  ms    vis   cav bi  renderable  supported
  id sz  l  r  g  b  a th cl ns b    id   eat nd gl es es2 vg surfaces
---------------------------------------------------------------------
0x01 32  0  8  8  8  8 24  8  0 0 0x00--         y  y  y     pb,str
0x02 32  0  8  8  8  8 24  0  0 0 0x00--         y  y  y     pb,str
0x03 32  0  8  8  8  8  0  8  0 0 0x00--         y  y  y     pb,str
0x04 32  0  8  8  8  8  0  0  0 0 0x00--         y  y  y     pb,str
0x05 32  0  8  8  8  8 24  8  2 1 0x00--         y  y  y     pb,str
0x06 32  0  8  8  8  8 24  0  2 1 0x00--         y  y  y     pb,str
0x07 32  0  8  8  8  8  0  8  2 1 0x00--         y  y  y     pb,str
0x08 32  0  8  8  8  8  0  0  2 1 0x00--         y  y  y     pb,str
0x09 32  0  8  8  8  8 24  8  4 1 0x00--         y  y  y     pb,str
0x0a 32  0  8  8  8  8 24  8  4 1 0x00--         y  y  y     pb,str
0x0b 32  0  8  8  8  8 24  0  4 1 0x00--         y  y  y     pb,str
0x0c 32  0  8  8  8  8 24  0  4 1 0x00--         y  y  y     pb,str
0x0d 32  0  8  8  8  8  0  8  4 1 0x00--         y  y  y     pb,str
0x0e 32  0  8  8  8  8  0  8  4 1 0x00--         y  y  y     pb,str
0x0f 32  0  8  8  8  8  0  0  4 1 0x00--         y  y  y     pb,str
0x10 32  0  8  8  8  8  0  0  4 1 0x00--         y  y  y     pb,str
0x11 32  0  8  8  8  8 24  8  8 1 0x00--         y  y  y     pb,str
0x12 32  0  8  8  8  8 24  0  8 1 0x00--         y  y  y     pb,str
0x13 32  0  8  8  8  8  0  8  8 1 0x00--         y  y  y     pb,str
0x14 32  0  8  8  8  8  0  0  8 1 0x00--         y  y  y     pb,str
0x15 24  0  8  8  8  0 24  8  0 0 0x00--         y  y  y     pb,str
0x16 24  0  8  8  8  0 24  0  0 0 0x00--         y  y  y     pb,str
0x17 24  0  8  8  8  0  0  8  0 0 0x00--         y  y  y     pb,str
0x18 24  0  8  8  8  0  0  0  0 0 0x00--         y  y  y     pb,str
0x19 24  0  8  8  8  0 24  8  2 1 0x00--         y  y  y     pb,str
0x1a 24  0  8  8  8  0 24  0  2 1 0x00--         y  y  y     pb,str
0x1b 24  0  8  8  8  0  0  8  2 1 0x00--         y  y  y     pb,str
0x1c 24  0  8  8  8  0  0  0  2 1 0x00--         y  y  y     pb,str
0x1d 24  0  8  8  8  0 24  8  4 1 0x00--         y  y  y     pb,str
0x1e 24  0  8  8  8  0 24  8  4 1 0x00--         y  y  y     pb,str
0x1f 24  0  8  8  8  0 24  0  4 1 0x00--         y  y  y     pb,str
0x20 24  0  8  8  8  0 24  0  4 1 0x00--         y  y  y     pb,str
0x21 24  0  8  8  8  0  0  8  4 1 0x00--         y  y  y     pb,str
0x22 24  0  8  8  8  0  0  8  4 1 0x00--         y  y  y     pb,str
0x23 24  0  8  8  8  0  0  0  4 1 0x00--         y  y  y     pb,str
0x24 24  0  8  8  8  0  0  0  4 1 0x00--         y  y  y     pb,str
0x25 24  0  8  8  8  0 24  8  8 1 0x00--         y  y  y     pb,str
0x26 24  0  8  8  8  0 24  0  8 1 0x00--         y  y  y     pb,str
0x27 24  0  8  8  8  0  0  8  8 1 0x00--         y  y  y     pb,str
0x28 24  0  8  8  8  0  0  0  8 1 0x00--         y  y  y     pb,str
0x29 16  0  5  6  5  0 24  8  0 0 0x00--         y  y  y     pb,str
0x2a 16  0  5  6  5  0 24  0  0 0 0x00--         y  y  y     pb,str
0x2b 16  0  5  6  5  0 16  0  0 0 0x00--         y  y  y     pb,str
0x2c 16  0  5  6  5  0  0  8  0 0 0x00--         y  y  y     pb,str
0x2d 16  0  5  6  5  0  0  0  0 0 0x00--         y  y  y     pb,str
0x2e 16  0  5  6  5  0 24  8  2 1 0x00--         y  y  y     pb,str
0x2f 16  0  5  6  5  0 24  0  2 1 0x00--         y  y  y     pb,str
0x30 16  0  5  6  5  0 16  0  2 1 0x00--         y  y  y     pb,str
0x31 16  0  5  6  5  0  0  8  2 1 0x00--         y  y  y     pb,str
0x32 16  0  5  6  5  0  0  0  2 1 0x00--         y  y  y     pb,str
0x33 16  0  5  6  5  0 24  8  4 1 0x00--         y  y  y     pb,str
0x34 16  0  5  6  5  0 24  8  4 1 0x00--         y  y  y     pb,str
0x35 16  0  5  6  5  0 24  0  4 1 0x00--         y  y  y     pb,str
0x36 16  0  5  6  5  0 24  0  4 1 0x00--         y  y  y     pb,str
0x37 16  0  5  6  5  0 16  0  4 1 0x00--         y  y  y     pb,str
0x38 16  0  5  6  5  0 16  0  4 1 0x00--         y  y  y     pb,str
0x39 16  0  5  6  5  0  0  8  4 1 0x00--         y  y  y     pb,str
0x3a 16  0  5  6  5  0  0  8  4 1 0x00--         y  y  y     pb,str
0x3b 16  0  5  6  5  0  0  0  4 1 0x00--         y  y  y     pb,str
0x3c 16  0  5  6  5  0  0  0  4 1 0x00--         y  y  y     pb,str
0x3d 16  0  5  6  5  0 24  8  8 1 0x00--         y  y  y     pb,str
0x3e 16  0  5  6  5  0 24  0  8 1 0x00--         y  y  y     pb,str
0x3f 16  0  5  6  5  0 16  0  8 1 0x00--         y  y  y     pb,str
0x40 16  0  5  6  5  0  0  8  8 1 0x00--         y  y  y     pb,str
0x41 16  0  5  6  5  0  0  0  8 1 0x00--         y  y  y     pb,str


STDERR: error: XDG_RUNTIME_DIR not set in the environment.
error: XDG_RUNTIME_DIR not set in the environment.

DEBUG  | local_test | Handler output: completed
DEBUG  | local_test | run_job return: {'output': 'completed'}
INFO   | Job local_test completed successfully.
INFO   | Job result: {'output': 'completed'}
INFO   | Local testing complete, exiting.
root@5da9acc94b1d:/app#
```


### Local testing with Replicate (good case)

```
✗ sudo cog predict
Building Docker image from environment in cog.yaml...
[+] Building 2.9s (22/22) FINISHED                                                                                                                                                                                     docker:default
 => [internal] load build definition from Dockerfile                                                                                                                                                                             0.0s
 => => transferring dockerfile: 2.20kB                                                                                                                                                                                           0.0s
 => resolve image config for docker.io/docker/dockerfile:1.4                                                                                                                                                                     0.8s
 => CACHED docker-image://docker.io/docker/dockerfile:1.4@sha256:9ba7531bd80fb0a858632727cf7a112fbfd19b17e94c4e84ced81e24ef1a0dbc                                                                                                0.0s
 => [internal] load .dockerignore                                                                                                                                                                                                0.0s
 => => transferring context: 2B                                                                                                                                                                                                  0.0s
 => [internal] load metadata for docker.io/nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04                                                                                                                                           1.5s
 => [internal] load metadata for docker.io/library/python:3.11                                                                                                                                                                   0.8s
 => [auth] nvidia/cuda:pull token for registry-1.docker.io                                                                                                                                                                       0.0s
 => [deps 1/5] FROM docker.io/library/python:3.11@sha256:47d0618fb878d93e1b8cacb184fd8f727ae95c1b85d5959723e1d3e1848e2aba                                                                                                        0.0s
 => [stage-1 1/7] FROM docker.io/nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04@sha256:8f9dd0d09d3ad3900357a1cf7f887888b5b74056636cd6ef03c160c3cd4b1d95                                                                             0.0s
 => [internal] load build context                                                                                                                                                                                                0.0s
 => => transferring context: 91.07kB                                                                                                                                                                                             0.0s
 => CACHED [stage-1 2/7] RUN --mount=type=cache,target=/var/cache/apt set -eux; apt-get update -qq; apt-get install -qqy --no-install-recommends curl; rm -rf /var/lib/apt/lists/*; TINI_VERSION=v0.19.0; TINI_ARCH="$(dpkg --p  0.0s
 => CACHED [stage-1 3/7] RUN --mount=type=cache,target=/var/cache/apt apt-get update -qq && apt-get install -qqy --no-install-recommends  make  build-essential  libssl-dev  zlib1g-dev  libbz2-dev  libreadline-dev  libsqlite  0.0s
 => CACHED [stage-1 4/7] RUN curl -s -S -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash &&  git clone https://github.com/momo-lab/pyenv-install-latest.git "$(pyenv root)"/plugins  0.0s
 => CACHED [stage-1 5/7] RUN --mount=type=cache,target=/var/cache/apt apt-get update -qq && apt-get install -qqy mesa-utils && rm -rf /var/lib/apt/lists/*                                                                       0.0s
 => CACHED [deps 2/5] COPY .cog/tmp/build3859760125/cog-0.0.1.dev-py3-none-any.whl /tmp/cog-0.0.1.dev-py3-none-any.whl                                                                                                           0.0s
 => CACHED [deps 3/5] RUN --mount=type=cache,target=/root/.cache/pip pip install -t /dep /tmp/cog-0.0.1.dev-py3-none-any.whl                                                                                                     0.0s
 => CACHED [deps 4/5] COPY .cog/tmp/build3859760125/requirements.txt /tmp/requirements.txt                                                                                                                                       0.0s
 => CACHED [deps 5/5] RUN --mount=type=cache,target=/root/.cache/pip pip install -t /dep -r /tmp/requirements.txt                                                                                                                0.0s
 => CACHED [stage-1 6/7] RUN --mount=type=bind,from=deps,source=/dep,target=/dep cp -rf /dep/* $(pyenv prefix)/lib/python*/site-packages || true                                                                                 0.0s
 => CACHED [stage-1 7/7] WORKDIR /src                                                                                                                                                                                            0.0s
 => preparing layers for inline cache                                                                                                                                                                                            0.0s
 => exporting to image                                                                                                                                                                                                           0.0s
 => => exporting layers                                                                                                                                                                                                          0.0s
 => => writing image sha256:1b48419b22dfe66e758a380520331830bf10207a32be4c711cf1f0b1c0628b91                                                                                                                                     0.0s
 => => naming to docker.io/library/cog-egldockertest-base                                                                                                                                                                        0.0s

Starting Docker image cog-egldockertest-base and running setup()...
Running prediction...
STDOUT: EGL client extensions string:
EGL_EXT_platform_base EGL_EXT_device_base EGL_EXT_device_enumeration
EGL_EXT_device_query EGL_KHR_client_get_all_proc_addresses
EGL_EXT_client_extensions EGL_KHR_debug EGL_KHR_platform_x11
EGL_EXT_platform_x11 EGL_EXT_platform_device
EGL_MESA_platform_surfaceless EGL_EXT_explicit_device
EGL_KHR_platform_gbm EGL_MESA_platform_gbm EGL_EXT_platform_wayland
EGL_KHR_platform_wayland EGL_EXT_platform_xcb
GBM platform:
EGL API version: 1.5
EGL vendor string: NVIDIA
EGL version string: 1.5
EGL client APIs: OpenGL_ES OpenGL
EGL extensions string:
EGL_ANDROID_native_fence_sync EGL_EXT_buffer_age EGL_EXT_client_sync
EGL_EXT_create_context_robustness EGL_EXT_image_dma_buf_import
EGL_EXT_image_dma_buf_import_modifiers EGL_MESA_image_dma_buf_export
EGL_EXT_output_base EGL_EXT_output_drm EGL_EXT_protected_content
EGL_EXT_stream_consumer_egloutput EGL_EXT_stream_acquire_mode
EGL_EXT_sync_reuse EGL_IMG_context_priority EGL_KHR_config_attribs
EGL_KHR_create_context_no_error EGL_KHR_context_flush_control
EGL_KHR_create_context EGL_KHR_fence_sync
EGL_KHR_get_all_proc_addresses EGL_KHR_partial_update
EGL_KHR_swap_buffers_with_damage EGL_KHR_no_config_context
EGL_KHR_gl_colorspace EGL_KHR_gl_renderbuffer_image
EGL_KHR_gl_texture_2D_image EGL_KHR_gl_texture_3D_image
EGL_KHR_gl_texture_cubemap_image EGL_KHR_image EGL_KHR_image_base
EGL_KHR_reusable_sync EGL_KHR_stream EGL_KHR_stream_attrib
EGL_KHR_stream_consumer_gltexture EGL_KHR_stream_cross_process_fd
EGL_KHR_stream_fifo EGL_KHR_stream_producer_eglsurface
EGL_KHR_surfaceless_context EGL_KHR_wait_sync EGL_NV_nvrm_fence_sync
EGL_NV_quadruple_buffer EGL_NV_stream_consumer_eglimage
EGL_NV_stream_cross_display EGL_NV_stream_cross_object
EGL_NV_stream_cross_process EGL_NV_stream_cross_system
EGL_NV_stream_dma EGL_NV_stream_flush EGL_NV_stream_metadata
EGL_NV_stream_remote EGL_NV_stream_reset EGL_NV_stream_socket
EGL_NV_stream_socket_inet EGL_NV_stream_socket_unix
EGL_NV_stream_sync EGL_NV_stream_fifo_next
EGL_NV_stream_fifo_synchronous EGL_NV_stream_consumer_gltexture_yuv
EGL_NV_stream_attrib EGL_NV_stream_origin EGL_NV_system_time
EGL_NV_output_drm_flip_event EGL_NV_triple_buffer
EGL_NV_robustness_video_memory_purge
Configurations:
bf lv colorbuffer dp st  ms    vis   cav bi  renderable  supported
id sz  l  r  g  b  a th cl ns b    id   eat nd gl es es2 vg surfaces
---------------------------------------------------------------------
0x01 32  0  8  8  8  8 24  8  0 0 0x34325241--         y  y  y     win,pb,str
0x02 32  0  8  8  8  8 24  0  0 0 0x34325241--         y  y  y     win,pb,str
0x03 32  0  8  8  8  8  0  8  0 0 0x34325241--         y  y  y     win,pb,str
0x04 32  0  8  8  8  8  0  0  0 0 0x34325241--         y  y  y     win,pb,str
0x05 32  0  8  8  8  8 24  8  2 1 0x34325241--         y  y  y     win,pb,str
0x06 32  0  8  8  8  8 24  0  2 1 0x34325241--         y  y  y     win,pb,str
0x07 32  0  8  8  8  8  0  8  2 1 0x34325241--         y  y  y     win,pb,str
0x08 32  0  8  8  8  8  0  0  2 1 0x34325241--         y  y  y     win,pb,str
0x09 32  0  8  8  8  8 24  8  4 1 0x34325241--         y  y  y     win,pb,str
0x0a 32  0  8  8  8  8 24  8  4 1 0x34325241--         y  y  y     win,pb,str
0x0b 32  0  8  8  8  8 24  0  4 1 0x34325241--         y  y  y     win,pb,str
0x0c 32  0  8  8  8  8 24  0  4 1 0x34325241--         y  y  y     win,pb,str
0x0d 32  0  8  8  8  8  0  8  4 1 0x34325241--         y  y  y     win,pb,str
0x0e 32  0  8  8  8  8  0  8  4 1 0x34325241--         y  y  y     win,pb,str
0x0f 32  0  8  8  8  8  0  0  4 1 0x34325241--         y  y  y     win,pb,str
0x10 32  0  8  8  8  8  0  0  4 1 0x34325241--         y  y  y     win,pb,str
0x11 32  0  8  8  8  8 24  8  8 1 0x34325241--         y  y  y     win,pb,str
0x12 32  0  8  8  8  8 24  0  8 1 0x34325241--         y  y  y     win,pb,str
0x13 32  0  8  8  8  8  0  8  8 1 0x34325241--         y  y  y     win,pb,str
0x14 32  0  8  8  8  8  0  0  8 1 0x34325241--         y  y  y     win,pb,str
0x15 24  0  8  8  8  0 24  8  0 0 0x34325258--         y  y  y     win,pb,str
0x16 24  0  8  8  8  0 24  0  0 0 0x34325258--         y  y  y     win,pb,str
0x17 24  0  8  8  8  0  0  8  0 0 0x34325258--         y  y  y     win,pb,str
0x18 24  0  8  8  8  0  0  0  0 0 0x34325258--         y  y  y     win,pb,str
0x19 24  0  8  8  8  0 24  8  2 1 0x34325258--         y  y  y     win,pb,str
0x1a 24  0  8  8  8  0 24  0  2 1 0x34325258--         y  y  y     win,pb,str
0x1b 24  0  8  8  8  0  0  8  2 1 0x34325258--         y  y  y     win,pb,str
0x1c 24  0  8  8  8  0  0  0  2 1 0x34325258--         y  y  y     win,pb,str
0x1d 24  0  8  8  8  0 24  8  4 1 0x34325258--         y  y  y     win,pb,str
0x1e 24  0  8  8  8  0 24  8  4 1 0x34325258--         y  y  y     win,pb,str
0x1f 24  0  8  8  8  0 24  0  4 1 0x34325258--         y  y  y     win,pb,str
0x20 24  0  8  8  8  0 24  0  4 1 0x34325258--         y  y  y     win,pb,str
0x21 24  0  8  8  8  0  0  8  4 1 0x34325258--         y  y  y     win,pb,str
0x22 24  0  8  8  8  0  0  8  4 1 0x34325258--         y  y  y     win,pb,str
0x23 24  0  8  8  8  0  0  0  4 1 0x34325258--         y  y  y     win,pb,str
0x24 24  0  8  8  8  0  0  0  4 1 0x34325258--         y  y  y     win,pb,str
0x25 24  0  8  8  8  0 24  8  8 1 0x34325258--         y  y  y     win,pb,str
0x26 24  0  8  8  8  0 24  0  8 1 0x34325258--         y  y  y     win,pb,str
0x27 24  0  8  8  8  0  0  8  8 1 0x34325258--         y  y  y     win,pb,str
0x28 24  0  8  8  8  0  0  0  8 1 0x34325258--         y  y  y     win,pb,str
0x29 16  0  5  6  5  0 24  8  0 0 0x36314752--         y  y  y     win,pb,str
0x2a 16  0  5  6  5  0 24  0  0 0 0x36314752--         y  y  y     win,pb,str
0x2b 16  0  5  6  5  0 16  0  0 0 0x36314752--         y  y  y     win,pb,str
0x2c 16  0  5  6  5  0  0  8  0 0 0x36314752--         y  y  y     win,pb,str
0x2d 16  0  5  6  5  0  0  0  0 0 0x36314752--         y  y  y     win,pb,str
0x2e 16  0  5  6  5  0 24  8  2 1 0x36314752--         y  y  y     win,pb,str
0x2f 16  0  5  6  5  0 24  0  2 1 0x36314752--         y  y  y     win,pb,str
0x30 16  0  5  6  5  0 16  0  2 1 0x36314752--         y  y  y     win,pb,str
0x31 16  0  5  6  5  0  0  8  2 1 0x36314752--         y  y  y     win,pb,str
0x32 16  0  5  6  5  0  0  0  2 1 0x36314752--         y  y  y     win,pb,str
0x33 16  0  5  6  5  0 24  8  4 1 0x36314752--         y  y  y     win,pb,str
0x34 16  0  5  6  5  0 24  8  4 1 0x36314752--         y  y  y     win,pb,str
0x35 16  0  5  6  5  0 24  0  4 1 0x36314752--         y  y  y     win,pb,str
0x36 16  0  5  6  5  0 24  0  4 1 0x36314752--         y  y  y     win,pb,str
0x37 16  0  5  6  5  0 16  0  4 1 0x36314752--         y  y  y     win,pb,str
0x38 16  0  5  6  5  0 16  0  4 1 0x36314752--         y  y  y     win,pb,str
0x39 16  0  5  6  5  0  0  8  4 1 0x36314752--         y  y  y     win,pb,str
0x3a 16  0  5  6  5  0  0  8  4 1 0x36314752--         y  y  y     win,pb,str
0x3b 16  0  5  6  5  0  0  0  4 1 0x36314752--         y  y  y     win,pb,str
0x3c 16  0  5  6  5  0  0  0  4 1 0x36314752--         y  y  y     win,pb,str
0x3d 16  0  5  6  5  0 24  8  8 1 0x36314752--         y  y  y     win,pb,str
0x3e 16  0  5  6  5  0 24  0  8 1 0x36314752--         y  y  y     win,pb,str
0x3f 16  0  5  6  5  0 16  0  8 1 0x36314752--         y  y  y     win,pb,str
0x40 16  0  5  6  5  0  0  8  8 1 0x36314752--         y  y  y     win,pb,str
0x41 16  0  5  6  5  0  0  0  8 1 0x36314752--         y  y  y     win,pb,str
Wayland platform:
eglinfo: eglInitialize failed
X11 platform:
eglinfo: eglInitialize failed
Device platform:
EGL API version: 1.5
EGL vendor string: NVIDIA
EGL version string: 1.5
EGL client APIs: OpenGL_ES OpenGL
EGL extensions string:
EGL_ANDROID_native_fence_sync EGL_EXT_buffer_age EGL_EXT_client_sync
EGL_EXT_create_context_robustness EGL_EXT_image_dma_buf_import
EGL_EXT_image_dma_buf_import_modifiers EGL_MESA_image_dma_buf_export
EGL_EXT_output_base EGL_EXT_output_drm EGL_EXT_protected_content
EGL_EXT_stream_consumer_egloutput EGL_EXT_stream_acquire_mode
EGL_EXT_sync_reuse EGL_IMG_context_priority EGL_KHR_config_attribs
EGL_KHR_create_context_no_error EGL_KHR_context_flush_control
EGL_KHR_create_context EGL_KHR_fence_sync
EGL_KHR_get_all_proc_addresses EGL_KHR_partial_update
EGL_KHR_swap_buffers_with_damage EGL_KHR_no_config_context
EGL_KHR_gl_colorspace EGL_KHR_gl_renderbuffer_image
EGL_KHR_gl_texture_2D_image EGL_KHR_gl_texture_3D_image
EGL_KHR_gl_texture_cubemap_image EGL_KHR_image EGL_KHR_image_base
EGL_KHR_reusable_sync EGL_KHR_stream EGL_KHR_stream_attrib
EGL_KHR_stream_consumer_gltexture EGL_KHR_stream_cross_process_fd
EGL_KHR_stream_fifo EGL_KHR_stream_producer_eglsurface
EGL_KHR_surfaceless_context EGL_KHR_wait_sync EGL_NV_nvrm_fence_sync
EGL_NV_quadruple_buffer EGL_NV_stream_consumer_eglimage
EGL_NV_stream_cross_display EGL_NV_stream_cross_object
EGL_NV_stream_cross_process EGL_NV_stream_cross_system
EGL_NV_stream_dma EGL_NV_stream_flush EGL_NV_stream_metadata
EGL_NV_stream_remote EGL_NV_stream_reset EGL_NV_stream_socket
EGL_NV_stream_socket_inet EGL_NV_stream_socket_unix
EGL_NV_stream_sync EGL_NV_stream_fifo_next
EGL_NV_stream_fifo_synchronous EGL_NV_stream_consumer_gltexture_yuv
EGL_NV_stream_attrib EGL_NV_stream_origin EGL_NV_system_time
EGL_NV_output_drm_flip_event EGL_NV_triple_buffer
EGL_NV_robustness_video_memory_purge
Configurations:
bf lv colorbuffer dp st  ms    vis   cav bi  renderable  supported
id sz  l  r  g  b  a th cl ns b    id   eat nd gl es es2 vg surfaces
---------------------------------------------------------------------
0x01 32  0  8  8  8  8 24  8  0 0 0x00--         y  y  y     pb,str
0x02 32  0  8  8  8  8 24  0  0 0 0x00--         y  y  y     pb,str
0x03 32  0  8  8  8  8  0  8  0 0 0x00--         y  y  y     pb,str
0x04 32  0  8  8  8  8  0  0  0 0 0x00--         y  y  y     pb,str
0x05 32  0  8  8  8  8 24  8  2 1 0x00--         y  y  y     pb,str
0x06 32  0  8  8  8  8 24  0  2 1 0x00--         y  y  y     pb,str
0x07 32  0  8  8  8  8  0  8  2 1 0x00--         y  y  y     pb,str
0x08 32  0  8  8  8  8  0  0  2 1 0x00--         y  y  y     pb,str
0x09 32  0  8  8  8  8 24  8  4 1 0x00--         y  y  y     pb,str
0x0a 32  0  8  8  8  8 24  8  4 1 0x00--         y  y  y     pb,str
0x0b 32  0  8  8  8  8 24  0  4 1 0x00--         y  y  y     pb,str
0x0c 32  0  8  8  8  8 24  0  4 1 0x00--         y  y  y     pb,str
0x0d 32  0  8  8  8  8  0  8  4 1 0x00--         y  y  y     pb,str
0x0e 32  0  8  8  8  8  0  8  4 1 0x00--         y  y  y     pb,str
0x0f 32  0  8  8  8  8  0  0  4 1 0x00--         y  y  y     pb,str
0x10 32  0  8  8  8  8  0  0  4 1 0x00--         y  y  y     pb,str
0x11 32  0  8  8  8  8 24  8  8 1 0x00--         y  y  y     pb,str
0x12 32  0  8  8  8  8 24  0  8 1 0x00--         y  y  y     pb,str
0x13 32  0  8  8  8  8  0  8  8 1 0x00--         y  y  y     pb,str
0x14 32  0  8  8  8  8  0  0  8 1 0x00--         y  y  y     pb,str
0x15 24  0  8  8  8  0 24  8  0 0 0x00--         y  y  y     pb,str
0x16 24  0  8  8  8  0 24  0  0 0 0x00--         y  y  y     pb,str
0x17 24  0  8  8  8  0  0  8  0 0 0x00--         y  y  y     pb,str
0x18 24  0  8  8  8  0  0  0  0 0 0x00--         y  y  y     pb,str
0x19 24  0  8  8  8  0 24  8  2 1 0x00--         y  y  y     pb,str
0x1a 24  0  8  8  8  0 24  0  2 1 0x00--         y  y  y     pb,str
0x1b 24  0  8  8  8  0  0  8  2 1 0x00--         y  y  y     pb,str
0x1c 24  0  8  8  8  0  0  0  2 1 0x00--         y  y  y     pb,str
0x1d 24  0  8  8  8  0 24  8  4 1 0x00--         y  y  y     pb,str
0x1e 24  0  8  8  8  0 24  8  4 1 0x00--         y  y  y     pb,str
0x1f 24  0  8  8  8  0 24  0  4 1 0x00--         y  y  y     pb,str
0x20 24  0  8  8  8  0 24  0  4 1 0x00--         y  y  y     pb,str
0x21 24  0  8  8  8  0  0  8  4 1 0x00--         y  y  y     pb,str
0x22 24  0  8  8  8  0  0  8  4 1 0x00--         y  y  y     pb,str
0x23 24  0  8  8  8  0  0  0  4 1 0x00--         y  y  y     pb,str
0x24 24  0  8  8  8  0  0  0  4 1 0x00--         y  y  y     pb,str
0x25 24  0  8  8  8  0 24  8  8 1 0x00--         y  y  y     pb,str
0x26 24  0  8  8  8  0 24  0  8 1 0x00--         y  y  y     pb,str
0x27 24  0  8  8  8  0  0  8  8 1 0x00--         y  y  y     pb,str
0x28 24  0  8  8  8  0  0  0  8 1 0x00--         y  y  y     pb,str
0x29 16  0  5  6  5  0 24  8  0 0 0x00--         y  y  y     pb,str
0x2a 16  0  5  6  5  0 24  0  0 0 0x00--         y  y  y     pb,str
0x2b 16  0  5  6  5  0 16  0  0 0 0x00--         y  y  y     pb,str
0x2c 16  0  5  6  5  0  0  8  0 0 0x00--         y  y  y     pb,str
0x2d 16  0  5  6  5  0  0  0  0 0 0x00--         y  y  y     pb,str
0x2e 16  0  5  6  5  0 24  8  2 1 0x00--         y  y  y     pb,str
0x2f 16  0  5  6  5  0 24  0  2 1 0x00--         y  y  y     pb,str
0x30 16  0  5  6  5  0 16  0  2 1 0x00--         y  y  y     pb,str
0x31 16  0  5  6  5  0  0  8  2 1 0x00--         y  y  y     pb,str
0x32 16  0  5  6  5  0  0  0  2 1 0x00--         y  y  y     pb,str
0x33 16  0  5  6  5  0 24  8  4 1 0x00--         y  y  y     pb,str
0x34 16  0  5  6  5  0 24  8  4 1 0x00--         y  y  y     pb,str
0x35 16  0  5  6  5  0 24  0  4 1 0x00--         y  y  y     pb,str
0x36 16  0  5  6  5  0 24  0  4 1 0x00--         y  y  y     pb,str
0x37 16  0  5  6  5  0 16  0  4 1 0x00--         y  y  y     pb,str
0x38 16  0  5  6  5  0 16  0  4 1 0x00--         y  y  y     pb,str
0x39 16  0  5  6  5  0  0  8  4 1 0x00--         y  y  y     pb,str
0x3a 16  0  5  6  5  0  0  8  4 1 0x00--         y  y  y     pb,str
0x3b 16  0  5  6  5  0  0  0  4 1 0x00--         y  y  y     pb,str
0x3c 16  0  5  6  5  0  0  0  4 1 0x00--         y  y  y     pb,str
0x3d 16  0  5  6  5  0 24  8  8 1 0x00--         y  y  y     pb,str
0x3e 16  0  5  6  5  0 24  0  8 1 0x00--         y  y  y     pb,str
0x3f 16  0  5  6  5  0 16  0  8 1 0x00--         y  y  y     pb,str
0x40 16  0  5  6  5  0  0  8  8 1 0x00--         y  y  y     pb,str
0x41 16  0  5  6  5  0  0  0  8 1 0x00--         y  y  y     pb,str
STDERR: error: XDG_RUNTIME_DIR not set in the environment.
error: XDG_RUNTIME_DIR not set in the environment.
completed
```


# Deployed on Runpod (bad case)

Nb: runpod logs are newest firsrt

```
2024-03-22 12:45:42.571 - [t9ma4uv4xl11bf] - [info] - Finished.
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] -
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] - error: XDG_RUNTIME_DIR not set in the environment. 
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] - STDERR: error: XDG_RUNTIME_DIR not set in the environment. -
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] - 
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] - 
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] eglinfo: eglInitialize failed - 
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] Device platform: - 
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info]
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] - eglinfo: eglInitialize failed
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] - X11 platform:
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] - 
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] - eglinfo: eglInitialize failed - 
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] - Wayland platform: - 
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] - 
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] - eglinfo: eglInitialize failed - 
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] - GBM platform: - 
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] - 
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] - EGL_MESA_platform_surfaceless - 
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] - EGL_MESA_platform_gbm EGL_KHR_platform_gbm - 
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] - EGL_EXT_platform_x11 EGL_KHR_platform_x11 EGL_EXT_platform_xcb -
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] - EGL_EXT_platform_wayland EGL_KHR_platform_wayland - 
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] - EGL_EXT_client_extensions EGL_KHR_debug EGL_EXT_platform_device - 
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] - EGL_EXT_platform_base EGL_KHR_client_get_all_proc_addresses - 
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] - EGL_EXT_device_base EGL_EXT_device_enumeration EGL_EXT_device_query - 
2024-03-22 12:45:42.324 - [t9ma4uv4xl11bf] - [info] - STDOUT: EGL client extensions string: - 
2024-03-22 12:45:42.319 - [t9ma4uv4xl11bf] - [info] - Started.
```


# Deployed on Replicate (bad case)


```
STDOUT: EGL client extensions string:
EGL_EXT_device_base EGL_EXT_device_enumeration EGL_EXT_device_query
EGL_EXT_platform_base EGL_KHR_client_get_all_proc_addresses
EGL_EXT_client_extensions EGL_KHR_debug EGL_EXT_platform_device
EGL_EXT_platform_wayland EGL_KHR_platform_wayland
EGL_EXT_platform_x11 EGL_KHR_platform_x11 EGL_EXT_platform_xcb
EGL_MESA_platform_gbm EGL_KHR_platform_gbm
EGL_MESA_platform_surfaceless
GBM platform:
eglinfo: eglInitialize failed
Wayland platform:
eglinfo: eglInitialize failed
X11 platform:
eglinfo: eglInitialize failed
Device platform:
eglinfo: eglInitialize failed
STDERR: error: XDG_RUNTIME_DIR not set in the environment.
error: XDG_RUNTIME_DIR not set in the environment.
```