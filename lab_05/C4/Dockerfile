FROM ubuntu:20.10

RUN sed -i 's/http:\/\/archive.ubuntu.com\/ubuntu/http:\/\/old-releases.ubuntu.com\/ubuntu/' /etc/apt/sources.list
RUN sed -i '/^deb.*security.ubuntu.com/s/^/#/' /etc/apt/sources.list
RUN apt update && apt install -y sudo net-tools openssh-client openssh-server
RUN apt-get install -y wireshark
RUN apt-get install -y tshark 
RUN useradd -m -s /bin/bash test && echo 'test:test' | chpasswd && adduser test sudo
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config


EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]