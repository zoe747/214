# 添加公钥
******
## 请求接口约定(均使用POST)

接口链接:'infrastructure/add_public_key'

public_key(必填)

## 返回值接口约定
***http状态码***

200:请求成功

400:请求不合法

# 获取公钥
******
## 请求接口约定(均使用POST)

接口链接:'infrastructure/get_public_key'

username(必填)

## 返回值接口约定
***http状态码 公钥列表***

200+json列表:成功+返回值

400:请求不合法