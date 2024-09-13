###### .配置ntp时间同步

时间不同步会导致hadoop启动失败,hive启动失败等,所以需要配置时间同步或者三台机器使用

要进行NTP时间同步配置，您可以按照以下步骤进行：

1. 安装NTP软件

在Linux系统上，您可以使用以下命令(<u>在线</u>)安装NTP软件：

```
sudo yum -y install ntp
```

2. master:配置NTP服务器

您可以在 `/etc/ntp.conf` 文件中配置NTP服务器。找到 `server` 关键字，设置同步服务器为master

例如：

```shell
#注释掉自带的

#server 0.centos.pool.ntp.org iburst
#server 1.centos.pool.ntp.org iburst
#server 2.centos.pool.ntp.org iburst
#server 3.centos.pool.ntp.org iburst
#添加下面内容
server 127.127.1.0
fudge 127.127.1.0 stratum 10
```

3. slave1:配置ntp客户端

```shell
#注释掉自带的
#server 0.centos.pool.ntp.org iburst
#server 1.centos.pool.ntp.org iburst
#server 2.centos.pool.ntp.org iburst
#server 3.centos.pool.ntp.org iburst
#添加服务段ip
server 192.168.85.11

scp分发到第三台机器
```



4.三台机器启动NTP服务并查看状态

执行以下命令来启动NTP服务：

```shell
systemctl start ntpd
systemctl status ntpd
```

5.验证时间同步

使用以下命令来检查时间同步是否正常运行：

```shell
#查看时间同步服务器
ntpq -p

#手动时间同步(默认64秒)
ntpdate -u 192.168.85.11
#检查三台机器时间
date
```



或者三台机器同时使用<u>date -s "2023-05-01 13:38:00"</u>设置日期时间