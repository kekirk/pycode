#! --*--coding:utf-8--*--
# pip install redis
from redis import StrictRedis
# https://www.cnblogs.com/cnkai/p/7642787.html
redis = StrictRedis(host="localhost",port=6379,db=0,password='masterpasswd')
print(redis)

# String操作
print(redis.set("name","value")) #True
print(redis.get("name"))
print(redis.getset("name","newvalue"))
print(redis.set("phone","12345"))
vl = redis.mget(['name','phone'])
print(redis.setnx("newname","value"))
redis.setex("newname",60,"newvalue")
print(redis.setnx("string","valueaaaaaaaaaa"))
redis.setrange("string",6,"bbb")
print(redis.substr("string",6,9))
print(redis.getrange("string",6,9))

# key操作

print(redis.exists("string"))
print(redis.type("string"))
print(redis.delete("string"))
print(redis.keys())
print(redis.randomkey())
print(redis.ttl("name"))
print(redis.move("name",2))
print(redis.flushdb())
print(redis.keys())
print(redis.flushall())

# List操作
print(redis.rpush("list",1,2,3))
print(redis.lpush("list",0,-1,-2))
print(redis.lrange("list",0,-1))
print(redis.llen("list"))
print(redis.lindex("list",1))
print(redis.lrem("list",2,3)) # 删除 p1个p2
print(redis.lrange("list",0,-1))
print(redis.lpush("list",3,2,4,3,5,3,7))
print(redis.lrange("list",0,-1))
print(redis.lrem("list",2,3))
print(redis.lrange("list",0,-1))
print(redis.lpop("list"))
print(redis.lrange("list",0,-1))
print(redis.rpop("list"))
print(redis.lrange("list",0,-1))
# while True:
# 	print(redis.brpop("list",0))
print(redis.rpoplpush("list","list"))

# set操作
print(redis.sadd("tags","book","author","content"))
print(redis.smembers("tags"))
print(redis.srem("tags","book"))
print(redis.smembers("tags"))
print(redis.spop("tags"))

print(redis.sadd("tags1","book","author","content"))
print(redis.sinter("tags","tags1"))
print(redis.sunion("tags","tags1"))

# Sorted Set操作
#print(redis.zadd("grade",12,"ttt"))
#print(redis.zadd('grade8',{"100":"100","200":"200"}))
print(redis.zadd('grade8',{"aa":100,"bb":200}))
print(redis.zadd('grade8',{"aa":200,"bb":100}))
# nx | xx | ch
# ``nx`` forces ZADD to only create new elements and not to update
#     scores for elements that already exist.
    
#     ``xx`` forces ZADD to only update scores of elements that already
#     exist. New elements will not be added.
# 重点:
# zadd 默认是ch模式，有就update分数，没有create element
# 或者指定nx与xx
# 注意：xx即便执行成功也返回0，执行不成功也返回0;

#print(redis.zincrby("grade8",200,"aa"))
print(redis.zscore("grade8","aa"))

# hash 操作
print(redis.hset("price","cake",5))
print(redis.hget("price","cake"))
print(redis.hmset("price",{"cake":6,"orange":7}))
print(redis.hexists("price","cake"))
print(redis.hdel("price","cake"))
print(redis.hkeys("price"))
print(redis.hvals("price"))
print(redis.hgetall("price"))
