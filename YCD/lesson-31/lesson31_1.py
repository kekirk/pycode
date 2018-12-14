#! --*--coding:utf-8--*--

# pip install pymongo
# pip install pymongo-3.7.2-cp26-cp26m-win_amd64.whl
# pip install pymongo>3.7.1
# pip install pymongo==3.7.1
# pip install --upgrade pip
# python 编译安装 .so 

# https://pypi.org
import bson
import pymongo
from pymongo.client_session import ClientSession
client = pymongo.MongoClient("localhost", 27017)
print(client)
print(client.__dict__)
# 星型
# 线型
# 图型

# 图遍历 图是一种数据结构 字典 元祖 列表 数组 链表 
# 广度优先
# 深度优先
# 拓扑学 
db = client.solr
print(db)
print(db.__dict__)
print(db.name)
# collection----table
print(db.finance)
#db.finance.insert_one({"x":10})
# document --- dict
doc = db.finance.find_one()
print(doc)
# ObjectId()---bson.objectid.ObjectId()
bsonId = doc[u"_id"]
newId= bson.objectid.ObjectId()
print(newId)
#db.finance.insert_one({"_id":newId,"x":10})
# pymongo.cursor.Cursor
#print(db.finance.find())
#print(client.__dict__)

cursor = db.finance.find()
#'_Cursor__session': None,  
#'_Cursor__address': None, 
#'_Cursor__killed': False, 
#'_Cursor__id': None, 
#print(cursor.__dict__)
# '_Cursor__collection'
# _Cursor__empty': False,
for doc in cursor:
	print(doc)
#print(cursor.__dict__)
#'_Cursor__session': <pymongo.client_session.ClientSession object at 0x00000000039EA710>, 
#'_Cursor__address': ('localhost', 27017), 
#'_Cursor__killed': True, 
#'_Cursor__id': 0L, 

# x_1
# print(db.finance.create_index("x"))
# print(pymongo.ASCENDING) # 1 
# # 1 升序 -1 降序
# for item in db.finance.find().sort("x", -1):
# 	try:
#  		print(item["x"])
#  	except KeyError:
#  		pass

# print([item for item in db.finance.find().limit(2).skip(1)])
# print([item for item in db.finance.find().limit(2)])
# # python mysql slqalchemy orm (object relationship mapping)


# # client = pymongo.MongoClient("localhost", 27017)
# #mysql://root:12345@localhost:3306/sqlalchemy
# client = pymongo.MongoClient('mongodb://localhost:27017/')
# print(client)
# print(client.list_database_names())

# #client.solr == client["solr"]
# # 定制类
# # __getattr__(self, name)
# # __getitem__(self, name)
# solr = client["solr"]
# print(solr)
# finance = solr["finance"]
# #print(finance)
# #finance = solr.finance
# print(solr.list_collection_names())

# # 增删改查
# #
# coll = solr["newtable"]
# #res = coll.insert_one({"x":1,"y":2})
# #print(help(res))
# #print(res.inserted_id)
# #应答式写入(缺省情形，安全写入，适用于数据强一致性场景)
# #非应答式写入(非安全写入，适用于数据弱一致性场景)
# #Is this the result of an acknowledged write operation?
# # acknowledged write 应答式写入
# #print(res.acknowledged)
# #print(client.__dict__)
# #'_BaseObject__read_concern': ReadConcern()
# #'_BaseObject__write_concern': WriteConcern()
# # _BaseObject__read_preference': Primary()
# #print(help(client))
# #client.drop_database("option")
# #print(client.is_locked)
# #print(client.write_concern)

# docs = [
# {"a":1},
# {"b":2},
# {"a":3}
# ]

# #coll.insert_many(docs)

# #print(help(coll))
# # list_indexes
# idxCur = coll.list_indexes()
# #print(idxCur.__dict__)
# # ('localhost', 27017)
# # 0L
# #print(client.close_cursor(0L, address=('localhost', 27017)))
# #help(help(idxCur))
# session = idxCur.session
# print(idxCur.cursor_id)
# print(session)
# idxCur.close()
# #del idxCur
# #print(idxCur.alive)
# for idx in idxCur:
# 	print(idx)
# print(idxCur.cursor_id)
# print(idxCur.alive)
# # kill_cursors_queue:[]

# # for a in range(10):
# # 	cur = coll.list_indexes()
# # 	#print(id(cur))
# # 	print(cur.cursor_id)
# # 	cur1 = coll.find()
# # 	print(type(cur1))
# # 	print(cur1.cursor_id)  # None
# # 	print("+==================")
# # 	for c in cur1:
# # 		print("cur1.cursor_id");
# # 		print(cur1.cursor_id)
# # 		print(c)
# # print(help(coll))
# # update_many
# # update
# # save
# # replace_one
# # rename
# # parallel_scan
# # map_reduce
# # list_indexes
# # insert_one
# # insert_many
# # insert

# cur2 = coll.find()
# for c in cur2:
# 	#print(c)
# 	print(cur2.cursor_id)
# 	print(cur2.session)

client.close()

# read preference
#with_options