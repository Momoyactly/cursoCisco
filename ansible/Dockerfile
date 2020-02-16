FROM ubuntu:18.04


RUN apt-get update -y  && apt-get install -y python3-pip python3-dev

CMD ["apt-add-repository", "--yes", "--update", "ppa:ansible/ansible"] 

RUN apt install -y ansible

CMD ["ansible", "--version"]