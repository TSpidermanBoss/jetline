from pyrogram import Client, Filters,Emoji
from pyrogram.errors import FloodWait
import time
from emoji import UNICODE_EMOJI
app = Client("mnnnnnnn",488556,"c722b7aadbf8b72109b2f96f30974c6d")
s = -1001146486274
d = -1001378725482
@app.on_deleted_messages(Filters.chat(s))
def main(client, messages):
 for v in messages:
  file = open("sure.txt" , "r")
  lines = file.readlines()
  file.close()
  for line in lines:
   x = line.split()
   id = str(v.message_id )
   if id in x:
    try:
     client.delete_messages(d,int(x[x.index(id)+1]))
    except FloodWait as e:
     time.sleep(e.x)
app.run()
