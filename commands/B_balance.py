from database import Bank

async def function(bot, event):
  if event.args:
    return await event.sendReply(":mono[This command dont need a parameter]",True)
  user = Bank(event.author_id)
  return await event.sendReply(f":bold[Balance:] {user.balance}",True)

config = {
  "name": 'bal',
  "def": function,
  "author": 'Muhammad Greegmon',
  "description": "Get the current money balance",
  "usage": '{p}bal',
  "usePrefix": False
}