# Redis QUEUE

## How To Use

Import module

```
from RedisQueue import RedisQueue
```

Define queue name

```
queue_name = 'whois_check'
```

Connect to Redis instance

```
r = RedisQUEUE(host='192.168.1.114', port=6379, db=0)
```

Fill the queue

```
r.set_item(queue_name, 'google1.com', unique=True)
r.set_item(queue_name, 'google1.com', unique=True)
r.set_item(queue_name, 'google2.com', unique=True)
r.set_item(queue_name, 'google3.com', unique=True)
r.set_item(queue_name, 'google4.com', unique=True)
r.set_item(queue_name, 'google5.com', unique=True)
```

Pop one item from queue

```
print r.pop_item(queue_name)
```

Show all items from queue

```
print r.get_queue(queue_name)
```
