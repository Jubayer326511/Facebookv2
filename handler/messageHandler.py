from util import (
  text_formatter
)
import os

class MessageData:
  def __init__(self, **data):
    self.bot = data.get('client')
    
    self.cmd = data.get('cmd')
    self.args = data.get('args')
    
    self.mid = data.get('mid')
    self.author_id = data.get('author_id')
    self.message = data.get('message')
    self.message_object = data.get('message_object')
    self.thread_id = data.get('thread_id')
    self.thread_type = data.get('thread_type')
    self.reply = None
    
    self.line = "━━━━━━━━━━━━━━━━━━"
    self.font = text_formatter
    
    if self.message_object.replied_to:
      self.reply = self.message_object.replied_to
  async def sendReply(self, message, auto_font=False, mentions=None):
    text = self.font(message) if auto_font else message
    return await self.bot.sendMessage(text, self.thread_id, self.thread_type, reply_to_id=self.mid, mentions=mentions)

async def handleMessage(bot,mid,author_id,message,message_object,thread_id,thread_type,**kwargs):
  try:
    _split = message.split(' ',1) if message else ['']
    cmd, args = _split if len(_split) != 1 else [_split[0],'']
    cnp = cmd if bot.prefix == "" or not cmd.startswith(bot.prefix) else cmd[1:];cnp = cnp.lower()
    if cnp in bot.commands:
      function = bot.commands[cnp]
      message_data = MessageData(
        cmd = cnp,
        args = args,
        mid = mid,
        client = bot,
        author_id = author_id,
        message = message,
        message_object = message_object,
        thread_id = thread_id,
        thread_type = thread_type
      )
      is_need_prefix = function.get('usePrefix', True)
      is_admin_only = function.get('adminOnly', False)
      if bot.prefix != '' and is_need_prefix and not cmd.startswith(bot.prefix):
        return await bot.sendMessage(text_formatter(":mono[This command require to use prefix]"), thread_id, thread_type)
      elif is_admin_only and str(author_id) not in bot.admin:
        return await bot.sendMessage(text_formatter(":mono[You dont have permission to use this command.]"), thread_id, thread_type)
      else:
        return await function['def'](bot, message_data)
  except Exception as err:
    print("\033[0;91m[ERROR][messageHandler] \033[0m{}".format(err))
