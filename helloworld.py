# -*- coding: utf-8 -*-
from important import *

# Setup Argparse
parser = argparse.ArgumentParser(description='Selfbot ZeroDAYS')
parser.add_argument('-t', '--token', type=str, metavar='', required=False, help='Token | Example : Exxxx')
parser.add_argument('-e', '--email', type=str, default='', metavar='', required=False, help='Email Address | Example : example@xxx.xx')
parser.add_argument('-p', '--passwd', type=str, default='', metavar='', required=False, help='Password | Example : xxxx')
parser.add_argument('-a', '--apptype', type=str, default='', metavar='', required=False, choices=list(ApplicationType._NAMES_TO_VALUES), help='Application Type | Example : CHROMEOS')
parser.add_argument('-s', '--systemname', type=str, default='', metavar='', required=False, help='System Name | Example : Chrome_OS')
parser.add_argument('-c', '--channelid', type=str, default='', metavar='', required=False, help='Channel ID | Example : 1341209950')
parser.add_argument('-T', '--traceback', type=str2bool, nargs='?', default=False, metavar='', required=False, const=True, choices=[True, False], help='Using Traceback | Use : True/False')
parser.add_argument('-S', '--showqr', type=str2bool, nargs='?', default=False, metavar='', required=False, const=True, choices=[True, False], help='Show QR | Use : True/False')
args = parser.parse_args()


# Login Client
listAppType = ['DESKTOPWIN', 'DESKTOPMAC', 'IOSIPAD', 'CHROMEOS']
try:
    print ('##----- LOGIN CLIENT -----##')
    line = None
    if args.apptype:
        tokenPath = Path('authToken.txt')
        if tokenPath.exists():
            tokenFile = tokenPath.open('r')
        else:
            tokenFile = tokenPath.open('w+')
        savedAuthToken = tokenFile.read().strip()
        authToken = savedAuthToken if savedAuthToken and not args.token else args.token
        idOrToken = authToken if authToken else args.email
        try:
            line = LINE(idOrToken, args.passwd, appType=args.apptype, systemName=args.systemname, channelId=args.channelid, showQr=args.showqr)
            tokenFile.close()
            tokenFile = tokenPath.open('w+')
            tokenFile.write(line.authToken)
            tokenFile.close()
        except TalkException as talk_error:
            if args.traceback: traceback.print_tb(talk_error.__traceback__)
            sys.exit('++ Error : %s' % talk_error.reason.replace('_', ' '))
        except Exception as error:
            if args.traceback: traceback.print_tb(error.__traceback__)
            sys.exit('++ Error : %s' % str(error))
    else:
        for appType in listAppType:
            tokenPath = Path('authToken.txt')
            if tokenPath.exists():
                tokenFile = tokenPath.open('r')
            else:
                tokenFile = tokenPath.open('w+')
            savedAuthToken = tokenFile.read().strip()
            authToken = savedAuthToken if savedAuthToken and not args.token else args.token
            idOrToken = authToken if authToken else args.email
            try:
                line = LINE(idOrToken, args.passwd, appType=appType, systemName=args.systemname, channelId=args.channelid, showQr=args.showqr)
                tokenFile.close()
                tokenFile = tokenPath.open('w+')
                tokenFile.write(line.authToken)
                tokenFile.close()
            except TalkException as talk_error:
                print ('++ Error : %s' % talk_error.reason.replace('_', ' '))
                if args.traceback: traceback.print_tb(talk_error.__traceback__)
                if talk_error.code == 1:
                    continue
                sys.exit(1)
            except Exception as error:
                print ('++ Error : %s' % str(error))
                if args.traceback: traceback.print_tb(error.__traceback__)
                sys.exit(1)
except Exception as error:
    print ('++ Error : %s' % str(error))
    if args.traceback: traceback.print_tb(error.__traceback__)
    sys.exit(1)

# Login Client 2
listAppType = ['DESKTOPWIN', 'DESKTOPMAC', 'IOSIPAD', 'CHROMEOS']
try:
    print ('##----- LOGIN CLIENT 2-----##')
    line2 = None
    if args.apptype:
        tokenPath2 = Path('authToken2.txt')
        if tokenPath2.exists():
            tokenFile2 = tokenPath2.open('r')
        else:
            tokenFile2 = tokenPath2.open('w+')
        savedAuthToken2 = tokenFile2.read().strip()
        authToken2 = savedAuthToken2 if savedAuthToken2 and not args.token else args.token
        idOrToken2 = authToken2 if authToken2 else args.email
        try:
            line2 = LINE(idOrToken2, args.passwd, appType=args.apptype, systemName=args.systemname, channelId=args.channelid, showQr=args.showqr)
            tokenFile2.close()
            tokenFile2 = tokenPath2.open('w+')
            tokenFile2.write(line2.authToken)
            tokenFile2.close()
        except TalkException as talk_error:
            if args.traceback: traceback.print_tb(talk_error.__traceback__)
            sys.exit('++ Error : %s' % talk_error.reason.replace('_', ' '))
        except Exception as error:
            if args.traceback: traceback.print_tb(error.__traceback__)
            sys.exit('++ Error : %s' % str(error))
    else:
        for appType in listAppType:
            tokenPath2 = Path('authToken2.txt')
            if tokenPath2.exists():
                tokenFile2 = tokenPath2.open('r')
            else:
                tokenFile2 = tokenPath2.open('w+')
            savedAuthToken2 = tokenFile2.read().strip()
            authToken2 = savedAuthToken2 if savedAuthToken2 and not args.token else args.token
            idOrToken2 = authToken2 if authToken2 else args.email
            try:
                line2 = LINE(idOrToken2, args.passwd, appType=appType, systemName=args.systemname, channelId=args.channelid, showQr=args.showqr)
                tokenFile2.close()
                tokenFile2 = tokenPath2.open('w+')
                tokenFile2.write(line2.authToken)
                tokenFile2.close()
            except TalkException as talk_error:
                print ('++ Error : %s' % talk_error.reason.replace('_', ' '))
                if args.traceback: traceback.print_tb(talk_error.__traceback__)
                if talk_error.code == 1:
                    continue
                sys.exit(1)
            except Exception as error:
                print ('++ Error : %s' % str(error))
                if args.traceback: traceback.print_tb(error.__traceback__)
                sys.exit(1)
except Exception as error:
    print ('++ Error : %s' % str(error))
    if args.traceback: traceback.print_tb(error.__traceback__)
    sys.exit(1)

if line:
    print ('++ Auth Token : %s' % line.authToken)
    print ('++ Timeline Token : %s' % line.tl.channelAccessToken)
    print ('##----- LOGIN CLIENT 1 & 2(Success) -----##')
else:
    sys.exit('##----- LOGIN CLIENT 1 & 2(Failed) -----##')

myMid = line.profile.mid
assistsMid = line2.profile.mid
programStart = time.time()
oepoll = OEPoll(line)



tmp_text = []
lurking = {}
msg_dict = {}
msg_dict1 = {}

settings = livejson.File('setting.json', True, False, 4)

plates = codecs.open("template.json","r","utf-8")
plate = json.load(plates)

bool_dict = {
    True: ['Yes', 'Active', 'Success', 'Open', 'On'],
    False: ['No', 'Not Active', 'Failed', 'Close', 'Off']
}

# Backup profile
profile = line.getContact(myMid)
settings['myProfile']['displayName'] = profile.displayName
settings['myProfile']['statusMessage'] = profile.statusMessage
settings['myProfile']['pictureStatus'] = profile.pictureStatus
coverId = line.profileDetail['result']['objectId']
settings['myProfile']['coverId'] = coverId
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))

    print("BYE")
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))

def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def restartProgram():
    print ('##----- PROGRAM RESTARTED -----##')
    python = sys.executable
    os.execl(python, python, *sys.argv)

def logError(error, write=True):
    errid = str(random.randint(100, 999))
    filee = open('tmp/errors/%s.txt'%errid, 'w') if write else None
    if args.traceback: traceback.print_tb(error.__traceback__)
    if write:
        traceback.print_tb(error.__traceback__, file=filee)
        filee.close()
        with open('errorLog.txt', 'a') as e:
            e.write('\n%s : %s'%(errid, str(error)))
    print ('++ Error : {error}'.format(error=error))

def command(text):
    pesan = text.lower()
    if settings['setKey']['status']:
        if pesan.startswith(settings['setKey']['key']):
            cmd = pesan.replace(settings['setKey']['key'],'')
        else:
            cmd = 'Undefined command'
    else:
        cmd = text.lower()
    return cmd

def genImageB64(path):
    with open(path, 'rb') as img_file:
        encode_str = img_file.read()
        b64img = base64.b64encode(encode_str)
        return b64img.decode('utf-8')

def genUrlB64(url):
    return base64.b64encode(url.encode('utf-8')).decode('utf-8')

def bs(link,hdr=True):
	if hdr == False:return bs4.BeautifulSoup(requests.get(link).content, "html5lib")
	else:return bs4.BeautifulSoup(requests.get(link,headers=z).content, "html5lib")

def removeCmd(text, key=''):
    if key == '':
        setKey = '' if not settings['setKey']['status'] else settings['setKey']['key']
    else:
        setKey = key
    text_ = text[len(setKey):]
    sep = text_.split(' ')
    return text_[len(sep[0] + ' '):]

def multiCommand(cmd, list_cmd=[]):
    if True in [cmd.startswith(c) for c in list_cmd]:
        return True
    else:
        return False

def replaceAll(text, dic):
    try:
        rep_this = dic.items()
    except:
        rep_this = dic.iteritems()
    for i, j in rep_this:
        text = text.replace(i, j)
    return text

def help():
    key = '' if not settings['setKey']['status'] else settings['setKey']['key']
    with open('help.txt', 'r') as f:
        text = f.read()
    helpMsg = text.format(key=key.title())
    return helpMsg

def parsingRes(res):
    result = ''
    textt = res.split('\n')
    for text in textt:
        if True not in [text.startswith(s) for s in ['╭', '├', '│', '╰']]:
            result += '\n│ ' + text
        else:
            if text == textt[0]:
                result += text
            else:
                result += '\n' + text
    return result

def mentionMembers(to, mids=[]):
    if myMid in mids: mids.remove(myMid)
    parsed_len = len(mids)//10+1
    result = '╭───「 Mention Members 」\n'
    mention = '@fakhrads\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*10:(point+1)*10]:
            no += 1
            result += '│ %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += '╰───「 ZeroDAYS 」\n'
        if result:
            if result.endswith('\n'): result = result[:-1]
            line.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
        result = ''

def cloneProfile(mid):
    contact = line.getContact(mid)
    profile = line.getProfile()
    profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
    line.updateProfile(profile)
    if contact.pictureStatus:
        pict = line.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus)
        line.updateProfilePicture(pict)
    coverId = line.getProfileDetail(mid)['result']['objectId']
    line.updateProfileCoverById(coverId)

def backupProfile():
    profile = line.getContact(myMid)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    coverId = line.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)

def restoreProfile():
    profile = line.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    line.updateProfile(profile)
    if settings['myProfile']['pictureStatus']:
        pict = line.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'])
        line.updateProfilePicture(pict)
    coverId = settings['myProfile']['coverId']
    line.updateProfileCoverById(coverId)

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey):
    if cmd == 'logoutbot':
        line.sendMessage(to, 'Bot will logged out')
        sys.exit('##----- PROGRAM STOPPED -----##')
    elif cmd == 'logoutdevicee':
        line.logout()
        sys.exit('##----- CLIENT LOGOUT -----##')
    elif cmd == 'restart':
        line.sendMessage(to, 'Bot will restarting')
        restartProgram()
    elif cmd == "xx":
        line.sendFlex(to, plate["help"])
    elif cmd == 'speed':
        start = time.time()
        line.sendMessage(to, 'Checking speed')
        elapse = time.time() - start
        line.sendMessage(to, 'Speed sending message took %s seconds' % str(elapse))
    elif cmd == 'me':
        line.sendContact(to, myMid)
    elif cmd == 'runtime':
        runtime = time.time() - programStart
        line.sendMessage(to, 'Bot already running on ' + format_timespan(runtime))
    elif cmd == 'author':
        line.sendContact(to, myMid)
    elif cmd == 'about':
        res = '╭───「 About 」'
        res += '\n├ Type : Selfbot Protect (Hello World)'
        res += '\n├ Version : 0.1'
        res += '\n├ Library : linepy (3.0.8)'
        res += '\n├ Creator : ZeroCool, Recode by ZeroDAYs'
        res += '\n╰───「 ZeroDAYS 」'
        line.sendMessage(to, res)
    elif cmd == 'status':
        res = '╭───「 Status 」'
        res += '\n├ Auto Add : ' + bool_dict[settings['autoAdd']['status']][1]
        res += '\n├ Auto Join : ' + bool_dict[settings['autoJoin']['status']][1]
        res += '\n├ Auto Respond : ' + bool_dict[settings['autoRespond']['status']][1]
        res += '\n├ Auto Respond Mention : ' + bool_dict[settings['autoRespondMention']['status']][1]
        res += '\n├ Auto Read : ' + bool_dict[settings['autoRead']][1]
        res += '\n├ Setting Key : ' + bool_dict[settings['setKey']['status']][1]
        res += '\n├ Mimic : ' + bool_dict[settings['mimic']['status']][1]
        res += '\n├ Greetings Join : ' + bool_dict[settings['greet']['join']['status']][1]
        res += '\n├ Greetings Leave : ' + bool_dict[settings['greet']['leave']['status']][1]
        res += '\n├ Check Contact : ' + bool_dict[settings['checkContact']][1]
        res += '\n├ Check Post : ' + bool_dict[settings['checkPost']][1]
        res += '\n├ Check Sticker : ' + bool_dict[settings['checkSticker']][1]
        res += '\n╰───「 ZeroDAYS 」'
        line.sendMessage(to, parsingRes(res))
    elif cmd == 'abort':
        aborted = False
        if to in settings['changeGroupPicture']:
            settings['changeGroupPicture'].remove(to)
            line.sendMessage(to, 'Change group picture aborted')
            aborted = True
        if settings['changePictureProfile']:
            settings['changePictureProfile'] = False
            line.sendMessage(to, 'Change picture profile aborted')
            aborted = True
        if settings['changeCoverProfile']:
            settings['changeCoverProfile'] = False
            line.sendMessage(to, 'Change cover profile aborted')
            aborted = True
        if not aborted:
            line.sendMessage(to, 'Failed abort, nothing to abort')
    elif cmd.startswith('error'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = '╭───「 Error 」'
        res += '\n├ Usage : '
        res += '\n│ • {key}Error'
        res += '\n│ • {key}Error Logs'
        res += '\n│ • {key}Error Reset'
        res += '\n│ • {key}Error Detail <errid>'
        res += '\n╰───「 ZeroDAYS 」'
        if cmd == 'error':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif cond[0].lower() == 'logs':
            try:
                filee = open('errorLog.txt', 'r')
            except FileNotFoundError:
                return line.sendMessage(to, 'Failed display error logs, error logs file not found')
            errors = [err.strip() for err in filee.readlines()]
            filee.close()
            if not errors: return line.sendMessage(to, 'Failed display error logs, empty error logs')
            res = '╭───「 Error Logs 」'
            res += '\n├ List :'
            parsed_len = len(errors)//200+1
            no = 0
            for point in range(parsed_len):
                for error in errors[point*200:(point+1)*200]:
                    if not error: continue
                    no += 1
                    res += '\n│ %i. %s' % (no, error)
                    if error == errors[-1]:
                        res += '\n╰───「 ZeroDAYS 」'
                if res:
                    if res.startswith('\n'): res = res[1:]
                    line.sendMessage(to, res)
                res = ''
        elif cond[0].lower() == 'reset':
            filee = open('errorLog.txt', 'w')
            filee.write('')
            filee.close()
            shutil.rmtree('tmp/errors/', ignore_errors=True)
            os.system('mkdir tmp/errors')
            line.sendMessage(to, 'Success reset error logs')
        elif cond[0].lower() == 'detail':
            if len(cond) < 2:
                return line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            errid = cond[1]
            if os.path.exists('tmp/errors/%s.txt' % errid):
                with open('tmp/errors/%s.txt' % errid, 'r') as f:
                    line.sendMessage(to, f.read())
            else:
                return line.sendMessage(to, 'Failed display details error, errorid not valid')
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif txt.startswith('setkey'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭───「 Setting Key 」'
        res += '\n├ Status : ' + bool_dict[settings['setKey']['status']][1]
        res += '\n├ Key : ' + settings['setKey']['key'].title()
        res += '\n├ Usage : '
        res += '\n│ • Setkey'
        res += '\n│ • Setkey <on/off>'
        res += '\n│ • Setkey <key>'
        res += '\n╰───「 ZeroDAYS 」'
        if txt == 'setkey':
            line.sendMessage(to, parsingRes(res))
        elif texttl == 'on':
            if settings['setKey']['status']:
                line.sendMessage(to, 'Setkey already active')
            else:
                settings['setKey']['status'] = True
                line.sendMessage(to, 'Success activated setkey')
        elif texttl == 'off':
            if not settings['setKey']['status']:
                line.sendMessage(to, 'Setkey already deactive')
            else:
                settings['setKey']['status'] = False
                line.sendMessage(to, 'Success deactivated setkey')
        else:
            settings['setKey']['key'] = texttl
            line.sendMessage(to, 'Success change set key to (%s)' % textt)
    elif cmd.startswith('autoadd'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = '╭───「 Auto Add 」'
        res += '\n├ Status : ' + bool_dict[settings['autoAdd']['status']][1]
        res += '\n├ Reply : ' + bool_dict[settings['autoAdd']['reply']][0]
        res += '\n├ Reply Message : ' + settings['autoAdd']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}AutoAdd'
        res += '\n│ • {key}AutoAdd <on/off>'
        res += '\n│ • {key}AutoAdd Reply <on/off>'
        res += '\n│ • {key}AutoAdd <message>'
        res += '\n╰───「 ZeroDAYS 」'
        if cmd == 'autoadd':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoAdd']['status']:
                line.sendMessage(to, 'Autoadd already active')
            else:
                settings['autoAdd']['status'] = True
                line.sendMessage(to, 'Success activated autoadd')
        elif texttl == 'off':
            if not settings['autoAdd']['status']:
                line.sendMessage(to, 'Autoadd already deactive')
            else:
                settings['autoAdd']['status'] = False
                line.sendMessage(to, 'Success deactivated autoadd')
        elif cond[0].lower() == 'reply':
            if len(cond) < 2:
                return line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            if cond[1].lower() == 'on':
                if settings['autoAdd']['reply']:
                    line.sendMessage(to, 'Reply message autoadd already active')
                else:
                    settings['autoAdd']['reply'] = True
                    line.sendMessage(to, 'Success activate reply message autoadd')
            elif cond[1].lower() == 'off':
                if not settings['autoAdd']['reply']:
                    line.sendMessage(to, 'Reply message autoadd already deactive')
                else:
                    settings['autoAdd']['reply'] = False
                    line.sendMessage(to, 'Success deactivate reply message autoadd')
            else:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        else:
            settings['autoAdd']['message'] = textt
            line.sendMessage(to, 'Success change autoadd message to `%s`' % textt)
    elif cmd.startswith('autojoin'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = '╭───「 Auto Join 」'
        res += '\n├ Status : ' + bool_dict[settings['autoJoin']['status']][1]
        res += '\n├ Reply : ' + bool_dict[settings['autoJoin']['reply']][0]
        res += '\n├ Reply Message : ' + settings['autoJoin']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}AutoJoin'
        res += '\n│ • {key}AutoJoin <on/off>'
        res += '\n│ • {key}AutoJoin Ticket <on/off>'
        res += '\n│ • {key}AutoJoin Reply <on/off>'
        res += '\n│ • {key}AutoJoin <message>'
        res += '\n╰───「 ZeroDAYS 」'
        if cmd == 'autojoin':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoJoin']['status']:
                line.sendMessage(to, 'Autojoin already active')
            else:
                settings['autoJoin']['status'] = True
                line.sendMessage(to, 'Success activated autojoin')
        elif texttl == 'off':
            if not settings['autoJoin']['status']:
                line.sendMessage(to, 'Autojoin already deactive')
            else:
                settings['autoJoin']['status'] = False
                line.sendMessage(to, 'Success deactivated autojoin')
        elif cond[0].lower() == 'reply':
            if len(cond) < 2:
                return line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            if cond[1].lower() == 'on':
                if settings['autoJoin']['reply']:
                    line.sendMessage(to, 'Reply message autojoin already active')
                else:
                    settings['autoJoin']['reply'] = True
                    line.sendMessage(to, 'Success activate reply message autojoin')
            elif cond[1].lower() == 'off':
                if not settings['autoJoin']['reply']:
                    line.sendMessage(to, 'Reply message autojoin already deactive')
                else:
                    settings['autoJoin']['reply'] = False
                    line.sendMessage(to, 'Success deactivate reply message autojoin')
            else:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif cond[0].lower() == 'ticket':
            if len(cond) < 2:
                return line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
            if cond[1].lower() == 'on':
                if settings['autoJoin']['ticket']:
                    line.sendMessage(to, 'Autojoin ticket already active')
                else:
                    settings['autoJoin']['ticket'] = True
                    line.sendMessage(to, 'Success activate autojoin ticket')
            elif cond[1].lower() == 'off':
                if not settings['autoJoin']['ticket']:
                    line.sendMessage(to, 'Autojoin ticket already deactive')
                else:
                    settings['autoJoin']['ticket'] = False
                    line.sendMessage(to, 'Success deactivate autojoin ticket')
            else:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        else:
            settings['autoJoin']['message'] = textt
            line.sendMessage(to, 'Success change autojoin message to `%s`' % textt)
    elif cmd.startswith('autorespondmention'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭───「 Auto Respond 」'
        res += '\n├ Status : ' + bool_dict[settings['autoRespondMention']['status']][1]
        res += '\n├ Reply Message : ' + settings['autoRespondMention']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}AutoRespondMention'
        res += '\n│ • {key}AutoRespondMention <on/off>'
        res += '\n│ • {key}AutoRespondMention <message>'
        res += '\n╰───「 ZeroDAYS 」'
        if cmd == 'autorespondmention':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoRespondMention']['status']:
                line.sendMessage(to, 'Autorespondmention already active')
            else:
                settings['autoRespondMention']['status'] = True
                line.sendMessage(to, 'Success activated autorespondmention')
        elif texttl == 'off':
            if not settings['autoRespondMention']['status']:
                line.sendMessage(to, 'Autorespondmention already deactive')
            else:
                settings['autoRespondMention']['status'] = False
                line.sendMessage(to, 'Success deactivated autorespondmention')
        else:
            settings['autoRespondMention']['message'] = textt
            line.sendMessage(to, 'Success change autorespondmention message to `%s`' % textt)
    elif cmd.startswith('help'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭─「 Help Menu 」'
        res += '\n├ Status : ONLINE'
        res += '\n├ Version : 1.0.2'
        res += '\n├ Usage : '
        res += '\n│ • {key}Me'
        res += '\n│ • {key}Speed'
        res += '\n│ • {key}Runtime'
        res += '\n│ • {key}Restart'
        res += '\n│ • {key}Author'
        res += '\n│ • {key}Status'
        res += '\n│ • {key}Abort'
        res += '\n│ • {key}Error'
        res += '\n│ • {key}Help '
        res += '\n│ • {key}Help Selfbot'
        res += '\n│ • {key}Help Media'
        res += '\n│ • {key}Help Group'
        res += '\n│ • {key}Help Protect'
        res += '\n│ • {key}Help Settings'
        res += '\n╰─「 ZeroDAYS 」'
        if cmd == 'help':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'media':
            textt = removeCmd(text, setKey)
            textsl = textt.lower()
            res = '╭───「 Media 」'
            res += '\n├ Usage : '
            res += '\n│ • {key}Praytime <location>'
            res += '\n│ • {key}Picture <query>'
            res += '\n│ • {key}Ig <instagram username>'
            res += '\n│ • {key}Weather <location>'
            res += '\n╰───「 ZeroDAYS 」'
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'selfbot':
            textt = removeCmd(text, setKey)
            textsl = textt.lower()
            res = '╭───「 Help Selfbot」'
            res += '\n├ Usage : '
            res += '\n│ • {key}MyProfile'
            res += '\n│ • {key}Profile'
            res += '\n│ • {key}Mimic'
            res += '\n│ • {key}Broadcast'
            res += '\n│ • {key}FriendList'
            res += '\n│ • {key}BlockList'
            res += '\n╰───「 ZeroDAYS 」'
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'protect':
            textt = removeCmd(text, setKey)
            textsl = textt.lower()
            res = '╭───「 Help Protect」'
            res += '\n├ Usage : '
            res += '\n│ • {key}Protect'
            res += '\n│ • {key}Ban'
            res += '\n╰───「 ZeroDAYS 」'
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'group':
            textt = removeCmd(text, setKey)
            textsl = textt.lower()
            res = '╭───「 Help Group」'
            res += '\n├ Usage : '
            res += '\n│ • {key}GroupInfo'
            res += '\n│ • {key}GroupList'
            res += '\n│ • {key}InvitationList'
            res += '\n│ • {key}MemberList'
            res += '\n│ • {key}PendingList'
            res += '\n│ • {key}OpenQr'
            res += '\n│ • {key}CloseQr'
            res += '\n│ • {key}ChangeGroupName <name>'
            res += '\n│ • {key}ChangeGroupPict'
            res += '\n│ • {key}Kickall'
            res += '\n│ • {key}Cancelall'
            res += '\n│ • {key}MentionAll'
            res += '\n│ • {key}Lurk'
            res += '\n│ • {key}Kick <mention>'
            res += '\n│ • {key}Vkick <mention>'
            res += '\n│ • {key}Greet'
            res += '\n╰───「 ZeroDAYS 」'
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'settings':
            textt = removeCmd(text, setKey)
            textsl = textt.lower()
            res = '╭───「 Help Settings」'
            res += '\n├ Usage : '
            res += '│ • {key}Setkey'
            res += '│ • {key}AutoAdd'
            res += '│ • {key}AutoJoin'
            res += '│ • {key}AutoRespond'
            res += '│ • {key}AutoRespondMention'
            res += '│ • {key}AutoRead <on/off>'
            res += '│ • {key}CheckContact <on/off>'
            res += '│ • {key}CheckPost <on/off>'
            res += '│ • {key}CheckSticker <on/off>'
            res += '\n╰───「 ZeroDAYS 」'
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('unsendmsg'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭───「 Get Unsended Message 」'
        res += '\n├ Status : ' + bool_dict[settings['unsendMessage']][1]
        res += '\n├ Usage : '
        res += '\n│ • {key}UnsendMSG'
        res += '\n│ • {key}UnsendMSG <on/off>'
        res += '\n╰───「 ZeroBOT 」'
        if cmd == 'unsendmsg':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['unsendMessage']:
                line.sendMessage(to, 'Get Unsended Message already active')
            else:
                settings['unsendMessage'] = True
                line.sendMessage(to, 'Success activated Get Unsended Message')
        elif texttl == 'off':
            if not settings['unsendMessage']:
                line.sendMessage(to, 'Get Unsended Message already deactive')
            else:
                settings['unsendMessage']= False
                line.sendMessage(to, 'Success deactivated Get Unsended Message')
    elif cmd.startswith('autorespond'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭───「 Auto Respond 」'
        res += '\n├ Status : ' + bool_dict[settings['autoRespond']['status']][1]
        res += '\n├ Reply Message : ' + settings['autoRespond']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}AutoRespond'
        res += '\n│ • {key}AutoRespond <on/off>'
        res += '\n│ • {key}AutoRespond <message>'
        res += '\n╰───「 ZeroDAYS 」'
        if cmd == 'autorespond':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['autoRespond']['status']:
                line.sendMessage(to, 'Autorespond already active')
            else:
                settings['autoRespond']['status'] = True
                line.sendMessage(to, 'Success activated autorespond')
        elif texttl == 'off':
            if not settings['autoRespond']['status']:
                line.sendMessage(to, 'Autorespond already deactive')
            else:
                settings['autoRespond']['status'] = False
                line.sendMessage(to, 'Success deactivated autorespond')
        else:
            settings['autoRespond']['message'] = textt
            line.sendMessage(to, 'Success change autorespond message to `%s`' % textt)
    elif cmd.startswith('autoread '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['autoRead']:
                line.sendMessage(to, 'Autoread already active')
            else:
                settings['autoRead'] = True
                line.sendMessage(to, 'Success activated autoread')
        elif texttl == 'off':
            if not settings['autoRead']:
                line.sendMessage(to, 'Autoread already deactive')
            else:
                settings['autoRead'] = False
                line.sendMessage(to, 'Success deactivated autoread')
    elif cmd.startswith('checkcontact '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['checkContact']:
                line.sendMessage(to, 'Checkcontact already active')
            else:
                settings['checkContact'] = True
                line.sendMessage(to, 'Success activated checkcontact')
        elif texttl == 'off':
            if not settings['checkContact']:
                line.sendMessage(to, 'Checkcontact already deactive')
            else:
                settings['checkContact'] = False
                line.sendMessage(to, 'Success deactivated checkcontact')
    elif cmd.startswith('checkpost '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['checkPost']:
                line.sendMessage(to, 'Checkpost already active')
            else:
                settings['checkPost'] = True
                line.sendMessage(to, 'Success activated checkpost')
        elif texttl == 'off':
            if not settings['checkPost']:
                line.sendMessage(to, 'Checkpost already deactive')
            else:
                settings['checkPost'] = False
                line.sendMessage(to, 'Success deactivated checkpost')
    elif cmd == 'join':
        X = line.getGroup(msg.to)
        X.preventedJoinByTicket = False
        line.updateGroup(X)
        Ti = line.reissueGroupTicket(msg.to)
        line2.acceptGroupInvitationByTicket(msg.to,Ti)
        G = line2.getGroup(msg.to)
        G.preventedJoinByTicket = True
        line2.updateGroup(G)
    elif cmd == 'leave':
        line2.leaveGroup(to)
    elif cmd.startswith('checksticker '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['checkSticker']:
                line.sendMessage(to, 'Checksticker already active')
            else:
                settings['checkSticker'] = True
                line.sendMessage(to, 'Success activated checksticker')
        elif texttl == 'off':
            if not settings['checkSticker']:
                line.sendMessage(to, 'Checksticker already deactive')
            else:
                settings['checkSticker'] = False
                line.sendMessage(to, 'Success deactivated checksticker')
    elif cmd.startswith('copy '):
       _name = msg.text.replace("copy @","")
       _nametarget = _name.rstrip('  ')
       gs = line.getGroup(to)
       targets = []
       for g in gs.members:
           if _nametarget == g.displayName:
               targets.append(g.mid)
       if targets == []:
           line.sendMessage(to, "Not Found...")
       else:
           for target in targets:
                try:
                   line.CloneContactProfile(target)
                   line.sendMessage(to, "sᴜᴄᴄᴇs ᴄᴏᴘʏ ᴘʀᴏғɪʟᴇ")
                except Exception as e:
                    print(e)
    elif cmd.startswith('myprofile'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        profile = line.getProfile()
        res = '╭───「 My Profile 」'
        res += '\n├ MID : ' + profile.mid
        res += '\n├ Display Name : ' + str(profile.displayName)
        res += '\n├ Status Message : ' + str(profile.statusMessage)
        res += '\n├ Usage : '
        res += '\n│ • {key}MyProfile'
        res += '\n│ • {key}MyProfile MID'
        res += '\n│ • {key}MyProfile Name'
        res += '\n│ • {key}MyProfile Bio'
        res += '\n│ • {key}MyProfile Pict'
        res += '\n│ • {key}MyProfile Cover'
        res += '\n│ • {key}MyProfile Change Name <name>'
        res += '\n│ • {key}MyProfile Change Bio <bio>'
        res += '\n│ • {key}MyProfile Change Pict'
        res += '\n│ • {key}MyProfile Change Cover'
        res += '\n╰───「 ZeroDAYS 」'
        if cmd == 'myprofile':
            if profile.pictureStatus:
                line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + profile.pictureStatus)
            cover = line.getProfileCoverURL(profile.mid)
            line.sendImageWithURL(to, str(cover))
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'mid':
            line.sendMessage(to, '「 MID 」\n' + str(profile.mid))
        elif texttl == 'name':
            line.sendMessage(to, '「 Display Name 」\n' + str(profile.displayName))
        elif texttl == 'bio':
            line.sendMessage(to, '「 Status Message 」\n' + str(profile.statusMessage))
        elif texttl == 'pict':
            if profile.pictureStatus:
                path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                line.sendImageWithURL(to, path)
                line.sendMessage(to, '「 Picture Status 」\n' + path)
            else:
                line.sendMessage(to, 'Failed display picture status, user doesn\'t have a picture status')
        elif texttl == 'cover':
            cover = line.getProfileCoverURL(profile.mid)
            line.sendImageWithURL(to, str(cover))
            line.sendMessage(to, '「 Cover Picture 」\n' + str(cover))
        elif texttl.startswith('change '):
            texts = textt[7:]
            textsl = texts.lower()
            if textsl.startswith('name '):
                name = texts[5:]
                if len(name) <= 20:
                    profile.displayName = name
                    line.updateProfile(profile)
                    line.sendMessage(to, 'Success change display name, changed to `%s`' % name)
                else:
                    line.sendMessage(to, 'Failed change display name, the length of the name cannot be more than 20')
            elif textsl.startswith('bio '):
                bio = texts[4:]
                if len(bio) <= 500:
                    profile.statusMessage = bio
                    line.updateProfile(profile)
                    line.sendMessage(to, 'Success change status message, changed to `%s`' % bio)
                else:
                    line.sendMessage(to, 'Failed change status message, the length of the bio cannot be more than 500')
            elif textsl == 'pict':
                settings['changePictureProfile'] = True
                line.sendMessage(to, 'Please send the image to set in picture profile, type `{key}Abort` if want cancel it.\nFYI: Downloading images will fail if too long upload the image'.format(key=setKey.title()))
            elif textsl == 'cover':
                settings['changeCoverProfile'] = True
                line.sendMessage(to, 'Please send the image to set in cover profile, type `{key}Abort` if want cancel it.\nFYI: Downloading images will fail if too long upload the image'.format(key=setKey.title()))
            else:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('profile'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        profile = line.getContact(to) if msg.toType == 0 else None
        res = '╭───「 My Profile 」'
        if profile:
            res += '\n├ MID : ' + profile.mid
            res += '\n├ Display Name : ' + str(profile.displayName)
            if profile.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(profile.displayNameOverridden)
            res += '\n├ Status Message : ' + str(profile.statusMessage)
        res += '\n├ Usage : '
        res += '\n│ • {key}Profile'
        res += '\n│ • {key}Profile Mid'
        res += '\n│ • {key}Profile Name'
        res += '\n│ • {key}Profile Bio'
        res += '\n│ • {key}Profile Pict'
        res += '\n│ • {key}Profile Cover'
        res += '\n│ • {key}Profile Steal Profile <mention>'
        res += '\n│ • {key}Profile Steal Mid <mention>'
        res += '\n│ • {key}Profile Steal Name <mention>'
        res += '\n│ • {key}Profile Steal Bio <mention>'
        res += '\n│ • {key}Profile Steal Pict <mention>'
        res += '\n│ • {key}Profile Steal Cover <mention>'
        res += '\n╰───「 ZeroDAYS 」'
        if cmd == 'profile':
            if profile:
                if profile.pictureStatus:
                    line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + profile.pictureStatus)
                cover = line.getProfileCoverURL(profile.mid)
                line.sendImageWithURL(to, str(cover))
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'mid':
            if msg.toType != 0: return line.sendMessage(to, 'Failed display mid user, use this command only in personal chat')
            line.sendMessage(to, '「 MID 」\n' + str(profile.mid))
        elif texttl == 'name':
            if msg.toType != 0: return line.sendMessage(to, 'Failed display mid user, use this command only in personal chat')
            line.sendMessage(to, '「 Display Name 」\n' + str(profile.displayName))
        elif texttl == 'bio':
            if msg.toType != 0: return line.sendMessage(to, 'Failed display mid user, use this command only in personal chat')
            line.sendMessage(to, '「 Status Message 」\n' + str(profile.statusMessage))
        elif texttl == 'pict':
            if msg.toType != 0: return line.sendMessage(to, 'Failed display mid user, use this command only in personal chat')
            if profile.pictureStatus:
                path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                line.sendImageWithURL(to, path)
                line.sendMessage(to, '「 Picture Status 」\n' + path)
            else:
                line.sendMessage(to, 'Failed display picture status, user doesn\'t have a picture status')
        elif texttl == 'cover':
            if msg.toType != 0: return line.sendMessage(to, 'Failed display mid user, use this command only in personal chat')
            cover = line.getProfileCoverURL(profile.mid)
            line.sendImageWithURL(to, str(cover))
            line.sendMessage(to, '「 Cover Picture 」\n' + str(cover))
        elif texttl.startswith('steal '):
            texts = textt[6:]
            textsl = texts.lower()
            if textsl.startswith('profile '):
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    for mention in mentions['MENTIONEES']:
                        profile = line.getContact(mention['M'])
                        if profile.pictureStatus:
                            line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + profile.pictureStatus)
                        cover = line.getProfileCoverURL(profile.mid)
                        line.sendImageWithURL(to, str(cover))
                        res = '╭───「 Profile 」'
                        res += '\n├ MID : ' + profile.mid
                        res += '\n├ Display Name : ' + str(profile.displayName)
                        if profile.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(profile.displayNameOverridden)
                        res += '\n├ Status Message : ' + str(profile.statusMessage)
                        res += '\n╰───「 ZeroDAYS 」'
                        line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'Failed steal profile, no one user mentioned')
            elif textsl.startswith('mid '):
                res = '╭───「 MID 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        mid = mentions['MENTIONEES'][0]['M']
                        return line.sendMessage(to, '「 MID 」\n' + mid)
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        no += 1
                        res += '\n│ %i. %s' % (no, mid)
                    res += '\n╰───「 ZeroDAYS 」'
                    line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'Failed steal mid, no one user mentioned')
            elif textsl.startswith('name '):
                res = '╭───「 Display Name 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        profile = line.getContact(mentions['MENTIONEES'][0]['M'])
                        return line.sendMessage(to, '「 Display Name 」\n' + str(profile.displayName))
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        profile = line.getContact(mid)
                        no += 1
                        res += '\n│ %i. %s' % (no, profile.displayName)
                    res += '\n╰───「 ZeroDAYS 」'
                    line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'Failed steal display name, no one user mentioned')
            elif textsl.startswith('bio '):
                res = '╭───「 Status Message 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        profile = line.getContact(mentions['MENTIONEES'][0]['M'])
                        return line.sendMessage(to, '「 Status Message 」\n' + str(profile.statusMessage))
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        profile = line.getContact(mid)
                        no += 1
                        res += '\n│ %i. %s' % (no, profile.statusMessage)
                    res += '\n╰───「 ZeroDAYS 」'
                    line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'Failed steal status message, no one user mentioned')
            elif textsl.startswith('pict '):
                res = '╭───「 Picture Status 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        profile = line.getContact(mentions['MENTIONEES'][0]['M'])
                        if profile.pictureStatus:
                            path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                            line.sendImageWithURL(to, path)
                            return line.sendMessage(to, '「 Picture Status 」\n' + path)
                        else:
                            return line.sendMessage(to, 'Failed steal picture status, user `%s` doesn\'t have a picture status' % profile.displayName)
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        profile = line.getContact(mid)
                        no += 1
                        if profile.pictureStatus:
                            path = 'http://dl.profile.line-cdn.net/' + profile.pictureStatus
                            line.sendImageWithURL(to, path)
                            res += '\n│ %i. %s' % (no, path)
                        else:
                            res += '\n│ %i. Not Found' % no
                    res += '\n╰───「 ZeroDAYS 」'
                    line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'Failed steal picture status, no one user mentioned')
            elif textsl.startswith('cover '):
                res = '╭───「 Cover Picture 」'
                no = 0
                if 'MENTION' in msg.contentMetadata.keys():
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    if len(mentions['MENTIONEES']) == 1:
                        mid = mentions['MENTIONEES'][0]['M']
                        cover = line.getProfileCoverURL(mid)
                        line.sendImageWithURL(to, str(cover))
                        line.sendMessage(to, '「 Cover Picture 」\n' + str(cover))
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        no += 1
                        cover = line.getProfileCoverURL(mid)
                        line.sendImageWithURL(to, str(cover))
                        res += '\n│ %i. %s' % (no, cover)
                    res += '\n╰───「 ZeroDAYS 」'
                    line.sendMessage(to, parsingRes(res))
                else:
                    line.sendMessage(to, 'Failed steal cover picture, no one user mentioned')
            else:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('protect'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭───「 Protect 」'
        if settings['protect']:
            if settings['protect']['gr'] == True: res += "\n├ Group Protection : Active"
            else: res += "\n├ Group Protection : inActive"
            if settings['protect']['qr'] == True: res += "\n├ Group QR Protection : Active"
            else: res += "\n├ Group QR Protection : inActive"
            if settings['protect']['join'] == True: res += "\n├ Group Join Protection : Active"
            else: res += "\n├ Group Join Protection : inActive"
        res += '\n├ Usage : '
        res += '\n│ • {key}Protect <on/off>'
        res += '\n│ • {key}Protect QR <on/off>'
        res += '\n│ • {key}Protect Join <on/off>'
        res += '\n╰───「 ZeroDAYS 」'
        if cmd == 'protect':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['protect']['gr']:
                line.sendMessage(to, 'Group protector already active')
            else:
                settings['protect']['gr'] = True
                line.sendMessage(to, 'Success activated Group protector')
        elif texttl == 'off':
            if not settings['protect']['gr']:
                line.sendMessage(to, 'Group Protector already deactive')
            else:
                settings['protect']['gr'] = False
                line.sendMessage(to, 'Success deactivated Group protector')
    elif cmd.startswith('ban'):
        textt = removeCmd(text, setKey)
        textsl = textt.lower()
        res = '╭───「 Banned User 」\n'
        if settings['protect']['bl'] == {}:
            line.sendMessage(to, "There is no user in banlist")
        else:
            mc = ""
            for mi_d in settings['protect']['bl']:
                mc += "├≽ " + line.getContact(mi_d).displayName + "\n"
            res += mc
        res += '\n├ Usage : '
        res += '\n│ • {key}Ban'
        res += '\n│ • {key}Ban <add/del> <mention>'
        res += '\n╰───「 ZeroDAYS 」'
        if cmd == 'ban':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        if textsl.startswith('add '):
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = line.getContact(mention['M']).mid
                    if mid not in settings['protect']['bl']:
                       settings['protect']['bl'][mid] = True
                       line.sendMessage(to, "User successfuly banned by system")
                    else:
                        line.sendMessage(to, "User already in banned list")
            else:
                line.sendMessage(to, 'Failed ban user, no one user mentioned')
        elif textsl.startswith('del '):
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = line.getContact(mention['M']).mid
                    if mid not in settings['protect']['bl']:
                       del settings['protect']['bl'][mid]
                       line.sendMessage(to, "Banned user successfuly removed")
                    else:
                        line.sendMessage(to, "User are not a banned user before")
            else:
                line.sendMessage(to, 'Failed ban user, no one user mentioned')
        elif textsl == ('list'):
            if settings['protect']['bl'] == {}:
                line.sendMessage(to, "There is no user in banlist")
            else:
                mc = ""
                for mi_d in settings['protect']['bl']:
                    mc += "├≽ " + line.getContact(mi_d).displayName + "\n"
                line.sendMessage(to,"╭──「 Banlist 」\n"+mc+"╰──「 ZeroDAYs 」")
        elif textsl == ('clear'):
            if settings['protect']['bl'] == {}:
                line.sendMessage(to, "There is no user in banlist")
            else:
                settings['protect']['bl'] == {}
                line.sendMessage(to,"successfuly clear all banned user in system")
    elif cmd.startswith('protect qr '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['protect']['qr']:
                line.sendMessage(to, 'QR protect already active')
            else:
                settings['protect']['qr'] = True
                line.sendMessage(to, 'Success activated QR protector')
        elif texttl == 'off':
            if not settings['protect']['qr']:
                line.sendMessage(to, 'QR Protector already deactive')
            else:
                settings['protect']['qr'] = False
                line.sendMessage(to, 'Success deactivated QR protector')
    elif cmd.startswith('protect join '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['protect']['join']:
                line.sendMessage(to, 'Join protect already active')
            else:
                settings['protect']['join'] = True
                line.sendMessage(to, 'Success activated join protector')
        elif texttl == 'off':
            if not settings['protect']['join']:
                line.sendMessage(to, 'Join Protector already deactive')
            else:
                settings['protect']['join'] = False
                line.sendMessage(to, 'Success deactivated join protector')
    elif cmd.startswith('checkcontact '):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if texttl == 'on':
            if settings['checkContact']:
                line.sendMessage(to, 'Checkcontact already active')
            else:
                settings['checkContact'] = True
                line.sendMessage(to, 'Success activated checkcontact')
        elif texttl == 'off':
            if not settings['checkContact']:
                line.sendMessage(to, 'Checkcontact already deactive')
            else:
                settings['checkContact'] = False
                line.sendMessage(to, 'Success deactivated checkcontact')
    elif cmd.startswith("image coursel"):
        url = "https://i.pinimg.com/originals/fc/b7/a5/fcb7a59766ad30a4160cdebbba53e16b.gif"
        data = {
            "type": "template",
            "altText": "this is a image carousel template",
            "template": {
                "type": "image_carousel",
                "columns": [
                    {
                        "imageUrl": url,
                        "action": {
                            "type": "uri",
                            "uri": url
                        }
                    }
                ]
            }
        }
        line.postJungelpang(to, data)
    elif cmd.startswith('mimic'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        targets = ''
        if settings['mimic']['target']:
            no = 0
            for target, status in settings['mimic']['target'].items():
                no += 1
                try:
                    name = line.getContact(target).displayName
                except TalkException:
                    name = 'Unknown'
                targets += '\n│ %i. %s//%s' % (no, name, bool_dict[status][1])
        else:
            targets += '\n│ Nothing'
        res = '╭───「 Mimic 」'
        res += '\n├ Status : ' + bool_dict[settings['mimic']['status']][1]
        res += '\n├ List :'
        res += targets
        res += '\n├ Usage : '
        res += '\n│ • {key}Mimic'
        res += '\n│ • {key}Mimic <on/off>'
        res += '\n│ • {key}Mimic Reset'
        res += '\n│ • {key}Mimic Add <mention>'
        res += '\n│ • {key}Mimic Del <mention>'
        res += '\n╰───「 ZeroDAYS 」'
        if cmd == 'mimic':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl == 'on':
            if settings['mimic']['status']:
                line.sendMessage(to, 'Mimic already active')
            else:
                settings['mimic']['status'] = True
                line.sendMessage(to, 'Success activated mimic')
        elif texttl == 'off':
            if not settings['mimic']['status']:
                line.sendMessage(to, 'Mimic already deactive')
            else:
                settings['mimic']['status'] = False
                line.sendMessage(to, 'Success deactivated mimic')
        elif texttl == 'reset':
            settings['mimic']['target'] = {}
            line.sendMessage(to, 'Success reset mimic list')
        elif texttl.startswith('add '):
            res = '╭───「 Mimic 」'
            res += '\n├ Status : Add Target'
            res += '\n├ Added :'
            no = 0
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    settings['mimic']['target'][mid] = True
                    no += 1
                    try:
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                if no == 0: res += '\n│ Nothing'
                res += '\n╰───「 ZeroDAYS 」'
                line.sendMessage(to, res)
            else:
                line.sendMessage(to, 'Failed add mimic target, no one user mentioned')
        elif texttl.startswith('del '):
            res = '╭───「 Mimic 」'
            res += '\n├ Status : Del Target'
            res += '\n├ Deleted :'
            no = 0
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid in settings['mimic']['target']:
                        settings['mimic']['target'][mid] = False
                    no += 1
                    try:
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                if no == 0: res += '\n│ Nothing'
                res += '\n╰───「 ZeroDAYS 」'
                line.sendMessage(to, res)
            else:
                line.sendMessage(to, 'Failed del mimic target, no one user mentioned')
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('broadcast'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cond = textt.split(' ')
        res = '╭───「 Broadcast 」'
        res += '\n├ Broadcast Type : '
        res += '\n│ 1 : Friends'
        res += '\n│ 2 : Groups'
        res += '\n│ 0 : All'
        res += '\n├ Usage : '
        res += '\n│ • {key}Broadcast'
        res += '\n│ • {key}Broadcast <type> <message>'
        res += '\n╰───「 ZeroDAYS 」'
        if cmd == 'broadcast':
            line.sendMessage(to, parsingRes(res).format(key=setKey.title()))
        elif cond[0] == '1':
            if len(cond) < 2:
                return line.sendMessage(to, 'Failed broadcast, no message detected')
            res = '「 Broadcast 」\n'
            res += textt[2:]
            res += '\n\n「 ZeroDAYS 」'
            targets = line.getAllContactIds()
            for target in targets:
                try:
                    line.sendMessage(target, res)
                except TalkException:
                    targets.remove(target)
                    continue
                time.sleep(0.8)
            line.sendMessage(to, 'Success broadcast to all friends, sent to %i friends' % len(targets))
        elif cond[0] == '2':
            if len(cond) < 2:
                return line.sendMessage(to, 'Failed broadcast, no message detected')
            res = '「 Broadcast 」\n'
            res += textt[2:]
            res += '\n\n「 ZeroDAYS 」'
            targets = line.getGroupIdsJoined()
            for target in targets:
                try:
                    line.sendMessage(target, res)
                except TalkException:
                    targets.remove(target)
                    continue
                time.sleep(0.8)
            line.sendMessage(to, 'Success broadcast to all groups, sent to %i groups' % len(targets))
        elif cond[0] == '0':
            if len(cond) < 2:
                return line.sendMessage(to, 'Failed broadcast, no message detected')
            res = '「 Broadcast 」\n'
            res += textt[2:]
            res += '\n\n「 ZeroDAYS 」'
            targets = line.getGroupIdsJoined() + line.getAllContactIds()
            for target in targets:
                try:
                    line.sendMessage(target, res)
                except TalkException:
                    targets.remove(target)
                    continue
                time.sleep(0.8)
            line.sendMessage(to, 'Success broadcast to all groups and friends, sent to %i groups and friends' % len(targets))
        else:
            line.sendMessage(to, parsingRes(res).format(key=setKey.title()))
    elif cmd == 'gift':
        line.sendMessage(to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '5'}, contentType=9)
    elif cmd.startswith('friendlist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cids = line.getAllContactIds()
        cids.sort()
        cnames = []
        ress = []
        res = '╭───「 Friend List 」'
        res += '\n├ List:'
        if cids:
            contacts = []
            no = 0
            if len(cids) > 200:
                parsed_len = len(cids)//200+1
                for point in range(parsed_len):
                    for cid in cids[point*200:(point+1)*200]:
                        try:
                            contact = line.getContact(cid)
                            contacts.append(contact)
                        except TalkException:
                            cids.remove(cid)
                            continue
                        no += 1
                        res += '\n│ %i. %s' % (no, contact.displayName)
                        cnames.append(contact.displayName)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for cid in cids:
                    try:
                        contact = line.getContact(cid)
                        contacts.append(contact)
                    except TalkException:
                        cids.remove(cid)
                        continue
                    no += 1
                    res += '\n│ %i. %s' % (no, contact.displayName)
                    cnames.append(contact.displayName)
        else:
            res += '\n│ Nothing'
        res += '\n├ Usage : '
        res += '\n│ • {key}FriendList'
        res += '\n│ • {key}FriendList Info <num/name>'
        res += '\n│ • {key}FriendList Add <mention>'
        res += '\n│ • {key}FriendList Del <mention/num/name/all>'
        res += '\n╰───「 ZeroDAYS 」'
        ress.append(res)
        if cmd == 'friendlist':
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('info '):
            texts = textt[5:].split(', ')
            if not cids:
                return line.sendMessage(to, 'Failed display info friend, nothing friend in list')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.pictureStatus:
                        line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL(contact.mid)
                    line.sendImageWithURL(to, str(cover))
                    res = '╭───「 Contact Info 」'
                    res += '\n├ MID : ' + contact.mid
                    res += '\n├ Display Name : ' + str(contact.displayName)
                    if contact.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(contact.displayNameOverridden)
                    res += '\n├ Status Message : ' + str(contact.statusMessage)
                    res += '\n╰───「 ZeroDAYS 」'
                    line.sendMessage(to, parsingRes(res))
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.pictureStatus:
                            line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                        cover = line.getProfileCoverURL(contact.mid)
                        line.sendImageWithURL(to, str(cover))
                        res = '╭───「 Contact Info 」'
                        res += '\n├ MID : ' + contact.mid
                        res += '\n├ Display Name : ' + str(contact.displayName)
                        if contact.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(contact.displayNameOverridden)
                        res += '\n├ Status Message : ' + str(contact.statusMessage)
                        res += '\n╰───「 ZeroDAYS 」'
                        line.sendMessage(to, parsingRes(res))

        elif texttl.startswith('add '):
            res = '╭───「 Friend List 」'
            res += '\n├ Status : Add Friend'
            res += '\n├ Added :'
            no = 0
            added = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid in cids or mid in added:
                        continue
                    no += 1
                    try:
                        line.findAndAddContactsByMid(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    added.append(mid)
                if no == 0: res += '\n│ Nothing'
                res += '\n╰───「 ZeroDAYS 」'
                line.sendMessage(to, res)
            else:
                line.sendMessage(to, 'Failed add contact to friend list, no one user mentioned')
        elif texttl.startswith('del '):
            texts = textt[4:].split(', ')
            if not cids:
                return line.sendMessage(to, 'Failed del contact from friend list, nothing friend in list')
            res = '╭───「 Friend List 」'
            res += '\n├ Status : Del Friend'
            res += '\n├ Deleted :'
            no = 0
            deleted = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid not in cids or mid in deleted:
                        continue
                    no += 1
                    try:
                        line.deleteContact(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    deleted.append(mid)
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.mid not in cids and contact.mid in deleted:
                        continue
                    no += 1
                    try:
                        line.deleteContact(contact.mid)
                        name = contact.displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    deleted.append(contact.mid)
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.mid not in cids and contact.mid in deleted:
                            continue
                        no += 1
                        try:
                            line.deleteContact(contact.mid)
                            name = contact.displayName
                        except TalkException:
                            name = 'Unknown'
                        res += '\n│ %i. %s' % (no, name)
                        deleted.append(contact.mid)
                elif texxt.lower() == 'all':
                    for contact in contacts:
                        if contact.mid not in cids and contact.mid in deleted:
                            continue
                        no += 1
                        try:
                            line.deleteContact(contact.mid)
                            name = contact.displayName
                        except TalkException:
                            name = 'Unknown'
                        res += '\n│ %i. %s' % (no, name)
                        deleted.append(contact.mid)
                        time.sleep(0.8)
            if no == 0: res += '\n│ Nothing'
            res += '\n╰───「 ZeroDAYS 」'
            line.sendMessage(to, res)
        else:
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('blocklist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        cids = line.getBlockedContactIds()
        cids.sort()
        cnames = []
        ress = []
        res = '╭───「 Block List 」'
        res += '\n├ List:'
        if cids:
            contacts = []
            no = 0
            if len(cids) > 200:
                parsed_len = len(cids)//200+1
                for point in range(parsed_len):
                    for cid in cids[point*200:(point+1)*200]:
                        try:
                            contact = line.getContact(cid)
                            contacts.append(contact)
                        except TalkException:
                            cids.remove(cid)
                            continue
                        no += 1
                        res += '\n│ %i. %s' % (no, contact.displayName)
                        cnames.append(contact.displayName)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for cid in cids:
                    try:
                        contact = line.getContact(cid)
                        contacts.append(contact)
                    except TalkException:
                        cids.remove(cid)
                        continue
                    no += 1
                    res += '\n│ %i. %s' % (no, contact.displayName)
                    cnames.append(contact.displayName)
        else:
            res += '\n│ Nothing'
        res += '\n├ Usage : '
        res += '\n│ • {key}BlockList'
        res += '\n│ • {key}BlockList Info <num/name>'
        res += '\n│ • {key}BlockList Add <mention>'
        res += '\n│ • {key}BlockList Del <mention/num/name/all>'
        res += '\n╰───「 ZeroDAYS 」'
        ress.append(res)
        if cmd == 'blocklist':
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('info '):
            texts = textt[5:].split(', ')
            if not cids:
                return line.sendMessage(to, 'Failed display info blocked user, nothing user in list')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.pictureStatus:
                        line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL(contact.mid)
                    line.sendImageWithURL(to, str(cover))
                    res = '╭───「 Contact Info 」'
                    res += '\n├ MID : ' + contact.mid
                    res += '\n├ Display Name : ' + str(contact.displayName)
                    if contact.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(contact.displayNameOverridden)
                    res += '\n├ Status Message : ' + str(contact.statusMessage)
                    res += '\n╰───「 ZeroDAYS 」'
                    line.sendMessage(to, parsingRes(res))
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.pictureStatus:
                            line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                        cover = line.getProfileCoverURL(contact.mid)
                        line.sendImageWithURL(to, str(cover))
                        res = '╭───「 Contact Info 」'
                        res += '\n├ MID : ' + contact.mid
                        res += '\n├ Display Name : ' + str(contact.displayName)
                        if contact.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(contact.displayNameOverridden)
                        res += '\n├ Status Message : ' + str(contact.statusMessage)
                        res += '\n╰───「 ZeroDAYS 」'
                        line.sendMessage(to, parsingRes(res))
        elif texttl.startswith('add '):
            res = '╭───「 Block List 」'
            res += '\n├ Status : Add Block'
            res += '\n├ Added :'
            no = 0
            added = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid in cids or mid in added:
                        continue
                    no += 1
                    try:
                        line.blockContact(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    added.append(mid)
                if no == 0: res += '\n│ Nothing'
                res += '\n╰───「 ZeroDAYS 」'
                line.sendMessage(to, res)
            else:
                line.sendMessage(to, 'Failed block contact, no one user mentioned')
        elif texttl.startswith('del '):
            texts = textt[4:].split(', ')
            if not cids:
                return line.sendMessage(to, 'Failed unblock contact, nothing user in list')
            res = '╭───「 Block List 」'
            res += '\n├ Status : Del Block'
            res += '\n├ Deleted :'
            no = 0
            deleted = []
            if 'MENTION' in msg.contentMetadata.keys():
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid not in cids or mid in deleted:
                        continue
                    no += 1
                    try:
                        line.unblockContact(mid)
                        name = line.getContact(mid).displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    deleted.append(mid)
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    contact = contacts[num - 1]
                    if contact.mid not in cids and contact.mid in deleted:
                        continue
                    no += 1
                    try:
                        line.unblockContact(contact.mid)
                        name = contact.displayName
                    except TalkException:
                        name = 'Unknown'
                    res += '\n│ %i. %s' % (no, name)
                    deleted.append(contact.mid)
                elif name != None:
                    if name in cnames:
                        contact = contacts[cnames.index(name)]
                        if contact.mid not in cids and contact.mid in deleted:
                            continue
                        no += 1
                        try:
                            line.unblockContact(contact.mid)
                            name = contact.displayName
                        except TalkException:
                            name = 'Unknown'
                        res += '\n│ %i. %s' % (no, name)
                        deleted.append(contact.mid)
                elif texxt.lower() == 'all':
                    for contact in contacts:
                        if contact.mid not in cids and contact.mid in deleted:
                            continue
                        no += 1
                        try:
                            line.unblockContact(contact.mid)
                            name = contact.displayName
                        except TalkException:
                            name = 'Unknown'
                        res += '\n│ %i. %s' % (no, name)
                        deleted.append(contact.mid)
                        time.sleep(0.8)
            if no == 0: res += '\n│ Nothing'
            res += '\n╰───「 ZeroDAYS 」'
            line.sendMessage(to, res)
        else:
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd == 'mentionall':
        members = []
        if msg.toType == 1:
            room = line.getCompactRoom(to)
            members = [mem.mid for mem in room.contacts]
        elif msg.toType == 2:
            group = line.getCompactGroup(to)
            members = [mem.mid for mem in group.members]
        else:
            return line.sendMessage(to, 'Failed mentionall members, use this command only on room or group chat')
        if members:
            mentionMembers(to, members)
    elif cmd == 'groupinfo':
        if msg.toType != 2: return line.sendMessage(to, 'Failed display group info, use this command only on group chat')
        group = line.getCompactGroup(to)
        try:
            ccreator = group.creator.mid
            gcreator = group.creator.displayName
        except:
            ccreator = None
            gcreator = 'Not found'
        if not group.invitee:
            pendings = 0
        else:
            pendings = len(group.invitee)
        qr = 'Close' if group.preventedJoinByTicket else 'Open'
        if group.preventedJoinByTicket:
            ticket = 'Not found'
        else:
            ticket = 'https://line.me/R/ti/g/' + str(line.reissueGroupTicket(group.id))
        created = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(group.createdTime) / 1000))
        path = 'http://dl.profile.line-cdn.net/' + group.pictureStatus
        res = '╭───「 Group Info 」'
        res += '\n├ ID : ' + group.id
        res += '\n├ Name : ' + group.name
        res += '\n├ Creator : ' + gcreator
        res += '\n├ Created Time : ' + created
        res += '\n├ Member Count : ' + str(len(group.members))
        res += '\n├ Pending Count : ' + str(pendings)
        res += '\n├ QR Status : ' + qr
        res += '\n├ Ticket : ' + ticket
        res += '\n╰───「 ZeroDAYS 」'
        line.sendImageWithURL(to, path)
        if ccreator:
            line.sendContact(to, ccreator)
        line.sendMessage(to, res)
    elif cmd.startswith('grouplist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        gids = line.getGroupIdsJoined()
        gnames = []
        ress = []
        res = '╭───「 Group List 」'
        res += '\n├ List:'
        if gids:
            groups = line.getGroups(gids)
            no = 0
            if len(groups) > 200:
                parsed_len = len(groups)//200+1
                for point in range(parsed_len):
                    for group in groups[point*200:(point+1)*200]:
                        no += 1
                        res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                        gnames.append(group.name)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for group in groups:
                    no += 1
                    res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                    gnames.append(group.name)
        else:
            res += '\n│ Nothing'
        res += '\n├ Usage : '
        res += '\n│ • {key}GroupList'
        res += '\n│ • {key}GroupList Leave <num/name/all>'
        res += '\n╰───「 ZeroDAYS 」'
        ress.append(res)
        if cmd == 'grouplist':
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('leave '):
            texts = textt[6:].split(', ')
            leaved = []
            if not gids:
                return line.sendMessage(to, 'Failed leave group, nothing group in list')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    if num <= len(groups) and num > 0:
                        group = groups[num - 1]
                        if group.id in leaved:
                            line.sendMessage(to, 'Already leave group %s' % group.name)
                            continue
                        line.leaveGroup(group.id)
                        leaved.append(group.id)
                        if to not in leaved:
                            line.sendMessage(to, 'Success leave group %s' % group.name)
                    else:
                        line.sendMessage(to, 'Failed leave group number %i, number out of range' % num)
                elif name != None:
                    if name in gnames:
                        group = groups[gnames.index(name)]
                        if group.id in leaved:
                            line.sendMessage(to, 'Already leave group %s' % group.name)
                            continue
                        line.leaveGroup(group.id)
                        leaved.append(group.id)
                        if to not in leaved:
                            line.sendMessage(to, 'Success leave group %s' % group.name)
                    else:
                        line.sendMessage(to, 'Failed leave group with name `%s`, name not in list' % name)
                elif texxt.lower() == 'all':
                    for gid in gids:
                        if gid in leaved:
                            continue
                        line.leaveGroup(gid)
                        leaved.append(gid)
                        time.sleep(0.8)
                    if to not in leaved:
                        line.sendMessage(to, 'Success leave all group')
        else:
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('invitationlist'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        gids = line.getGroupIdsInvited()
        gnames = []
        ress = []
        res = '╭───「 Invitation List 」'
        res += '\n├ List:'
        if gids:
            groups = line.getGroups(gids)
            no = 0
            if len(groups) > 200:
                parsed_len = len(groups)//200+1
                for point in range(parsed_len):
                    for group in groups[point*200:(point+1)*200]:
                        no += 1
                        res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                        gnames.append(group.name)
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        if point != parsed_len - 1:
                            ress.append(res)
                    if point != parsed_len - 1:
                        res = ''
            else:
                for group in groups:
                    no += 1
                    res += '\n│ %i. %s//%i' % (no, group.name, len(group.members))
                    gnames.append(group.name)
        else:
            res += '\n│ Nothing'
        res += '\n├ Usage : '
        res += '\n│ • {key}InvitationList'
        res += '\n│ • {key}InvitationList Accept <num/name/all>'
        res += '\n│ • {key}InvitationList Reject <num/name/all>'
        res += '\n╰───「 ZeroDAYS 」'
        ress.append(res)
        if cmd == 'invitationlist':
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('accept '):
            texts = textt[7:].split(', ')
            accepted = []
            if not gids:
                return line.sendMessage(to, 'Failed accept group, nothing invitation group in list')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    if num <= len(groups) and num > 0:
                        group = groups[num - 1]
                        if group.id in accepted:
                            line.sendMessage(to, 'Already accept group %s' % group.name)
                            continue
                        line.acceptGroupInvitation(group.id)
                        accepted.append(group.id)
                        line.sendMessage(to, 'Success accept group %s' % group.name)
                    else:
                        line.sendMessage(to, 'Failed accept group number %i, number out of range' % num)
                elif name != None:
                    if name in gnames:
                        group = groups[gnames.index(name)]
                        if group.id in accepted:
                            line.sendMessage(to, 'Already accept group %s' % group.name)
                            continue
                        line.acceptGroupInvitation(group.id)
                        accepted.append(group.id)
                        line.sendMessage(to, 'Success accept group %s' % group.name)
                    else:
                        line.sendMessage(to, 'Failed accept group with name `%s`, name not in list' % name)
                elif texxt.lower() == 'all':
                    for gid in gids:
                        if gid in accepted:
                            continue
                        line.acceptGroupInvitation(group.id)
                        accepted.append(group.id)
                        time.sleep(0.8)
                    line.sendMessage(to, 'Success accept all invitation group')
        elif texttl.startswith('reject '):
            texts = textt[7:].split(', ')
            rejected = []
            if not gids:
                return line.sendMessage(to, 'Failed reject group, nothing invitation group in list')
            for texxt in texts:
                num = None
                name = None
                try:
                    num = int(texxt)
                except ValueError:
                    name = texxt
                if num != None:
                    if num <= len(groups) and num > 0:
                        group = groups[num - 1]
                        if group.id in rejected:
                            line.sendMessage(to, 'Already reject group %s' % group.name)
                            continue
                        line.acceptGroupInvitation(group.id)
                        rejected.append(group.id)
                        line.sendMessage(to, 'Success reject group %s' % group.name)
                    else:
                        line.sendMessage(to, 'Failed reject group number %i, number out of range' % num)
                elif name != None:
                    if name in gnames:
                        group = groups[gnames.index(name)]
                        if group.id in rejected:
                            line.sendMessage(to, 'Already reject group %s' % group.name)
                            continue
                        line.acceptGroupInvitation(group.id)
                        rejected.append(group.id)
                        line.sendMessage(to, 'Success reject group %s' % group.name)
                    else:
                        line.sendMessage(to, 'Failed reject group with name `%s`, name not in list' % name)
                elif texxt.lower() == 'all':
                    for gid in gids:
                        if gid in rejected:
                            continue
                        line.acceptGroupInvitation(group.id)
                        rejected.append(group.id)
                        time.sleep(0.8)
                    line.sendMessage(to, 'Success reject all invitation group')
        else:
            for res in ress:
                line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd == 'memberlist':
        if msg.toType == 1:
            room = line.getRoom(to)
            members = room.contacts
        elif msg.toType == 2:
            group = line.getGroup(to)
            members = group.members
        else:
            return line.sendMessage(to, 'Failed display member list, use this command only on room or group chat')
        if not members:
            return line.sendMessage(to, 'Failed display member list, no one contact')
        res = '╭───「 Member List 」'
        parsed_len = len(members)//200+1
        no = 0
        for point in range(parsed_len):
            for member in members[point*200:(point+1)*200]:
                no += 1
                res += '\n│ %i. %s' % (no, member.displayName)
                if member == members[-1]:
                    res += '\n╰───「 ZeroDAYS 」'
            if res:
                if res.startswith('\n'): res = res[1:]
                line.sendMessage(to, res)
            res = ''
    elif cmd == 'pendinglist':
        if msg.toType != 2: return line.sendMessage(to, 'Failed display pending list, use this command only on group chat')
        group = line.getGroup(to)
        members = group.members
        if not members:
            return line.sendMessage(to, 'Failed display pending list, no one contact')
        res = '╭───「 Pending List 」'
        parsed_len = len(members)//200+1
        no = 0
        for point in range(parsed_len):
            for member in members[point*200:(point+1)*200]:
                no += 1
                res += '\n│ %i. %s' % (no, member.displayName)
                if member == members[-1]:
                    res += '\n╰───「 ZeroDAYS 」'
            if res:
                if res.startswith('\n'): res = res[1:]
                line.sendMessage(to, res)
            res = ''
    elif cmd == 'openqr':
        if msg.toType != 2: return line.sendMessage(to, 'Failed open qr, use this command only on group chat')
        group = line.getCompactGroup(to)
        group.preventedJoinByTicket = False
        line.updateGroup(group)
        line.sendMessage(to, 'Success open group qr, you must be careful')
    elif cmd == 'closeqr':
        if msg.toType != 2: return line.sendMessage(to, 'Failed close qr, use this command only on group chat')
        group = line.getCompactGroup(to)
        group.preventedJoinByTicket = True
        line.updateGroup(group)
        line.sendMessage(to, 'Success close group qr')
    elif cmd.startswith('changegroupname '):
        if msg.toType != 2: return line.sendMessage(to, 'Failed change group name, use this command only on group chat')
        group = line.getCompactGroup(to)
        gname = removeCmd(text, setKey)
        if len(gname) > 50:
            return line.sendMessage(to, 'Failed change group name, the number of names cannot exceed 50')
        group.name = gname
        line.updateGroup(group)
        line.sendMessage(to, 'Success change group name to `%s`' % gname)
    elif cmd == 'changegrouppict':
        if msg.toType != 2: return line.sendMessage(to, 'Failed change group picture, use this command only on group chat')
        if to not in settings['changeGroupPicture']:
            settings['changeGroupPicture'].append(to)
            line.sendMessage(to, 'Please send the image, type `{key}Abort` if want cancel it.\nFYI: Downloading images will fail if too long upload the image'.format(key=setKey.title()))
        else:
            line.sendMessage(to, 'Command already active, please send the image or type `{key}Abort` if want cancel it.\nFYI: Downloading images will fail if too long upload the image'.format(key=setKey.title()))
    elif cmd == 'kickall':
        if msg.toType != 2: return line.sendMessage(to, 'Failed kick all members, use this command only on group chat')
        group = line.getCompactGroup(to)
        if not group.members:
            return line.sendMessage(to, 'Failed kick all members, no member in list')
        for member in group.members:
            if member.mid == myMid:
                continue
            try:
                line.kickoutFromGroup(to, [member.mid])
            except TalkException as talk_error:
                return line.sendMessage(to, 'Failed kick all members, the reason is `%s`' % talk_error.reason)
            time.sleep(0.8)
        line.sendMessage(to, 'Success kick all members, totals %i members' % len(group.members))
    elif cmd.startswith("unsend "):
	    sep = text.split(" ")
	    args = text.replace(sep[0] + " ","")
	    mes = int(sep[1])
	    M = line.getRecentMessages(to, 1001)
	    MId = []
	    for ind,i in enumerate(M):
	    	if ind == 0:
	    		pass
	    	else:
	    		if i._from == client.profile.mid:
	    			MId.append(i.id)
	    			if len(MId) == mes:
	    				break
	    def unsMes(id):
	    	line.unsendMessage(id)
	    for i in MId:
	    	thread1 = threading.Thread(target=unsMes, args=(i,))
	    	thread1.daemon = True
	    	thread1.start()
	    	thread1.join()
	    line.sendMessage(to, "「UNSEND」\nSuccess unsend {} message.".format(len(MId)))

    elif cmd == 'cancelall':
        if msg.toType != 2: return line.sendMessage(to, 'Failed cancel all pending members, use this command only on group chat')
        group = line.getCompactGroup(to)
        if not group.invitee:
            return line.sendMessage(to, 'Failed cancel all pending members, no pending member in list')
        for member in group.invitee:
            if member.mid == myMid:
                continue
            try:
                line.cancelGroupInvitation(to, [member.mid])
            except TalkException as talk_error:
                return line.sendMessage(to, 'Failed cancel all pending members, the reason is `%s`' % talk_error.reason)
            time.sleep(0.8)
        line.sendMessage(to, 'Success cancel all pending members, totals %i pending members' % len(pendings))

    #==============================#
    #========MEDIA SECTION=========#
    #==============================#

    elif cmd.startswith("praytime"):
        a = 'Peta Lokasi'
        c = 'https://png.pngtree.com/element_pic/16/12/02/51e6452ca365f618ab4b723c7aa18be9.jpg'
        separate = msg.text.split(" ")
        location = msg.text.replace(separate[0] + " ","")
        r = requests.get("https://rest.farzain.com/api/shalat.php?apikey=Aovsyfk9UmvCAag1w5rupglGb&id={}".format(location))
        data = r.text
        data = json.loads(data)
        tz = pytz.timezone("Asia/Makassar")
        timeNow = datetime.now(tz=tz)
        if data["status"] == "success":
            ret_ = "╭───「 Praytime for  " + str(location) + " 」"
            ret_ += "\n├≽ Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
            ret_ += "\n├≽ Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
            ret_ += "\n├≽ Shubuh : " + data['respon']['shubuh']
            ret_ += "\n├≽ Dzuhur " + data['respon']['dzuhur']
            ret_ += "\n├≽ Ashar " + data['respon']['ashar']
            ret_ += "\n├≽ Maghrib " + data['respon']['maghrib']
            ret_ += "\n├≽ Isya " + data['respon']['isya']
            ret_ += "\n╰───「 ZeroDAYs x Hello World 」"
            line.sendImageWithURL(to,data['peta_gambar'])
            line.sendMessage(to, str(ret_))

    elif cmd.startswith("gambar"):
        try:
            separate = msg.text.split(" ")
            search = msg.text.replace(separate[0] + " ","")
            r = requests.get("https://rest.farzain.com/api/gambarg.php?apikey=Aovsyfk9UmvCAag1w5rupglGb&id={}".format(search))
            data = r.text
            data = json.loads(data)
            if data["status"] == "success":
                line.sendImageWithURL(to,data['url'])
            else:
                line.sendMessage(to,'Parameter Error!')
        except Exception as error:
            line.sendMessage(to, str(error))
    elif cmd.startswith("weather"):
        try:
            sep = text.split(" ")
            location = text.replace(sep[0] + " ","")
            r = requests.get("https://rest.farzain.com/api/cuaca.php?apikey=Aovsyfk9UmvCAag1w5rupglGb&id={}".format(location))
            data = r.text
            data = json.loads(data)
            tz = pytz.timezone("Asia/Jakarta")
            timeNow = datetime.now(tz=tz)
            if data["status"] == "success":
                ret_ = "╭───「 Cuaca 」"
                ret_ += "\n├≽ Weather status : " + data['respon']['cuaca'].replace("Kondisi cuaca ","")
                ret_ += "\n├≽ Location : " + data['respon']['tempat'].replace("Temperatur di kota ","")
                ret_ += "\n├≽ Temp : " + data['respon']['suhu'].replace("Suhu : ","") + "°C"
                ret_ += "\n├≽ Moisture : " + data['respon']['kelembapan'].replace("Kelembaban : ","") + "%"
                ret_ += "\n├≽ Air pressure : " + data['respon']['udara'].replace("Tekanan udara : ","") + "HPa"
                ret_ += "\n├≽ Wind speed : " + data['respon']['angin'].replace("Kecepatan angin : ","") + "m/s"
                ret_ += "\n├──「 Time Status 」"
                ret_ += "\n├≽ Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                ret_ += "\n├≽ Jam : " + datetime.strftime(timeNow,'%H:%M:%S') + " WIB"
                ret_ += "\n╰───「 ZeroDAYs x Hello World 」"
                line.sendMessage(to, str(ret_))
        except Exception as error:
            line.sendMessage(to, str(error))
    elif cmd.startswith("gambar"):
        try:
            separate = msg.text.split(" ")
            search = msg.text.replace(separate[0] + " ","")
            r = requests.get("https://rest.farzain.com/api/gambarg.php?apikey=Aovsyfk9UmvCAag1w5rupglGb&id={}".format(search))
            data = r.text
            data = json.loads(data)
            if data["status"] == "success":
                line.sendImageWithURL(to,data['url'])
            else:
                line.sendMessage(to,'Failed to get data')
        except Exception as error:
            line.sendMessage(to, str(error))
    elif cmd == "samehadaku":
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        list,no="[ Samehadaku Update ]\n\n",1
        for anime in data.findAll("li",class_="post-item tie-standard"):
            link=anime.a.get("href")
            title=anime.a.get("title").split("Subtitle")[0]
            list+="{}. {}\n".format(no,title)
            no+=1
            animes.append({"title":title,"link":link})
        list+="\n[ Finish ]\nUntuk melihat link download anime, silahkan klik : \n{key}samehadaku download <number> "
        line.sendMessage(to, parsingRes(list).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('download '):
        print("testing")
        sep = text.split(" ")
        search = text.replace(sep[0] + " ","")
        data,no,animes=bs("https://samehadaku.tv"),1,[]
        list,no="[ Samehadaku Update ]\n\n",1
        for anime in data.findAll("li",class_="post-item tie-standard"):
            link=anime.a.get("href")
            title=anime.a.get("title").split("Subtitle")[0]
            list+="{}. {}\n".format(no,title)
            no+=1
            animes.append({"title":title,"link":link})
            a = search
            z = bs(animes[a-1]["link"]).find("div",class_="download-eps").findAll("li")
            links=[]
            for linkk in z:
                links.append({linkk.strong.text:[{"link":linkx.get("href"),"via":linkx.text} for linkx in linkk.findAll("a")][:5]})
                if len(links) >= 4:
                    del links[0];del links[1]
                elif len(links[0]) >= 5:
                    links[0] = links[0][:5]
                print(json.dumps(links,indent=4))
                line.sendMessage(to,json.dumps(links,indent=4))
    elif cmd.startswith("ig"):
        try:
            sep = text.split(" ")
            search = text.replace(sep[0] + " ","")
            r = requests.get("https://rest.farzain.com/api/ig_profile.php?apikey=Aovsyfk9UmvCAag1w5rupglGb&id={}".format(search))
            data = r.text
            data = json.loads(data)
            if data != []:
                ret_ = "╭───「 Instagram Profile 」"
                ret_ += "\n├≽ Nama : {}".format(str(data["info"]["full_name"]))
                ret_ += "\n├≽ Username : {}".format(str(data["info"]["username"]))
                ret_ += "\n├≽ Bio : {}".format(str(data["info"]["bio"]))
                ret_ += "\n├≽ Pengikut : {}".format(str(data["count"]["followers"]))
                ret_ += "\n├≽ Diikuti : {}".format(str(data["count"]["following"]))
                ret_ += "\n├≽ Total Post : {}".format(str(data["count"]["post"]))
                ret_ += "\n├≽ [ https://www.instagram.com/{} ]".format(search)
                ret_ += "╰───「 ZeroDAYs x Hello World 」"
                path = data["info"]["profile_pict"]
                line.sendImageWithURL(to, str(path))
                line.sendMessage(to, str(ret_))
        except Exception as error:
            line.sendMessage(to, str(error))
    elif cmd.startswith('lurk'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        if msg.toType in [1, 2] and to not in lurking:
            lurking[to] = {
                'status': False,
                'time': None,
                'members': [],
                'reply': {
                    'status': False,
                    'message': settings['defaultReplyReader']
                }
            }
        res = '╭───「 Lurking 」'
        if msg.toType in [1, 2]: res += '\n├ Status : ' + bool_dict[lurking[to]['status']][1]
        if msg.toType in [1, 2]: res += '\n├ Reply Reader : ' + bool_dict[lurking[to]['reply']['status']][1]
        if msg.toType in [1, 2]: res += '\n├ Reply Reader Message : ' + lurking[to]['reply']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}Lurk'
        res += '\n│ • {key}Lurk <on/off>'
        res += '\n│ • {key}Lurk Result'
        res += '\n│ • {key}Lurk Reset'
        res += '\n│ • {key}Lurk ReplyReader <on/off>'
        res += '\n│ • {key}Lurk ReplyReader <message>'
        res += '\n╰───「 ZeroDAYS 」'
        if cmd == 'lurk':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif msg.toType not in [1, 2]:
            return line.sendMessage(to, 'Failed execute command lurking, use this command only on room or group chat')
        elif texttl == 'on':
            if lurking[to]['status']:
                line.sendMessage(to, 'Lurking already active')
            else:
                lurking[to].update({
                    'status': True,
                    'time': datetime.now(tz=pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%d %H:%M:%S'),
                    'members': []
                })
                line.sendMessage(to, 'Success activated lurking')
        elif texttl == 'off':
            if not lurking[to]['status']:
                line.sendMessage(to, 'Lurking already deactive')
            else:
                lurking[to].update({
                    'status': False,
                    'time': None,
                    'members': []
                })
                line.sendMessage(to, 'Success deactivated lurking')
        elif texttl == 'result':
            if not lurking[to]['status']:
                line.sendMessage(to, 'Failed display lurking result, lurking has not been activated')
            else:
                if not lurking[to]['members']:
                    line.sendMessage(to, 'Failed display lurking result, no one members reading')
                else:
                    members = lurking[to]['members']
                    res = '╭───「 Lurking 」'
                    if msg.toType == 2: res += '\n├ Group Name : ' + line.getGroup(to).name
                    parsed_len = len(members)//200+1
                    no = 0
                    for point in range(parsed_len):
                        for member in members[point*200:(point+1)*200]:
                            no += 1
                            try:
                                name = line.getContact(member).displayName
                            except TalkException:
                                name = 'Unknown'
                            res += '\n│ %i. %s' % (no, name)
                            if member == members[-1]:
                                res += '\n│'
                                res += '\n├ Time Set : ' + lurking[to]['time']
                                res += '\n╰───「 ZeroDAYS 」'
                        if res:
                            if res.startswith('\n'): res = res[1:]
                            line.sendMessage(to, res)
                        res = ''
        elif texttl == 'reset':
            if not lurking[to]['status']:
                line.sendMessage(to, 'Failed reset lurking, lurking has not been activated')
            else:
                lurking[to].update({
                    'status': True,
                    'time': datetime.now(tz=pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%d %H:%M:%S'),
                    'members': []
                })
                line.sendMessage(to, 'Success resetted lurking')
        elif texttl.startswith('replyreader '):
            texts = textt[12:]
            if texts == 'on':
                if lurking[to]['reply']['status']:
                    line.sendMessage(to, 'Reply reader already active')
                else:
                    lurking[to]['reply']['status'] = True
                    line.sendMessage(to, 'Success activated reply reader')
            elif texts == 'off':
                if not lurking[to]['reply']['status']:
                    line.sendMessage(to, 'Reply reader already deactive')
                else:
                    lurking[to]['reply']['status'] = False
                    line.sendMessage(to, 'Success deactivated reply reader')
            else:
                lurking[to]['reply']['message'] = texts
                line.sendMessage(to, 'Success set reply reader message to `%s`' % texts)
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('greet'):
        textt = removeCmd(text, setKey)
        texttl = textt.lower()
        res = '╭───「 Greet Message 」'
        res += '\n├ Greetings Join Status : ' + bool_dict[settings['greet']['join']['status']][1]
        res += '\n├ Greetings Join Message : ' + settings['greet']['join']['message']
        res += '\n├ Greetings Leave Status : ' + bool_dict[settings['greet']['leave']['status']][0]
        res += '\n├ Greetings Join Message : ' + settings['greet']['leave']['message']
        res += '\n├ Usage : '
        res += '\n│ • {key}Greet'
        res += '\n│ • {key}Greet Join <on/off>'
        res += '\n│ • {key}Greet Join <message>'
        res += '\n│ • {key}Greet Leave <on/off>'
        res += '\n│ • {key}Greet Leave <message>'
        res += '\n╰───「 ZeroDAYS 」'
        if cmd == 'greet':
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
        elif texttl.startswith('join '):
            texts = textt[5:]
            textsl = texts.lower()
            if textsl == 'on':
                if settings['greet']['join']['status']:
                    line.sendMessage(to, 'Greetings join already active')
                else:
                    settings['greet']['join']['status'] = True
                    line.sendMessage(to, 'Success activated greetings join')
            elif textsl == 'off':
                if not settings['greet']['join']['status']:
                    line.sendMessage(to, 'Greetings join already deactive')
                else:
                    settings['greet']['join']['status'] = False
                    line.sendMessage(to, 'Success deactivated greetings join')
            else:
                settings['greet']['join']['message'] = texts
                line.sendMessage(to, 'Success change greetings join message to `%s`' % texts)
        elif texttl.startswith('leave '):
            texts = textt[6:]
            textsl = texts.lower()
            if textsl == 'on':
                if settings['greet']['leave']['status']:
                    line.sendMessage(to, 'Greetings leave already active')
                else:
                    settings['greet']['leave']['status'] = True
                    line.sendMessage(to, 'Success activated greetings leave')
            elif textsl == 'off':
                if not settings['greet']['leave']['status']:
                    line.sendMessage(to, 'Greetings leave already deactive')
                else:
                    settings['greet']['leave']['status'] = False
                    line.sendMessage(to, 'Success deactivated greetings leave')
            else:
                settings['greet']['leave']['message'] = texts
                line.sendMessage(to, 'Success change greetings leave message to `%s`' % texts)
        else:
            line.sendMessage(to, parsingRes(res).format_map(SafeDict(key=setKey.title())))
    elif cmd.startswith('kick '):
        if msg.toType != 2: return line.sendMessage(to, 'Failed kick member, use this command only on group chat')
        if 'MENTION' in msg.contentMetadata.keys():
            mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
            for mention in mentions['MENTIONEES']:
                mid = mention['M']
                if mid == myMid:
                    continue
                try:
                    line.kickoutFromGroup(to, [mid])
                except TalkException as talk_error:
                    return line.sendMessage(to, 'Failed kick members, the reason is `%s`' % talk_error.reason)
                time.sleep(0.8)
            line.sendMessage(to, 'Success kick members, totals %i members' % len(mentions['MENTIONEES']))
        else:
            line.sendMessage(to, 'Failed kick member, please mention user you want to kick')
    elif cmd.startswith('vkick '):
        if msg.toType != 2: return line.sendMessage(to, 'Failed vultra kick member, use this command only on group chat')
        if 'MENTION' in msg.contentMetadata.keys():
            mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
            for mention in mentions['MENTIONEES']:
                mid = mention['M']
                if mid == myMid:
                    continue
                try:
                    line.kickoutFromGroup(to, [mid])
                    line.findAndAddContactsByMid(mid)
                    line.inviteIntoGroup(to, [mid])
                    line.cancelGroupInvitation(to, [mid])
                except TalkException as talk_error:
                    return line.sendMessage(to, 'Failed vultra kick members, the reason is `%s`' % talk_error.reason)
                time.sleep(0.8)
            line.sendMessage(to, 'Success vultra kick members, totals %i members' % len(mentions['MENTIONEES']))
        else:
            line.sendMessage(to, 'Failed vultra kick member, please mention user you want to kick')
    ##----- CLIENT 2 COMMAND-----##
    elif cmd == 'hai':
          line2.sendMessage(to,'hai sayang')

def executeOp(op):
    try:
        print ('++ Operation : ( %i ) %s' % (op.type, OpType._VALUES_TO_NAMES[op.type].replace('_', ' ')))
        if op.type == 5:
            if settings['autoAdd']['status']:
                line.findAndAddContactsByMid(op.param1)
            if settings['autoAdd']['reply']:
                if '@!' not in settings['autoAdd']['message']:
                    line.sendMessage(op.param1, settings['autoAdd']['message'])
                else:
                    line.sendMentionV2(op.param1, settings['autoAdd']['message'], [op.param1])
        if op.type == 13:
            if settings['autoJoin']['status'] and myMid in op.param3:
                line.acceptGroupInvitation(op.param1)
                if settings['autoJoin']['reply']:
                    if '@!' not in settings['autoJoin']['message']:
                        line.sendMessage(op.param1, settings['autoJoin']['message'])
                    else:
                        line.sendMentionV2(op.param1, settings['autoJoin']['message'], [op.param2])
            elif op.param3 in settings['protect']['bl']:
              if op.param2 not in assistsMid and myMid and settings['protect']['join'] == True:
                line.cancelGroupInvitation(op.param1,[op.param3])
                line.kickoutFromGroup(op.param1, [op.param2])
                line.sendMessage(op.param1, "Blacklist Detected")
            else:
               pass
        if op.type == 19:
            if myMid in op.param3:
                if op.param2 in myMid and assistsMid:
                    pass
                else:
                    line2.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 in settings['protect']['bl']:
                        pass
                    if op.param2 in settings['protect']['wl']:
                        pass
                    else:
                        settings['protect']['bl'][op.param2] = True
                G = line2.getGroup(op.param1)
                G.preventedJoinByTicket = False
                line2.updateGroup(G)
                Ti = line2.reissueGroupTicket(op.param1)
                line.acceptGroupInvitationByTicket(op.param1,Ti)
                X = line.getGroup(op.param1)
                X.preventedJoinByTicket = True
                line.updateGroup(X)
            elif assistsMid in op.param3:
                if op.param2 in myMid and assistsMid:
                    pass
                else:
                    line.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 in settings['protect']['bl']:
                        pass
                    if op.param2 in settings['protect']['wl']:
                        pass
                    else:
                        settings['protect']['bl'][op.param2] = True
                G = line.getGroup(op.param1)
                G.preventedJoinByTicket = False
                line.updateGroup(G)
                Ti = line.reissueGroupTicket(op.param1)
                line2.acceptGroupInvitationByTicket(op.param1,Ti)
                X = line2.getGroup(op.param1)
                X.preventedJoinByTicket = True
                line2.updateGroup(X)
            elif op.param3 not in assistsMid and myMid:
                if op.param2 in myMid and assistsMid:
                    pass
                else:
                     if settings['protect']['gr'] == True:
                       line.kickoutFromGroup(op.param1,[op.param2])
                     elif op.param2 in settings['protect']['bl']:
                       pass
                     elif op.param2 in settings['protect']['wl']:
                       del settings['protect']['wl'][op.param2]
                     else:
                        settings['protect']['bl'][op.param2] = True
        if op.type == 15:
            if settings['greet']['leave']['status']:
                if '@!' not in settings['greet']['leave']['message']:
                    line.sendMessage(op.param1, settings['greet']['leave']['message'].format(name=line.getCompactGroup(op.param1).name))
                else:
                    line.sendMentionV2(op.param1, settings['greet']['leave']['message'].format(name=line.getCompactGroup(op.param1).name), [op.param2])
        if op.type == 17:
            if settings['greet']['join']['status']:
                if '@!' not in settings['greet']['join']['message']:
                    line.sendMessage(op.param1, settings['greet']['join']['message'].format(name=line.getCompactGroup(op.param1).name))
                else:
                    line.sendMentionV2(op.param1, settings['greet']['join']['message'].format(name=line.getCompactGroup(op.param1).name), [op.param2])
        if op.type == 11:
            if settings['protect']['qr'] == True:
                if op.param2 in bots:
                  pass
                if op.param2 not in bots:
                  try:
                      G = line.getGroup(op.param1)
                      G.preventedJoinByTicket = True
                      line.kickoutFromGroup(op.param1,[op.param2])
                      line.updateGroup(G)
                      settings["blacklist"][op.param2] = True
                  except Exception as e:
                      line.log('ERROR!')
                else:
                    pass

        if op.type == 25:
            msg      = op.message
            text     = str(msg.text)
            msg_id   = msg.id
            receiver = msg.to
            sender   = msg._from
            to       = sender if not msg.toType and sender != myMid else receiver
            txt      = text.lower()
            cmd      = command(text)
            setKey   = settings['setKey']['key'] if settings['setKey']['status'] else ''
            if text in tmp_text:
                return tmp_text.remove(text)
            if msg.contentType == 0: # Content type is text
                if '/ti/g/' in text and settings['autoJoin']['ticket']:
                    regex = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = regex.findall(text)
                    tickets = []
                    gids = line.getGroupIdsJoined()
                    for link in links:
                        if link not in tickets:
                            tickets.append(link)
                    for ticket in tickets:
                        try:
                            group = line.findGroupByTicket(ticket)
                        except:
                            continue
                        if group.id in gids:
                            line.sendMessage(to, 'I\'m aleady on group ' + group.name)
                            continue
                        line.acceptGroupInvitationByTicket(group.id, ticket)
                        if settings['autoJoin']['reply']:
                            if '@!' not in settings['autoJoin']['message']:
                                line.sendMessage(to, settings['autoJoin']['message'])
                            else:
                                line.sendMentionV2(to, settings['autoJoin']['message'], [sender])
                        line.sendMessage(to, 'Success join to group ' + group.name)
                try:
                    executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey)
                except TalkException as talk_error:
                    logError(talk_error)
                    if talk_error.code in [7, 8, 20]:
                        sys.exit(1)
                    line.sendMessage(to, 'Execute command error, ' + str(talk_error))
                    time.sleep(3)
                except Exception as error:
                    logError(error)
                    line.sendMessage(to, 'Execute command error, ' + str(error))
                    time.sleep(3)
            elif msg.contentType == 1: # Content type is image
                if settings['changePictureProfile']:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/picture.jpg')
                    line.updateProfilePicture(path)
                    line.sendMessage(to, 'Success change picture profile')
                    settings['changePictureProfile'] = False
                elif settings['changeCoverProfile']:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/cover.jpg')
                    line.updateProfileCover(path)
                    line.sendMessage(to, 'Success change cover profile')
                    settings['changeCoverProfile'] = False
                elif to in settings['changeGroupPicture'] and msg.toType == 2:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/grouppicture.jpg')
                    line.updateGroupPicture(to, path)
                    line.sendMessage(to, 'Success change group picture')
                    settings['changeGroupPicture'].remove(to)
            elif msg.contentType == 7: # Content type is sticker
                if settings['checkSticker']:
                    res = '╭───「 Sticker Info 」'
                    res += '\n├ Sticker ID : ' + msg.contentMetadata['STKID']
                    res += '\n├ Sticker Packages ID : ' + msg.contentMetadata['STKPKGID']
                    res += '\n├ Sticker Version : ' + msg.contentMetadata['STKVER']
                    res += '\n├ Sticker Link : line://shop/detail/' + msg.contentMetadata['STKPKGID']
                    res += '\n╰───「 ZeroDAYS 」'
                    line.sendMessage(to, parsingRes(res))
            elif msg.contentType == 13: # Content type is contact
                if settings['checkContact']:
                    mid = msg.contentMetadata['mid']
                    try:
                        contact = line.getContact(mid)
                    except:
                        return line.sendMessage(to, 'Failed get details contact with mid ' + mid)
                    res = '╭───「 Details Contact 」'
                    res += '\n├ MID : ' + mid
                    res += '\n├ Display Name : ' + str(contact.displayName)
                    if contact.displayNameOverridden: res += '\n├ Display Name Overridden : ' + str(contact.displayNameOverridden)
                    res += '\n├ Status Message : ' + str(contact.statusMessage)
                    res += '\n╰───「 ZeroDAYS 」'
                    if contact.pictureStatus:
                        line.sendImageWithURL(to, 'http://dl.profile.line-cdn.net/' + contact.pictureStatus)
                    cover = line.getProfileCoverURL(mid)
                    line.sendImageWithURL(to, str(cover))
                    line.sendMessage(to, parsingRes(res))
            elif msg.contentType == 16: # Content type is album/note
                if settings['checkPost']:
                    if msg.contentMetadata['serviceType'] in ['GB', 'NT', 'MH']:
                        if msg.contentMetadata['serviceType'] in ['GB', 'NT']:
                            contact = line.getContact(sender)
                            author = contact.displayName
                        else:
                            author = msg.contentMetadata['serviceName']
                        posturl = msg.contentMetadata['postEndUrl']
                        res = '╭───「 Details Post 」'
                        res += '\n├ Creator : ' + author
                        res += '\n├ Post Link : ' + posturl
                        res += '\n╰───「 ZeroDAYS 」'
        elif op.type == 26:
            msg      = op.message
            text     = str(msg.text)
            msg_id   = msg.id
            receiver = msg.to
            sender   = msg._from
            to       = sender if not msg.toType and sender != myMid else receiver
            txt      = text.lower()
            if settings['autoRead']:
                line.sendChatChecked(to, msg_id)

            if msg.contentType == 0: # Content type is text
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                if '/ti/g/' in text and settings['autoJoin']['ticket']:
                    regex = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = regex.findall(text)
                    tickets = []
                    gids = line.getGroupIdsJoined()
                    for link in links:
                        if link not in tickets:
                            tickets.append(link)
                    for ticket in tickets:
                        try:
                            group = line.findGroupByTicket(ticket)
                        except:
                            continue
                        if group.id in gids:
                            line.sendMessage(to, 'I\'m aleady on group ' + group.name)
                            continue
                        line.acceptGroupInvitationByTicket(group.id, ticket)
                        if settings['autoJoin']['reply']:
                            if '@!' not in settings['autoJoin']['message']:
                                line.sendMessage(to, settings['autoJoin']['message'])
                            else:
                                line.sendMentionV2(to, settings['autoJoin']['message'], [sender])
                        line.sendMessage(to, 'Success join to group ' + group.name)
                if settings['mimic']['status']:
                    if sender in settings['mimic']['target'] and settings['mimic']['target'][sender]:
                        try:
                            line.sendMessage(to, text, msg.contentMetadata)
                            tmp_text.append(text)
                        except:
                            pass
                if settings['autoRespondMention']['status']:
                    if msg.toType in [1, 2] and 'MENTION' in msg.contentMetadata.keys() and sender != myMid and msg.contentType not in [6, 7, 9]:
                        mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = [mention['M'] for mention in mentions['MENTIONEES']]
                        if myMid in mentionees:
                            if line.getProfile().displayName in text:
                                if '@!' not in settings['autoRespondMention']['message']:
                                    line.sendMessage(to, settings['autoRespondMention']['message'])
                                else:
                                    line.sendMentionV2(to, settings['autoRespondMention']['message'], [sender])
                if settings['autoRespond']['status']:
                    if msg.toType == 0:
                        contact = line.getContact(sender)
                        if contact.attributes != 32 and 'MENTION' not in msg.contentMetadata.keys():
                            if '@!' not in settings['autoRespond']['message']:
                                line.sendMessage(to, settings['autoRespond']['message'])
                            else:
                                line.sendMentionV2(to, settings['autoRespond']['message'], [sender])
            if msg.contentType == 1:
                    path = line.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}

            if msg.contentType == 7:
                    msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}

        if op.type == 55:
            if op.param1 in lurking:
                if lurking[op.param1]['status'] and op.param2 not in lurking[op.param1]['members']:
                    lurking[op.param1]['members'].append(op.param2)
                    if lurking[op.param1]['reply']['status']:
                        if '@!' not in lurking[op.param1]['reply']['message']:
                            line.sendMessage(op.param1, lurking[op.param1]['reply']['message'])
                        else:
                            line.sendMentionV2(op.param1, lurking[op.param1]['reply']['message'], [op.param2])

        if op.type == 65:
            if settings["unsendMessage"] == True:
                print("++ Someone has unsended a message")
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = line.getGroup(at)
                                target = line.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "╭───「 Gambar di Hapus 」\n├ Pengirim : "
                                ret_ = "├ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n├ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += '\n╰───「 ZeroDAYS 」'
                                ry = str(target.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':target.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                line.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                line.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = line.getGroup(at)
                                target = line.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(target.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                line.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if settings["unsendMessage"] == True:
                print("++ Someone has unsended a sticker message")
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = line.getGroup(at)
                                target = line.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(target.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                line.sendMessage(at, str(ret_))
                                line.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

    except TalkException as talk_error:
        logError(talk_error)
        if talk_error.code in [7, 8, 20]:
            sys.exit(1)
    except KeyboardInterrupt:
        sys.exit('##---- KEYBOARD INTERRUPT -----##')
    except Exception as error:
        logError(error)

def runningProgram():
    while True:
        try:
            ops = oepoll.singleTrace(count=50)
        except TalkException as talk_error:
            logError(talk_error)
            if talk_error.code in [7, 8, 20]:
                sys.exit(1)
            continue
        except KeyboardInterrupt:
            sys.exit('##---- KEYBOARD INTERRUPT -----##')
        except Exception as error:
            logError(error)
            continue
        if ops:
            for op in ops:
                executeOp(op)
                oepoll.setRevision(op.revision)

if __name__ == '__main__':
    print ('##---- RUNNING PROGRAM -----##')
    runningProgram()
