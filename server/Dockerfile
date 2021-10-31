FROM python:3.8.6

RUN apt update && apt install -y \
  sudo \
  wget \
  vim \
  mecab \
  libmecab-dev \
  mecab-ipadic-utf8 \
  git \
  make \
  curl \
  xz-utils \
  file

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
RUN cd mecab-ipadic-neologd && \
  ./bin/install-mecab-ipadic-neologd -n -y && \
  echo "dicdir=/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd">/etc/mecabrc && \
  mv /etc/mecabrc /usr/local/etc/

WORKDIR /server

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV HOST 0.0.0.0

CMD ["uwsgi", "--ini", "uwsgi.ini"]