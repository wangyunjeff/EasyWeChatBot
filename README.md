# EasyWeChatBot
1分钟实现用python调用ChatGPT API实现微信聊天机器人。支持上下文回复（分别记忆每个人的上下文），重启对话。

## 安装和使用

在chatgpt.py中修改自己的密钥。

![image](https://user-images.githubusercontent.com/17672204/222629610-d1390652-b8a7-483e-a7b9-52ec699529fe.png)
在main.py中进行配置。

![image](https://user-images.githubusercontent.com/17672204/222629441-04445459-db13-48c1-90ca-7997170f1620.png)
1. 安装wxauto库：`pip install wxauto`
2. 运行代码：`python main.py`
3. 在微信中找到你想要聊天的群，输入`chatgpt`加上你想要问的问题，例如`chatgpt你喜欢什么颜色？`



4. 等待机器人回复，如果想要开始新回答，请输入`请开始新回答`

![image](https://user-images.githubusercontent.com/17672204/222627909-8b188c45-d09c-49ed-8817-8a6d6866f864.png)
![image](https://user-images.githubusercontent.com/17672204/222628935-14f6aaab-2f1e-4b0a-aebc-7acd79ea25b2.png)

