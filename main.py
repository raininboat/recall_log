# -*- coding: utf-8 -*-
'''
       ___  ___   _____  ____  __
      / _ \/ _ | /  _/ |/ /\ \/ /
     / , _/ __ |_/ //    /  \  / 
    /_/|_/_/ |_/___/_/|_/   /_/  

    群聊撤回消息本地记录
        主文件

    Copyright (C) 2021  RainyZhou  
                        Email: thunderain_zhou@163.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''
import OlivOS
import sys
import os
import time

status={
    # 打开后即可将撤回内容同时输出到文件中
    'logOnFile' : False
}

class Event(object):
    def init(plugin_event,Proc):
        if status['logOnFile']:
            create_dir()
    def group_message_recall(plugin_event, Proc):
        Group_Platform = plugin_event.platform['platform']
        Group_ID = int(plugin_event.data.group_id)
        User_ID = int(plugin_event.data.user_id)
        Operator_ID = int(plugin_event.data.operator_id)
        message_id = int(plugin_event.data.message_id)
        msgdata = plugin_event.get_msg(message_id,False)['data']
        msg = msgdata['message']
        Proc.log(2,'[Message Recall] Platform: {0}, Group: {1}, User: {2}, Operator: {3}, \nMessage: {4}'.format(Group_Platform,Group_ID,User_ID,Operator_ID,msg))
        if status['logOnFile'] and msgdata['time'] != -1:
            logname = time.strftime('%Y-%m-%d.txt',time.localtime())
            with open(status['path']+logname,'a',encoding='utf-8',errors='ignore') as file:
                msgtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(msgdata['time']))
                fmtdict = {
                    'time' : msgtime,
                    'platform' : Group_Platform,
                    'group' : Group_ID,
                    'sender' : User_ID,
                    'operator' : Operator_ID,
                    'message' : msg
                }
                string = 'msgSendTime: {time} ; platform: {platform} ; group : {group} ; sender : {sender} ; operator: {operator} ; message: \n{message}\n\n'.format_map(fmtdict)
                file.write(string)

def create_dir():
    OlivOS_Path = sys.path[0]
    Data_Path = OlivOS_Path + '/plugin/data/recall_log/'
    status['path'] = Data_Path
    if not os.path.exists(Data_Path):
        os.mkdir(Data_Path)
