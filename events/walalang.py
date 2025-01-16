async def function(bot, data):
  message = data.get('message', '') or ''
  tid = data.get('thread_id')
  typ = data.get('thread_type')
  def check(text):
    return True if text in message.lower() else False
  
  if check("junmar"):
    return await bot.sendMessage("Junmar bakla!!", tid, typ)
  elif check("greegmon") or check(' greeg '):
    return await bot.sendMessage("Wala si Gregemon, naga lulu pa", tid, typ)
  elif check('prince har'):
    return await bot.sendMessage("No need facebook chat application programming interface.", tid, typ)

config = {
  "event": 'type:message',
  "def": function,
  "author": 'Muhammad Greeg'
}
