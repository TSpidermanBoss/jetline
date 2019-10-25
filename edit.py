from pyrogram import Client, Filters,Emoji
from pyrogram.errors import FloodWait
import time
app = Client("edit",715451,"d2cba6f7bf5d1a45682da5bb9071a307")
s = -1001146486274
d = -1001378725482
@app.on_message(Filters.chat(s) & Filters.text & Filters.edited)
def forward(client,Message):
 file = open("sure.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
  x = line.split()
  id = str(Message.message_id)
  if id in x:
   try:
    if "🎾" in Message.text:
     client.edit_message_text(d,int(x[x.index(id)+1]),"<b>" + ' '.join(Message.text.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶").split("🎾")[:-1]) + "</b>" + "🎾",parse_mode="html")
    else:
     client.edit_message_text(d,int(x[x.index(id)+1]),Message.text.markdown.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶")) 
   except FloodWait as e:
    time.sleep(e.x)
app.run()
