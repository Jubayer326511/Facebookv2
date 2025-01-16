import dataset
import datetime

class Thread:
  def __init__(self, thread_id):
    self._connect = dataset.connect('sqlite:///database/threads.db')
    self.db = self._connect[thread_id]
  
  def insert(self, data):
    self.db.insert(data)
  
  def find(self, *_clause, **kwargs):
    return self.db.find(*_clause, **kwargs)
  
  def find_one(self, *arg, **kwarg):
    return self.db.find_one(*arg, **kwarg)
  
  def update(self, row, keys):
    self.db.update(row, keys)


class Database:
  def __init__(self, table):
    self._connect = dataset.connect('sqlite:///database/database.db')
    self.db = self._connect[table]
  
  def insert(self, data):
    self.db.insert(data)
  
  def find(self, *_clause, **kwargs):
    return self.db.find(*_clause, **kwargs)
  
  def find_one(self, *arg, **kwarg):
    return self.db.find_one(*arg, **kwarg)
  
  def update(self, row, keys):
    self.db.update(row, keys)
  
  def upsert(self, row, keys):
    self.db.upsert(row, keys)

class Bank(Database):
  def __init__(self, uid):
    self.uid = uid
    
    super().__init__('bank')
    if not self.find_one(uid=self.uid):
      self._new()
  
  def _new(self):
    self.upsert(dict(
      uid = self.uid,
      money = 200, # default
    ), ['uid'])
    print(f"\033[32m[BANK] \033[0mNew data - \033[96m{self.uid}")
  
  @property
  def balance(self):
    user = self.find_one(uid=self.uid)
    return user.get('money', 0)
  
  def add_money(self, amount:int):
    prev = self.balance
    if not isinstance(amount, int):
      print("\033[91m[BANK] \033[0mInvalid argument")
      return prev
    if amount <= 0:
      print("\033[91m[BANK] \033[0mInvalid amount of money")
      return prev
    self.upsert(dict(uid=self.uid,money=prev+amount), ['uid'])
    return prev + amount
  
  def sub_money(self, amount:int):
    prev = self.balance
    if not isinstance(amount, int):
      print("\033[91m[BANK] \033[0mInvalid argument")
      return prev
    if amount > prev:
      print(f"\033[91m[BANK] \033[0mCurrent money is not enough to subtract by {amount}")
      return prev
    self.upsert(dict(uid=self.uid,money=prev-amount), ['uid'])
    return prev - amount
