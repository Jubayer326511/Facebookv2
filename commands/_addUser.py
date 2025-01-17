from util import getUid

async def add_user(bot, event):
  if not event.args:
    return await event.sendReply("Missing an argument")
  if event.thread_type == bot.thread_user:
    return await event.sendReply("This command only works in group chat")
  if not event.args:
    return await event.sendReply("Please provide a uid or link of the user you want to add")
  try:
    uid = event.args
    if ' ' in event.args:
      return await event.sendReply("Invalid command usage")
    if 'facebook.com' in event.args:
      uid_ = getUid(event.args)
      if 'error' in uid_:
        return await event.sendReply("Unable to add the user, try adding the user by uid")
      uid = uid_
    await bot.addUsersToGroup(uid, event.thread_id)
  except Exception as err:
    bot.error(err)
    await event.sendReply(event.font(f":mono[An error occured while adding the user]"))

config = {
  "name": 'add',
  "author": 'Muhammad Greeg',
  "def": add_user,
  "adminOnly": True,
  "usage": '{p}add [uid/link]',
  "description": 'Add user to the thread'
}