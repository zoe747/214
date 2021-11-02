# 发送者消息到服务器
******
## 请求(POST)
请求链接:char/send/

参数:

toUsername(需要发送到的人的名字)

plaintext(消息内容)

## 返回值
422:此人不存在

423:你们不是好友关系

400:请求不合法

200:成功发送

# 获取与某好友消息漫游
******
## 请求(POST)
请求链接:char/filter_message/

参数:

username(好友的名称)

## 返回值

422:此人不存在

423:你们不是好友关系

400:请求不合法

200+列表:成功+消息记录

(列表中每个元素是一个字典，分别有from_user_name，to_user_name，plaintext)

# 接收者请求未曾被接收的消息
******
## 请求(POST)
请求链接:chat/request_message/

参数:无
## 返回值
200+列表:成功+未被接受的消息列表

(列表中每个元素都是一个字典，分别有from_user_name，to_user_name，plaintext,message_id)

# 成功接收消息
******
## 请求(POST)
请求链接:chat/receive_successfully/

参数:

message_id:消息id

## 返回值
423：消息不存在

400：请求不合法

200：成功访问