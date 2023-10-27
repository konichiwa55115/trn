from torrentp import TorrentDownloader
import shutil
from pyrogram import Client, filters
import os
from os import system as cmd


bot = Client(
    "myfirstorrent",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6280972722:AAG3GrropPJhZvfjljtgppKeeXpfpBVZG4Y"
)
@bot.on_message(filters.private & filters.incoming & filters.text  )
def _telegram_file(client, message):

  user_id = message.from_user.id 
  url = message.text
  torrent_file = TorrentDownloader(f"{url}", './downloads/')
  torrent_file.start_download()
  cmd('7z x \*')
  cmd(f'''uploadgram {user_id} ./downloads/''')
  
  
  shutil.rmtree('./downloads/') 



bot.run()
