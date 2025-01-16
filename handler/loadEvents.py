import os
import importlib

events = []

def loadEvents():
  global events
  if events:
    return events
  files = list(filter(lambda file: file.endswith('.py') and
  file!='__init__.py',os.listdir('./events')))
  print("\033[97m⦿━━━━━━━━━━━━━━━⦿ \033[96mLoad Events\033[97m ⦿━━━━━━━━━━━━━━━⦿")
  for file in files:
    filepath = f"events.{os.path.splitext(file)[0]}"
    module = importlib.import_module(filepath)
    config = getattr(module, 'config', None)
    if config:
      event_type = config.get('event')
      function = config.get('def')
      if not event_type:
        print(f"\033[0;93m({file}) \033[97mEVENT NOT LOADED - \033[0;31mMissing event type")
      elif not function:
        print(f"\033[0;93m({file}) \033[97mEVENT NOT LOADED - \033[0;31mMissing event function")
      else:
        if not event_type.startswith('type:'):
          print(f"\033[0;93m({file}) \033[97mEVENT NOT LOADED - \033[0;31mInvalid event type")
        else:
          config["event"] = config["event"].lower()
          events.append(config)
          print(f"\033[0;97mEVENT LOADED: \033[0;32m{file}\033[0m")
  print()
  return events
