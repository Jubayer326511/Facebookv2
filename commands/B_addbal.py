from database import Bank

async def fubction(bot, event):
  try:
    sub, args = event.args.split(' ', 1) if event.args else [event.args, '']
    if not sub:
      return await event.sendReply(":mono[ERROR: Invalid usage]",True)
    elif not args:
      return await event.sendReply(":mono[ERROR: Missing amount of money to send]",True)
    user = Bank(int(sub))
    n = user.add_money(int(args))
    await event.sendReply(f"Successfully added {args} to {sub}\n\n:bold[Balance:] {n}", True)
  except ValueError:
    await event.sendReply(":mono[Value error, please try again]",True)

config = {
  "name": 'addbal',
  "def": fubction,
  "author": 'Muhammad Greeg',
  "adminOnly": True,
  "usage": '{p}addbal [uid] [amount]',
  "usePrefix": False,
  "description": 'Add money balance to the given user uid'
}