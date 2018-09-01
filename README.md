# dht

# /dht 构造dht网络, 捕获种子

# supervisor 配置
/etc/supervisor/conf.d/dht.conf
```
[program:dht-worker]
process_name=%(program_name)s_%(process_num)02d
command=/bin/bash -c "source /opt/dht/venv/bin/activate && python /opt/dht/main.py"
autostart=true
autorestart=true
user=root
numprocs=1
redirect_stderr=true
stdout_logfile=/tmp/dht.log
```