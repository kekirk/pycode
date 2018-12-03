#! --*--coding:utf-8--*--

# mongodb 原子性,不能跨表操作,也不能跨document
# db.books.findAndModify({query:{"_id":123456789,"checkout.by":"abcd"},update:{$set:{"title":"aaaaaa","db.book.findOne().pages":316,"checkout":[{"by":"abcd","date":new Date()}]},$inc:{"pages":1000,"available":1000}}})
# db.books.update
# 316/0 = Infinity

# 操作符
# $set
# $unset
# $inc
# $push
# $pull
# $rename
# $addToSet
# $pop:弹出数据结构中的最后一个元素，最后一条数据是指最后插入的数据
# $pushAll  --- mongodb很早前的版本就合并了$push和$pushAll，然后mongodb 3.6取消了$pushAll所以要么mongodb降级到3.4

# 增加数据的时候，[](array) push,{}(map) set


# 在一次原子性操作中，不同的操作符不能同时操作同一个field

# 全文检索(全文检索，数据检索，语义检索)
# 全文检索
# 搜索引擎(全文检索是指计算机索引程序通过扫描文章中的每一个词,对每一个词建立一个索引，指明该词在文章中出现的次数和位置)
# 分词器+索引器+检索器

# mysql:数据检索,
# select * from text_content where topic = "python project";
# select * from text_content where topic like "%python%";

# 语义检索
# 语义搜索的本质是通过数学来摆脱当今搜索中使用的猜测和近似，
# 并为词语的含义以及它们如何关联到我们在搜索引擎输入框中所找的东西引进一种清晰的理解方式

# 中国的首都是哪里

# 数据检索：select * from words where title="中国的首都是哪里";
# 全文检索：url?query=中国的首都是哪里; 中国 首都 哪里 
# 语义检索: return 北京

# posts:

# db.posts.createIndex({"post_text":1}) 数据检索的索引

# db.posts.find({post_text:"enjoy the mongodb articles on Runoob"})
# db.posts.find({$text:{$search:"on"}}) 没有结果
# db.posts.find({$text:{$search:"mongodb"}}) 有结果
# 为什么？
# 分词器的分词算法：stop_words(废止词the on is if else i you she him)


# MapReduce
# Map-Reduce是一种计算模型，简单的说就是将大批量的工作（数据）分解（MAP）执行，
# 然后再将结果合并成最终结果（REDUCE）。
# MongoDB提供的Map-Reduce非常灵活，对于大规模数据分析也相当实用。

# emit(this.)

# 每一年分别花了多少钱
# map() emit(year:money)
# year:2015
# reduce()
# year:2016
# reduce()
# year:2017
# reduce(function(sum(moneys)))

# out:
# keys:values

# 优势
# server1 server2 server3
# server1 server2
# 负载均衡算法

# 正则表达式 regular expression
# db.regx.find({"post_text":{$regex:"runoob"}})
# db.regx.find({"post_text":/runoob/})
# db.regx.find({"post_text":{$regex:"Runoob",$options:"$i"}}) #ignore
# db.regx.find({"tags":{$regex:"un",$options:"$i"}})
# db.regx.find({"tags":/Run/i})
# re.match(默认起始位置匹配) re.search(不需要起始位置)

# 正则优化 ： complie(python)
# eval mongodb
# var re = eval("/"+"enjoy"+"/i")
# db.regx.find({post_text:re})

# 正则是否走索引
# 正则是走索引的，走的是数据检索的索引，不支持全文检索的索引
# 如果是全文检索，走的是text索引

# enjoy the mongodb articles on runoob
# enjoy 
# mongodb
# articles
# runoob

# db.regx.find(post_text:/les o/)
