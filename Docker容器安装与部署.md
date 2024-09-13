# Docker容器安装与部署

Docker 是一种容器化平台，它允许您在独立的、轻量级容器中打包、分发和运行应用程序和服务。每个 Docker 容器包含应用程序及其所有依赖项，包括库、运行时环境和配置文件。类似于虚拟机,但比虚拟机更轻量。

- 快速部署

## Windows部署

### 1.安装适用于Windos的Linux子系统(win7/10无需配置,但需要打开hyper-v) 

- 打开windows终端(管理员)

- 安装基于ubuntu-20.04的wsl

  ```bash
  wsl --install -d Ubuntu-20.04
  ```
  
- 设置Ubuntu用户名与密码

- 启动ubuntu终端

  ```bash
  wsl
  ```
  
- wsl其他常用命令

  ```bash
  wsl -l -o #列出wsl可使用的linux发行版
  wsl --status #查看wsl状态信息
  wsl --set-default-version 2 #设置默认wsl版本
  wsl -l -v #检查已安装的linux发行版所使用的wsl版本
  ```

  

### 2.安装Docker

1. 使用链接下载

https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module

2. 开始安装

双击安装程序,勾选 **WSL2** =>点击 **OK**

3. 启动并配置

- 双击桌面的 **Docker Desktop** 图标

- 点击右上角 **设置**	=>  **Resources** => **WSL integration** => **勾选Ubuntu-20.04**

- 点击 **Docker Engine** => **修改配置**

```json
{
  "builder": {
    "gc": {
      "defaultKeepStorage": "20GB",
      "enabled": true
    }
  },
  "debug": true,
  "experimental": false,
  "insecure-registries": [],
  "registry-mirrors": [
    "http://hub-mirror.c.163.com",
    "https://docker.mirrors.ustc.edu.cn"
  ]
}
```

- 点击 **Software updates** => **取消勾选Automatically check for updates** =>点击 **Apply&restart**

### 3.下载镜像和创建容器

1. 打开ubuntu终端

   ```
   wsl
   ```

2. 验证docker环境

   ```bash
   docker --version
   Docker version 24.0.5, build ced0996
   ```

3. 下载centos7镜像

   ```bash
 docker pull centos:7
   ```

4. 创建容器

   ```bash
   '''
   
   - `-p 60001:22`: 这个选项将容器的端口映射，将容器内的 SSH 服务（默认端口22）映射到主机的端口60001。
   
   
   - `--name master`: 这个选项为容器指定了一个名称，即容器的名称为 "master"。
   -- `privileged`: 这个选项为容器提供了特权访问，允许容器内的进程拥有与宿主机相同的权限。请注意，使用 --privileged 选项可能会有安全风险，因为容器内的进程将拥有更高的权限。
   
   - `-itd`: 这个选项结合了 `-i`（交互式）、`-t`（分配伪终端）、和 `-d`（后台运行）选项，允许你以交互式方式在容器内执行命令，并将容器放入后台运行。
   
   - `--restart=always`: 这个选项指定容器总是在退出时自动重启。
   
   - `centos:7`: 这是使用的基础镜像，即 CentOS 7。
   
   - `/usr/sbin/init`: 这是容器内部启动的命令，通常用于启动系统初始化进程。这个命令启动了容器中的初始化系统。
   - `hostname`:固定主机名,如果不在创建容器时固定,每次重启主机名都会被重置
   '''
   
   docker run --privileged -p 60001:22 --name master --hostname master -itd --restart=always centos:7 /usr/sbin/init
   docker run --privileged -p 60002:22 --name slave1 -itd --hostname slave1 --restart=always centos:7 /usr/sbin/init
   docker run --privileged -p 60003:22 --name slave2 -itd --hostname slave2 --restart=always centos:7 /usr/sbin/init
   
   ```
   

### 4.配置容器基础环境

1. 分别三台进入容器

   ```bash
     docker exec -it master /bin/bash
     docker exec -it slave1 /bin/bash
     docker exec -it slave2 /bin/bash
   ```

2. 分别修改主机名(容器重启后用户名和ip会重新分配)

   ```bash
   hostname master
   bash
   hostname slave1
   bash
   hostname slave2
   bash
   ```

3. 安装基本工具

   ```bash
   yum install vim -y
   yum install net-tools.x86_64 -y
   yum install passwd openssl openssh-server -y
   yum install openssh-clients -y
   ```

4. 启动ssh服务

```
systemctl start sshd
```

   5.设置root密码

```
passwd root
```

即可使用ssh root@ip连接

   6.复制软件包的master容器中

```bash
[root@master opt]# mkdir software
docker cp 宿主机文件 master:/opt/software
```

   7.将容器打包成镜像

```bash
docker commit master centos:master
docker commit slave1 centos:slave1
docker commit slave2 centos:slave2
```

如需在其他机器docker中使用可以:

- 将镜像输出为tar文件

```bash
docker save centos:master -o  master.tar
docker save centos:slave1 -o  slave1.tar
docker save centos:slave2 -o  slave2.tar
```

- 通过tar加载镜像

```bash
 docker load master.tar
 docker load slave1.tar
 docker load slave2.tar
```

8. 至此集群搭建docker环境搭建完毕,如搭建完毕需重置环境,可以使用下面命令重新创建容器

```bash
docker rm -f master slave1 slave2
docker run --privileged -p 60001:22 --name master -itd --hostname master --restart=always centos:master /usr/sbin/init
docker run --privileged -p 60002:22 --name slave1 -itd --hostname slave1 --restart=always centos:slave1 /usr/sbin/init
docker run --privileged -p 60003:22 --name slave2 -itd --hostname slave2 --restart=always centos:slave2 /usr/sbin/init
```



## Ubuntu部署

###  1: 更新包列表
```bash
sudo apt update
```

###  2: 安装必要的依赖项
```bash
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
```

###  3: 添加Docker官方GPG密钥
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

###  4: 添加Docker存储库
```bash
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

###  5: 更新包列表（再次）
```bash
sudo apt update
```

###  6: 安装Docker
```bash
sudo apt install -y docker-ce docker-ce-cli containerd.io
```

###  7: 启动并设置Docker服务
```bash
sudo systemctl start docker
sudo systemctl status docker
sudo systemctl enable docker
```

###  8: 验证安装
```bash
sudo docker --version
```

## Docker教程

### 1.例子-部署MySQL

#### 1.打开ubuntu终端

#### 2.下载镜像(image)并运行容器

```bash
#docker run 创建并运行成一个容器
#-d 让容器后台运行
#--name 容器名
#-p 外部:内部 设置端口映射 
#-e 设置环境变量(参数)  在这里为时区和root密码
#镜像:版本号(如省略版本默认最新版)

docker run -d \
--name mysql \
-p 3636:3306 \
-e TZ=Asia/Shanghai \
-e MYSQL_ROOT_PASSWORD=123456 \
mysql
```

ps:

```
当我们利用Docker安装应用时，Docker会自动搜索并下载应用镜像（image）。镜像不仅包含应用本身，还包含应用
运行所需要的环境、配置、系统函数库。Docker会在运行镜像时创建一个隔离环境，称为容器（container）。

Docker是做什么的?
Docker可以帮助我们下载应用镜像，创建并运行镜像的容器，从而快速部署应用

什么是镜像?
将应用所需的函数库、依赖、配置等与应用一起打包得到的就是镜像

什么是容器?
为每个镜像的应用进程创建的隔离运行环境就是容器

什么是镜像仓库?
存储和管理镜像的服务就是镜像仓库，
DockerHub是目前最大的镜像仓库，其中包含各种常见的应用镜像
```



#### 3.查看运行中的镜像

```
docker ps
```



### 2.常用命令

详见官方文档 https://docs.docker.com/

#### 1.镜像操作


| 指令               | 说明                         |
|--------------------|----------------------------|
| docker pull 镜像:版本 | 下载指定版本的镜像             |
| docker images      | 查看本地镜像                   |
| docker build       | 构建镜像                      |
| docker save        | 镜像打包                      |
| docker load        | 加载镜像                      |
| docker push        | 上传镜像                      |
| docker rmi         | 删除镜像                      |


#### 2.容器操作

| 指令                 | 说明                         |
|----------------------|----------------------------|
| docker run           | 创建并运行容器               |
| docker exec          | 进入容器                     |
| docker stop          | 停止容器                     |
| docker start         | 启动容器                     |
| docker restart       | 重启容器                     |
| docker rename        | 容器重命名                   |
| docker rm            | 删除容器                     |
| docker logs          | 查看容器日志                 |
| docker inspect       | 查看容器详细信息             |


#### 3.例子-部署 nginx

1.下载 nginx镜像

```bash
docker pull nginx
```

2.查看本地镜像列表

```bash
docker images
```
输出:
```bash
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
nginx        latest    f5a6b296b8a2   4 days ago      187MB
```

3.创建容器并运行

```bash
docker run -d --name nginx -p 80:80 nginx
```

4.查看正在容器进程

```bash
docker ps
```

5.查看日志

```bash
docker logs -f nginx #-f持续滚动
```

5.停止容器

```
docker stop nginx
```

6.修改容器名

```bash
docker rename nginx new_nginx
```

7.查看所有容器(包括未启动)

```
docker ps -a
```

8.执行(进入)容器

```bash
#exec执行bash
#it 返回一个终端
docker exec -it new_nginx /bin/bash
```

9.访问nginx

```bash
#在浏览器地址栏输入localhos访问web页面
```



10.删除容器

```bash
docker stop new_nginx
docker rm new_nginx
```

### 3.数据卷

数据卷（volume）是一个虚拟目录，是容器内目录与宿主机目录衣间映射的桥梁。

- 共享文件夹

为什么不让容器目录直接指向宿主机目录呢?

- 因为直接把容器目录与宿主机目录绑定，就与宿主机
  耦合了。假如将来切换了环境，宿主机目录发生了变
  更，容器就无法运行了。
- 而容器目录通过数据卷间接关联宿主机目录，如果宿
  主机目录发生变更，只要改变数据卷的指向即可

#### 1.数据券命令

| 命令                    | 说明                 |
| ----------------------- | -------------------- |
| `docker volume create`  | 创建数据卷           |
| `docker volume ls`      | 查看所有数据卷       |
| `docker volume rm`      | 删除指定数据卷       |
| `docker volume inspect` | 查看某个数据卷的详情 |
| `docker volume prune`   | 清除数据卷           |

#### 2.例子-挂载nginx的html数据卷

1.创建nginx容器并挂载名为html数据卷

```bash
#在执行docker run命令时，使用-v 数据卷:容器内目录可以完成数据卷挂载
#当创建容器时，如果挂载了数据卷且数据卷不存在，会自动创建数据卷
docker run -d \
--name nginx \
-p 80:80 \
-v html:/usr/share/nginx/html \
nginx
```



2.查看所有数据卷

```bash
docker volume ls
```

输出:

```bash
DRIVER    VOLUME NAME
local     html
```



3.查看html数据卷的详细信息

```bash
docker volume inspect html
```

输出:

```bash
[
    {
        "CreatedAt": "2023-09-12T08:16:59Z",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/html/_data",
        "Name": "html",
        "Options": null,
        "Scope": "local"
    }
]
```



4.找到html数据卷在磁盘中的位置

```
/var/lib/docker/volumes/html/_data
```



5.修改html数据卷下的index.html文件，查看页面是否变化

```bash
cd /var/lib/docker/volumes/html/_data
vim index.html
#修改后在浏览器输入localhost访问web页面
```



#### 3.例子-给mysql容器挂载本地目录



1.查看mysql容器，判断是否有数据卷挂载

```bash
docker inspect mysql
```

输出:

```bash
...
#数据卷
"Mounts": [
{
    "Type": "volume",
    "Name": "71bf07f53874bc9b2f5c3e5c87ad9d09ded1e73fea04b335647ecc627158ae0c",
    #挂载位置(匿名)
    "Source": "/var/lib/docker/volumes/71bf07f53874bc9b2f5c3e5c87ad9d09ded1e73fea04b335647ecc627158ae0c/_data",
    #数据存储目录
    "Destination": "/var/lib/mysql",
    "Driver": "local",
    "Mode": "",
    "RW": true,
    "Propagation": ""
            }
        ],
...
```



2.重新创建mysql容器，并完成目录挂载

- 挂载 mysql数据目录 到容器内的/var/lib/mysql目录

- 挂载 初始化脚本 到容器内的/docker-entrypoint-initdb.d目录

- 挂载 配置文件 到容器内的/etc/mysql/conf.d目录

```bash
#强行删除容器
docker rm mysql -f
#在执行docker run命令时，使用-v 本地目录：容器内目录可以完成本地目录挂载
#本地目录必须以“/”或"./“开头，如果直接以名称开头，会被识别为数据卷而非本地目录
#•-v mysql:/var/lib/mysql 会被识别为一个数据卷叫mysql，运行时会自动创建这个数据卷
#•-v./mysql:/var/lib/mysql 会被识别为当前目录下的mysql目录，如果不存在会自动创建



docker run -d \
--name mysql \
-p 3636:3306 \
-e TZ=Asia/Shanghai \
-e MYSQL_ROOT_PASSWORD=123456 \
-v /opt/mysql/data:/var/lib/mysql \
-v /opt/mysql/init:/docker-entrypoint-initdb.d \
-v /opt/mysql/conf:/etc/mysql/conf.d \
mysql


```

4.查看挂载的本地目录

```bash
master@Spark-pc:/opt/mysql$ ls
conf  data  init
```

5.进入mysql

```bash
master@Spark-pc:/opt/mysql$ docker exec -it mysql mysql -uroot -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.1.0 MySQL Community Server - GPL

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```



### 4.自定义镜像

镜像就是包含了应用程序、程序运行的系统函数库、运行配置等文件的文件包。构建镜像的过程其实就是把上述文件按
照顺序逐层打包。

Dockerfile就是一个文本文件，其中包含一个个的指令(Instruction)，用指令来说明要执行什么操作来构建镜像。将
来Docke?可以根据Dockerfile帮我们构建镜像。

#### 1.Dockerfile常用指令

| 指令       | 说明                                         |
| ---------- | -------------------------------------------- |
| FROM       | 指定基础镜像                                 |
| ENV        | 设置环境变量，可在后续指令使用               |
| COPY       | 拷贝本地文件到镜像的指定目录                 |
| RUN        | 执行Linux的shell命令，一般是安装过程的命令   |
| EXPOSE     | 指定容器运行时监听的端口，是给镜像使用者看的 |
| ENTRYPOINT | 镜像中应用的启动命令，容器运行时调用         |

#### 2.Dockerfile部署自定义java镜像

创建Dockerfile文件

  - 使用ubuntu作为基础镜像

```bash
#指定基础镜像
FROM ubuntu:18.04 
#配置环境变量，JDK的安装目录、容器内时区
ENV JAVA_DIR=/usr/local
ENV TZ=Asia/Shanghai
#拷贝jdk和java项目的包
COPY ./jdk8.tar.gz $JAVA_DIR/
COPY ./docker-demo.jar /tmp/app.jar
#设定时区
RUN ln -snf /usr/share/zoneinfo/ $TZ/etc/localtime && echo $TZ >/etc/timezone
#安装JDK
RUN cd $JAVA_DIR \ && tar -xf ./jdk8.tar.gz && mv ./jdk1.8.0_144 ./java8
#配置环境变量
ENV JAVA_HOME=$JAVA_DIR/java8
ENV PATH=$PATH:$JAVA_HOME/bin
#入口，java项目的启动命令
ENTRYPOINT ["java","-jar","/app.jar"]
```

   - 使用openjdk作为基础镜像

```bash
#基础镜像
FROM openjdk:11.0-jre-buster 
#设定时区
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/ $TZ/etc/localtime && echo $TZ >/etc/timezone
#拷贝jar包这里需要自己准备
COPY docker-demo.jar /app.jar
#入口
ENTRYPOINT ["java","-jar","/app.jar"]
```

#### 2.加载或者下载镜像

```bash
#下载
docker pull openjdk:11.0-jre-buster
#如果有tar的jdk镜像文件
docker load -i docker.tar
```



#### 3.构建dockerFile

```bash
# -t：是给镜像起名，格式依然是repository:tag的格 式，不指定tag时，默认为latest
# .：是指定Dockerfile所在目录，如果就在当前目录，则指定为"."

docker build -t 镜像名:版本号 dockerFile目录
```

#### 4.启动容器

```bash
docker run -d --name newDocker -p 8080:8080 镜像名:版本号
```



### 5. 网络

默认情况下，所有容器都是以bridge方式连接到Docker的一个虚拟网桥上

加入自定义网络的容器可以直接通过容器名互相访问,不必使用ip

#### 1.常用网络操作命令

| 命令                      | 说明                     |
| ------------------------- | ------------------------ |
| docker network create     | 创建一个网络             |
| docker network ls         | 查看所有网络             |
| docker network rm         | 删除指定网络             |
| docker network prune      | 清除未使用的网络         |
| docker network connect    | 使指定容器连接加入某网络 |
| docker network disconnect | 使指定容器连接离开某网络 |
| docker network inspect    | 查看网络详细信息         |

#### 2.创建新网络

```bash
docker network create newnet
```

#### 3.使已存在的容器连接到新网络

```bash
docker network connect 网络名 容器名
#如需创建容器时就自定义网络
#docker run -d --name xxx --network 网络名
```



### 6.  Docker Compose

Docker Compose通过一个单独的docker-compose.yml模板文件（YAML 格式）来定义一组相关联的应用容器，帮助我们实现多个相互关联的Docker容器的快速部署。

#### 1. Docker compose模板

创建名为docker-compose.yml的文件

```yaml
version: '3'
services:
  master:
    image: centos:master
    container_name: master
    privileged: true
    ports:
      - "60001:22"
    hostname: master
    restart: always
    command: /usr/sbin/init

  slave1:
    image: centos:slave1
    container_name: slave1
    privileged: true
    ports:
      - "60002:22"
    hostname: slave1
    restart: always
    command: /usr/sbin/init

  slave2:
    image: centos:slave2
    container_name: slave2
    privileged: true
    ports:
      - "60003:22"
    hostname: slave2
    restart: always
    command: /usr/sbin/init

```

```bash
#构建容器组 -f指定文件 up构建 -d后台运行
docker compose -f docker-compose.yml up -d
#进入容器
docker exec -it 容器名 /bin/bash
#删除容器组
docker compose -f docker-compose.yml down
```



#### 2. Docker compose常用命令

```bash
docker compose [option]
```



| 选项/命令 | 说明                                            |
| --------- | ----------------------------------------------- |
| `-f`      | 指定 Docker Compose 文件的路径和名称。          |
| `-P`      | 指定项目（Project）的名称。                     |
| `up`      | 创建并启动所有定义在 Compose 文件中的服务容器。 |
| `down`    | 停止并移除所有由 Compose 启动的容器和相关网络。 |
| `ps`      | 列出所有已启动的容器。                          |
| `logs`    | 查看指定容器的日志。                            |
| `stop`    | 停止指定的容器。                                |
| `start`   | 启动指定的容器。                                |
| `restart` | 重启指定的容器。                                |
| `top`     | 查看指定容器内运行的进程。                      |
| `exec`    | 在指定的正在运行的容器中执行命令。              |
