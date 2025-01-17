def byPage(commands, page=1):
  message = f"╭─── :bold[COMMANDS] ───\n"
  for cmd in commands[page-1]:
    message += f"│ ○ {cmd}\n"
  message += f"╰────{'─'*len('COMMANDS')}───\n"
  message += f"📖 Page: ({page}/{len(commands)})\n"
  return message

def getAll(commands):
  message = f"╭─── :bold[COMMANDS] ───\n"
  for cmd in commands:
    message += f"│ ○ {cmd}\n"
  message += f"╰────{'─'*len('COMMANDS')}───\n"
  return message
  

async def function(bot, event):
  commands = list(map(lambda x: x,bot.commands))
  chunk = 15
  COMMANDS = [commands[i:i+chunk] for i in range(0, len(commands), chunk)]
  sub, *_ = event.args.split(' ',1) if event.args else [event.args,'']
  args = ' '.join(_)
  
  if args:
    return await event.sendReply("ⓘ Invalid command usage, type 'help help' to see how to use this command.")
  
  if sub.lower() == 'all':
    message = getAll(commands)
    message += f"📦 Total commands: {len(commands)}\n"
    message += f"ⓘ 𝖨𝖿 𝗒𝗈𝗎 𝗁𝖺𝗏𝖾 𝖺𝗇𝗒 𝗊𝗎𝖾𝗌𝗍𝗂𝗈𝗇𝗌 𝗈𝗋 𝗇𝖾𝖾𝖽 𝖺𝗌𝗌𝗂𝗌𝗍𝖺𝗇𝖼𝖾, 𝗉𝗅𝖾𝖺𝗌𝖾 𝖼𝗈𝗇𝗍𝖺𝖼𝗍 𝗍𝗁𝖾 𝖽𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋."
    return await event.sendReply(message, True)
    
  
  # command info
  if sub.lower() in commands:
    cmd = bot.commands.get(sub.lower())
    message = f"╭─── :bold[{sub.lower()}] ───\n"
    message += f":bold[author]: {cmd.get('author', "Unknown")}\n"
    message += f":bold[adminOnly]: {cmd.get('adminOnly', False)}\n"
    message += f":bold[usage]: {cmd.get('usage')}\n"
    message += f":bold[description]: {cmd.get('description')}\n"
    message += f"╰────{'─'*len(sub.lower())}───\n"
    return await event.sendReply(message, True)
  elif sub:
    try:
      __nothing__ = int(sub)
    except ValueError:
      return await event.sendReply(f"ⓘ Command '{sub.lower()}' not found, type 'help all' to see all the commands.")
  
  # by page
  if sub:
    if len(COMMANDS) < int(sub) or len(COMMANDS) > int(sub):
        return await event.sendReply(f"Page {sub} is not defined, total command page {len(COMMANDS)}")
  message = byPage(COMMANDS, page=int(sub) if sub else 1)
  message += f"📦 Total commands: {len(commands)}\n"
  message += f"ⓘ 𝖨𝖿 𝗒𝗈𝗎 𝗁𝖺𝗏𝖾 𝖺𝗇𝗒 𝗊𝗎𝖾𝗌𝗍𝗂𝗈𝗇𝗌 𝗈𝗋 𝗇𝖾𝖾𝖽 𝖺𝗌𝗌𝗂𝗌𝗍𝖺𝗇𝖼𝖾, 𝗉𝗅𝖾𝖺𝗌𝖾 𝖼𝗈𝗇𝗍𝖺𝖼𝗍 𝗍𝗁𝖾 𝖽𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋."
  return await event.sendReply(message, True)

config = {
  "name": 'help',
  "def": function,
  "author": 'Muhammad Greeg',
  "usePrefix": False,
  "adminOnly": False,
  "description": "Show the bot available commands",
  "usage": '{p}help [<None>|<page>|<cmd name>|all]'
}