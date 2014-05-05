fabric_project
==============

fabric project

Usage:
=============
1、首先要在服务器上安装fabric
 安装方法请见官方的文档
2、下载代码
 git clone https://github.com/yekeqiang/fabric_project
3、进入fabric_project的stockd目录
  cd stockd
4、查看可用的fab的列表
   fab -l 

可以看到有如下的模块可用：

Available commands:

    comment_crontabl
    get_host_name
    get_version
    kill_apps_stockd
    offline_stockd
    shutdown_stockd

5、运行相关命令：

1）获取主机名
fab get_host_name
2) 获取版本
fab get_version
3) 注销crontab
fab comment_crontabl
4) 停止所有的stockd服务
fab kill_apps_stockd
5) 批量关机
fab shutdown_stockd

待优化：
1、把主机列表单独放置一个配置文件中