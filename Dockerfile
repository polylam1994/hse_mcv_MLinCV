FROM ubuntu:20.04 as builder

# set OS without UI
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies for ubuntu build
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && apt-get install -y --no-install-recommends python3 python3-pip python3.8-venv python3.8-dev

RUN apt-get install -y --fix-missing ffmpeg libsm6 libxext6

RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install build

#install requirements and package
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY dist/hse_mcv_dbface-0.0.4-py3-none-any.whl .
RUN python3 -m pip install --user hse_mcv_dbface-0.0.4-py3-none-any.whl \
    && python3 -m pip install --user streamlit

WORKDIR /web_demo
COPY src/hse_mcv_dbface/streamlit_app.py /web_demo

# run streamlit app via localhost:8501
EXPOSE 8501

CMD streamlit run streamlit_app.py
