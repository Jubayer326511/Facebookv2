import asyncio

async def handleEvent(bot, event_type, **data):
  try:
    events = bot.events
    baho_event = list()
    for tae_event in events:
      if event_type == tae_event['event']:
        baho_event.append(tae_event['def'])
    if len(baho_event) != 0:
      data_event = {key:val for key, val in data.items()}
      for ako_event in baho_event:
        asyncio.create_task(ako_event(bot, data_event))
  except Exception as err:
    print("\033[0;91m[ERROR] \033[0m{}".format(err))
