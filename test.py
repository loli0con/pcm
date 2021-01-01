from main import Main
import os

lst = [
    # (生产者数量，消费者数量),
    (1, 1),
    (1, 2),
    (2, 2),
    (2, 4)
]

if __name__ == '__main__':
    # 用于写实验报告-实验结果及讨论
    for pn, cn in lst:
        m = Main(queue_type="redis_queue",
                 queue_argument={"host": os.getenv("REDIS_HOST")},
                 product_number=200,
                 producer_number=pn, consumer_number=cn)
        m.run()
