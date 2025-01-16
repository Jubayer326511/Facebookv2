import urllib.parse

async def bagong_tao(bot, event):
  try:
    data = event.get('msg')
    tid = event['thread_id']
    typ = event['thread_type']
    for fbuser in data.get('addedParticipants'):
      if fbuser['userFbId'] == bot.uid:
        await bot.shareContact(event.font(":mono[Thank you for adding me.]"), bot.uid, tid)
    else:
      fbuser = data.get('addedParticipants')[0]
      name = fbuser['fullName']
      await bot.shareContact(f"Welcome! {name} to the group chat", event['added_ids'][0], tid)
  except Exception as err:
    bot.error(err)

config = {
  "event": "type:addedParticipants",
  "def": bagong_tao,
  "author": "Muhammad Greeg"
}
