#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f','--files', type=str, help='List of files to include (example : "./some_datas.py,./other_files.txt,./main.py)"', required=True)
parser.add_argument('-m', '--main', type=str, help='Specify the main file', required=True)
parser.add_argument('-p', '--path', type=str, help='Specify the output path', required=True)


def create_dockerfile(files, main):
    files = " ".join(files.split(","))
    
    return f"""FROM alpine:3.16.0

ARG DEBIAN_FRONTEND=noninteractive
WORKDIR /app/

RUN apk add socat python3 py-pip

RUN python3 -m pip install pycryptodome

COPY {files} /app/

RUN addgroup -S ctf && \
    adduser -S player -G ctf && \
    chmod u+s /app/{main}

RUN echo "FLAG(PLACEHOLDER_GG)" > /app/flag.txt
RUN chown player:ctf /app/{main}
USER player

ENTRYPOINT ["socat","TCP-LISTEN:3000,reuseaddr,fork","EXEC:'python3.10 /app/{main}',stderr"]"""

def create_dockercompose():
    return f"""version: "1"
services:
  lemote:
    build:
      context: ./
      dockerfile: Dockerfile
    ports:
      - 3000"""

if __name__ == "__main__":
    args = parser.parse_args()
    files = args.files
    main_file = args.main
    path = args.path
    dockerfile = create_dockerfile(files, main_file)
    docker_compose = create_dockercompose()

    with open(f"{path}/Dockerfile","w") as f:
        f.write(dockerfile)
    with open(f"{path}/docker-compose.yml", "w") as f:
        f.write(docker_compose)
