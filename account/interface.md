# 登录
******

## 请求接口约定(均使用POST)

接口链接:'account/login'

username(选填)

password(选填)

token(必填，若客户端无token，则传输字符串'token'来表示无token)

## 返回值接口约定

***http状态码 token***

420:token已过期，请重新登录
  
401:账户或密码错误

400:请求不合法

200+token:成功+返回新token 

# 登出
******

## 请求接口约定(均使用POST)
接口链接:'account/logout'

## 返回值接口约定
***http状态码***

200:登出成功

# 注册
******
## 请求接口约定(均使用POST)

接口链接:'account/register'

username(必填)

password(必填)

password2(必填)

## 返回值接口约定

***http状态码***

200:注册成功，请登录

400：请求不合法

# 编辑用户资料
******
## 请求接口约定(均使用POST)

接口链接:'account/edit/(username)'

bio(选填)

avatar(选填)(头像)

phone(选填)

## 返回值接口约定
***http状态码***

403:你没有权限进行此操作(修改此用户信息的操作)

200:编辑成功

400:请求不合法


# 获得用户资料
******
## 请求接口约定(均使用POST)

接口链接:'account/profile/(username)'

## 返回值接口约定
***http状态码 用户资料字典***

200+字典:获取成功+用户资料字典

400:请求不合法


