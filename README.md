# 群组撤回消息本地记录
用于把群聊别人撤回的消息在ovo框架终端记录的小插件，获取具体撤回的消息内容<br>
main.py 中 status['logOnFile'] 设置为 True 打开本地文件记录
```log
[2021-10-07 14:32:00.031381] - [INFO] - [qq] - [group_message] - Group(1234567) User[雨鸣于舟](87654321) : 测试消息
[2021-10-07 14:32:04.395274] - [INFO] - [qq] - [group_message_recall] - Group(1234567) User(87654321) <- Operator(87654321) Message_id(-1111111)
[2021-10-07 14:32:04.410895] - [INFO] - [Message Recall] Platform: qq, Group: 1234567, User: 87654321, Operator: 87654321, Message: 测试消息
```