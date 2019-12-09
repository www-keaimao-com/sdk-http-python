# -*- coding:utf-8 -*-
# @name='python wx_bot API',
# @version='1.0.1',
# @author='wordgao',
# @author_email='wordgao@163.com',
# @description='根据官方提供的PHP版API翻译后的API插件 Q 257386'
import requests
import json

""""
 * @param int type                 =>   事件类型（事件列表可参考 - 事件列表demo）
 * @param string from_wxid         =>   1级来源id（比如发消息的人的id）
 * @param string from_name         =>   1级来源昵称（比如发消息的人昵称）
 * @param string final_from_wxid   =>   2级来源id（群消息事件下，1级来源为群id，2级来源为发消息的成员id，私聊事件下都一样）
 * @param string final_nickname    =>   2级来源昵称
 * @param string robot_wxid        =>   当前登录的账号（机器人）标识id
 * @param string msg               =>   消息内容
 * @param string parameters        =>   附加参数（暂未用到，请忽略）
 * @param int time                 =>   请求时间(时间戳10位版本)
 
【功能名】                【demo中函数名】
发送文本消息              send_text_msg()
发送群消息并艾特某人      send_group_at_msg()
发送图片消息              send_iamge_msg()
发送视频消息              send_video_msg()
发送文件消息              send_file_msg()
发送动态表情              send_emoji_msg()
发送分享链接              send_link_msg()
发送音乐消息              send_music_msg()
取指定登录账号的昵称      get_robot_name()
取指定登录账号的头像      get_robot_headimgurl()
取登录账号列表            get_logged_account_list()
取好友列表                get_friend_list()
取群聊列表                get_group_list()
取群成员资料              get_group_member()
取群成员列表              get_group_member_list()
接收好友转账              accept_transfer()
同意群聊邀请              agree_group_invite()
同意好友请求              agree_friend_verify()
修改好友备注              modify_friend_note()
删除好友                  delete_friend()
踢出群成员                remove_group_member()
修改群名称                modify_group_name()
修改群公告                modify_group_notice()
建立新群                  building_group()
退出群聊                  quit_group()
邀请加入群聊              invite_in_group()
"""

# 主动调用发送接口
API_URL = "http://127.0.0.1:8073/send"
# TODO data['msg'] = requests.utils.quote(msg)  # 发送内容 发送的信息如果出现乱码，请按照此方式修改


def send_text_msg(robwxid, to_wxid, msg):
    """
    发送文字消息(好友或者群)
    * @access public
    * @param  string robwxid 登录账号id，用哪个账号去发送这条消息
    * @param  string to_wxid 对方的id，可以是群或者好友id
    * @param  string msg     消息内容
    * @return string json_string
    """
    data = dict()
    data['type'] = 100  # Api数值（可以参考 - api列表demo）
    data['msg'] = requests.utils.quote(msg)  # 发送内容
    data['to_wxid'] = to_wxid  # 对方id
    data['robot_wxid'] = robwxid  # 账户id，用哪个账号去发送这条消息
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def send_group_at_msg(robwxid, to_wxid, at_wxid, at_name, msg):
    """
    * 发送群消息并艾特某人
    *
    * @access public
    * @param  string robwxid 账户id，用哪个账号去发送这条消息
    * @param  string to_wxid 群id
    * @param  string at_wxid 艾特的id，群成员的id
    * @param  string at_name 艾特的昵称，群成员的昵称
    * @param  string msg     消息内容
    * @return string json_string
    """
    data = dict()
    data['type'] = 102  # Api数值（可以参考 - api列表demo）
    data['msg'] = requests.utils.quote(msg)  # 发送的文件的绝对路径
    data['to_wxid'] = to_wxid  # 群id
    data['at_wxid'] = at_wxid  # 艾特的id，群成员的id
    data['at_name'] = at_name  # 艾特的昵称，群成员的昵称
    data['robot_wxid'] = robwxid  # 账户id，用哪个账号去发送这条消息
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def send_image_msg(robwxid, to_wxid, path):
    """
    * 发送图片消息
    *
    * @access public
    * @param  string robwxid 登录账号id，用哪个账号去发送这条消息
    * @param  string to_wxid 对方的id，可以是群或者好友id
    * @param  string path    图片的绝对路径
    * @return string json_string
    """
    data = dict()
    data['type'] = 103  # Api数值（可以参考 - api列表demo）
    data['msg'] = path  # 发送的图片的绝对路径
    data['to_wxid'] = to_wxid  # 对方id
    data['robot_wxid'] = robwxid  # 账户id，用哪个账号去发送这条消息
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def send_video_msg(robwxid, to_wxid, path):
    """
    * 发送视频消息
    *
    * @access public
    * @param  string robwxid 账户id，用哪个账号去发送这条消息
    * @param  string to_wxid 对方的id，可以是群或者好友id
    * @param  string path    视频的绝对路径
    * @return string json_string
    """
    data = dict()
    data['type'] = 104  # Api数值（可以参考 - api列表demo）
    data['msg'] = path  # 发送的视频的绝对路径
    data['to_wxid'] = to_wxid  # 对方id
    data['robot_wxid'] = robwxid  # 账户id，用哪个账号去发送这条消息
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def send_file_msg(robwxid, to_wxid, path):
    """
    * 发送文件消息
    *
    * @access public
    * @param  string robwxid 账户id，用哪个账号去发送这条消息
    * @param  string to_wxid 对方的id，可以是群或者好友id
    * @param  string path    文件的绝对路径
    * @return string json_string
    """
    data = dict()
    data['type'] = 105  # Api数值（可以参考 - api列表demo）
    data['msg'] = path  # 发送的文件的绝对路径
    data['to_wxid'] = to_wxid  # 对方id（默认发送至来源的id，也可以发给其他人）
    data['robot_wxid'] = robwxid  # 账户id，用哪个账号去发送这条消息
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def send_emoji_msg(robwxid, to_wxid, path):
    """
    * 发送动态表情
    *
    * @access public
    * @param  string robwxid 账户id，用哪个账号去发送这条消息
    * @param  string to_wxid 对方的id，可以是群或者好友id
    * @param  string path    动态表情文件（通常是gif）的绝对路径
    * @return string json_string
    """
    data = dict()
    data['type'] = 106  # Api数值（可以参考 - api列表demo）
    data['msg'] = path  # 发送的动态表情的绝对路径
    data['to_wxid'] = to_wxid  # 对方id（默认发送至来源的id，也可以发给其他人）
    data['robot_wxid'] = robwxid  # 账户id，用哪个账号去发送这条消息
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def send_link_msg(robwxid, to_wxid, title, text, target_url, pic_url):
    """
    * 发送分享链接
    *
    * @access public
    * @param  string robwxid    账户id，用哪个账号去发送这条消息
    * @param  string to_wxid    对方的id，可以是群或者好友id
    * @param  string title      链接标题
    * @param  string text       链接内容
    * @param  string target_url 跳转链接
    * @param  string pic_url    图片链接
    * @return string json_string
    """
    link = dict()
    link['title'] = title
    link['text'] = text
    link['url'] = target_url
    link['pic'] = pic_url

    # 封装返回数据结构
    data = dict()
    data['type'] = 107  # Api数值（可以参考 - api列表demo）
    data['msg'] = link  # 发送的分享链接结构体
    data['to_wxid'] = to_wxid  # 对方id（默认发送至来源的id，也可以发给其他人）
    data['robot_wxid'] = robwxid  # 账户id，用哪个账号去发送这条消息
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def send_music_msg(robwxid, to_wxid, name):
    """
    * 发送音乐分享
    *
    * @access public
    * @param  string robwxid 账户id，用哪个账号去发送这条消息
    * @param  string to_wxid 对方的id，可以是群或者好友id
    * @param  string name    歌曲名字
    * @return string json_string
    """
    data = dict()
    data['type'] = 108  # Api数值（可以参考 - api列表demo）
    data['msg'] = name  # 歌曲名字
    data['to_wxid'] = to_wxid  # 对方id（默认发送至来源的id，也可以发给其他人）
    data['robot_wxid'] = robwxid  # 账户id，用哪个账号去发送这条消息
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def get_robot_name(robwxid):
    """
    * 取指定登录账号的昵称
    *
    * @access public
    * @param  string robwxid 账户id
    * @return string 账号昵称
    """
    data = dict()
    data['type'] = 201  # Api数值（可以参考 - api列表demo）
    data['robot_wxid'] = robwxid  # 账户id
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def get_robot_headimgurl(robwxid):
    """
    * 取指定登录账号的头像
    *
    * @access public
    * @param  string robwxid 账户id
    * @return string 头像http地址
    """
    data = dict()
    data['type'] = 202  # Api数值（可以参考 - api列表demo）
    data['robot_wxid'] = robwxid  # 账户id
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def get_logged_account_list():
    """
    * 取登录账号列表
    *
    * @access public
    * @param  string robwxid 账户id
    * @return string 当前框架已登录的账号信息列表
    """
    data = dict()
    data['type'] = 203  # Api数值（可以参考 - api列表demo）
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def get_friend_list(robwxid='', is_refresh=0):
    """
    * 取好友列表
    *
    * @access public
    * @param  string robwxid    账户id
    * @param  string is_refresh 是否刷新
    * @return string 当前框架已登录的账号信息列表
    """
    data = dict()
    data['type'] = 204  # Api数值（可以参考 - api列表demo）
    data['robot_wxid'] = robwxid  # 账户id（可选，如果填空字符串，即取所有登录账号的好友列表，反正取指定账号的列表）
    data['is_refresh'] = is_refresh  # 是否刷新列表，0 从缓存获取 / 1 刷新并获取
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def get_group_list(robwxid='', is_refresh=0):
    """
    * 取群聊列表
    *
    * @access public
    * @param  string robwxid    账户id
    * @param  string is_refresh 是否刷新
    * @return string 当前框架已登录的账号信息列表
    """
    data = dict()
    data['type'] = 205  # Api数值（可以参考 - api列表demo）
    data['robot_wxid'] = robwxid  # 账户id（可选，如果填空字符串，即取所有登录账号的好友列表，反正取指定账号的列表）
    data['is_refresh'] = is_refresh  # 是否刷新列表，0 从缓存获取 / 1 刷新并获取
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def get_group_member_list(robwxid, group_wxid, is_refresh=0):
    """
    * 取群成员列表
    *
    * @access public
    * @param  string robwxid    账户id
    * @param  string group_wxid 群id
    * @param  string is_refresh 是否刷新
    * @return string 当前框架已登录的账号信息列表
    """
    data = dict()
    data['type'] = 206  # Api数值（可以参考 - api列表demo）
    data['robot_wxid'] = robwxid  # 账户id
    data['group_wxid'] = group_wxid  # 群id
    data['is_refresh'] = is_refresh  # 是否刷新列表，0 从缓存获取 / 1 刷新并获取
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def get_group_member(robwxid, group_wxid, member_wxid):
    """
    * 取群成员资料
    *
    * @access public
    * @param  string robwxid     账户id
    * @param  string group_wxid  群id
    * @param  string member_wxid 群成员id
    * @return string json_string
    """
    data = dict()
    data['type'] = 207  # Api数值（可以参考 - api列表demo）
    data['robot_wxid'] = robwxid  # 账户id，取哪个账号的资料
    data['group_wxid'] = group_wxid  # 群id
    data['member_wxid'] = member_wxid  # 群成员id
    result = json.dumps(data)
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def accept_transfer(robwxid, friend_wxid, json_string):
    """
    * 接收好友转账
    *
    * @access public
    * @param  string robwxid     账户id
    * @param  string friend_wxid 朋友id
    * @param  string json_string 转账事件原消息
    * @return string json_string
    """
    data = dict()
    data['type'] = 301  # Api数值（可以参考 - api列表demo）
    data['robot_wxid'] = robwxid  # 账户id
    data['friend_wxid'] = friend_wxid  # 朋友id
    data['msg'] = json_string  # 转账事件原消息
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def agree_group_invite(robwxid, json_string):
    """
    * 同意群聊邀请
    *
    * @access public
    * @param  string robwxid     账户id
    * @param  string json_string 同步消息事件中群聊邀请原消息
    * @return string json_string
    """
    data = dict()
    data['type'] = 302  # Api数值（可以参考 - api列表demo）
    data['robot_wxid'] = robwxid  # 账户id
    data['msg'] = json_string  # 同步消息事件中群聊邀请原消息
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def agree_friend_verify(robwxid, json_string):
    """
    * 同意好友请求
    *
    * @access public
    * @param  string robwxid     账户id
    * @param  string json_string 好友请求事件中原消息
    * @return string json_string
    """
    data = dict()
    data['type'] = 303  # Api数值（可以参考 - api列表demo）
    data['robot_wxid'] = robwxid  # 账户id
    data['msg'] = json_string  # 好友请求事件中原消息
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def modify_friend_note(robwxid, friend_wxid, note):
    """
    * 修改好友备注
    *
    * @access public
    * @param  string robwxid     账户id
    * @param  string friend_wxid 好友id
    * @param  string note 新备注（空字符串则是删除备注）
    * @return string json_string
    """
    data = dict()
    data['type'] = 304  # Api数值（可以参考 - api列表demo）
    data['robot_wxid'] = robwxid  # 账户id
    data['friend_wxid'] = friend_wxid  # 朋友id
    data['note'] = note  # 新备注（空字符串则是删除备注）
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def delete_friend(robwxid, friend_wxid):
    """
    * 删除好友
    *
    * @access public
    * @param  string robwxid     账户id
    * @param  string friend_wxid 好友id
    * @return string json_string
    """
    data = dict()
    data['type'] = 305  # Api数值（可以参考 - api列表demo）
    data['robot_wxid'] = robwxid  # 账户id
    data['friend_wxid'] = friend_wxid  # 朋友id
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def remove_group_member(robwxid, group_wxid, member_wxid):
    """
    * 踢出群成员
    *
    * @access public
    * @param  string robwxid     账户id
    * @param  string group_wxid  群id
    * @param  string member_wxid 群成员id
    * @return string json_string
    """
    data = dict()
    data['type'] = 306  # Api数值（可以参考 - api列表demo）
    data['robot_wxid'] = robwxid  # 账户id
    data['group_wxid'] = group_wxid  # 群id
    data['member_wxid'] = member_wxid  # 群成员id
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def modify_group_name(robwxid, group_wxid, group_name):
    """
    * 修改群名称
    *
    * @access public
    * @param  string robwxid     账户id
    * @param  string group_wxid  群id
    * @param  string group_name  新群名
    * @return string json_string
    """
    data = dict()
    data['type'] = 307  # Api数值（可以参考 - api列表demo）
    data['robot_wxid'] = robwxid  # 账户id
    data['group_wxid'] = group_wxid  # 群id
    data['group_name'] = group_name  # 新群名
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def modify_group_notice(robwxid, group_wxid, notice):
    """
    * 修改群公告
    *
    * @access public
    * @param  string robwxid     账户id
    * @param  string group_wxid  群id
    * @param  string notice      新公告
    * @return string json_string
    """
    data = dict()
    data['type'] = 308  # Api数值（可以参考 - api列表demo）
    data['robot_wxid'] = robwxid  # 账户id
    data['group_wxid'] = group_wxid  # 群id
    data['notice'] = notice  # 新公告
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def building_group(robwxid, friends):
    """
    * 建立新群
    *
    * @access public
    * @param  string robwxid     账户id
    * @param  array  friends     三个人及以上的好友id数组，['wxid_1xxx', 'wxid_2xxx', 'wxid_3xxx', 'wxid_4xxx']
    * @return string json_string
    """
    data = dict()
    data['type'] = 309  # Api数值（可以参考 - api列表demo）
    data['robot_wxid'] = robwxid  # 账户id
    data['friends'] = friends  # 好友id数组
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def quit_group(robwxid, group_wxid):
    """
    * 退出群聊
    *
    * @access public
    * @param  string robwxid     账户id
    * @param  string group_wxid  群id
    * @return string json_string
    """
    data = dict()
    data['type'] = 310  # Api数值（可以参考 - api列表demo）
    data['robot_wxid'] = robwxid  # 账户id
    data['group_wxid'] = group_wxid  # 群id
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def invite_in_group(robwxid, group_wxid, friend_wxid):
    """
    * 邀请加入群聊
    *
    * @access public
    * @param  string robwxid     账户id
    * @param  string group_wxid  群id
    * @param  string friend_wxid 好友id
    * @return string json_string
    """
    data = dict()
    data['type'] = 311  # Api数值（可以参考 - api列表demo）
    data['robot_wxid'] = robwxid  # 账户id
    data['group_wxid'] = group_wxid  # 群id
    data['friend_wxid'] = friend_wxid  # 好友id
    result = json.dumps(data)
    try:
        return requests.post(API_URL, data={"data": result})
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"请检查当前的回复地址是否正确！ {API_URL}")


def sendSGHttp(url, params, method='get', timeout=3):
    """
     * 执行一个 HTTP 请求，仅仅是post组件，其他语言请自行替换即可
     *
     * @param  string url 执行请求的url地址
     * @param  mixed  params  表单参数
     * @param  int    timeout 超时时间
     * @param  string method  请求方法 post / get
     * @return array  结果数组
     """
    if url is None:
        return None
    ret = None
    err = None
    if method.lower() == "get":
        try:
            ret = requests.get(url, data=params, timeout=timeout).text
        except Exception as e:
            err = e
    else:
        try:
            ret = requests.post(url, data=params, timeout=timeout).text
        except Exception as e:
            err = e
    data = {"result": ret, "error_msg": err}
    return data
