from pyrogram import Client, Filters,Emoji
from pyrogram.errors import FloodWait
import time
from emoji import UNICODE_EMOJI
app = Client("send",715451,"d2cba6f7bf5d1a45682da5bb9071a307")
s = -1001146486274
d = -1001378725482
g = ["0","1","2","3","4","6","NEED","RUN","CATCH","DROP","BALL","HAWA","WD","WIDE","NB","PLAYING","OVER","WON","WIN","START","STOP","ME","+","XI","✔️","GANA","GAANA","TIE","WKT","WICKET","☄️"]
@app.on_message(Filters.chat(s) & Filters.text & ~Filters.edited)
def forward(client,Message):
 r = s = False
 words = ['dekho','TRUST','join','fix','😱','😳','👆','👇','☝️','https://','😂','🤔','pass','chase','link','suno','member','❓','loss','audio','open',"report",'paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','only','chut','tennis','teen','lavde','chutiya','bc','kya','line','LUND','WICKET LU','?','loda','telegram','chor',"kama","lakh",' id','स',"kitna"]
 for word in words:
  if word.casefold() in Message.text.casefold():
   return
 for i in Message.text.split(' '):
  if i in UNICODE_EMOJI:
   r = True
  for p in g:
   if p.casefold() in Message.text.casefold():
    s = True
 if r or s:
  if "🎾" in Message.text:
   mes = client.send_message(d,"<b>" + ' '.join(Message.text.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶").split("🎾")[:-1]) + "🎾" + "</b>",parse_mode= "html")
  else:
   mes = client.send_message(d, Message.text.markdown.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶")) 
  with open("sure.txt", "r") as f:
   x = f.readlines()
  y = [j for j in x[0].split(" ")]
  del y[:2]
  y = " ".join(str(x) for x in y)
  o = open("sure.txt","w")
  o.write(y + " " +str(Message.message_id) + " " + str(mes.message_id))
  o.close()
@app.on_message(Filters.command("c"))
def main(client, message):
 with open("sure.txt" , "w") as files:
  files.write("000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000")
  files.close()
  message.reply("Done") 
app.run()
