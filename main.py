import time
from queue import Queue

from wxauto import *

from chatgpt import *

if __name__ == '__main__':

    who = '尬聊群' # 设置聊天对象，微信群名
    nickname = 'chatgpt'  # 触发chatgpt回复的关键字
    speakList = ['Ike', 'Y', '王二', '消烦员', '～'] #设置谁可以发言
    wx = WeChat()
    wx.ChatWith(who)
    q = Queue()
    while True:
        msgobject1 = wx.GetLastMessage
        speaker1, msgcontent, speakerid1 = msgobject1
        time.sleep(1)
        # 如果收到的消息包含 chatgpt 的昵称，并且发件人在聊天群中：
        if nickname in msgcontent and speaker1 in speakList:

            if '请开始新回答' in msgcontent:
                flag = 0
            else:
                flag = 1
            wx.SendMsg('message received %s asked' % (speaker1) + msgcontent[7:])
            sccess = False
            while not sccess:
                try:
                    returnMessage = ChatGPT(msgcontent[7:], flag=flag, name=speaker1)
                    sccess = True
                except:
                    wx.SendMsg('error! retrying...')
                    time.sleep(1)

            wx.SendMsg('@%s' % (speaker1) + returnMessage)

            continue
