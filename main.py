# -*- coding: utf8 -*-
import requests
import json
from zhdate import ZhDate
from datetime import date, datetime

# 请输入你的姓名
user = "白天玺"

# 请在这里输入出生日期
chusheng_nian = 2003
chusheng_yue = 1
chusheng_ri = 26

# 企业微信接口信息

# 你复制的企业ID
corpid = "ww9asfasf93b"
# 你复制的secret
corpsecret = "m5rG8IsgALc"
# 你复制的agentld值
agentid = 100

# 所在地区
# 只能是地级市，不可以写区县
city = "唐山"
# 可以为地级市也可以为区县，请在Meizu_city中找城市代码
cityIds = "101090512"


# 魅族天气api
url_meizu = "http://aider.meizu.com/app/weather/listWeather?cityIds=" + cityIds
res_meizu = requests.get(url_meizu).json()
weather_meizu = res_meizu['value'][0]['indexes'][0]['content'] #穿衣指数
# 这里是get天气
url_weather = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
res_weather = requests.get(url_weather).json()
weather = res_weather['data']['list'][0]
msg1 = "今天是：" + weather['date']
msg2 ="您所在的地区是：" + weather['city']
msg3 ="今天的天气是：" + weather['weather']
msg4 ="最高温度为：%s"%weather['high']
msg5 ="最低温度为：%s"%weather['low']
msg6 ="体感温度为：%s"%weather['temp']
msg7 = "风力风向为：" + weather['wind']
msg8 = "污染指数为：" + weather['airQuality']
msg9 = "穿衣指数：" + weather_meizu

# 每日一句
url_note = "http://open.iciba.com/dsapi/"
res_note = requests.get(url_note).json()
msg10 = "每日一句：" + res_note["note"]
msg11 = res_note["content"]

# 距离下次生日
now = str(ZhDate.today()).split("农历")
now2 = now[1].split("年")
nongli = int(now2[0])
nongli_z = ZhDate(nongli,chusheng_yue,chusheng_ri) - ZhDate.today()
if not nongli_z == 0:
    if nongli_z > 0 and nongli_z < 354:
        next_bir = ZhDate(nongli,chusheng_yue,chusheng_ri)-ZhDate.today()
        msg12 = "今天是距离您的下次生日还有" + str(next_bir) + "天"
    else:
        if nongli_z >= 354:
            next_bir = ZhDate(nongli,chusheng_yue,chusheng_ri)-ZhDate.today()
            msg12 = "今天是距离您的下次生日还有" + str(next_bir) + "天"
        else:
            next_bir = ZhDate(nongli + 1,chusheng_yue,chusheng_ri)-ZhDate.today()
            msg12 = "今天距离您的下次生日还有" + str(next_bir) + "天"
else:
    msg12 = "今天是您的生日，生日快乐！！！"

# 距离出生日期已过多少天
today_b = ZhDate.today() - ZhDate(chusheng_nian,chusheng_yue,chusheng_ri)
msg13 = "今天距离您的出生日期已经过了" + str(today_b) +"天"
print(msg13)

# 距离春节还有多少天
chunjie_next = ZhDate(nongli + 1,1,1) - ZhDate.today()
msg14 = "距离春节还有" + str(chunjie_next) +"天"

def getTocken():
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=" + corpid + "&corpsecret=" + corpsecret

    r =requests.get(url)
    tocken_json = json.loads(r.text)
    sendText(tocken=tocken_json['access_token'])

def sendText(tocken):
    sendUrl = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + tocken
    data = json.dumps({
        "totag" : "1",
        "msgtype" : "text",
        "agentid" : 1000002,
        "text" : {
            "content" : user + "小同志请查收今天的消息\n[庆祝][庆祝][庆祝][庆祝][庆祝][庆祝]" + "\n" + msg1 + "\n" + msg2 + "\n" + msg3  + "\n" + msg4 + "\n" + msg5 + "\n" + msg6 + "\n" + msg7 + "\n" + msg8 + "\n" + msg9 + "\n" + msg12 + "\n" + msg13 + "\n" + msg14 + "\n" + msg10 + "\n" + msg11 + "\n[玫瑰][玫瑰][玫瑰][玫瑰][玫瑰][玫瑰]"
        }
    })
    requests.post(sendUrl,data)

getTocken()