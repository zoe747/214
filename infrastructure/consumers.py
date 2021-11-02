from channels.generic.websocket import WebsocketConsumer
import json

user_dict = {}


class KnockConsumer(WebsocketConsumer):
    # websocket建立连接时执行方法
    def connect(self):
        self.accept()
        username = self.scope.get("url_route").get("kwargs").get("username")
        user_dict[username] = self
        print(user_dict)
        return True


def knock_knock(username, message):
    ws = user_dict.get(username)
    message = json.dumps({'message': message})
    ws.send(message)
    print(message)
    return True
