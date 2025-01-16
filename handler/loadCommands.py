import os
import importlib

commands = {}

def loadCommands(_prefix):
  global commands
  if commands:
    return commands
  files = list(filter(lambda file: file.endswith('.py') and file!='__init__.py',os.listdir('./commands')))
  print("\033[97m⦿━━━━━━━━━━━━━━━⦿ \033[96mLoad Commands\033[97m ⦿━━━━━━━━━━━━━━━⦿")
  for file in files:
    filepath = f"commands.{os.path.splitext(file)[0]}"
    module = importlib.import_module(filepath)
    config = getattr(module, 'config', None)
    if config:
      name = config.get('name')
      function = config.get('def')
      if config.get('function'):
        function = config.get('function')
        config['def'] = config.get('function')
        del config['function']
      if not name:
        print(f"\033[31m[COMMAND]\033[0m{file} NOT LOADED - Missing command name")
      elif not function:
        print(f"\033[31m[COMMAND]\033[0m{file} NOT LOADED - Missing command function")
      else:
        usePrefix = config.get('usePrefix', True)
        if not name.isalnum():
          print(f"\033[31m[COMMAND]\033[0m{file} NOT LOADED - Invalid command name")
        elif name.lower() in commands:
          print(f"\033[31m[COMMAND]\033[0m{file} NOT LOADED - Command name already exist")
        elif usePrefix not in [True, False]:
          print(f"\033[31m[COMMAND]\033[0m{file} NOT LOADED - Invalid usePrefix value")
        else:
          admin_only = config.get('admin_only', False)
          if not admin_only in [True,False]:
            admin_only = False
            print(f"\033[0m   - Invalid 'adminOnly' key in config, It will automatically set to False")
          config['admin_only'] = admin_only if admin_only in [True, False] else False
          
          config["usage"] = config.get("usage", "").replace('{p}', _prefix)
          config["description"] = config.get("description", 'No description.').replace('{p}', _prefix)
          commands[name.lower()] = config
          print(f"\033[36m[COMMAND] \033[0mLOADED \033[33m{name} \033[0m- \033[35m({file})\033[0m")
  print()
  return commands
