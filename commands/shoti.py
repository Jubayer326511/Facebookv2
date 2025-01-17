import requests

async def function(bot, event):
  if event.args: return await event.sendReply(event.font(":mono[This command dont need an argument]"))
  loading = await bot.sendMessage(event.font(":mono[Fetching random shoti, please wait...]"), event.thread_id, event.thread_type)
  try:
    url = "https://sitebot-production-3143.up.railway.app/api/shoti"
    res = requests.get(url)
    data = res.json()
    if res.status_code != 200:
      await bot.unsend(loading)
      return await event.sendReply(event.font(f":mono[{data['error']}]"))
    message = f":bold[user]: {data['username']}\n"
    message += f":bold[views]: {data['views']}\n"
    message += f":bold[shares]: {data['shares']}\n"
    message += f":bold[comments]: {data['comments']}\n"
    message += f":bold[music]: {data['music']}\n"
    message += f"{event.line}\n"
    message += f":mono[{data['description']}]"
    video = data['videoSource']
    with open('commands/cache/shoti.mp4', 'wb') as file:
      video_data = requests.get(video).content
      file.write(video_data)
    await bot.sendLocalFiles(
      "commands/cache/shoti.mp4",
      event.font(message),
      thread_id = event.thread_id,
      thread_type = event.thread_type
    )
    await bot.unsend(loading)
  except Exception as e:
    print(f"\033[91m[ERROR] \033[0m{e}")
    await event.sendReply(event.font(f":mono[{e}]"))


config = {
  "name": 'shoti',
  "def": function,
  "author": "Muhammad Greeg",
  "usage": '{p}shoti',
  "description": 'Fetch a random shoti video',
  "usePrefix": False
}
