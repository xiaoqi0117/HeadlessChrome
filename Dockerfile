FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Shanghai
CMD echo "创建文件夹"


RUN \
    mkdir -p /usr/local \
    && mkdir /usr/local/java \
    && mkdir /app  \
    && mkdir /app/logs\
    && mkdir /app/data
CMD echo "复制文件"

COPY export.py /app
COPY requirements.txt /app
COPY docker/google-chrome-stable_current_amd64_86.deb /google-chrome-stable_current_amd64_86.deb
COPY docker/ttf-mscorefonts-installer_3.8_all.deb /ttf-mscorefonts-installer_3.8_all.deb

CMD echo "更新apt"
RUN \
   apt update &&  apt --fix-broken install

CMD echo "安装中文字体"
RUN \
   apt-get install -y language-pack-zh-han*
RUN \
   apt-get --fix-missing install -y fonts-droid-fallback fonts-arphic-ukai fonts-arphic-uming
RUN \
   apt --fix-broken install -y /ttf-mscorefonts-installer_3.8_all.deb

RUN \
   apt-get install -y  dbus

CMD echo "安装google-chrome"

UN \
   apt --fix-broken install -y  /google-chrome-stable_current_amd64_86.deb

CMD echo "安装google-chrome完成"

RUN \
   google-chrome -version \

CMD echo "安装python3.7"

# 安装系统依赖
RUN apt-get install -y \
    python3.7 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/* \

RUN \
   python3 --version

# 安装 Python 依赖
RUN python3 -m pip install --no-cache-dir -r /app/requirements.txt


CMD echo "设置系统编码"
ENV LANGUAGE=zh_CN.utf8
ENV LANG=zh_CN.utf8
ENV LC_ALL=zh_CN.utf8

EXPOSE 12306

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 运行应用
CMD ["python3", "/app/export.py"]
