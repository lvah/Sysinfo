# Sysinfo
## 简介
sysinfo 使用 Python Django 框架和 psutil 开发的一个中文版 Linux 服务器信息查看应用，
可查看的信息包括系统、CPU、内存、硬盘、进程、网络、登录用户等，
同时可查看并导出部分数据的图表(正在更新完成中)。

## 需要安装的 Python 包
- Django==3.x
- psutil
```bash
# 安装项目需要的第三方python软件包
pip install -r requirements.txt
```

### 运行
```bash
python manage.py runserver
```
### 参考资料: 
Github参考网址: https://github.com/hypersport/sysinfo