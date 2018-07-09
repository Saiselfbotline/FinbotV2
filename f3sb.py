from FinbotV1.finbotpy import *
from FinbotV1.finbot.MessageService import Client
from FinbotV1.finbotToken import FinbotService
from FinbotV1.finbotToken import FinbotLoginService
from FinbotV1.finbotToken.ttypes import LoginRequest
from FinbotServer.protocol import TCompactProtocol
from FinbotServer.transport import THttpClient
from datetime import datetime
from datetime import timedelta, date
from time import sleep
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import asyncio, pytz, pafy, time, timeit, random, sys, ast, re, os, json, requests, threading, subprocess, string, codecs, tweepy, ctypes, urllib, urllib.parse, shutil, atexit, six, youtube_dl
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
_session = requests.session()

botStart = time.time()
mulai = time.time()
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

bot_login = codecs.open('finbotLogged.json', 'r', 'utf-8')
run_bot = json.load(bot_login)

if run_bot['authToken'] == "":
    kang = FINBOTV1()
    timeline = FinbotChannel(kang,channelId="1341209850")
    run_bot['authToken'] = str(kang.authToken)
    kangMID = kang.getProfile().mid
    run_bot['Mid'] = kangMID
    run_bot['Admin'] = kangMID
    with open('finbotLogged.json', 'w') as fp:
    	json.dump(run_bot, fp, sort_keys=True, indent=4)
else:
    try:
        kang = FINBOTV1(run_bot['authToken'])
        timeline = FinbotChannel(kang,channelId="1341209850")
        kangMID = kang.getProfile().mid
        run_bot['Mid'] = kangMID
        run_bot['Admin'] = kangMID
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)
    except:
        kang = FINBOTV1(run_bot['authToken'])
        timeline = FinbotChannel(kang,channelId="1341209850")
        kangMID = kang.getProfile().mid
        run_bot['Mid'] = kangMID
        run_bot['Admin'] = kangMID
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)
 
if run_bot['fino1'] == "":
    fino1 = FINBOTV1()
    timeline = FinbotChannel(fino1,channelId="1341209850")
    run_bot['fino1'] = str(fino1.authToken)
    fino1MID = fino1.getProfile().mid
    with open('finbotLogged.json', 'w') as fp:
    	json.dump(run_bot, fp, sort_keys=True, indent=4)
else:
    try:
        fino1 = FINBOTV1(run_bot['fino1'])
        timeline = FinbotChannel(fino1,channelId="1341209850")
        fino1MID = fino1.getProfile().mid
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)
    except:
        fino1 = FINBOTV1(run_bot['fino1'])
        timeline = FinbotChannel(fino1,channelId="1341209850")
        fino1MID = fino1.getProfile().mid
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)
 
if run_bot['fino2'] == "":
    fino2 = FINBOTV1()
    timeline = FinbotChannel(fino2,channelId="1341209850")
    run_bot['fino2'] = str(fino2.authToken)
    fino2MID = fino2.getProfile().mid
    with open('finbotLogged.json', 'w') as fp:
    	json.dump(run_bot, fp, sort_keys=True, indent=4)
else:
    try:
        fino2 = FINBOTV1(run_bot['fino2'])
        timeline = FinbotChannel(fino2,channelId="1341209850")
        fino2MID = fino2.getProfile().mid
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)
    except:
        fino2 = FINBOTV1(run_bot['fino2'])
        timeline = FinbotChannel(fino2,channelId="1341209850")
        fino2MID = fino2.getProfile().mid
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)
 
if run_bot['fino3'] == "":
    fino3 = FINBOTV1()
    timeline = FinbotChannel(fino3,channelId="1341209850")
    run_bot['fino3'] = str(fino3.authToken)
    fino3MID = fino3.getProfile().mid
    with open('finbotLogged.json', 'w') as fp:
    	json.dump(run_bot, fp, sort_keys=True, indent=4)
else:
    try:
        fino3 = FINBOTV1(run_bot['fino3'])
        timeline = FinbotChannel(fino3,channelId="1341209850")
        fino3MID = fino3.getProfile().mid
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)
    except:
        fino3 = FINBOTV1(run_bot['fino3'])
        timeline = FinbotChannel(fino3,channelId="1341209850")
        fino3MID = fino3.getProfile().mid
        with open('finbotLogged.json', 'w') as fp:
        	json.dump(run_bot, fp, sort_keys=True, indent=4)

finbotpoll = FinbotPoll(kang)
kangSettings = kang.getSettings()
fino1Settings = fino1.getSettings()
fino2Settings = fino2.getSettings()
fino3Settings = fino3.getSettings()

FNO = [kang, fino1, fino2, fino3]
ListBots = [kangMID, fino1MID, fino2MID, fino3MID]
Creator = run_bot['Creator']
masterAdmin = run_bot['Mid']
admin = run_bot["Admin"] + Creator
Master = Creator + masterAdmin + admin

settBot = codecs.open("finbot.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")

bot_run = json.load(settBot)
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)

protectname = []
msg_dict = {}
msg_dict1 = {}

host = 'https://gfs.line.naver.jp'
FINBOT_AUTH_QUERY_PATH = '/api/v4p/rs'
FINBOT_AUTH_QUERY_PATH_FIR = '/api/v4/TalkService.do'
FINBOT_CERTIFICATE_PATH = '/Q'
FINBOT_API_QUERY_PATH_FIR = '/S4'

UA, LA = ("Line/10.10.2 iPad4,1 9.0.2",'DESKTOPMAC 10.10.2\x64 MAC 4.5.0')
UA1, LA1 = ('Line/8.3.3','CHROMEOS\t091.4.13\tChrome_OS\t091')
UA2, LA2 = ('Line/8.3.3','DESKTOPWIN\t8.3.\t18.99')
UA3, LA3 = ('Line/8.3.3','IOSIPAD\t6.9\tFinBot-PC\t6.9')
UA4, LA4 = ('Line/8.3.3','WIN10\t5.5.1\tFinBot-PC\tV1.5\10.13.2')
UA5, LA5 = ('Line/8.3.3','CLOVAFRIENDS\t5.5.1\tFinBot-PC\tV1.5\10.13.2')
wait = {"finbot":True,"bb":True}

if bot_run["restartBot"] != None:
    kang.sendMessage(bot_run["restartBot"], "🄵🄸🄽 🄱🄾🅃\nRestart")
try:
    run_bot["assist"] = {}
    run_bot["assist"][kangMID] = True
    run_bot["assist"][fino1MID] = True
    run_bot["assist"][fino2MID] = True
    run_bot["assist"][fino3MID] = True
    backupData()
    print ("ই۝🄵🄸🄽 🄱🄾🅃۝ईई═┅\nRunning...")
except:
    print ("\nই۝🄵🄸🄽 🄱🄾🅃۝ईई═┅\nRunning...")
try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")

class bot():
    def botLogin():
        try:
            bot1 = FINBOTV1(run_bot["Token"])
            botMID = bot1.getProfile().mid
            run_bot["TokenMid"] = botMID
            with open("finbotLogged.json", "w") as fp:
        	    json.dump(run_bot, fp, sort_keys=True, indent=4)
            return bot1
        except:
            bot1 = FINBOTV1(run_bot["Token"])
            botMID = bot1.getProfile().mid
            bot1Settings = bot1.getSettings()
            return bot1

def getJson(url, headers=None):
    if headers is None:
        return json.loads(_session.get(url).text)
    else:
        return json.loads(_session.get(url, headers=headers).text)

def defaultCallback(str):
    print(str)

def createTransport(path=None, update_headers=None, service=None):
    Headers = {'User-Agent': UA,'X-Line-Application': LA,"x-lal": "ja-US_US"}
    Headers.update({"x-lpqs" : path})
    if(update_headers is not None):
        Headers.update(update_headers)
    transport = THttpClient.THttpClient(host + path)
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = service(protocol)
    return client

def createTransport1(path=None, update_headers=None, service=None):
    Headers = {'User-Agent': UA1,'X-Line-Application': LA1,"x-lal": "ja-US_US"}
    Headers.update({"x-lpqs" : path})
    if(update_headers is not None):
        Headers.update(update_headers)
    transport = THttpClient.THttpClient(host + path)
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = service(protocol)
    return client
 
def createTransport2(path=None, update_headers=None, service=None):
    Headers = {'User-Agent': UA2,'X-Line-Application': LA2,"x-lal": "ja-US_US"}
    Headers.update({"x-lpqs" : path})
    if(update_headers is not None):
        Headers.update(update_headers)
    transport = THttpClient.THttpClient(host + path)
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = service(protocol)
    return client

def createTransport3(path=None, update_headers=None, service=None):
    Headers = {'User-Agent': UA3,'X-Line-Application': LA3,"x-lal": "ja-US_US"}
    Headers.update({"x-lpqs" : path})
    if(update_headers is not None):
        Headers.update(update_headers)
    transport = THttpClient.THttpClient(host + path)
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = service(protocol)
    return client

def createTransport4(path=None, update_headers=None, service=None):
    Headers = {'User-Agent': UA4,'X-Line-Application': LA4,"x-lal": "ja-US_US"}
    Headers.update({"x-lpqs" : path})
    if(update_headers is not None):
        Headers.update(update_headers)
    transport = THttpClient.THttpClient(host + path)
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = service(protocol)
    return client

def createTransport5(path=None, update_headers=None, service=None):
    Headers = {'User-Agent': UA5,'X-Line-Application': LA5,"x-lal": "ja-US_US"}
    Headers.update({"x-lpqs" : path})
    if(update_headers is not None):
        Headers.update(update_headers)
    transport = THttpClient.THttpClient(host + path)
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = service(protocol)
    return client

def autoRestart():
    if time.time() - botStart > int(bot_run["timeRestart"]):
        backupData()
        time.sleep(5)
        restartBot()

def backupData():
    try:
        backup = bot_run
        f = codecs.open('finbot.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup3 = run_bot
        f = codecs.open('finbotLogged.json','w','utf-8')
        json.dump(backup3, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        print (error)
        return False

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                kang.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])) > timedelta(1):
            del msg_dict1[msg_id]

def atend():
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
atexit.register(atend)

def atend1():
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4,separators=(',', ': '))
atexit.register(atend)

def restart_program():
    print ("\nই۝🄵🄸🄽 🄱🄾🅃۝ईई═\nRestarted\nPlease Wait...\n")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def restartBot():
    print ("\nই۝🄵🄸🄽 🄱🄾🅃۝ईई═\nRestarting\nPlease Wait...\n")
    backupData() #Restart and backup data
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d 針D %02d 時間H %02d 分M %02d 秒S' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d 針D %02d 時間H %02d 分M %02d 秒S' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "[ 合計Total {} ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i.) " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(kang.getGroup(to).name))
                except:
                    no = "\n╚══[ ┅═ই۝🄵🄸🄽 🄱🄾🅃۝ईई═┅ ]"
        kang.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kang.sendMessage(to, "[ INFO Mention member] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "は hai..? ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+bot_run["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(kang.getGroup(to).name))
                except:
                    no = "\n╚══ই۝🄵🄸🄽 🄱🄾🅃۝ईई"
        kang.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kang.sendMessage(to, "[ INFO Sider Member] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "ようこそWelcome ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = kang.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+bot_run["welcome"]+"\nGrup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(kang.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        kang.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kang.sendMessage(to, "[ INFO Welcome Member] Error :\n" + str(error))

def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kang.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kang.sendMessage(to, "[ INFO ] Send Mention Error :\n" + str(error))

def sendMentionV1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kang.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kang.sendMessage(to, "[ INFO ] Send MentionV1 Error :\n" + str(error))

def sendMentionV2(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kang.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kang.sendMessage(to, "[ INFO ] Send mentionV2 Error :\n" + str(error))

def sendMentionV3(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kang.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kang.sendMessage(to, "[ INFO ] Send mentionV2 Error :\n" + str(error))

def sendMentionV4(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kang.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        kang.sendMessage(to, "[ INFO ] Send mentionV2 Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(bot_run["keyCommand1"]):
        cmd = pesan.replace(bot_run["keyCommand1"],"")
    else:
        cmd = "command"
    return cmd

groupParam = ""
def SiriMalvado(target):
    kang.kickoutFromGroup(groupParam,[target])

def patada(target):
    kang.kickoutFromGroup(groupParam,[target])

def finbot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if bot_run["autoBlock"] == True:
                kang.sendMessage(op.param1, "申し訳ありません...Autoblock on！自動ブロックがアクティブです。")
                kang.blockContact(op.param1)
            if bot_run["autoAdd"] == True:
                if op.param2 not in ListBots and op.param2 not in Master:
                    if (bot_run["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        kang.findAndAddContactsByMid(op.param1)
                        kang.sendMessage(op.param1, bot_run["message"])

        if op.type == 0:
            return
        if op.type == 11:
            if op.param1 in bot_run["Pro_Qr"]:
                try:
                    if kang.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in ListBots and op.param2 not in Master:
                            Ticket = kang.reissueGroupTicket(op.param1)
                            fino3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            X = kang.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            kang.updateGroup(X)
                            bot_run["Blacklist_User"][op.param2] = True
                            kang.kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        if fino1.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in ListBots and op.param2 not in Master:
                                Ticket = fino1.reissueGroupTicket(op.param1)
                                fino3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                X = fino1.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                fino1.updateGroup(X)
                                bot_run["Blacklist_User"][op.param2] = True
                                fino3.kickoutFromGroup(op.param1,[op.param2])
                                fino3.leaveGroup(op.param1)
                    except:
                        try:
                            if fino2.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in ListBots and op.param2 not in Master:
                                    Ticket = fino2.reissueGroupTicket(op.param1)
                                    fino3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    X = fino2.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    fino2.updateGroup(X)
                                    bot_run["Blacklist_User"][op.param2] = True
                                    fino3.kickoutFromGroup(op.param1,[op.param2])
                                    fino3.leaveGroup(op.param1)
                        except:
                            pass
            if bot_run["nyusup"] == True:
                try:
                    if kang.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in ListBots and op.param2 not in Master:
                            Ticket = kang.reissueGroupTicket(op.param1)
                            fino1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            fino2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            fino3.acceptGroupInvitationByTicket(op.param1,Ticket)
                except:
                    pass
            if op.param3 == '1':
                if op.param1 in protectname:
                    try:
                        if op.param2 not in ListBots and op.param2 not in Master:
                        	group = kang.getGroup(op.param1)
                        group.name = bot_run["pro_name"][op.param1]
                        kang.updateGroup(group)
                        kang.sendMessage(op.param1, "Group Name protected\nYou have been warned..!")
                        kang.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        bot_run["Blacklist_User"][op.param2] = True
                    except:
                        pass
            if op.param3 == '1':
                if op.param1 in bot_run['pname']:
                    try:
                        G = fino1.getGroup(op.param1)
                    except:
                        try:
                            G = fino2.getGroup(op.param1)
                        except:
                            try:
                                G = fino3.getGroup(op.param1)
                            except:
                                pass
                    G.name = bot_run['pro_name'][op.param1]
                    try:
                        fino1.updateGroup(G)
                    except:
                        try:
                            fino2.updateGroup(G)
                        except:
                            try:
                                fino3.updateGroup(G)
                            except:
                                pass
                    if op.param2 in ListBots and op.param2 in Master:
                        pass
                    else:
                        try:
                            fino1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                fino2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    fino3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    kang.sendMessage(op.param1,"No permission! \nPlease do not change group name")

        if op.type == 13:
            if kangMID in op.param3:
                if bot_run["autoLeave"] == True:
                    if op.param2 not in ListBots and op.param2 not in Master:
                        kang.acceptGroupInvitation(op.param1)
                        ginfo = kang.getGroup(op.param1)
                        contact = kang.getContact(op.param2)
                        kang.sendMessage(op.param1,"السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ" +str(ginfo.name))
                        kang.sendMessage(op.param1,"Maaf...! kak" +str(contact.displayName) + "\nizin dulu klo invite, jangan asal comot")
                        kang.leaveGroup(op.param1)
                    else:
                        kang.acceptGroupInvitation(op.param1)
                        ginfo = kang.getGroup(op.param1)
                        kang.sendMessage(op.param1,"السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ" +str(ginfo.name))
            if kangMID in op.param3:
                G = kang.getGroup(op.param1)
                if bot_run["autoJoin"] == True:
                    if bot_run["limiter"]["on"] == True:
                        if len(G.members) <= bot_run["limiter"]["members"]:
                            kang.acceptGroupInvitation(op.param1)
                            group = kang.getGroup(op.param1)
                            kang.sendMessage(op.param1,"Maaf jumlah member\n " + str(group.name) + " kurang dari " + str(bot_run["limiter"]["members"]))
                            kang.leaveGroup(op.param1)
                        else:
                            kang.acceptGroupInvitation(op.param1)
                    else:
                        kang.acceptGroupInvitation(op.param1)
                elif bot_run["limiter"]["on"] == True:
                    if len(G.members) <= bot_run["limiter"]["members"]:
                        kang.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in bot_run["Blacklist_User"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    kang.cancelGroupInvitation(op.param1, matched_list)
            if fino1MID in op.param3:
                if bot_run["autoJoin"] == True:
                    if op.param2 not in Listbot and op.param2 not in Master:
                        fino1.acceptGroupInvitation(op.param1)
                        ginfo = fino1.getGroup(op.param1)
                        contact = fino1.getGroup(op.param2)
                        fino1.sendMessage(op.param1,"Sorry...! " + str(contact.displayName) + "You're not an admin")
                        fino1.leaveGroup(op.param1)
                    else:
                        fino1.acceptGroupInvitation(op.param1)
            if fino2MID in op.param3:
                if bot_run["autoJoin"] == True:
                    if op.param2 not in Listbot and op.param2 not in Master:
                        fino2.acceptGroupInvitation(op.param1)
                        ginfo = fino2.getGroup(op.param1)
                        contact = fino2.getGroup(op.param2)
                        fino2.sendMessage(op.param1,"Sorry...! " + str(contact.displayName) + "You're not an admin")
                        fino2.leaveGroup(op.param1)
                    else:
                        fino2.acceptGroupInvitation(op.param1)
            if fino3MID in op.param3:
                if bot_run["autoJoin"] == True:
                    if op.param2 not in Listbot and op.param2 not in Master:
                        fino3.acceptGroupInvitation(op.param1)
                        ginfo = fino3.getGroup(op.param1)
                        contact = fino3.getGroup(op.param2)
                        fino3.sendMessage(op.param1,"Sorry...! " + str(contact.displayName) + "You're not an admin")
                        fino3.leaveGroup(op.param1)
                    else:
                        fino3.acceptGroupInvitation(op.param1)
            if bot_run["BLinviter"] == True:
            	if op.param2 not in ListBots:
                	kang.cancelGroupInvitation(op.param1,[op.param3])
            	random.choice(FNO).kickoutFromGroup(op.param1,[op.param2])
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in bot_run["Blacklist_User"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    kang.cancelGroupInvitation(op.param1, matched_list)
            if op.param1 in bot_run["Pro_Invite"]:
                if op.param2 not in ListBots and op.param2 not in Master:
                    try:
                        group = fino1.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            fino1.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = fino2.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                fino2.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = fino3.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    fino3.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                pass

        if op.type == 17:
            if op.param2 in bot_run["Blacklist_User"]:
                random.choice(FNO).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
            if op.param1 in bot_run["Welcome"]:
                if op.param2 in ListBots:
                    pass
                ginfo = kang.getGroup(op.param1)
                contact = kang.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                kang.sendImageWithURL(op.param1, image)
            if op.param1 in bot_run["Pro_Join"]:
                if op.param2 not in ListBots and op.param2 not in Master:
                    bot_run["Blacklist_User"][op.param2] = True
                    try:
                        fino1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            fino2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                fino3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

        if op.type == 32:
            if op.param1 in bot_run["Pro_Cancel"]:
                if op.param2 not in ListBots or Master:
                    bot_run["Blacklist_User"][op.param2] = True
                    try:
                        if op.param3 not in bot_run["Blacklist_User"]:
                            fino1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in bot_run["blacklist"]:
                                fino2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in bot_run["blacklist"]:
                                    fino3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                random.choice(FNO).kickoutFromGroup(op.param1,[op.param2])
            if op.param2 in bot_run["Blacklist_User"]:
                if op.param2 not in ListBots or Master:
                    try:
                        if op.param3 not in bot_run["Blacklist_User"]:
                            random.choice(FNO).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass

        if op.type == 19:
            if op.param1 in bot_run["Pro_Member"]:
                if op.param2 not in ListBots or Master:
                    bot_run["Blacklist_User"][op.param2] = True
                    random.choice(FNO).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
            if kangMID in op.param3:
                if op.param2 in ListBots:
                    pass
                if op.param2 in Master:
                    pass
                else:
                    bot_run["Blacklist_User"][op.param2] = True
                    try:
                        fino1.kickoutFromGroup(op.param1,[op.param2])
                        fino1.inviteIntoGroup(op.param1,[op.param3])
                        kang.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            fino2.kickoutFromGroup(op.param1,[op.param2])
                            fino2.inviteIntoGroup(op.param1,[op.param3])
                            kang.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                fino3.kickoutFromGroup(op.param1,[op.param2])
                                fino3.inviteIntoGroup(op.param1,[op.param3])
                                kang.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = fino1.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    fino1.updateGroup(G)
                                    Ticket = fino1.reissueGroupTicket(op.param1)
                                    kang.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = fino1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    fino1.updateGroup(G)
                                    Ticket = fino1.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        fino1.kickoutFromGroup(op.param1,[op.param2])
                                        fino1.inviteIntoGroup(op.param1,[op.param3])
                                        kang.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            fino2.inviteIntoGroup(op.param1,[op.param3])
                                            fino2.kickoutFromGroup(op.param1,[op.param2])
                                            kang.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if fino1MID in op.param3:
                if op.param2 in ListBots:
                    pass
                if op.param2 in Master:
                    pass
                else:
                    bot_run["Blacklist_User"][op.param2] = True
                    try:
                        fino2.kickoutFromGroup(op.param1,[op.param2])
                        fino2.inviteIntoGroup(op.param1,[op.param3])
                        fino1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            fino3.kickoutFromGroup(op.param1,[op.param2])
                            fino3.inviteIntoGroup(op.param1,[op.param3])
                            fino1.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kang.kickoutFromGroup(op.param1,[op.param2])
                                kang.inviteIntoGroup(op.param1,[op.param3])
                                fino1.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = fino3.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    fino2.kickoutFromGroup(op.param1,[op.param2])
                                    fino3.updateGroup(G)
                                    Ticket = fino3.reissueGroupTicket(op.param1)
                                    kang.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kang.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kang.updateGroup(G)
                                    kang.kickoutFromGroup(op.param1,[op.param2])
                                    Ticket = kang.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        fino2.kickoutFromGroup(op.param1,[op.param2])
                                        fino2.inviteIntoGroup(op.param1,[op.param3])
                                        fino1.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            fino3.inviteIntoGroup(op.param1,[op.param3])
                                            fino3.kickoutFromGroup(op.param1,[op.param2])
                                            fino1.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if fino2MID in op.param3:
                if op.param2 in ListBots:
                    pass
                if op.param2 in Master:
                    pass
                else:
                    bot_run["Blacklist_User"][op.param2] = True
                    try:
                        fino3.kickoutFromGroup(op.param1,[op.param2])
                        fino3.inviteIntoGroup(op.param1,[op.param3])
                        fino2.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            fino1.kickoutFromGroup(op.param1,[op.param2])
                            fino1.inviteIntoGroup(op.param1,[op.param3])
                            fino2.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kang.kickoutFromGroup(op.param1,[op.param2])
                                kang.inviteIntoGroup(op.param1,[op.param3])
                                fino2.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = fino1.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    fino3.kickoutFromGroup(op.param1,[op.param2])
                                    fino1.updateGroup(G)
                                    Ticket = fino1.reissueGroupTicket(op.param1)
                                    kang.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = fino1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    fino1.updateGroup(G)
                                    fino3.kickoutFromGroup(op.param1,[op.param2])
                                    Ticket = fino1.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        fino3.kickoutFromGroup(op.param1,[op.param2])
                                        fino3.inviteIntoGroup(op.param1,[op.param3])
                                        fino2.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            fino1.inviteIntoGroup(op.param1,[op.param3])
                                            fino1.kickoutFromGroup(op.param1,[op.param2])
                                            fino2.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if fino3MID in op.param3:
                if op.param2 in ListBots:
                    pass
                if op.param2 in Master:
                    pass
                else:
                    bot_run["Blacklist_User"][op.param2] = True
                    try:
                        kang.kickoutFromGroup(op.param1,[op.param2])
                        kang.inviteIntoGroup(op.param1,[op.param3])
                        fino3.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            fino1.kickoutFromGroup(op.param1,[op.param2])
                            fino1.inviteIntoGroup(op.param1,[op.param3])
                            fino3.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                fino2.kickoutFromGroup(op.param1,[op.param2])
                                fino2.inviteIntoGroup(op.param1,[op.param3])
                                fino3.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = fino1.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    fino3.kickoutFromGroup(op.param1,[op.param2])
                                    fino1.updateGroup(G)
                                    Ticket = fino1.reissueGroupTicket(op.param1)
                                    kang.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    fino3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = fino1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    fino1.updateGroup(G)
                                    kang.kickoutFromGroup(op.param1,[op.param2])
                                    Ticket = fino1.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        fino1.kickoutFromGroup(op.param1,[op.param2])
                                        fino1.inviteIntoGroup(op.param1,[op.param3])
                                        fino3.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            fino2.inviteIntoGroup(op.param1,[op.param3])
                                            fino2.kickoutFromGroup(op.param1,[op.param2])
                                            fino3.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
        if op.type == 55:
            try:
                if op.param1 in bot_run["readPoint"]:
                   if op.param2 in bot_run["readMember"][op.param1]:
                       pass
                   else:
                       bot_run["readMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass
            if bot_run['setWicked'][op.param1]==True:
                if op.param1 in bot_run['setTime']:
                    Name = kang.getContact(op.param2).displayName
                    Ppname = kang.getContact(op.param2).pictureStatus
                    if Name in bot_run['setSider'][op.param1]:
                        pass
                    else:
                        bot_run['setSider'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        kang.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Ppname)
            if op.param2 in bot_run["Blacklist_User"]:
                random.choice(FNO).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != kang.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if bot_run["scanner"] == True:
                    kang.sendChatChecked(to, msg_id)
                if to in bot_run["scanPoint"]:
                    if sender not in bot_run["scanROM"][msg.to]:
                        bot_run["scanROM"][msg.to][sender] = True
                if bot_run["unsendMessage"] == True:
                    try:
                        msg = op.message
                        if msg.toType == 0:
                            kang.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                        else:
                            kang.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                            msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                    except Exception as error:
                        print (error)
                if msg.contentType == 0:
                    msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                if msg.contentType == 1:
                    path = kang.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
                if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n• Sticker ID : {}".format(stk_id)
                   ret_ += "\n• Sticker Version : {}".format(stk_ver)
                   ret_ += "\n• Sticker Package : {}".format(pkg_id)
                   ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                       data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                       path = kang.downloadFileURL(data)
                       msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}

        if op.type == 65:
            if bot_run["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = kang.getGroup(at)
                                pelaku = kang.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(pelaku.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':pelaku.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                kang.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                kang.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = kang.getGroup(at)
                                pelaku = kang.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(pelaku.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                kang.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

            if bot_run["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = kang.getGroup(at)
                                pelaku = kang.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(pelaku.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                kang.sendMessage(at, str(ret_))
                                kang.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 26:
           if wait["finbot"] == True:
               msg = op.message
               if msg._from not in ListBots:
                 if bot_run["talkban"] == True:
                   if msg._from in bot_run["Talkblacklist"]:
                      try:
                          kang.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          pass

        if op.type == 26:
           if wait["finbot"] == True:
               if bot_run["ResponPc"] == True:
                 if msg.toType == 0:
                     kang.sendChatChecked(msg._from,msg.id)
                     contact = kang.getContact(msg._from)
                     #kang.sendImageWithURL(msg._from, "http://dl.profile.line-cdn.net{}".format(contact.picturePath))
                     kang.sendMessage(msg._from, "╔═══════════════╗\n「Auto Reply」\n  ??🄸🄽 🄱🄾🅃\nHaii... {}".format(contact.displayName) + "\n Mohon maaf....!\nIni adalah pesan otomatis, \nJika ada yang penting hubungi saya nanti\n Terima Kasih\n\n╚═══════════════╝")
               if "MENTION" in msg.contentMetadata.keys() != None:
                 if bot_run['detectMention'] == True:
                     contact = kang.getContact(msg._from)
                     cName = contact.pictureStatus
                     balas = ["http://dl.profile.line-cdn.net/" + cName]
                     ret_ = random.choice(balas)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention["MENTIONEES"]
                     for mention in mentionees:
                           if mention["M"] in mid:
                                  #kang.sendImageWithURL(msg._from,ret_)
                                  sendMessageWithMention(msg._from,bot_run["Respontag"])
                                  break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if bot_run["MentionKick"] == True:
                     contact = kang.getContact(msg._from)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in mid:
                                  kang.sendMessage(msg.to,"don't tag me")
                                  random.choice(FNO).kickoutFromGroup(msg.to,[msg._from])
                                  break

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 1:
                 if msg._from in Master:
                    if bot_run["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = kang.server.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % bot_run["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            kang.sendMessage(msg.to, "Add image success")
                        bot_run["Img"] = {}
                        bot_run["Addimage"] = False
               if msg.contentType == 2:
                 if msg._from in Master:
                    if bot_run["Addvideo"]["status"] == True:
                        path = kang.downloadObjectMsg(msg.id)
                        videos[bot_run["Addvideo"]["name"]] = str(path)
                        f = codecs.open("video.json","w","utf-8")
                        json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                        kang.sendMessage(msg.to, "Berhasil menambahkan video {}".format(str(bot_run["Addvideo"]["name"])))
                        bot_run["Addvideo"]["status"] = False                
                        bot_run["Addvideo"]["name"] = ""
               if msg.contentType == 3:
                 if msg._from in Master:
                    if bot_run["Addaudio"]["status"] == True:
                        path = kang.downloadObjectMsg(msg.id)
                        audios[bot_run["Addaudio"]["name"]] = str(path)
                        f = codecs.open("audio.json","w","utf-8")
                        json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                        kang.sendMessage(msg.to, "Berhasil menambahkan mp3 {}".format(str(bot_run["Addaudio"]["name"])))
                        bot_run["Addaudio"]["status"] = False                
                        bot_run["Addaudio"]["name"] = ""
               if msg.contentType == 7:
                 if msg._from in Master:
                    if bot_run["Addsticker"]["status"] == True:
                        stickers[bot_run["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                        f = codecs.open("sticker.json","w","utf-8")
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        kang.sendMessage(msg.to, "Berhasil menambahkan sticker {}".format(str(bot_run["Addsticker"]["name"])))
                        bot_run["Addsticker"]["status"] = False                
                        bot_run["Addsticker"]["name"] = ""
               if msg.contentType == 1:
                 if msg._from in Master:
                    if bot_run["changePicture"] == True:
                       path = kang.downloadObjectMsg(msg_id)
                       path1 = fino1.downloadObjectMsg(msg_id)
                       path2 = fino2.downloadObjectMsg(msg_id)
                       path3 = fino3.downloadObjectMsg(msg_id)
                       bot_run["changePicture"] = False
                       kang.updateProfilePicture(path)
                       kang.sendMessage(msg.to, bot_run["Responcft"])
                       fino1.updateProfilePicture(path1)
                       fino1.sendMessage(msg.to, bot_run["Responcft"])
                       fino2.updateProfilePicture(path2)
                       fino2.sendMessage(msg.to, bot_run["Responcft"])
                       fino3.updateProfilePicture(path3)
                       fino3.sendMessage(msg.to, bot_run["Responcft"])

                 if msg._from in Master:
                     if kangMID in bot_run["foto"]:
                         path = kang.downloadObjectMsg(msg.id)
                         del bot_run["foto"][kangMID]
                         kang.updateProfilePicture(path)
                         kang.sendMessage(msg.to,bot_run["Responcft"])
                 if msg._from in Master:
                     if fino1MID in bot_run["foto"]:
                         path = fino1.downloadObjectMsg(msg.id)
                         del bot_run["foto"][fino1MID]
                         fino1.updateProfilePicture(path)
                         fino1.sendMessage(msg.to,bot_run["Responcft"])
                 if msg._from in Master:
                     if fino2MID in bot_run["foto"]:
                         path = fino2.downloadObjectMsg(msg.id)
                         del bot_run["foto"][fino2MID]
                         fino2.updateProfilePicture(path)
                         fino2.sendMessage(msg.to,bot_run["Responcft"])
                 if msg._from in Master:
                     if fino3MID in bot_run["foto"]:
                         path = fino3.downloadObjectMsg(msg.id)
                         del bot_run["foto"][fino3MID]
                         fino3.updateProfilePicture(path)
                         fino3.sendMessage(msg.to,bot_run["Responcft"])

               if msg.contentType == 2:
                   if msg._from in Master:
                       if kangMID in bot_run["video"]:
                            path = kang.downloadObjectMsg(msg_id)
                            del bot_run["video"][kangMID]
                            kang.updateProfileVideoPicture(path)
                            kang.sendMessage(msg.to,"Photo Profile switch to video")

               if msg.toType == 2:
                 if msg._from in Master:
                   if bot_run["groupPicture"] == True:
                     path = kang.downloadObjectMsg(msg_id)
                     bot_run["groupPicture"] = False
                     kang.updateGroupPicture(msg.to, path)
                     kang.sendMessage(msg.to, bot_run["Responcft"])

               if msg.contentType == 13:
                  if bot_run["invite1"] == True:
                    if msg._from in Master:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = kang.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                kang.sendMessage(msg.to,"-> " + _name + "\nThis user has been joined ")
                                break
                            elif invite in bot_run["Blacklist_User"]:
                                kang.sendMessage(msg.to,"Failure invitation, " + _name + "Blacklist user")
                                kang.sendMessage(msg.to,"Please contact an owner/admin!, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    kang.findAndAddContactsByMid(target)
                                    kang.inviteIntoGroup(msg.to,[target])
                                    kang.sendMessage(msg.to,"Target invited : \n ➡" + _name)
                                    bot_run["invite1"] = False
                                    break
                                except:
                                    try:
                                        kang.findAndAddContactsByMid(invite)
                                        kang.inviteIntoGroup(op.param1,[invite])
                                        bot_run["invite1"] = False
                                    except:
                                        kang.sendMessage(msg.to,"Negative, Error invitation")
                                        bot_run["invite1"] = False
                                        break

               if msg.contentType == 13:
                 if bot_run["contact"] == True:
                    msg.contentType = 0
                    kang.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = kang.getContact(msg.contentMetadata["mid"])
                        path = kang.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        kang.sendMessage(msg.to,"♐ Nama : " + msg.contentMetadata["displayName"] + "\n♐ MID : " + msg.contentMetadata["mid"] + "\n♐ Status Msg : " + contact.statusMessage + "\n♐ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        kang.sendImageWithURL(msg.to, image)
                 if msg._from in Master:
                  if bot_run["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in bot_run["Blacklist_User"]:
                        kang.sendMessage(msg.to,"This user is already blacklist")
                        bot_run["wblacklist"] = False
                    else:
                        bot_run["wblacklist"] = True
                        bot_run["Blacklist_User"][msg.contentMetadata["mid"]] = True
                        kang.sendMessage(msg.to,bot_run["ResponWBL"])
                        bot_run["wblacklist"] = False
                 if msg._from in Master:
                  if bot_run["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in bot_run["Blacklist_User"]:
                        del bot_run["Blacklist_User"][msg.contentMetadata["mid"]]
                        kang.sendMessage(msg.to,bot_run["ResponDBL"])
                        bot_run["dblacklist"] = False
                    else:
                        kang.sendMessage(msg.to,"No blacklist")
                        bot_run["dblacklist"] = False
                 if msg._from in Master:
                  if bot_run["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in bot_run["Talkblacklist"]:
                        kang.sendMessage(msg.to,"This user is already Talkblacklist")
                        bot_run["Talkwblacklist"] = False
                    else:
                        bot_run["Talkwblacklist"] = True
                        bot_run["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        kang.sendMessage(msg.to,bot_run["ResponWTBL"])
                        bot_run["Talkwblacklist"] = False
                 if msg._from in Master:
                  if bot_run["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in bot_run["Talkblacklist"]:
                        del bot_run["Talkblacklist"][msg.contentMetadata["mid"]]
                        kang.sendMessage(msg.to,bot_run["ResponDTBL"])
                        bot_run["Talkdblacklist"] = False
                    else:
                        kang.sendMessage(msg.to,"No Talkblacklist")
                        bot_run["Talkdblacklist"] = False

               if msg.contentType == 16:
                 if bot_run["checkPost"] == True:
                     try:
                         ret_ = "╔════[ Post Detail ]"
                         if msg.contentMetadata["serviceType"] == "GB":
                             contact = kang.getContact(sender)
                             auth = "\n╠❐ Author : {}".format(str(contact.displayName))
                         else:
                             auth = "\n╠❐ Author : {}".format(str(msg.contentMetadata["serviceName"]))
                         purl = "\n╠❐ Url : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                         ret_ += auth
                         ret_ += purl
                         if "mediaOid" in msg.contentMetadata:
                             object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                             if msg.contentMetadata["mediaType"] == "V":
                                 if msg.contentMetadata["serviceType"] == "GB":
                                     ourl = "\n╠❐ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                     murl = "\n╠❐ Url Media : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                 else:
                                     ourl = "\n╠❐ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                     murl = "\n╠❐ Url Media : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                 ret_ += murl
                             else:
                                 if msg.contentMetadata["serviceType"] == "GB":
                                     ourl = "\n╠❐ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                 else:
                                     ourl = "\n╠❐ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                             ret_ += ourl
                         if "stickerId" in msg.contentMetadata:
                             stck = "\n╠❐ Sticker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                             ret_ += stck
                         if "text" in msg.contentMetadata:
                             text = "\n╠❐ Note : {}".format(str(msg.contentMetadata["text"]))
                             ret_ += text
                         ret_ += "\n╚══[ 🄵🄸🄽 🄱🄾🅃 ]"
                         kang.sendMessage(to, str(ret_))
                     except:
                         kang.sendMessage(msg.to,"Invalid Post")
               if msg.contentType == 7:
                if bot_run["stickerOn"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        r = s.get("https://store.line.me/stickershop/product/{}/id".format(urllib.parse.quote(pkg_id)))
                        soup = BeautifulSoup(r.content, 'html5lib')
                        data = soup.select("[class~=mdBtn01Txt]")[0].text
                        if data == 'Lihat Produk Lain':
                            ret_ = "「 Sticker Info 」"
                            ret_ += "\n• STICKER ID : {}".format(stk_id)
                            ret_ += "\n• STICKER PACKAGES ID : {}".format(pkg_id)
                            ret_ += "\n• STICKER VERSION : {}".format(stk_ver)
                            ret_ += "\n• STICKER URL : line://shop/detail/{}".format(pkg_id)
                            kang.sendMessage(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = kang.downloadFileURL(data)
                               kang.sendImage(msg.to,path)
                        else:
                            ret_ = "「 Sticker Info 」"
                            ret_ += "\n• PRICE : "+soup.findAll('p', attrs={'class':'mdCMN08Price'})[0].text
                            ret_ += "\n• AUTHOR : "+soup.select("a[href*=/stickershop/author]")[0].text
                            ret_ += "\n• STICKER ID : {}".format(str(stk_id))
                            ret_ += "\n• STICKER PACKAGES ID : {}".format(str(pkg_id))
                            ret_ += "\n• STICKER VERSION : {}".format(str(stk_ver))
                            ret_ += "\n• STICKER URL : line://shop/detail/{}".format(str(pkg_id))
                            ret_ += "\n• DESCRIPTION :\n"+soup.findAll('p', attrs={'class':'mdCMN08Desc'})[0].text
                            kang.sendMessage(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = kang.downloadFileURL(data)
                               kang.sendImage(msg.to,path)

               if msg.contentType == 0:
                    if bot_run["AutoRead"] == True:
                        kang.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                    	for sticker in stickers:
                         if msg._from in Master:
                           if text.lower() == sticker:
                              sid = stickers[text.lower()]["STKID"]
                              spkg = stickers[text.lower()]["STKPKGID"]
                              kang.sendSticker(to, spkg, sid)
                         for image in images:
                          if msg._from in Master:
                           if text.lower() == image:
                              kang.sendImage(msg.to, images[image])
                         for audio in audios:
                          if msg._from in Master:
                           if text.lower() == audio:
                              kang.sendAudio(msg.to, audios[audio])
                         for video in videos:
                          if msg._from in Master:
                           if text.lower() == video:
                              kang.sendVideo(msg.to, videos[video])
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               helpMessage = helpHeaders()
                               kang.sendMessage(msg.to, str(helpMessage))
                        if cmd == "@login" or cmd == "bot on":
                            if msg._from in Master:
                                wait["finbot"] = True
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                kang.sendMessage(msg.to, "🔄 @Relogin \n❏ Day : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n❏ Time : [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                        elif cmd == "@logout" or cmd == "bot off":
                            if msg._from in Master:
                                wait["finbot"] = False
                                kang.sendMessage(msg.to, "@Logout")
                        elif cmd == "auth@login" or cmd == "authbot on":
                            if msg._from in Master:
                                wait["bb"] = True
                                kang.sendMessage(msg.to, "Authentication@Relogin on\n❏ Day : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n❏ Time : [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                        elif cmd == "auth@logout" or cmd == "authbot off":
                            if msg._from in Master:
                                wait["bb"] = False
                                kang.sendMessage(msg.to, "Non authentication")
                        elif cmd == "setting" or cmd == 'settbot':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╔═══════════\n"
                                md+="║۝🄵🄸🄽 🄱🄾🅃۝\n"
                                md+="╠═══════════\n"
                                if bot_run["autoJoin"] == True: md+="║❏〘 Auto join 〙『 📲 』\n"
                                else: md+="║❏〘 Auto join 〙『 📴 』\n"
                                if bot_run["autoAdd"] == True: md+="║❏〘 Auto add 〙『 📲 』\n"
                                else: md+="║❏〘 Auto add 〙『 📴 』\n"
                                if bot_run["autoBlock"] == True: md+="║❏〘 Auto block 〙『 📲 』\n"
                                else: md+="║❏〘 Auto block 〙『 📴 』\n"
                                if bot_run["autoLeave"] == True: md+="║❏〘 Auto leave 〙『 📲 』\n"
                                else: md+="║❏〘 Auto leave 〙『 📴 』\n"
                                if bot_run["AutoRead"] == True: md+="║❏〘 Auto read 〙『 📲 』\n"
                                else: md+="║❏〘 Auto read 〙『 📴 』\n"
                                if bot_run["invite1"] == True: md+="║❏〘 Auto Inv 〙『 📲 』\n"
                                else: md+="║❏〘 Auto Inv 〙『 📴 』\n"
                                if bot_run["autokick"] == True: md+="║❏〘 Warning 〙『 📲 』\n"
                                else: md+="║❏〘 Warning 〙『 📴 』\n"
                                if bot_run["addbackupmem"] == True: md+="║❏〘 Backup mem 〙『 📲 』\n"
                                else: md+="║❏〘 Backup mem 〙『 📴 』\n"
                                if bot_run["checkPost"] == True: md+="║❏〘 CheckPost 〙『 📲 』\n"
                                else: md+="║❏〘 CheckPost 〙『 📴 』\n"
                                if bot_run["contact"] == True: md+="║❏〘 Contact 〙『 📲 』\n"
                                else: md+="║❏〘 Contact 〙『 📴 』\n"
                                if bot_run["changePicture"] == True: md+="║❏〘 Change pict 〙『 📲 』\n"
                                else: md+="║❏〘 Change pict 〙『 📴 』\n"
                                if bot_run["nyusup"] == True: md+="║❏〘 Mode Nyusup 〙『 📲 』\n"
                                else: md+="║❏〘 Mode Nyusup 〙『 📴 』\n"
                                if bot_run["limiter"]["on"] == True: md+="║❏〘 limiter 〙" + "『 " + str(bot_run["limiter"]["members"]) + " 』" + "\n"
                                else: md+="􀠁􀆩􏿿║❏〘 limiter 〙:『 📴 』\n"
                                if bot_run["scanner"] == True: md+="║❏〘 Scanner 〙『 📲 』\n"
                                else: md+="║❏〘 Scanner 〙『 📴 』\n"
                                if bot_run["detectMention"] == True: md+="║❏〘 Respon 〙『 📲 』\n"
                                else: md+="║❏〘 Respon 〙『 📴 』\n"
                                if bot_run["detectMention1"] == True: md+="║❏〘 Respon cont 〙『 📲 』\n"
                                else: md+="║❏〘 Respon cont 〙『 📴 』\n"
                                if bot_run["ResponPc"] == True: md+="║❏〘 Respon PC 〙『 📲 』\n"
                                else: md+="║❏〘 Respon PC 〙『 📴 』\n"
                                if bot_run["MentionKick"] == True: md+="║❏〘 Respon kick 〙『 📲 』\n"
                                else: md+="║❏〘 Respon kick 〙『 📴 』\n"
                                if bot_run["unsendMessage"] == True: md+="║❏〘 unsend Msg 〙『 📲 』\n"
                                else: md+="║❏〘 unsend Msg 〙『 📴 』\n"
                                if msg.to in welcome: md+="║❏〘 Welcome 〙『 📲 』\n"
                                else: md+="║❏〘 Welcome 〙『 📴 』\n"
                                if bot_run["pname"] == True: md+="║❏〘 Lockname 〙『 📲 』\n"
                                else: md+="║❏〘 Lockname 〙『 📴 』\n╚═══════════\n"
                                kang.sendMessage(msg.to, md+"╔═══════════\n" + "║〘 日付 〙: ["+ datetime.strftime(timeNow,'%Y-%m-%d')+"]\n" + "╠═══════════\n" + "║〘 時間 〙[ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n" + "╚═══════════")

                        elif ("token mac" in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                            	data = {'nama': '{}'.format(msg._from),'submit4': ''}
                            	post_response = requests.post(url = 'https://lazybot.us/snipz/', data = data)
                            	qr = post_response.text
                            	kang.sendMessage(msg.to, '{}'.format(qr))

                        elif ("token win10" in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                            	data = {'nama': '{}'.format(msg._from),'submit3': ''}
                            	post_response = requests.post(url = 'https://lazybot.us/snipz/', data = data)
                            	qr = post_response.text
                            	kang.sendMessage(msg.to, '{}'.format(qr))

                        elif ("token ios" in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                            	data = {'nama': '{}'.format(msg._from),'submit2': ''}
                            	post_response = requests.post(url = 'https://lazybot.us/snipz/', data = data)
                            	qr = post_response.text
                            	kang.sendMessage(msg.to, '{}'.format(qr))

                        elif ("token done" in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                            	data = {'nama': '{}'.format(msg._from),'submit5': ''}
                            	post_response = requests.post(url = 'https://lazybot.us/snipz/', data = data)
                            	qr = post_response.text
                            	kang.sendMessage(msg.to,"Give thanks for ۝🄵🄸🄽 🄱🄾🅃۝")
                            	kang.sendMessage(msg.to, '{}'.format(qr))

                        elif cmd == "autologin" or cmd == 'bot login':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               finolog = FINBOTV1()
                               run_bot["Token1"] = str(finolog.authToken)
                               user2 = finolog.getProfile().mid
                               kang.sendMessage(to,user2)
                               kang.sendMessage(to,run_bot["Token1"])
                               with open("finbotLogged.json", "w") as fp:
                               	json.dump(run_bot, fp, sort_keys=True, indent=4)

                        elif 'bot1 login: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('bot1 login: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendMessage(msg.to, "Replace failed")
                              else:
                                  run_bot["kang1"] = spl
                                  with open('finbotLogged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  kang.sendMessage(msg.to, "bot1 login by new authToken\n「{}」".format(str(spl)))

                        elif 'bot2 login: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('bot2 login: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendMessage(msg.to, "Replace failed")
                              else:
                                  run_bot["kang2"] = spl
                                  with open('finbotLogged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  kang.sendMessage(msg.to, "bot2 login by new authToken\n「{}」".format(str(spl)))

                        elif 'bot3 login: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('bot3 login: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendMessage(msg.to, "Replace failed")
                              else:
                                  run_bot["fino1"] = spl
                                  with open('finbotLogged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  kang.sendMessage(msg.to, "bot3 login by new authToken\n「{}」".format(str(spl)))

                        elif 'bot4 login: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('bot4 login: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendMessage(msg.to, "Replace failed")
                              else:
                                  run_bot["fino2"] = spl
                                  with open('finbotLogged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  kang.sendMessage(msg.to, "bot4 login by new authToken\n「{}」".format(str(spl)))

                        elif 'bot5 login: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('bot5 login: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendMessage(msg.to, "Replace failed")
                              else:
                                  run_bot["fino3"] = spl
                                  with open('finbotLogged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  kang.sendMessage(msg.to, "bot5 login by new authToken\n「{}」".format(str(spl)))

                        elif 'bot login: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('bot login: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendMessage(msg.to, "Replace failed")
                              else:
                                  run_bot["kang"] = spl
                                  with open('finbotLogged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  kang.sendMessage(msg.to, "bot login by new authToken\n「{}」".format(str(spl)))

                        elif 'change login: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('change login: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendMessage(msg.to, "Replace failed")
                              else:
                                  run_bot["authToken"] = spl
                                  with open('finbotLogged.json', 'w') as fp:
                                  	json.dump(run_bot, fp, sort_keys=True, indent=4)
                                  kang.sendMessage(msg.to, "bot login by new client\n「{}」".format(str(spl))+"\n\nPlease restart for run your client")

                        elif cmd == "rm bot" or cmd == 'rm allbot':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                kang.sendMessage(msg.to,"Caution!\nYour bot authThoken has been removed\nPlease regenerate your authToken for run back With auto relogin by type >Restart<")
                                run_bot["kang"] = ""
                                run_bot["kang1"] = ""
                                run_bot["kang2"] = ""
                                run_bot["fino1"] = ""
                                run_bot["fino2"] = ""
                                run_bot["fino3"] = ""
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                

                        elif cmd == "creator" or cmd == 'owner':
                            if msg._from in Master:
                                kang.sendMessage(msg.to,"╔═══════════\n║Creator \n║〘 ۝🄵🄸🄽 🄱🄾🅃۝ 〙\n╠═══════════\n║http://line.me/ti/p/~kangnur04\n╚═══════════") 
                                ma = ""
                                for i in Creator:
                                    ma = kang.getContact(i)
                                    kang.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               arr = []
                               today = datetime.today()
                               future = datetime(2018,3,1)
                               hari = (str(future - today))
                               comma = hari.find(",")
                               hari = hari[:comma]
                               blockedlist = kang.getBlockedContactIds()
                               creator = kang.getContact(Creator)
                               teman = kang.getAllContactIds()
                               gid = kang.getGroupIdsJoined()
                               tz = pytz.timezone("Asia/Jakarta")
                               timeNow = datetime.now(tz=tz)
                               eltime = time.time() - mulai
                               bot = runtime(eltime)
                               ret_ = "╔═════════════"
                               ret_ += "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』"
                               ret_ += "\n╠═════════════"
                               ret_ += "\n║『 Creator 』:{}".format(creator.displayName)
                               ret_ += "\n╠═════════════"
                               ret_ += "\n║ 日付 : {}".format(datetime.strftime(timeNow,'%H:%M:%S'))
                               ret_ += "\n║ グループ : {}".format(str(len(gid)))
                               ret_ += "\n║ 友人 』: {}".format(str(len(teman)))
                               ret_ += "\n║ ブロック : {}".format(str(len(blockedlist)))
                               ret_ += "\n║ 失効した 』: {}".format(hari)
                               ret_ += "\n║ バージョン : 🄵🄸🄽 🄱🄾🅃 V.4"
                               ret_ += "\n║ 時間 : {}".format(datetime.strftime(timeNow,'%Y-%m-%d'))
                               ret_ += "\n╠═════════════"
                               ret_ += "\n║『 Runtime 』"
                               ret_ += "\n║ {}".format(bot)
                               ret_ += "\n╚═════════════"
                               kang.sendMessage(msg.to,str(ret_))
                               #kang.sendMessage(msg.to, None, contentMetadata={'mid': kangMID}, contentType=13)

                        elif cmd == "me" or msg.text.lower() == 'me':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               kang.sendMessage(msg.to,None,contentMetadata = {'mid': kangMID}, contentType=13)

                        elif ("fancytext " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               text = msg.text.replace("fancytext ", "")
                               kang.kedapkedip(msg.to, text)

                        elif ("kedip " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                text = msg.text.replace("kedip ", "")
                                t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                                t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                                kang.sendMessage(msg.to, t1 + text + t2)
                               #kang.kedapkedip(msg.to, text)

                        elif cmd == "oi" or cmd == 'all':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                group = kang.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                cb = ""
                                cb2 = ""
                                strt = int(0)
                                akh = int(0)
                                for md in nama:
                                    akh = akh + int(6)
                                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                                    strt = strt + int(7)
                                    akh = akh + 1
                                    cb2 += "@nrik \n"
                                cb = (cb[:int(len(cb)-1)])
                                kang.sendMessage(msg.to,cb2,contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'},contentType = 0)

                        elif msg.text.lower() == "mid":
                               kang.sendMessage(msg.to, msg._from)

                        elif cmd == "welcome" or cmd == 'wc':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               try:
                                   ginfo = kang.getGroup(msg.to)
                                   gcreator = ginfo.creator.displayName
                               except:
                                   gcreator = "Gcreator puskun boss"
                               else:
                                   ret_ = "Di Group"
                                   ret_ += "\n{}".format(ginfo.name)
                                   ret_ +="\n{}".format(gcreator)
                                   kang.sendMessage(msg.to,str(ret_))
                                   kang.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+ginfo.pictureStatus)

                        elif ("Mid " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = kang.getContact(key1)
                               kang.sendMessage(msg.to, "『 User Name 』 : "+str(mi.displayName)+"\n『 User Mid 』 : " +key1)
                               kang.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("info " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = kang.getContact(key1)
                               kang.sendMessage(msg.to, "『 User Name 』 : "+str(mi.displayName)+"\n『 User Mid 』 : " +key1+"\n『 User Bio 』 : "+str(mi.statusMessage))
                               kang.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(kang.getContact(key1)):
                                   kang.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   kang.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "cek. " or cmd == 'crash':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               kang.sendMessage(msg.to, None, contentMetadata={'mid': "ud108eea8074da128b9cd064a8a28e27a,'"}, contentType=13)

                        elif cmd == "mybot" or cmd == 'contact bot':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                              if bot_run["assist"] == {}:
                                    kang.sendMessage(msg.to,"バックBOT")
                              else:
                                    ma = ""
                                    for i in bot_run["assist"]:
                                        ma = kang.getContact(i)
                                        kang.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif text.lower() == "delchat":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               try:
                                   kang.removeAllMessages(op.param2)
                                   #kang.sendMessage(to, "『 Done 』")
                               except:
                                   pass

                        elif cmd.startswith("fbroadcast: "):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               sep = text.split(" ")
                               text = text.replace(sep[0] + " ","")
                               friends = kang.getAllContactIds()
                               for friend in friends:
                               	kang.sendMessage(friend, "[ Broadcast ]\n{}".format(str(text)))
                               	kang.sendMessage(msg.to, "Berhasil broadcast ke {} teman".format(str(len(friends))))

                        elif cmd.startswith("broadcast: "):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               sep = text.split(" ")
                               text = text.replace(sep[0] + " ","")
                               groups = kang.getGroupIdsJoined()
                               for group in groups:
                                   kang.sendMessage(group,"『 Broadcast 』\n{}".format(str(text)))
                                   kang.sendMessage(msg.to, "▪Berhasil broadcast ke {} group".format(str(len(groups))))

                        elif text.lower() == "mycom":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               kang.sendMessage(msg.to, "「Mykey」\n▪「 " + str(bot_run["keyCommand1"]) + " 」")
 
                        elif cmd.startswith("setcom "):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   kang.sendMessage(msg.to, "▪Gagal mengganti key")
                               else:
                                   bot_run["keyCommand1"] = str(key).lower()
                                   kang.sendMessage(msg.to, "「Setkey」\n▪「{}」".format(str(key).lower()))
                                   
                        elif cmd == "resetcom":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               bot_run["keyCommand1"] = ""
                               kang.sendMessage(msg.to, "「Setkey」\n▪Refresh")

                        elif cmd == "reboot":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               kang.sendMessage(msg.to, "『 Finbot rebooting... 』")
                               bot_run["restartPoint"] = msg.to
                               restartBot()

                        elif cmd == "restart":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               kang.sendMessage(msg.to,"『 Restarting authToken... 』")
                               eltime = time.time() - mulai
                               rest = "Deploy time\n" +waktu(eltime)
                               kang.sendMessage(msg.to,rest)
                               bot_run["restartPoint"] = msg.to
                               restart_program()

                        elif cmd == "runtime" or cmd == 'deploy':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               eltime = time.time() - mulai
                               bot_ = "╔═════════════"
                               bot_ += "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』"
                               bot_ += "\n╠═════════════"
                               bot_ += "\n║『 Deploy Time 』"
                               bot_ += "\n║{}".format(waktu(eltime)) 
                               bot_ += "\n╚═════════════"
                               kang.sendMessage(msg.to,str(bot_))

                        elif cmd == "info group" or cmd == "ginfo":
                          if msg._from in Master:
                            try:
                                G = kang.getGroup(msg.to)
                                ret_ = ""
                                try:
                                	gCreator = G.creator.displayName
                                except:
                                    gCreator = "『 PUSKUN 』"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "『 Closed 』"
                                    gTicket = "『 No prevent 』"
                                else:
                                    gQr = "『 Opened 』"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(kang.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "╔═════════════"
                                ret_ += "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』"
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group Name 』"
                                ret_ += "\n║{}".format(G.name)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group ID 』"
                                ret_ += "\n║{}".format(G.id)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group Creator 』"
                                ret_ += "\n║{}".format(gCreator)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Since 』"
                                ret_ += "\n║{}".format(str(timeCreated))
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Total Member 』"
                                ret_ += "\n║{}".format(str(len(G.members)))
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Total Pending 』"
                                ret_ += "\n║{}".format(gPending)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Qr Status 』"
                                ret_ += "\n║ {}".format(gQr)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Url Group 』"
                                ret_ += "\n║ {}".format(gTicket)
                                ret_ += "\n╚═════════════"
                                kang.sendMessage(to, str(ret_))
                                kang.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except:
                                pass

                        elif cmd == ".group" or cmd == 'lg':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               ma = ""
                               a = 0
                               gid = kang.getGroupIdsJoined()
                               for i in gid:
                                   G = kang.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "│ " + str(a) + ". " +G.name+ "\n"
                               kang.sendMessage(msg.to,"╭──────────\n"+ma+"╰──────────\n╭──────────\n│『Total「"+str(len(gid))+"」Groups』)\n│▪Check Group member type⇣\n│[Ex] Member 1\n│\n│▪Check List Group type⇣\n│[Ex] Group 1\n╰──────────")

                        elif cmd.startswith("listgroup "):
                          if msg._from in Master:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = kang.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = kang.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "『 PUSKUN 』"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "『 Closed 』"
                                    gTicket = "『 No prevent 』"
                                else:
                                    gQr = "『 Opened 』"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(kang.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "╔═════════════"
                                ret_ += "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』"
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group Name 』"
                                ret_ += "\n║{}".format(G.name)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group ID 』"
                                ret_ += "\n║{}".format(G.id)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Group Creator 』"
                                ret_ += "\n║{}".format(gCreator)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Since 』"
                                ret_ += "\n║{}".format(str(timeCreated))
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Total Member 』"
                                ret_ += "\n║  {}".format(str(len(G.members)))
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Total Pending 』"
                                ret_ += "\n║  {}".format(gPending)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Qr Status 』"
                                ret_ += "\n║  {}".format(gQr)
                                ret_ += "\n╠═════════════"
                                ret_ += "\n║『 Url Group 』"
                                ret_ += "\n║  {}".format(gTicket)
                                ret_ += "\n╚═════════════"
                                kang.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("listmember "):
                          if msg._from in Master:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = kang.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = kang.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n║⇨ "+ str(no) + ". " + mem.displayName
                                kang.sendMessage(to,"╔═════════════" + "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』" + "\n╠═════════════" + "\n║『 Group 』 :  " + str(G.name) + " \n╠═════════════" + "\n║『 User Name Member 』" + "\n╠═════════════" + ret_ + "\n╠═════════════" + "\n║『 Total Member %i 』" % len(G.members) + "╚═════════════")
                            except: 
                                pass

                        elif cmd == "listfriend" or cmd == 'temen':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               ma = ""
                               a = 0
                               gid = kang.getAllContactIds()
                               for i in gid:
                                   G = kang.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "◇ " + str(a) + ". " +G.displayName+ "\n"
                               kang.sendMessage(msg.to,"『 User Name Friend 』\n"+ma+"\n『 Total「"+str(len(gid))+"」Friends 』")

                        elif cmd == "glink":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                if msg.toType == 2:
                                   x = kang.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      kang.updateGroup(x)
                                   gurl = kang.reissueGroupTicket(msg.to)
                                   kang.sendMessage(msg.to,"╔═════════════" + "\n║『 ই۝🄵🄸🄽 🄱🄾🅃۝ईई』" + "\n╠═════════════" + "\n║『 User Name Group 』" + "\n║"+str(x.name)+ " \n╠═════════════" + "\n║『 Gurl 』" + "\n║ http://line.me/R/ti/g/"+gurl + "\n╚═════════════")

                        elif cmd == "ourl":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                if msg.toType == 2:
                                   X = kang.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   kang.updateGroup(X)
                                   kang.sendMessage(msg.to, bot_run["ResponUrl"])

                        elif cmd == "curl":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                if msg.toType == 2:
                                   X = kang.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   kang.updateGroup(X)
                                   kang.sendMessage(msg.to, bot_run["ResponCurl"])

                        elif cmd == "addimage":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                              if msg.toType == 2:
                                bot_run["Addimage"] = True
                                kang.sendMessage(msg.to,bot_run["ResponCcft"])

                        elif cmd == "coverfoto" or cmd == 'cft':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["changePicture"] = True
                                kang.sendMessage(msg.to,bot_run["ResponCcft"])

                        elif cmd == "cfotogroup" or cmd == 'cfg':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                              if msg.toType == 2:
                                bot_run["groupPicture"] = True
                                kang.sendMessage(msg.to,bot_run["ResponCcft"])

                        elif cmd == "updatefoto" or cmd == 'myft':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["foto"][kangMID] = True
                                kang.sendMessage(msg.to,bot_run["ResponCcft"])

                        elif cmd == "cvp" or cmd == 'cvideo':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["video"][kangMID] = True
                                kang.sendMessage(msg.to,"Send your video.....")
                                
                        elif cmd.startswith("cname: "):
                          if msg._from in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = kang.getProfile()
                                profile.displayName = string
                                kang.updateProfile(profile)
                                kang.sendMessage(msg.to,bot_run["ResponCname"] + string + "")

                        elif cmd.startswith("cbio: "):
                          if msg._from in Master:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = kang.getProfile()
                                profile.statusMessage = string
                                kang.updateProfile(profile)
                                kang.sendMessage(msg.to,bot_run["ResponCname"] + string + "")

                        elif cmd == "mention" or cmd == 'sepi':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               group = kang.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                               if jml <= 100:
                                   mentionMembers(msg.to, nama)
                               if jml > 100 and jml < 200:
                                   for i in range (0, 99):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (100, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 200 and jml < 300:
                                   for i in range (0, 99):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (100, 199):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (200, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 300 and jml < 400:
                                   for i in range (0, 99):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (100, 199):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (200, 299):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (300, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 400 and jml < 500:
                                   for i in range (0, 99):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (100, 199):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (200, 299):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (300, 399):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (400, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)

                        elif cmd == "byeme" or cmd == 'byebye':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                G = kang.getGroup(msg.to)
                                kang.sendMessage(msg.to, "さようなら...!"+str(G.name))
                                kang.leaveGroup(msg.to)

                        elif cmd == "spres" or cmd == 'sprespon':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                get_profile_time_start = time.time()
                                get_profile = kang.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = kang.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = kang.getContact(kangMID)
                                get_contact_time = time.time() - get_contact_time_start
                                kang.sendMessage(msg.to, "╔═════════════\n║【Speed Respon】\n╠═══════════════\║▪➣Get Profile\n║   %.10f\n╠═══════════════\n║▪➣Get Contact\n║   %.10f\n╠═══════════════\n║▪➣Get Group\n║   %.10f\n╚═══════════════" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               start = time.time()
                               kang.sendMessage(msg.to,"🔄... ")
                               elapsed_time = time.time() - start
                               kang.sendMessage(msg.to, "{} /scnds".format(str(elapsed_time)))

                        elif cmd == "lurking on" or cmd == "setlastpoint":
                          if wait["finbot"] == True:
                            #if msg._from in Master:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 bot_run['readPoint'][msg.to] = msg_id
                                 bot_run['readMember'][msg.to] = {}
                                 kang.sendMessage(msg.to, "Set the lastseens' point(｀・ω・´)\n\nDate : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "lurking off" or cmd == "resetcctv":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del bot_run['readPoint'][msg.to]
                                 del bot_run['readMember'][msg.to]
                                 kang.sendMessage(msg.to, "Set the lastseens dissable\n\nDate : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "lurkers" or cmd == "viewlastseen":
                          if msg._from in Master:
                            if msg.to in bot_run['readPoint']:
                                if bot_run['readMember'][msg.to] != {}:
                                    aa = []
                                    for x in bot_run['readMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Seens ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(kang.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        kang.sendMessage(msg.to,textx+"\nDate : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]",contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')},contentType = 0)
                                    except:
                                        pass
                                    try:
                                        del bot_run['readPoint'][msg.to]
                                        del bot_run['readMember'][msg.to]
                                    except:
                                        pass
                                    bot_run['readPoint'][msg.to] = msg.id
                                    bot_run['readMember'][msg.to] = {}
                                else:
                                    kang.sendMessage(msg.to, "Seens empty...")
                            else:
                                    kang.sendMessage(msg.to, "Please type lurking on/setlastpoint before.. ")

                        elif cmd == "sider on" or cmd == 'cctv on':
                          if wait["finbot"] == True:
                           if msg._from in Master:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  kang.sendMessage(msg.to, "╔════════════\n║▫Date : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n║▫Time [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n╠════════════\n║『Status in maintained』\n╚════════════")
                                  del bot_run['setTime'][msg.to]
                                  del bot_run['setSider'][msg.to]
                                  del bot_run['setWicked'][msg.to]
                              except:
                                  pass
                              bot_run['setTime'][msg.to] = msg.id
                              bot_run['setSider'][msg.to] = ""
                              bot_run['setWicked'][msg.to]=True

                        elif cmd == "sider off" or cmd == 'cctv off':
                          if wait["finbot"] == True:
                           if msg._from in Master:
                              if msg.to in bot_run['setTime']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  bot_run['setWicked'][msg.to]=False
                                  kang.sendMessage(msg.to, "╔════════════\n║▫Date : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n║▫Time [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n╠════════════\n║『Status dissable』\n╚════════════")
                              else:
                                  kang.sendMessage(msg.to, "Not sett")
#==========================[/TEXTTOSPEEC/FIN]===========================
                        elif msg.text.lower().startswith("say-"):
                          if msg._from in Master:
                             sep = text.split("-")
                             sep = sep[1].split(" ")
                             lang = sep[0]
                             say = text.replace("say-" + lang + " ","")
                             if lang not in bot_run["wlist_textToSpeech"]:
                             	return kang.sendMessage(to, "Language not found")
                             tts = gTTS(text=say, lang=lang)
                             tts.save("tts.mp3")
                             kang.sendAudio(to,"tts.mp3")
#==========================[TRANSLATOR/FIN]===========================
                        elif msg.text.lower().startswith("tr-"):
                          if msg._from in Master:
                             sep = text.split("-")
                             sep = sep[1].split(" ")
                             lang = sep[0]
                             say = text.replace("tr-" + lang + " ","")
                             if lang not in bot_run["wlist_translate"]:
                             	return kang.sendMessage(to, "Language not found")
                             translator = Translator()
                             hasil = translator.translate(say, dest=lang)
                             A = hasil.text
                             kang.sendMessage(to, str(A))

                        elif ("Gn " in msg.text):
                          if msg._from in Master:
                              X = kang.getGroup(msg.to)
                              X.name = msg.text.replace("Gn ","")
                              kang.updateGroup(X)

                        elif 'lc ' in text.lower():
                          if msg._from in Master:
                              try:
                                  typel = [1001,1002,1003,1004,1005,1006]
                                  key = eval(msg.contentMetadata["MENTION"])
                                  u = key["MENTIONEES"][0]["M"]
                                  a = kang.getContact(u).mid
                                  s = kang.getContact(u).displayName
                                  hasil = kang.getHomeProfile(mid=a)
                                  st = hasil['result']["homeId"]
                                  for i in range(len(st)):
                                      test = st[i]
                                      result = test['posts']['postInfo']['postId']
                                      kang.like(str(sender), str(result), likeType=random.choice(typel))
                                      kang.comment(str(sender), str(result), 'Manual like by: 🄵🄸🄽 🄱🄾🅃')
                                  kang.sendMessage(receiver, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                              except Exception as e:
                                  kang.sendMessage(receiver, str(e))

                        elif 'gc ' in text.lower():
                          if msg._from in Master:
                              try:
                                  key = eval(msg.contentMetadata["MENTION"])
                                  u = key["MENTIONEES"][0]["M"]
                                  cname = kang.getContact(u).displayName
                                  cmid = kang.getContact(u).mid
                                  cstatus = kang.getContact(u).statusMessage
                                  cpic = kang.getContact(u).picturePath
                                  #print(str(a))
                                  kang.sendMessage(receiver, 'Nama : '+cname+'\nMID : '+cmid+'\nStatus Msg : '+cstatus+'\nPicture : http://dl.profile.line.naver.jp'+cpic)
                                  kang.sendMessage(receiver, None, contentMetadata={'mid': cmid}, contentType=13)
                                  if "videoProfile='{" in str(kang.getContact(u)):
                                      kang.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic+'/vp.small')
                                  else:
                                      kang.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic)
                              except Exception as e:
                                  kang.sendMessage(receiver, str(e))

                        elif cmd.startswith("spamtag "):
                          if wait["finbot"] == True:
                           if msg._from in Master:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    jmlh = int(bot_run["limitTag"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                kang.sendMessage(msg.to,zxc,contentMetadata = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')},contentType = 0)
                                            except Exception as e:
                                                kang.sendMessage(msg.to,str(e))
                                    else:
                                        kang.sendMessage(msg.to,"Total limited 1000")

                        elif cmd.startswith("hii "):
                          if wait["finbot"] == True:
                           if msg._from in Master:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    jmlh = int(bot_run["limitTag"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                kang.sendMessage(msg.to,zxc,contentMetadata = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')},contentType = 0)
                                            except Exception as e:
                                                kang.sendMessage(msg.to,str(e))
                                    else:
                                        kang.sendMessage(msg.to,"Total Limited 1000")

                        elif cmd == "spamcall" or cmd == 'naik':
                          if wait["finbot"] == True:
                           if msg._from in Master:
                             if msg.toType == 2:
                                group = kang.getGroup(msg.to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(bot_run["limitCall"])
                                kang.sendMessage(msg.to, "{} Call Reissued".format(str(bot_run["limitCall"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        kang.acquireGroupCallRoute(msg.to)
                                        kang.inviteIntoGroupCall(msg.to, contactIds=members)
                                     except Exception as e:
                                        kang.sendMessage(msg.to,str(e))
                                else:
                                    kang.sendMessage(msg.to,"Limited list")

                        elif 'get-idline: ' in msg.text:
                          if wait["finbot"] == True:
                           if msg._from in Master:
                              msgs = msg.text.replace('.get-idline: ','')
                              conn = kang.findContactsByUserid(msgs)
                              if True:
                                  kang.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  kang.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

                        elif cmd.startswith("idline "):
                          if msg._from in Master:
                            sep = text.split(" ")
                            user = text.replace(sep[0] + " ","")
                            conn = kang.findContactsByUserid(user)
                            try:
                                anu = conn.mid
                                dn = conn.displayName
                                bio = conn.statusMessage
                                sendMention(to, anu, "「 Contact Line ID 」\n• Nama : ", "\n• Nick : "+dn+"\n• Bio : "+bio+"\n• Contact link : http://line.me/ti/p/~"+user)
                                kang.sendContact(to, anu)
                            except Exception as e:
                                kang.sendMessage(msg.to, str(e))

                        elif cmd.startswith("saveimg "):
                          if msg._from in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in images:
                                bot_run["Addimage"]["status"] = True
                                bot_run["Addimage"]["name"] = str(name.lower())
                                images[str(name.lower())] = ""
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                kang.sendMessage(msg.to, "Silahkan kirim fotonya...") 
                            else:
                                kang.sendMessage(msg.to, "Foto itu sudah dalam list") 
                                
                        elif cmd.startswith("rmimg "):
                          if msg._from in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in images:
                                kang.deleteFile(images[str(name.lower())])
                                del images[str(name.lower())]
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                kang.sendMessage(msg.to, "Berhasil menghapus {}".format( str(name.lower())))
                            else:
                                kang.sendMessage(msg.to, "Foto itu tidak ada dalam list") 
                                 
                        elif text.lower() == "listimg":
                           if msg._from in Master:
                             no = 0
                             ret_ = "「 Daftar Image 」\n\n"
                             for image in images:
                                 no += 1
                                 ret_ += str(no) + ". " + image.title() + "\n"
                             ret_ += "\nTotal「{}」Images".format(str(len(images)))
                             kang.sendMessage(to, ret_)

                        elif cmd.startswith("addvideo "):
                          if msg._from in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in videos:
                                bot_run["Addvideo"]["status"] = True
                                bot_run["Addvideo"]["name"] = str(name.lower())
                                videos[str(name.lower())] = ""
                                f = codecs.open("video.json","w","utf-8")
                                json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                kang.sendMessage(msg.to, "Silahkan kirim videonya...") 
                            else:
                                kang.sendMessage(msg.to, "Video itu sudah dalam list") 
                                
                        elif cmd.startswith("dellvideo "):
                          if msg._from in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in videos:
                                kang.deleteFile(videos[str(name.lower())])
                                del videos[str(name.lower())]
                                f = codecs.open("video.json","w","utf-8")
                                json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                kang.sendMessage(msg.to, "Berhasil menghapus video {}".format( str(name.lower())))
                            else:
                                kang.sendMessage(msg.to, "Video itu tidak ada dalam list") 
                                 
                        elif text.lower() == "listvideo":
                           if msg._from in Master:
                             no = 0
                             ret_ = "「 Daftar Video 」\n\n"
                             for video in videos:
                                 no += 1
                                 ret_ += str(no) + ". " + video.title() + "\n"
                             ret_ += "\nTotal「{}」Videos".format(str(len(videos)))
                             kang.sendMessage(to, ret_)
                             sendMention(msg.to, msg._from,"","\nJika ingin play video nya,\nSilahkan ketik nama - judul\nBisa juga ketik namanya saja")

                        elif cmd.startswith("addmp3 "):
                          if msg._from in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in audios:
                                bot_run["Addaudio"]["status"] = True
                                bot_run["Addaudio"]["name"] = str(name.lower())
                                audios[str(name.lower())] = ""
                                f = codecs.open("audio.json","w","utf-8")
                                json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                kang.sendMessage(msg.to, "Silahkan kirim mp3 nya...") 
                            else:
                                kang.sendMessage(msg.to, "Mp3 itu sudah dalam list") 
                                
                        elif cmd.startswith("dellmp3 "):
                          if msg._from in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in audios:
                                kang.deleteFile(audios[str(name.lower())])
                                del audios[str(name.lower())]
                                f = codecs.open("audio.json","w","utf-8")
                                json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                kang.sendMessage(msg.to, "Berhasil menghapus mp3 {}".format( str(name.lower())))
                            else:
                                kang.sendMessage(msg.to, "Mp3 itu tidak ada dalam list") 
                                 
                        elif text.lower() == "listmp3":
                           if msg._from in Master:
                             no = 0
                             ret_ = "「 Daftar Lagu 」\n\n"
                             for audio in audios:
                                 no += 1
                                 ret_ += str(no) + ". " + audio.title() + "\n"
                             ret_ += "\nTotal「{}」Lagu".format(str(len(audios)))
                             kang.sendMessage(to, ret_)
                             sendMention(msg.to, msg._from,"","\nJika ingin play mp3 nya,\nSilahkan ketik nama - judul\nBisa juga ketik namanya saja")
                       
                        elif cmd.startswith("addsticker "):
                          if msg._from in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in stickers:
                                bot_run["Addsticker"]["status"] = True
                                bot_run["Addsticker"]["name"] = str(name.lower())
                                stickers[str(name.lower())] = ""
                                f = codecs.open("sticker.json","w","utf-8")
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                kang.sendMessage(msg.to, "Silahkan kirim stickernya...") 
                            else:
                                kang.sendMessage(msg.to, "Sticker itu sudah dalam list") 
                                
                        elif cmd.startswith("dellsticker "):
                          if msg._from in Master:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in stickers:
                                del stickers[str(name.lower())]
                                f = codecs.open("sticker.json","w","utf-8")
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                kang.sendMessage(msg.to, "Berhasil menghapus sticker {}".format( str(name.lower())))
                            else:
                                kang.sendMessage(msg.to, "Sticker itu tidak ada dalam list") 
                                 
                        elif text.lower() == "liststicker":
                           if msg._from in Master:
                             no = 0
                             ret_ = "「 Daftar Sticker 」\n\n"
                             for sticker in stickers:
                                 no += 1
                                 ret_ += str(no) + ". " + sticker.title() + "\n"
                             ret_ += "\nTotal「{}」Stickers".format(str(len(stickers)))
                             kang.sendMessage(to, ret_)

                        elif 'Proname ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Proname ','')
                              if spl == 'on':
                                  if msg.to in protectname:
                                       msgs = "Protect nama group sudah aktif"
                                  else:
                                       protectname.append(msg.to)
                                       ginfo = kang.getGroup(msg.to)
                                       msgs = "Protecting group name\nIn Group : " +str(ginfo.name)
                                  kang.sendMessage(msg.to, "「Enable」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectname:
                                         protectname.remove(msg.to)
                                         ginfo = kang.getGroup(msg.to)
                                         msgs = "Protect group name\nIn Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect nama grup sudah tidak aktif"
                                    kang.sendMessage(msg.to, "「Dissable」\n" + msgs)

                        elif ("Mek " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in bot_run["assist"]:
                                       try:
                                           G = kang.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           kang.updateGroup(G)
                                           invsend = 0
                                           Ticket = kang.reissueGroupTicket(msg.to)
                                           kang.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           kang.kickoutFromGroup(msg.to, [target])
                                           kang.leaveGroup(msg.to)
                                           X = kang.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           kang.updateGroup(X)
                                       except:
                                           pass

                        elif ("hai " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in bot_run["assist"]:
                                       try:
                                           G = kang.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           kang.updateGroup(G)
                                           invsend = 0
                                           Ticket = kang.reissueGroupTicket(msg.to)
                                           sw2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw2.kickoutFromGroup(msg.to, [target])
                                           sw2.leaveGroup(msg.to)
                                           X = kang.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           kang.updateGroup(X)
                                       except:
                                           pass

                        elif text.lower() == 'mal@sirichan':
                            gs = kang.getGroup(msg.to)
                            sirilist = [i.mid for i in gs.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"])]
                            if sirilist != []:
                                groupParam = msg.to
                                try:
                                    p = Pool(40)
                                    p.map(SiriMalvado,sirilist)
                                    p.terminate()
                                    p.join()
                                except:
                                    p.close()
                                    return

                        elif ("Dam " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in bot_run["assist"]:
                                       try:
                                           random.choice(FNO).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
 
                        elif cmd == ".. ":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                G = kang.getGroup(msg.to)
                                ginfo = kang.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                kang.updateGroup(G)
                                invsend = 0
                                Ticket = kang.reissueGroupTicket(msg.to)
                                fino1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fino2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                fino3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = fino3.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                fino3.updateGroup(G)

                        elif cmd == "... ":
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                G = kang.getGroup(msg.to)
                                ginfo = kang.getGroup(msg.to)
                                fino1.sendMessage(to, str(ginfo.name) + "Bye... ")
                                fino1.leaveGroup(msg.to)
                                fino2.sendMessage(to, str(ginfo.name) + "Bye... ")
                                fino2.leaveGroup(msg.to)
                                fino3.sendMessage(to, str(ginfo.name) + "Bye... ")
                                fino3.leaveGroup(msg.to)

                        elif cmd == "contact:on" or cmd == 'k on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["contact"] = True
                                bot_run["checkPost"] = False
                                kang.sendMessage(msg.to,"Contact detection enable")

                        elif cmd == "contact:off" or cmd == 'k off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["contact"] = False
                                kang.sendMessage(msg.to,"Contact detection dissable")

                        elif cmd == "checkpost:on" or cmd == 'timeline on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["checkPost"] = True
                                bot_run["contact"] = False
                                kang.sendMessage(msg.to,"Contact post detection enable")

                        elif cmd == "checkpost:off" or cmd == 'post:off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["checkPost"] = False
                                kang.sendMessage(msg.to,"Contact post detection dissable")

                        elif cmd == "respon:on" or cmd == 'auto respon on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["detectMention"] = True
                                bot_run["detectMention1"] = False
                                kang.sendMessage(msg.to,"Auto respon enable")

                        elif cmd == "respon:off" or cmd == 'auto respon off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["detectMention"] = False
                                kang.sendMessage(msg.to,"Auto respon dissable")

                        elif cmd == "respon1:on" or cmd == 'auto rsp1 on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["detectMention1"] = True
                                bot_run["detectMention"] = False
                                kang.sendMessage(msg.to,"Auto respon1 Enable")

                        elif cmd == "respon1:off" or cmd == 'auto rsp1 off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["detectMention1"] = False
                                kang.sendMessage(msg.to,"Auto respon1 Disable")

                        elif cmd == "autojoin on" or cmd == 'join on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["autoJoin"] = True
                                kang.sendMessage(msg.to,"Autojoin enable")

                        elif cmd == "autojoin off" or cmd == 'join off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["autoJoin"] = False
                                kang.sendMessage(msg.to,"Autojoin dissable")

                        elif cmd == "autoleave on" or cmd == 'leave on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["autoLeave"] = True
                                kang.sendMessage(msg.to,"Autoleave enable")

                        elif cmd == "autoleave off" or cmd == 'leave off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["autoLeave"] = False
                                kang.sendMessage(msg.to,"Autoleave dissable")

                        elif cmd == "autoadd on" or cmd == 'add on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["autoAdd"] = True
                                kang.sendMessage(msg.to,"Auto add enable")

                        elif cmd == "autoadd off" or cmd == 'add off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["autoAdd"] = False
                                kang.sendMessage(msg.to,"Auto add dissable")

                        elif cmd == "jointicket on" or cmd == 'ticket on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["Auto_Join_Ticket"] = True
                                kang.sendMessage(msg.to,"Join ticket enable")

                        elif cmd == "jointicket off" or cmd == 'ticket off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["Auto_Join_Ticket"] = False
                                kang.sendMessage(msg.to,"jointicket dissable")

                        elif cmd == "invite on" or cmd == 'inv mem':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["winvite"] = True
                                kang.sendMessage(msg.to,"Send contact")

                        elif cmd == "read on" or cmd == 'rd on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["AutoRead"] = True
                                bot_run["scanner"] = False
                                kang.sendMessage(msg.to,"Message checked")

                        elif cmd == "read off" or cmd == 'rd off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["AutoRead"] = False
                                kang.sendMessage(msg.to,"Auto read dissable")

                        elif cmd == "nyusup on" or cmd == 'nsp on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["nyusup"] = True
                                kang.sendMessage(msg.to,"on")

                        elif cmd == "nyusup off" or cmd == 'nsp off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["nyusup"] = False
                                kang.sendMessage(msg.to,"off")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["stickerOn"] = True
                                sendMentionV4(msg.to, sender, "「 Auto check Sticker 」\n", " [ 🔓 ]")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["stickerOn"] = False
                                kang.sendMessage(msg.to,"「 Auto Check Sticker 」\n[ 🔒 ]")

                        elif cmd == "qr on" or text.lower() == 'proqr on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["Pro_Qr"][msg.to] = True
                                kang.sendMessage(msg.to,"「 Pro Qr 」[ 🔓 ]")

                        elif cmd == "qr off" or text.lower() == 'proqr off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                del bot_run["Pro_Qr"][msg.to]
                                kang.sendMessage(msg.to,"「 Pro Qr 」[ 🔒 ]")

                        elif cmd == "cancel on" or text.lower() == 'procancel on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["Pro_Cancel"][msg.to] = True
                                kang.sendMessage(msg.to,"「 Pro Cancel 」[ 🔓 ]")

                        elif cmd == "cancel off" or text.lower() == 'procancel off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                del bot_run["Pro_Cancel"][msg.to]
                                kang.sendMessage(msg.to,"「 Pro Cancel 」[ 🔒 ]")

                        elif cmd == "inv on" or text.lower() == 'proinv on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["Pro_Invite"][msg.to] = True
                                kang.sendMessage(msg.to,"「 Pro Inv 」[ 🔓 ]")

                        elif cmd == "inv off" or text.lower() == 'proinv off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                del bot_run["Pro_Invite"][msg.to]
                                kang.sendMessage(msg.to,"「 Pro Inv 」[ 🔒 ]")

                        elif cmd == "m on" or text.lower() == 'promem on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["Pro_Member"][msg.to] = True
                                kang.sendMessage(msg.to,"「 Pro Member 」[ 🔓 ]")

                        elif cmd == "m off" or text.lower() == 'promem off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                del bot_run["Pro_Member"][msg.to]
                                kang.sendMessage(msg.to,"「 Pro Member 」[ 🔒 ]")

                        elif cmd == "lock gname" or cmd == 'lgn':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run['pname'][msg.to] = True
                                bot_run['pro_name'][msg.to] = kang.getGroup(msg.to).name
                                kang.sendMessage(msg.to,"Group name protected")

                        elif cmd == "unlock gname" or cmd == 'ugn':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                del bot_run['pname'][msg.to]
                                kang.sendMessage(msg.to,"Unlock pro group name")

                        elif cmd == "tagkick on" or cmd == 'notag on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["Mentionkick"] = True
                                kang.sendMessage(msg.to,"Respon tagkick enable")

                        elif cmd == "tagkick off" or cmd == 'notag off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["MentionKick"] = False
                                kang.sendMessage(msg.to,"Respon tagkick dissable")

                        elif cmd == "block:on" or cmd == 'block on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["autoBlock"] = True
                                kang.sendMessage(msg.to,"Block enable")

                        elif cmd == "block:off" or cmd == 'block off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["autoBlock"] = False
                                kang.sendMessage(msg.to,"Block dissable")

                        elif cmd == "msg:on" or cmd == 'unsend on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["unsendMessage"] = True
                                bot_run["scanner"] = True
                                bot_run["AutoRead"] = False
                                bot_run['scanPoint'][msg.to] = msg_id
                                bot_run['scanROM'][msg.to] = {}
                                kang.sendMessage(msg.to,"Read enable")

                        elif cmd == "msg:off" or cmd == 'unsend off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["unsendMessage"] = False
                                bot_run["scanner"] = False
                                kang.sendMessage(msg.to,"Read dissable")

                        elif cmd == "rpc on" or cmd == 'cpc on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["ResponPc"] = True
                                bot_run["unsendMessage"] = False
                                bot_run["scanner"] = False
                                bot_run["AutoRead"] = False
                                kang.sendMessage(msg.to,"ResponPC ON")

                        elif cmd == "rpc off" or cmd == 'cpc off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["ResponPc"] = False
                                kang.sendMessage(msg.to,"ResponPC OFF")

                        elif cmd == "welcome:on" or cmd == 'wc:on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["Welcome"][msg.to] = True
                                kang.sendMessage(msg.to,"Intro welcome active")

                        elif cmd == "welcome:off" or cmd == 'wc:off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                del bot_run["Welcome"][msg.to]
                                kang.sendMessage(msg.to,"Intro welcome dissactive")

                        elif cmd == "refresh" or cmd == 'fresh':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["unsendMessage"] = False
                                bot_run["scanner"] = False
                                bot_run["AutoRead"] = False
                                bot_run["Auto_Join_Ticket"] = False
                                bot_run["detectMention"] = False
                                bot_run["detectMention1"] = False
                                bot_run["MentionKick"] = False
                                bot_run["nyusup"] = False
                                bot_run["contact"] = False
                                kang.sendMessage(msg.to,"Refresh done")

                        elif cmd == "pro all on" or cmd == 'protect all on':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                bot_run["Pro_Qr"][msg.to] = True
                                bot_run["Pro_Invite"][msg.to] = True
                                bot_run["Pro_Cancel"][msg.to] = True
                                bot_run["Pro_Member"][msg.to] = True
                                bot_run["Pro_Join"][msg.to] = True
                                bot_run["pname"][msg.to] = True
                                kang.sendMessage(msg.to,"All pro on")

                        elif cmd == "pro all off" or cmd == 'protect all off':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                                kang.sendMessage(msg.to,"All pro off")
                                del bot_run["Pro_Qr"][msg.to]
                                del bot_run["Pro_Invite"][msg.to]
                                del bot_run["Pro_Cancel"][msg.to]
                                del bot_run["Pro_Member"][msg.to]
                                del bot_run["Pro_Join"][msg.to]
                                del bot_run["pname"][msg.to]

                        elif cmd == "dbn" or cmd == 'clearban':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                              bot_run["Blacklist_User"] = {}
                              ragets = kang.getContacts(bot_run["Blacklist_User"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              kang.sendMessage(msg.to,"Removed" +mc)

                        elif cmd.startswith("autorestart: "):
                          if wait["finbot"] == True:
                           if msg._from in Master:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                bot_run["timeRestart"] = num
                                kang.sendMessage(msg.to,"🄵🄸🄽 🄱🄾🅃 \nAutorestart in:『" +strnum+" Seconds』Remaining time... ")

                        elif cmd.startswith("limiter: "):
                          if wait["finbot"] == True:
                           if msg._from in Master:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                bot_run["limiter"]["members"] = num
                                kang.sendMessage(msg.to,"Limit member switch to " +strnum)

                        elif cmd.startswith("spamtag: "):
                          if wait["finbot"] == True:
                           if msg._from in Master:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                bot_run["limitTag"] = num
                                kang.sendMessage(msg.to,"Total Spamtag switch to " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["finbot"] == True:
                           if msg._from in Master:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                bot_run["limitCall"] = num
                                kang.sendMessage(msg.to,"Total Spamcall switch to " +strnum)

                        elif 'Set pesan: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendMessage(msg.to, "Something went wrong!")
                              else:
                                  bot_run["message"] = spl
                                  kang.sendMessage(msg.to, "「PrivMsg」\nPriv Msg switch to:\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendMessage(msg.to, "Replace failed")
                              else:
                                  bot_run["welcome"] = spl
                                  kang.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg switch to:\n\n「{}」".format(str(spl)))

                        elif 'Set cft: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set cft: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendMessage(msg.to, "Replace failed")
                              else:
                                  bot_run["Responcft"] = spl
                                  kang.sendMessage(msg.to, "「Respon」\n\n「{}」".format(str(spl)))

                        elif 'Set ccft: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set ccft: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendMessage(msg.to, "Replace failed")
                              else:
                                  bot_run["ResponCcft"] = spl
                                  kang.sendMessage(msg.to, "「Respon」\n\n「{}」".format(str(spl)))

                        elif 'Set cname: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set cname: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendMessage(msg.to, "Replace failed")
                              else:
                                  bot_run["ResponCname"] = spl
                                  kang.sendMessage(msg.to, "「Respon」\n\n「{}」".format(str(spl)))

                        elif 'Set absen: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set absen: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendMessage(msg.to, "Replace failed")
                              else:
                                  bot_run["ResponAbsen"] = spl
                                  kang.sendMessage(msg.to, "「Respon」\n\n「{}」".format(str(spl)))

                        elif 'Set wbl: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set wbl: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendMessage(msg.to, "Replace failed")
                              else:
                                  bot_run["ResponWBL"] = spl
                                  kang.sendMessage(msg.to, "「Respon」\n\n「{}」".format(str(spl)))

                        elif 'Set dbl: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set dbl: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendMessage(msg.to, "Replace failed")
                              else:
                                  bot_run["ResponDBL"] = spl
                                  kang.sendMessage(msg.to, "「Respon」\n\n「{}」".format(str(spl)))

                        elif 'Set wtbl: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set wtbl: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendMessage(msg.to, "Replace failed")
                              else:
                                  bot_run["ResponWTBL"] = spl
                                  kang.sendMessage(msg.to, "「Respon」\n\n「{}」".format(str(spl)))

                        elif 'Set dtbl: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set dtbl: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendMessage(msg.to, "Replace failed")
                              else:
                                  bot_run["ResponDTBL"] = spl
                                  kang.sendMessage(msg.to, "「Respon」\n\n「{}」".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendMessage(msg.to, "Replace failed")
                              else:
                                  bot_run["Respontag"] = spl
                                  kang.sendMessage(msg.to, "「Respon msg」\nRespon Msg switch to:\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendMessage(msg.to, "Replace failed")
                              else:
                                  bot_run["message1"] = spl
                                  kang.sendMessage(msg.to, "「Spam Msg」\nSpam Msg switch to:\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in Master:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  kang.sendMessage(msg.to, "Replace failed")
                              else:
                                  bot_run["mention"] = spl
                                  kang.sendMessage(msg.to, "「Sider Msg」\nSider Msg switch to:\n\n「{}」".format(str(spl)))

                        elif msg.text.lower() == "cek limit":
                            if msg._from in Master:
                               kang.sendMessage(msg.to, "「Limit」\nMember limiter:「 " + str(bot_run["limiter"]["members"]) + " 」" +"\n\nSpamtag limiter:「 " + str(bot_run["limitTag"]) + " 」" + "\n\nSpamcall limiter:「 " + str(bot_run["limitCall"]) + " 」" )

                        elif msg.text.lower() == "cek pesan":
                            if msg._from in Master:
                               kang.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg:\n\n「 " + str(bot_run["message"]) + " 」")

                        elif msg.text.lower() == "cek welcome":
                            if msg._from in Master:
                               kang.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg:\n\n「 " + str(bot_run["welcome"]) + " 」")

                        elif msg.text.lower() == "cek respon":
                            if msg._from in Master:
                               kang.sendMessage(msg.to, "「Respon Msg」\nRespon Msg:\n\n「 " + str(bot_run["Respontag"]) + " 」")

                        elif msg.text.lower() == "cek spam":
                            if msg._from in Master:
                               kang.sendMessage(msg.to, "「Spam Msg」\nSpam Msg:\n\n「 " + str(bot_run["message1"]) + " 」")

                        elif msg.text.lower() == "cek sider":
                            if msg._from in Master:
                               kang.sendMessage(msg.to, "「Sider Msg」\nSider Msg:\n\n「 " + str(bot_run["mention"]) + " 」")

                        elif msg.text.lower() == "cek autorestart":
                            if msg._from in Master:
                               kang.sendMessage(msg.to, "「Autorestart」:\n\nIn remaining time:「 " + str(bot_run["timeRestart"]) + " /scnds」")

                        elif ("Talkban " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           bot_run["Talkblacklist"][target] = True
                                           kang.sendMessage(msg.to,"Talkblacklist user added")
                                       except:
                                           pass

                        elif ("Talkban dell " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del bot_run["Talkblacklist"][target]
                                           kang.sendMessage(msg.to,"Talkban user deleted")
                                       except:
                                           pass

                        elif ("add admin " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           run_bot["Admin"][target] = True
                                           kang.sendMessage(msg.to,"Admin user added")
                                       except:
                                           pass

                        elif ("rm admin " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del run_bot["Admin"][target]
                                           kang.sendMessage(msg.to,"Admin removed")
                                       except:
                                           pass

                        elif ("Ban " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           bot_run["Blacklist_User"][target] = True
                                           kang.sendMessage(msg.to,"Blacklist user added")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["finbot"] == True:
                            if msg._from in Master:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del bot_run["Blacklist_User"][target]
                                           kang.sendMessage(msg.to,"User unbanned")
                                       except:
                                           pass

                        elif cmd == "banlist" or cmd == 'bn':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                              if bot_run["Blacklist_User"] == {}:
                                kang.sendMessage(msg.to,"No blacklist user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in bot_run["Blacklist_User"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + "│ " +kang.getContact(m_id).displayName + "\n"
                                kang.sendMessage(msg.to,"╭─「 Banned List 」─\n"+ma+"\n╰──────────\nTotal「%s」Blacklist User" %(str(len(bot_run["Blacklist_User"]))))

                        elif cmd == "talkbanlist" or cmd == 'tbn':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                              if bot_run["Talkblacklist"] == {}:
                                kang.sendMessage(msg.to,"No Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in bot_run["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +kang.getContact(m_id).displayName + "\n"
                                kang.sendMessage(msg.to,"|| Talkban List\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(bot_run["Talkblacklist"]))))

                        elif cmd == "blc" or cmd == 'blcontact':
                          if wait["finbot"] == True:
                            if msg._from in Master:
                              if bot_run["Blacklist_User"] == {}:
                                    kang.sendMessage(msg.to,"No blacklist")
                              else:
                                    ma = ""
                                    for i in bot_run["Blacklist_User"]:
                                        ma = kang.getContact(i)
                                        kang.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif "/ti/g/" in msg.text.lower():
                          if wait["finbot"] == True:
                            #if msg._from in Master:
                              if bot_run["Auto_Join_Ticket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = kang.findGroupByTicket(ticket_id)
                                     kang.acceptGroupInvitationByTicket(group.id,ticket_id)

    except Exception as error:
        print (error) 


while True:
    try:
        autoRestart()
        operations = finbotpoll.singleTrace(count=50)
        if operations is not None:
            for op in operations:
                finbot(op)
                finbotpoll.setRevision(op.revision)
                #_td = threading.Thread(target=finbot, args=(op))#finbot.OpInterrupt[op.type], args=(op)
                #_td.daemon = False
                #_td.start()
                #_td.join()
    except Exception as e:
        print (e)
