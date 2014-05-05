#!/usr/bin/python env
# -*- coding: utf-8 -*-
from fabric.api import env
from fabric.api import cd
from fabric.api import run
from fabric.api import local
from fabric.api import get
from fabric.api import put
 


env.user = 'username'
env.password = 'passwd'
env.hosts = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4']
 
def get_version():
    local('cat /etc/issue')
    run('cat /etc/issue')
    #with cd('/root/'):
    #    put('/home/libaoyin/test.txt', 'test.txt', mode=0755)
    #    get('hello_world.txt')
    run('ls')
 
def get_host_name():
    run('hostname')

#kill all stockd'service
def kill_apps_stockd():
    run('killall stockd')

#discharge the crontab
def comment_crontabl():
    put ('/home/apps/ykq/crontab.txt','crontab.txt')
    run('crontab crontab.txt')

# offline stockd's service
def offline_stockd():
    kill_apps_stockd()
    comment_crontabl()

#shutdown all stockd server
def shutdown_stockd_server():
    run('sudo poweroff')