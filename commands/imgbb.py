from util import upload_imgbb

async def imgbb(bot, event):
  if not event.reply:
    return await event.sendReply(event.font(":mono[Please reply to the image]"))
  try:
    urls = []
    for url in event.reply.attachments:
      if '.mp4' in url.large_preview_url:
        print(f"\033[0;31m[ERROR] \033[0m{res['error']}")
        return await event.sendReply(event.font(":mono[Invalid image attachment]"))
      res = upload_imgbb(url.large_preview_url)
      if 'error' in res:
        print(f"\033[0;31m[ERROR] \033[0m{res['error']}")
        return await event.sendReply(event.font(":mono[An error occurred while uploading the image.]"))
      else:
        urls.append(res['image_url'])
    if len(urls) == 0:
      print(f"\033[0;31m[ERROR] \033[0m{res['error']}")
      return await event.sendReply(event.font(":mono[An error occurred while uploading the image.]"))
    else:
      message = event.font(":bold[IMGBB]")
      message += "\nImage successfully uploaded\n"
      for index, link in enumerate(urls):
        message += f"\n{index+1}. {link}"
      await event.sendReply(message)
  except Exception as e:
    print("\033[0;31m[ERROR] \033[0m{}".format(e))
    return await event.sendReply(event.font(":mono[An error occurred while uploading the image.]"))

config = {
  "name": 'imgbb',
  "def": imgbb,
  "description": 'Upload image to imgbb and get the image link',
  "usage": '{p}imgbb <reply to image>',
  "author": 'ako SI choru',
  "usePrefix": True
}