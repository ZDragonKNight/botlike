# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,base64,requests,urllib

cl = LINETCR.LINE()
cl.login(qr=True)
#cl.login(token="")
cl.loginResult()

ki = kk = kc = cl 

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')
KAC=[cl,ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid]
admin=["u31ef22df7f538df1d74dc7f756ef1a32","u9cc2323f5b84f9df880c33aa9f9e3ae1"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me, Jgn lupa bahagia ya, mau akunmu setengah bot pm aja ya »»»»» http://line.me/ti/p/GkwfNjoPDH «««««",
    "lang":"JP",
    "comment":"Thanks for add me, Jgn lupa bahagia ya, mau akunmu setengah bot pm aja ya »»»»» http://line.me/ti/p/GkwfNjoPDH «««««",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True,
    "atjointicket":False
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

#---------------------------[AutoLike-nya]---------------------------#
#Like By Syams Copyright 2017 
def autolike():#Like By Syams Copyright 2017
     for zx in range(0,20):#Like By Syams copyright 2017
        hasil = cl.activity(limit=20)#Like By Syams Copyright 2017
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:#Like By Syams Copyright 2017
          try:    #Like By Syams Copyright 2017
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)#Like By Syams Copyright 2017
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Autolike By Kris-thea\n\nBot Auto Like Ini Gunakanlah Dengan Bijak（＾ω＾）\nAuto Like By »»»»» http://line.me/ti/p/GkwfNjoPDH «««««")#Like By Syams Copyright 2017
            print "Like"#Like By Syams Copyright 2017
          except:#Like By Syams Copyright 2017
            pass#Like By Syams Copyright 2017
        else:#Like By Syams Copyright 2017
            print "Already Liked"#Like By Syams Copyright 2017
     time.sleep(500)#Like By Syams Copyright 2017
thread2 = threading.Thread(target=autolike)#Like By Syams Copyright 2017
thread2.daemon = True#Like By Syams Copyright 2017
thread2.start()#Like By Syams Copyright 2017
#Like By Syams Copyright 2017
#---------------------------[AutoLike-nya]---------------------------#

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

#-------------------------[Jangan Dihapus]------------------------#

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 15:
            kk.sendText(op.param1,cl.getContact(op.param2).displayName + ", Selamat Jalan\nMoga selalu Bahagia ya ^_^\nMakasih")
            print "Ada Member Keluar Dari Grup"
        if op.type == 17:
            kk.sendText(op.param1,cl.getContact(op.param2).displayName + ", Selamat Datang di Room FS3I Family ^_^\nJangan Nakal & Jangan Baper Ya ^_^")
            print "Ada Member Masuk ke Grup"
        if op.type == 19:
            kk.sendText(op.param1,cl.getContact(op.param2).displayName + ", Dia Kicker :(\nGimana Donk\nSaya Gk Bisa Anuin Dia")
            print "Ada Kicker"
        if op.type == 32:
            kk.sendText(op.param1,cl.getContact(op.param2).displayName + ", Jiah Dibatalin?\nMungkin Dia Belum Kemeng neh")
            print "Ada Yang Ngebatalin Invite-an Dari Grup"
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

#----------------------[Masukin Semua SC Yang Ente Pengen Disini]----------------------#
        if op.type == 25:
            msg = op.message
            
            
#----------------------------[Cek SPEED]----------------------------#WORK
            if msg.text in ["Speed","speed"]:
                    start = time.time()
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))
#----------------------------[Cek SPEED]----------------------------#WORK

#----------------------------[TAG ALL]----------------------------#WORK
            if msg.text in ["Summon"]:
			    group = cl.getGroup(msg.to)
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
			    msg.contentType = 0
			    msg.text = cb2
			    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
			    try:
			        kc.sendMessage(msg)
			    except Exception as error:
			        print error
#----------------------------[TAG ALL]----------------------------#WORK

#----------------------------[Spam]----------------------------#WORK
            if "Spam: " in msg.text:
                cond = msg.text.split(" ")
                value = int(cond[2])
                text = msg.text.replace("Spam: " + str(cond[1]) + " " + str(value) + " ","")
                ballon1 = value * (text + "\n")
                if cond[1] == "on":
                    if value <= 150:
                        for x in range(value):
                            cl.sendText(msg.to, text)
                    else:
                        cl.sendText(msg.to,"Jumlah spamming melebihi batas")
                elif cond[1] == "off":
                    if value <= 200:
                        cl.sendText(msg.to,ballon1)
                    else:
                        cl.sendText(msg.to,"Jumlah spamming melebihi batas")
                else:
                    cl.sendText(msg.to,"Error condition")
#----------------------------[Spam]----------------------------#WORK 

#----------------------------[Spam To Contact]----------------------------#WORK 
            elif "Spamcontact @" in msg.text:
                _name = msg.text.replace("Spamcontact @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam") 
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(msg.to, "Done")
                       print " Spammed !"
#----------------------------[Spam To Contact]----------------------------#WORK 

#----------------------------[Kick By Multi Tag]----------------------------#WORK 
            if ("Bye " in msg.text):
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
#----------------------------[Kick By Multi Tag]----------------------------#WORK                  

#----------------------------[Invite Group Creator]----------------------------#WORK
            elif msg.text in ["Gcreator:inv"]:
              if msg.toType == 2:
                 ginfo = cl.getGroup(msg.to)
                 gCreator = ginfo.creator.mid
                 try:
                    cl.findAndAddContactsByMid(gCreator)
                    cl.inviteIntoGroup(msg.to,[gCreator])
                    print "Berhasil Invite Pembuat Grup"
                 except:
                    pass
#----------------------------[Invite Group Creator]----------------------------#WORK

#----------------------------[Group BroadCast]----------------------------#WORK
            if "Gbc " in msg.text:
                print "Berhasil BC ke Semua Grup"
                bctxt = msg.text.replace("Gbc ","")
                n = cl.getGroupIdsJoined()
                for people in n:
                    cl.sendText(people, (bctxt))
#----------------------------[Group BroadCast]----------------------------#WORK  

#----------------------------[Kick All Member]----------------------------#WORK  
                if msg.text == "Kick all ready":
                    print "ok"
                    _name = msg.text.replace("Kick all","")
                    gs = cl.getGroup(msg.to)
                    sendMessage(msg.to,"Kick By Kris - thea\nsaya tidak bertanggung jawab apabila grup anda rata karena bot ini, silahkan kalian intropeksi sendiri aja\nTerimakasih")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        sendMessage(msg.to,"error")
                    else:
                        for target in targets:
                            try:
                                klist=[cl]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg.to,"error")
#----------------------------[Kick All Member]----------------------------#WORK  

#----------------------------[Friend BroadCast]----------------------------#WORK 
                if "Fbc " in msg.text:
                    print "BroadCast Ke Semua Teman Berhasil"
                    bctxt = msg.text.replace("Fbc ","")
                    n = cl.getAllContactIds()
                    for people in n:
                        cl.sendText(people, (bctxt))
#----------------------------[Friend BroadCast]----------------------------#WORK



#----------------------[Masukin Semua SC Yang Ente Pengen Disini]----------------------#

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

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
            
#-------------------------[Jangan Dihapus]------------------------#            
