import redis

redis_host = '192.168.2.90'

client = redis.Redis(host=redis_host, port=6379, password='huN7e4_123', decode_responses=True)  

def counter(video_id):
    # 设置 key video_id的值是runoob
    # client.set('video_id', 'runoob')

    # 将 key 中储存的数字值增一
    client.incr(video_id)

    current_cnt = client.get(video_id)

    print(current_cnt)

if __name__ == '__main__':
    counter(1001) # 返回 1  
    counter(1001) # 返回 2  
    counter(1002) # 返回 1    
    counter(1001) # 返回 3  
    counter(1002) # 返回 2  