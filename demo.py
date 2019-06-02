# coding=utf8
import itchat
from itchat.content import TEXT
import logging
import time

# 日志设置
filehandler = logging.FileHandler(filename='logs/%s.log' % time.strftime("%Y-%m-%d", time.localtime()),
                                  encoding="utf-8")
fmter = logging.Formatter(fmt="%(asctime)s %(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
filehandler.setFormatter(fmter)
loger = logging.getLogger(__name__)
loger.addHandler(filehandler)
loger.setLevel(logging.INFO)
loger.fatal("------日志开始-------")

# 登录
# itchat.auto_login()
# 发送消息
# itchat.send('Hello, filehelper', toUserName='filehelper')

if __name__ == '__main__':
    # 登录，hotReload=True表示暂存登录状态，不需要每次都扫码
    itchat.auto_login(hotReload=True)
    # 获取自己的用户信息
    my = itchat.search_friends()
    loger.info('用户信息：%s' % my)
    # 获取个人UserName
    my_username = my['UserName']

    # 安达刷学时群
    serach_room_anda = itchat.search_chatrooms(name='安达刷学时群')
    loger.info('安达群信息：%s' % serach_room_anda)
    # 判断是否搜索到结果
    if len(serach_room_anda) == 1:
        room_anda = serach_room_anda[0]
        print('安达驾校的UserName:%s' % room_anda['UserName'])
    # 注册群文本消息监听
    @itchat.msg_register(TEXT, isGroupChat=True)
    def text_reply(msg):
        # print(msg['isAt'])
        if msg['Type'] == 'Text':
            # 获取安达群信息
            if msg['FromUserName'] == room_anda['UserName']:
                if msg['Text'].find('开始') != -1 and (
                        msg['ActualNickName'] == '躲过雨的屋檐' or msg['ActualNickName'] == '邱大雨'):
                    loger.error('邱大雨说开始了：%s' % msg['Text'])
                    # return '教练，周旭阳预约明天下午17：00到19：00的，谢谢'
                print(msg['FromUserName'], msg['Text'], msg['ActualNickName'])
                loger.info('群消息：%s %s %s' % (msg['FromUserName'], msg['Text'], msg['ActualNickName']))
                loger.info('群消息：%s' % msg)
    # 运行
    itchat.run()
