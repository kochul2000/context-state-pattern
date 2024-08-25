# for dev test
FROM debian:bookworm
# 환경변수 설정
ENV PYTHONUNBUFFERED=1
# apt package install
RUN apt update && apt install --no-install-recommends -y \
  python3 python3-pip python3-setuptools python3-wheel python-is-python3

# dependencies install
WORKDIR /opt/app/
COPY ./app/requirements.txt .
RUN pip3 install -r requirements.txt --break-system-packages

# copy source code
# For development, the code is mounted instead of being copied to avoid duplication.
# If deploying with Docker, the code should be copied.
# COPY ./app .

# start service
CMD ["python3", "main.py"]
