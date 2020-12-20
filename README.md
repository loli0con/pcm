# ProducerConsumerModel

### 运行结果

##### mac
> intel i5-5257U, 8G RAM
- 1生产者,生产1000000个产品，由1个消费者处理,耗时为246.39605402946472秒
- 1生产者,生产1000000个产品，由2个消费者处理,耗时为237.65198636054993秒
- 2生产者,生产1000000个产品，由4个消费者处理,耗时为229.00558400154114秒

##### win
> intel i7-4790K, 16G RAM
- 1生产者,生产1000000个产品，由1个消费者处理,耗时为172.08207082748413秒
- 1生产者,生产1000000个产品，由2个消费者处理,耗时为161.05003571510315秒
- 2生产者,生产1000000个产品，由4个消费者处理,耗时为151.66406607627870秒

### 想法
1. 更多的消费者和生产者并没有线性地加速整个程序的运行速度。  
对比win和mac的运行结果(不同的硬件设备)，同样表现出该现象。  
个人估计瓶颈出现在了进程队列上。
