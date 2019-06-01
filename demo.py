# coding=utf8
import itchat
from itchat.content import TEXT
import logging
import time

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
    # loger.info('个人信息：%s' % my)
    # 获取个人UserName
    my_username = my['UserName']
    print(my_username)
    print(my)

    # 安达刷学时群
    serach_room_anda = itchat.search_chatrooms(name='安达刷学时群')
    # 判断是否搜索到结果
    if len(serach_room_anda) == 1:
        room_anda = serach_room_anda[0]
        print('安达驾校的UserName:%s' % room_anda['UserName'])

    serach_room_628 = itchat.search_chatrooms(name='628')
    # 判断是否搜索到结果
    if len(serach_room_628) == 1:
        room_628 = serach_room_628[0]
        print('628的UserName:%s' % room_628['UserName'])


    # 注册群文本消息监听
    @itchat.msg_register(TEXT, isGroupChat=True)
    def text_reply(msg):
        # print("群消息")
        # print(msg['isAt'])
        # print(msg['ActualNickName'])
        # print(msg['Content'])
        if msg['Type'] == 'Text':
            # if msg['FromUserName'] == my_username and msg['ToUserName'] == room_anda['UserName']:
            #     print('安达驾校群：%s 说：%s' % ('我', msg['Text']))
            # elif msg['FromUserName'] == room_anda['UserName'] and msg['ToUserName'] == my_username:
            #     print('安达驾校群：%s 说：%s' % (msg['ActualNickName'], msg['Text']))
            # # return 'I received: %s' % msg['Text']
            # elif msg['FromUserName'] == my_username and msg['ToUserName'] == room_628['UserName']:
            #     print('628群：%s 说：%s' % ('我', msg['Text']))
            # elif msg['FromUserName'] == room_628['UserName'] and msg['ToUserName'] == my_username:
            #     print('628群：%s 说：%s' % (msg['ActualNickName'], msg['Text']))
            # else:
            #     pass
            # if msg['FromUserName'] == room_628['UserName']:
            #     if msg['ActualNickName'] == '韩翰' and msg['Text'].find('开始') != -1:
            #         return '建阁说的开始'
            #     if msg['ActualNickName'] == '许*辉' and msg['Text'].find('开始') != -1:
            #         return '许*辉说的开始'
            if msg['FromUserName'] == room_anda['UserName']:
                loger.error('邱大雨说%s' % msg['Text'])
                if msg['Text'].find('开始') != -1 and (
                        msg['ActualNickName'] == '躲过雨的屋檐' or msg['ActualNickName'] == '邱大雨'):
                    loger.error('邱大雨开始了%s' % msg['Text'])
                    # return '教练，我约明天下午17：00到19：00的，谢谢'
            # if msg['Text'].find('开始') != -1 and msg['ActualNickName'] == '躲过雨的屋檐':
            #     return '收到有关开始的信号啦'
            print(msg['FromUserName'], msg['Text'], msg['ActualNickName'])
            loger.info('群消息：%s %s %s' % (msg['FromUserName'], msg['Text'], msg['ActualNickName']))
            loger.info('群消息：%s' % msg)


    # # 628宿舍群
    # serach_628_room = itchat.search_chatrooms(name='628')
    # if len(serach_628_room) == 1:
    #     room_628 = serach_628_room[0]
    #     print('628UserName:%s' % room_628['UserName'])
    #     print(room_628)

    # 私信
    # @itchat.msg_register(TEXT, isGroupChat=False)
    # def simple_reply(msg):
    #     if msg['Type'] == 'Text':
    #         if msg['FromUserName'] == my_username:
    #             print('我：%s' % (msg['Text']))
    #         else:
    #             print('%s：%s' % (msg['User']['NickName'], msg['Text']))
    #         # return 'I received: %s' % msg['Text']
    #         print(msg)
    #         loger.info('私信：%s' % msg)

    # 群消息

    itchat.run()
