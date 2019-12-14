from flask import Flask, request, jsonify
from api import *

"""
【事件数值】             【事件描述】
100                       私聊消息
200                       群聊消息
300                       暂无
400                       群成员增加
410                       群成员减少
500                       收到好友请求
600                       二维码收款
700                       收到转账
800                       软件开始启动
900                       新的账号登录完成
910                       账号下线
"""

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        wx_type = request.form.get("type")  # 数据类型
        msg = request.form.get("msg")  # 发送内容
        to_wxid = request.form.get("from_wxid")  # 1级来源id（比如发消息的人的id）
        from_name = request.form.get("from_name")  # 1级来源昵称（比如发消息的人昵称）
        final_from_wxid = request.form.get("final_from_wxid")  # 2级来源id（群消息事件下，1级来源为群id，2级来源为发消息的成员id，私聊事件下都一样）
        final_nickname = request.form.get("final_from_name")  # 2级来源昵称
        robot_wxid = request.form.get("robot_wxid")  # 当前登录的账号（机器人）标识id
        parameters = request.form.get("parameters")  # 附加参数（暂未用到，请忽略）
        ws_time = request.form.get("time")  # 请求时间(时间戳10位版本)
        try:
            file_url = request.form.get("file_url")  # 如果是文件消息（图片、语音、视频、动态表情），这里则是可直接访问的网络地址，非文件消息时为空
        except:
            raise TypeError("请使用 http-api 2.4+以上的版本")

        if wx_type == "100":
            send_text_msg(robot_wxid, to_wxid, "Hello")
        elif wx_type == "200":  # 群聊消息
            send_group_at_msg(robot_wxid, to_wxid, final_from_wxid, final_nickname, "Hello！请加我私聊")
        else:
            pass
    else:
        return "wxbot test get page"
    return jsonify({"code": 200, "data": "result ok"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8073, debug=True)
