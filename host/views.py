from django.shortcuts import render
from django.http import HttpResponse
import os
import platform
from datetime import datetime
import time
import psutil


# Create your views here.
# 需求1: 用户访问http://127.0.0.1:8000,返回主机的详情信息
def index(request):
    try:
        # 如果是Linux系统,执行下面内容
        # os.uname在windows系统中不能执行
        system_info = os.uname()
        node = system_info.nodename
        system = system_info.sysname
    except Exception as e:
        # 如果是Windows系统,执行下面内容
        system_info = platform.uname()
        node = system_info.node
        system = system_info.system

    boot_time = psutil.boot_time()
    boot_time = datetime.fromtimestamp(boot_time)
    now_time = datetime.fromtimestamp(time.time())
    info = {
        'node': node,
        'system': system,
        "kernel_name": system,
        'release': system_info.release,
        'version': system_info.version,
        'machine': system_info.machine,
        'now_time': now_time,
        'boot_time': boot_time,
        'boot_delta': now_time - boot_time
    }
    # 默认情况下返回的是普通字符串，不美观， 需要模板
    return render(request, 'host/index.html', {'info': info})

# 需求2:用户访问http://ip/disk/,返回磁盘分区的详细信息
def disk(request):
    # 获取系统所有的磁盘分区
    parts = psutil.disk_partitions()
    disks = []
    # 依次遍历获取每个分区的详细信息
    for part in parts:
        # 查看当前磁盘分区的使用率
        usage = psutil.disk_usage(part.device)
        # 每个分区的详细信息存储到列表中
        disk = {
            'device': part.device,
            'mountpoint': part.mountpoint,
            'fstype': part.fstype,
            'opts': part.opts,
            'total': usage.total,
            'percent': usage.percent
        }
        disks.append(disk)
    # 返回html页面信息
    return render(request, 'host/disk.html', {'disks': disks})

# 需求3：用户访问http://ip/users/,返回当前登录用户的详细信息
def users(requests):
    all_users = []
    # [suser(name='Fan', terminal=None, host=None, started=1595661568.4721968, pid=None)]
    users = psutil.users()
    for user in users:
        one_user = {
            'name':user.name,
            'host':user.host,
            'started': datetime.fromtimestamp(user.started)
        }
        all_users.append(one_user)
    return  render(requests, 'host/users.html', {'users':all_users})

# 需求4：用户访问http://ip/, diff/,返回html页面，可以让用户上传文件
def diff(request):
    return  render(request, 'host/diff.html')

