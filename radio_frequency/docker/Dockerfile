FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y wget python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


COPY search_path.sh extract_path_value.py config.txt /tmp/
RUN chmod +x /tmp/search_path.sh /tmp/extract_path_value.py