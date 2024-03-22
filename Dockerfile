FROM nvidia/cuda:12.3.2-cudnn9-devel-ubuntu22.04

# Install build tools
 RUN apt-get update && \
     apt-get install --no-install-recommends -y \
        mesa-utils \
        #libegl1-mesa-dev \
        #libegl1 \
        #libgbm1 \
        python3 \
        python3-pip \
     && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

WORKDIR /app
COPY ./handler.py /app/handler.py

ENV EGL_PLATFORM=surfaceless NVIDIA_DRIVER_CAPABILITIES=all

CMD [ "python3", "-u", "handler.py"]

