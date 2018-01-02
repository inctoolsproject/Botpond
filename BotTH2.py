# -*- coding: utf-8 -*-
import LineAlpha
from LineAlpha.Gen.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob

cl = LineAlpha.LINE()
cl.login(token="EorMCh9rPnx0wOjETNWd.Q0gIW4FFpcj+6R6rCl9vBq.Mp8PtaBBLpDUecGApN5Hr4N2PwUpFKBb/Jl+DiDxpn8=")
cl.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""".............

"""
KAC=[cl]
mid = cl.getProfile().mid
admin=["ud3e765e5dc3b818ffddde7c6d853b6e3"]
wait = {
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":False,"members":1},
    'leaveRoom':False,
    'timeline':True,
    'autoAdd':False,
    'message':"""􀌂􀆿rose stalk􏿿ขายบอท􂜁􀄖V􏿿􂠁􀄵one􏿿􂠁􀄾zero􏿿􀌂􀆿rose stalk􏿿
􁜁􀄑1 candle􏿿Siri v10
􁜁􀄒2 candle􏿿Eliza v10
􁜁􀄓3 candle􏿿Parry v10
􁜁􀄔4 candle􏿿Rakko v10
􁜁􀄕5 candle􏿿Doctor.A v10

􀌂􀇃star􏿿บอทเสริม􀌂􀇃star􏿿
しりちゃん追加保護ボット379(7ตัว)


􁜁􀆎wreath􏿿􁜁􀆔candy cane􏿿ความสามารถBOT􁜁􀆎wreath􏿿􁜁􀆔candy cane􏿿


🔒1.ป้องกันคนลบสมาชิคเกิน 4 คนบอทเตะทันที
🔒2.ป้องกันคนเชิญเพื่อนเข้ากลุ่ม
🔒3.ป้องกันคนเปลี่ยนรูปกลุ่ม
🔒4.ป้องกันคนเปลี่ยนชื่อกลุ่ม
🔒5.ป้องกันคนเปิดลิ้งกลุ่ม  
🔒6.ป้องกันคนรันติกเกิน 15 ตัว ใน 1 นาที
🔒7.สามารถดูได้ว่าใครแอบอ่าน
🔒8.สามารถตั้งแอดมินได้สองคน
🔒9.สามารถเลือกแอดมินผู้ช่วยได้
🔒10.บอทจะดึงสมาชิกกลับอัตโนมัติเมื่อโดนลบออก

􁜁􀆓gingerbread man􏿿􁜁􀆓gingerbread man􏿿􁜁􀆓gingerbread man􏿿􁜁􀆓gingerbread man􏿿􁜁􀆓gingerbread man􏿿􁜁􀆓gingerbread man􏿿􁜁􀆓gingerbread man􏿿
🔰【❖Ŧềάм β✪† †ђάї❖】🔰
ขายบอทแท็กครับ
💲ตัวละ200บ.💲
👍👍คุณสมบัติ👍👍
1.แท็กคนได้ทักห้องด้วยคำสั้งเดียว
2.มีคำสั่งSiriv10
3.มีระบบต้อนรับ
4.สามารถเช็คคนอ่านได้

สนใจติดต่อสอบถามได้

🚀ปอนด์🚀
http://line.me/ti/p/~botth.
""",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "cName":"ฺBot.โปรเต้",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
            if op.type == 26:
                msg = op.message
                if msg.text =="ดีครับ":
                    cl.sendText(msg.to,"ดีค่าบ")
            if op.type == 26:
                msg = op.message
                if msg.text =="ดีค่ะ":
                    cl.sendText(msg.to,"ดีครับคนสวยอิอิ")
            if op.type == 26:
                msg = op.message
                if msg.text =="บอท":
                    cl.sendText(msg.to,"ว่าไงครับ")
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text in ["Admin"]:
                msg.contentType = 13
                adm = 'uac2c4ab02e7656b2ee079985f7a95d7d'
                msg.contentMetadata = {'mid': adm}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"ผู้สร้างบอท")
            elif msg.text is None:
                return
            elif msg.text in ["ล้างค้างเชิญ","Cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","K on","Contact on","é¡¯ç¤ºï¼šé–‹"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","K off","Contact off","é¡¯ç¤ºï¼šé—œ"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","J on","Auto join:on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","J off","Auto join:off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text == "เช็ค":
                    cl.sendText(msg.to, "!โปรดรอ..กรุณาพิมพ์ อ่าน")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                           pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "อ่าน":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "╔═══════════════%s\n╠════════════════\n%s║Readig point creation:\n║ [%s]\n╚════════════════"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "กรุณาพิม..เช็คก่อนครับ")
						
            elif msg.text in ["555"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
#-----------------------------------------------------------
            elif msg.text in ["Delete chat"]:
                cl.removeAllMessages(op.param2)
                cl.sendText(msg.to,"Chatbot Delete")
                cl.sendText(msg.to,"Success...")
#-----------------------------------------------------------
            elif msg.text.lower() == "ไวลัส":                                           
                msg.contentType = 13                                                    
                msg.text = None                                                         
                msg.contentMetadata = {'mid': msg.to+"',"}                              
                cl.sendMessage(msg)                                    
                #×××××××××××××××××××××××××××××××××××××××××××××××
            elif msg.text in ["ล็อกห้อง"]:
                    cl.sendText(msg.to,"Set:iconlock:on")
                    cl.sendText(msg.to,"Set:blockinvite:on")
                    cl.sendText(msg.to,"Set:ownerlock:on")
                    cl.sendText(msg.to,"Set:changenamelock:on")
                    cl.sendText(msg.to,"Siri:groupcreator")
            elif msg.text in ["ปิดเชิญ"]:
                    cl.sendText(msg.to,"Set:blockinvite:on")
            elif msg.text in ["เปิดเชิญ"]:
                    cl.sendText(msg.to,"Set:blockinvite:off")
            elif msg.text in ["ล็อกหัวห้อง"]:
                    cl.sendText(msg.to,"Set:ownerlock:on")
            elif msg.text in ["ล็อกชื่อ"]:
                    cl.sendText(msg.to,"Set:changenamelock:on")
            elif msg.text in ["ล็อกรูป"]:
                    cl.sendText(msg.to,"Set:iconlock:on")
            elif msg.text in ["ตั้งค่า"]:
                    cl.sendText(msg.to,"set:status")
            elif msg.text in ["@","แอด"]:
                    cl.sendText(msg.to,"Siri:groupcreator")
                    cl.sendText(msg.to,"แอดมินบอทSiri")
            elif msg.text in ["ดำ"]:
                    cl.sendText(msg.to,"set:addblacklist")
                    cl.sendText(msg.to,"ส่งContectเพื่อเพิ่มบัญชีดำ")
            elif msg.text in ["ขาว"]:
                    cl.sendText(msg.to,"set:addwhitelist")
                    cl.sendText(msg.to,"ส่งContectเพื่อเพิ่มบัญชีขาว")
            elif msg.text in ["เปิดลิ้งค์"]:
                    cl.sendText(msg.to,"Siri:inviteurl")
            elif msg.text in ["ปิดลิ้งค์"]:
                    cl.sendText(msg.to,"siriv10: DenyInviteURL")
            elif msg.text in ["ยกเลิกค้างเชิญ"]:
                    cl.sendText(msg.to,"Siriv10:cancellnvite(สั่ง2รอบครับ)")
                    cl.sendText(msg.to,"Cancel(สั่งBOT-THครั้งเดียว)")
            elif msg.text in ["ขอแอดมินใหม่"]:
                    cl.sendText(msg.to,"set:changeowner")
            elif msg.text in ["ปลดหัวห้องว่าง"]:
                    cl.sendText(msg.to,"Siriv10:forcerelease")
                    cl.sendText(msg.to,"ใช้สำหรับแอดมินลบบัญชี")
            elif msg.text in ["เพิ่มแอดรอง"]:
                    cl.sendText(msg.to,"設定:予備作")
            elif msg.text in ["สลับแอด"]:
                    cl.sendText(msg.to,"設定:作者交換")
            elif msg.text in ["@@"]:
                    cl.sendText(msg.to,"siriv10:予備作成者")
            elif msg.text in ["บอทออก"]:
                    cl.sendText(msg.to,"Siri:bye")
            elif msg.text in ["เรียกบอท","รี"]:
                    cl.sendText(msg.to,"Siriv10:再招待")
            elif msg.text in ["เปลียน@"]:
                    cl.sendText(msg.to,"set:changeowner")
            elif msg.text in ["เปลี่ยน@@"]:
                    cl.sendText(msg.to,"set:changeextracreator")
            elif msg.text in ["ลบ@@"]:
                    cl.sendText(msg.to,"Set:deleteextracreator")
            elif msg.text in ["เช็คตั๋ว"]:
                    cl.sendText(msg.to,"Siri:招待回数")
            elif msg.text in ["Help v10"]:
                    cl.sendText(msg.to,"""􀬁􀄆heart eyes􏿿คำสั่งv10ใช้ง่ายๆ􀬁􀄊nervous laugh􏿿
➫ล็อกห้อง[ชุดคำสั่งล็อกห้อง]
☞ล็อกเชิญ[ป้องกันสมาชิกเชิญคน]
➫ล็อกหัวห้อง[ล็อกแอดมินห้อง]
☞ล็อกชื่อ[ล็อกชื่อกลุ่ม]
➫ล็อกรูป[ล็อกรูปกลุ่ม]
☞เช็คตั้งค่า[เช็คตั้งค่าบอท]
➫@[แอดมินกลุ่มคนที่1]
☞@@[แอดมินกลุ่มคนที่2]
➫ดำ[เพิ่มบัญชีดำ]
☞ขาว[เพิ่มบัญชีขาว]
➫เปิดลิ้งค์[เปิดลิ้งค์กลุ่ม]
☞ปิดลิ้งค์[ป้องกันคนเปิดลิ้งค์]
➫ยกเลิกค้างเชิญ[ล้างคำเชิญกลุ่ม]
☞ขอแอดมินใหม่
➫เพิ่มแอดรอง[เพิ่มแอดมินที่2]
☞ปลดหัวห้องว่าง
➫สลับแอด[สลับแอดลองให้เป็นตัวจิง]
☞บอทออก[บอทออกกลุ่ม]
➫เรียกบอท[เรียกบอทเวลาดับ]
☞เปลียน@[เปลี่ยน@1]
➫เปลี่ยน@@[เปลี่ยน@2]
➫ลบ@@[ลบแอดมินที่2]
""")
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif msg.text in ["ยกเริก","Cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "ผู้สร้างลบบัญชี"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "ปิด"
                        else:
                            u = "เปิด"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#-----------------------------------------------
            elif msg.text in ["Tagall"]:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg) 

#-----------------------------------------------
            elif msg.text in ["Bye all"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
        if op.type == 17:
            group = cl.getGroup(op.param1)
            cb = Message()
            cb.to = op.param1
            cb.text = cl.getContact(op.param2).displayName +"\n🌟ยินดีต้อนรับเข้าสู่🌟\n👉"+group.name
            cl.sendMessage(cb)

        if op.type == 15:
            group = cl.getGroup(op.param1)
            cb = Message()
            cb.to = op.param1
            cb.text = cl.getContact(op.param2).displayName + "\n😭😭ไปแล้วหรอคิดถึงก็กลับมา\n"+group.name+"ใหม่นะ😢"
            cl.sendMessage(cb)
#------------------------------------------------------------------------------------
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n☑" + Name
                else:
                    cl.sendText
            except:
                  pass
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
