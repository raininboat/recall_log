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
class Event(object):
    def group_message_recall(plugin_event, Proc):
        group_message_recall_reply(plugin_event, Proc)

def group_message_recall_reply(plugin_event, Proc):
    Group_Platform = plugin_event.platform['platform']
    Group_ID = int(plugin_event.data.group_id)
    User_ID = int(plugin_event.data.user_id)
    Operator_ID = int(plugin_event.data.operator_id)
    message_id = int(plugin_event.data.message_id)
    msg = plugin_event.get_msg(message_id,False)['data']['message']
    Proc.log(2,'[Message Recall] Platform: {0}, Group: {1}, User: {2}, Operator: {3}, Message: {4}'.format(Group_Platform,Group_ID,User_ID,Operator_ID,msg))
