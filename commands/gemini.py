import requests

async def gemini(bot, event):
  if not event.args: return await event.sendReply(
    event.font(":mono[No prompt provided]")
  )
  try:
    res = requests.get(f"https://api.joshweb.click/gemini?prompt={event.args.replace(' ','+')}").json()
    if 'error' in res:
      return await event.sendReply(event.font(f":mono[{res['error']}]"))
    await event.sendReply(event.font(
      ":bold[GEMINI]\n"
      f"{event.line}\n"
      f"{res['gemini']}"
    ))
  except Exception as e:
    print("\033[0;32m[ERROR] \033[0m{}".format(e))
    await event.sendReply(event.font(":mono[An error occured while proccessing the request]"))

config = {
  "name": 'gemini',
  "def": gemini,
  "author": 'Muhammad Greeg',
  "usage": '{p}gemini [question]'
}