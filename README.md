# dht 网络爬虫

建议先了解 (BitTorrent DHT)[http://justjavac.com/other/2015/02/01/bittorrent-dht-protocol.html]

# 支持
- mysql
- redis

# 配置
```cp .env.example .env```

# 部署


```git clone https://github.com/douyacun/Bittorrent```

```cd Bittorrent```

```virtualenv --no-site-packages venv```

```pip install -r requirements.txt```

```python main.py```


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