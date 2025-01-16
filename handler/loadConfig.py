import json
import asyncio

async def loadConfig(botName=None):
  data = {
    "prefix": None,
    "botName": botName,
    "owner": "Anonymous",
    "admin": [
      61571117768115
    ]
  }
  print(f"\033[97m⦿━━━━━━━━━━━━━━━⦿ \033[96mLoad Config \033[97m⦿━━━━━━━━━━━━━━━⦿")
  try:
    config = json.load(open('config.json', 'r'))
  except FileNotFoundError:
    print("\033[0;31m[CONFIG] \033[0mConfig file not found\n")
    return data
  await asyncio.sleep(0.2)
  prefix = config.get('prefix', '')
  if not prefix:
    print("\033[0;36m[CONFIG] \033[0mNo prefix")
    prefix = ''
  elif not isinstance(prefix, str):
    print("\033[0;31m[CONFIG] \033[0mInvalid prefix data types")
    prefix = ''
  elif ' ' in list(prefix):
    prefix = ''
    print("\033[0;31m[CONFIG] \033[0mPrefix must not include space")
  else:
    print(f"\033[0;36m[CONFIG] \033[0mPrefix loaded    : \033[1;97m{prefix}")
  
  botName = config.get('botName', data['botName'])
  print(f"\033[0;36m[CONFIG] \033[0mBot name loaded  : \033[1;97m{botName}")
  owner = config.get("owner", data['owner'])
  print(f"\033[0;36m[CONFIG] \033[0mBot owner loaded : \033[1;97m{owner}")
  _admin = config.get("admin", data['admin'])
  admin = [str(ad) for ad in _admin if isinstance(ad, int) or isinstance(ad, str)]
  print(f"\033[0;36m[CONFIG] \033[0mBot admin loaded : \033[1;97m{len(admin)}")
  
  data['prefix'] = prefix
  data['botName'] = botName
  data['owner'] = owner
  data['admin'] = admin
  return data
