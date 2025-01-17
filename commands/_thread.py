import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from database import Thread

on_proccess = {}

def fetch(uid):
  try:
    response = requests.get(f"https://facebook.com/{uid}", headers={
      "User-Agent": 'Mozilla/5.0 (Windows; U; Windows NT 5.0; de-AT; rv:1.7.11) Gecko/20050728'
    })
    html = BeautifulSoup(response.text, 'html.parser')
    name = html.find('title').get_text()
    
    user_id = uid
    user_name = name if 'error' not in name.lower() or 'Facebook' != name else 'Facebook User'
    print(f"\033[96m[DATABASE]\033[0m {user_id} | {user_name}")
    return {uid:user_name}
  except Exception as er:
    print("\033[31m[ERROR] \033[0m{}".format(er))

def trabaho(thread_id):
  db = Thread(thread_id)
  data = on_proccess.get(thread_id)
  if data:
    ids = data.get('participants')
    admin_ids = data.get('admins')
    with ThreadPoolExecutor(max_workers=5 if len(ids)>20 else 3) as executor:
      resulta = list(executor.map(fetch, ids))
    for result in resulta:
      for uid, name in result.items():
        tao = db.find_one(uid=uid)
        role = 'member' if uid not in admin_ids else 'admin'
        if tao:
          db.update(dict(uid=uid, name=name, role=role), ['uid'])
        else:
          db.insert(dict(uid=uid, name=name, role=role))
    del on_proccess[thread_id]

async def function(bot, event):
  sub = event.args.lower()
  if sub:
    return await event.sendReply(":mono[This command dont need a parameters]", True)
  if event.thread_id in on_proccess:
    return await event.sendReply(
      event.font(":mono[Thread is still updating...]")
    )
  if event.thread_id != event.author_id:
    info = await bot.fetchThreadInfo(event.thread_id)
    thread = info.get(event.thread_id)
    on_proccess[event.thread_id] = {
      "participants": thread.participants,
      "admins": thread.admins
    }
    await event.sendReply(":mono[Updating thread data, please wait...]",True)
    trabaho(event.thread_id)
    await event.sendReply(":mono[Thread data is now updated]",True)
config = {
  "name": 'update',
  "def": function,
  "adminOnly": True
}