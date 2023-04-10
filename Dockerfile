FROM python:3.9
COPY --from=openjdk:11.0-jre-slim /usr/local/openjdk-11 /usr/local/openjdk-11

ENV JAVA_HOME /usr/local/openjdk-11
ENV GOOGLE_APPLICATION_CREDENTIALS=./test-dev.json

RUN update-alternatives --install /usr/bin/java java /usr/local/openjdk-11/bin/java 1

RUN apt-get update
RUN apt-get install -y git gcc --no-install-recommends
RUN rm -rf /var/lib/apt/lists/*

# create project folder with the name test_root
RUN mkdir /test_root

# project scope
WORKDIR /test_root

COPY . /test_root

# install requirements
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH="/opt/venv/lib/python3.9/site-packages"
RUN python3 -m venv /opt/venv && pip3 install -r requirements.txt

# Set Docker entry
RUN pwd
RUN chmod +x /test_root/docker-entry_dev.sh
ENTRYPOINT ["/test_root/docker-entry_dev.sh"]