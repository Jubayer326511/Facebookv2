async def prefix(bot, event):
  if not event.args:
    message = "My prefix is: {}".format(bot.prefix) if bot.prefix != '' else "I dont have prefix"
    await event.sendReply(message)

config = {
  "name": 'prefix',
  "def": prefix,
  "usePrefix": False
}