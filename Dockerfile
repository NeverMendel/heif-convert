FROM alpine:3.19.0

RUN apk add --no-cache \
      nss \
      ca-certificates \
      python3 \
      py3-pip

# Copy current directory to /usr/src/app
ADD . /usr/app
WORKDIR /usr/app

# Create out folder
RUN mkdir -p out

# Install heif-convert
RUN pip3 install .

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
