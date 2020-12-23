# ProducerConsumerModel

### 运行说明
- 请安装redis库，可以运行requirement.py安装，也可以手动安装
- 请自行配置好redis
- 使用main.py函数运行程序
- queue_type只支持redis_queue和process_queue
- 使用redis_queue时，请参考[RedisQueue](redis_queue.py)的初始化方法，在queue_argument参数中传入redis的相关信息

### 运行结果
###### (使用进程队列,即process_queue.py)
##### mac
> intel i5-5257U, 8G RAM
- 1生产者,生产1000000个产品,由1个消费者处理,耗时为246.39605402946472秒
- 1生产者,生产1000000个产品,由2个消费者处理,耗时为237.65198636054993秒
- 2生产者,生产1000000个产品,由4个消费者处理,耗时为229.00558400154114秒

##### win
> intel i7-4790K, 16G RAM
- 1生产者,生产1000000个产品,由1个消费者处理,耗时为172.08207082748413秒
- 1生产者,生产1000000个产品,由2个消费者处理,耗时为161.05003571510315秒
- 2生产者,生产1000000个产品,由4个消费者处理,耗时为151.66406607627870秒

### 想法
1. 更多的消费者和生产者并没有线性地加速整个程序的运行速度。  
对比win和mac的运行结果(不同的硬件设备)，同样表现出该现象。  
个人估计瓶颈出现在了进程队列上。求大佬指点。

2. MyQueue(ProcessQueue)里面包含了三个对象：  
信号量，表示生产是否已经结束  
进程锁，保证信号量的安全  
进程队列，来自标准库

### 参考资料
https://www.runoob.com/redis/redis-tutorial.html  
https://www.runoob.com/w3cnote/python-redis-intro.html  
https://cloud.tencent.com/developer/article/1151834  
https://blog.csdn.net/xuelians/article/details/79999275  
https://python-cookbook-3rd-edition.readthedocs.io/zh_CN/latest/c05/p21_serializing_python_objects.html  
https://blog.csdn.net/weixin_41935140/article/details/81153611  