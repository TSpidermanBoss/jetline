from pyrogram import Client, Filters
import time
from pyrogram.errors import FloodWait
import asyncio
async def main():
 msg_ids = {}
 app = Client("send",715451,"d2cba6f7bf5d1a45682da5bb9071a307")
 s = -1001146486274
 d = -1001378725482
 @app.on_message(Filters.chat(s) & Filters.text & ~Filters.edited)
 def forward(client,Message):
  words = ['dekho','TRUST','join','fix','😱','😳','👆','👇','☝️','https://','😂','🤔','pass','chase','link','suno','member','❓','loss','audio','open',"report",'paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','only','chut','tennis','teen','lavde','chutiya','bc','kya','LUND','WICKET LU','?','loda','telegram','chor',"kama","lakh",' id','स',"kitna"]
  for word in words:
   if word.casefold() in Message.text.casefold():
     return 
  if "🎾" in Message.text:
   z = client.send_message(d,"<b>" + ' '.join(Message.text.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶").split("🎾")[:-1]) + "🎾" + "</b>",parse_mode= "html").message_id
  else:
   z = client.send_message(d, Message.text.markdown.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶").replace("Live","Bullet")).message_id
  msg_ids[Message.message_id] = z
 @app.on_message(Filters.chat(s) & Filters.text & Filters.edited)
 def forward(client,Message):
  if not Message.message_id in msg_ids:
   return
  try:
   if "🎾" in Message.text:
    client.edit_message_text(d,msg_ids[Message.message_id],"<b>" + ' '.join(Message.text.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶").split("🎾")[:-1]) + "</b>" + "🎾",parse_mode="html")
   else:
    client.edit_message_text(d,msg_ids[Message.message_id],Message.text.markdown.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶").replace("Live","Bullet") ) 
  except FloodWait as e:
   time.sleep(e.x)
 @app.on_deleted_messages(Filters.chat(s))
 def main(client, Messages):
   for Message in Messages:
    if not Message.message_id in msg_ids:
     return
    client.delete_messages(d,msg_ids[Message.message_id])
 app.run()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
