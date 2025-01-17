import requests

async def ImageGen(bot, event):
  if not event.args:
    return await event.sendReply(event.font(":mono[Provide an image prompt.]"))
  try:
    nigro = await event.sendReply(event.font(":mono[Generating image, please wait.]"))
    await bot.sendRemoteFiles(
      [f"https://imgen.duck.mom/prompt/{event.args.replace(' ','+')}"],
      thread_id=event.thread_id,
      thread_type=event.thread_type
    )
    await bot.unsend(nigro)
  except Exception as e:
    print("\033[0;31m[ERROR] \033[0m{}".format(e))
    return await event.sendReply(event.font(":mono[An error occurred while generating the image.]"))

config = {
  "name": 'imgen',
  "def": ImageGen,
  "description": "Generate an image",
  "usage": "{p}imgen [prompt]",
  "author": 'Muhammad Greegmon',
  "usePrefix": False
}