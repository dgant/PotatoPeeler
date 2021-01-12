import glob
import itertools
import json
import os
import shutil
import traceback

user_dir = os.path.expanduser('~')
scbw_root = os.path.join(user_dir, 'appdata', 'roaming', 'scbw')
games_root = os.path.join(scbw_root, 'games')
replay_dir = os.path.join(scbw_root, 'losses')
foes = {}
maps = {}

class Matchup:
  def __init__(self, name):
    self.name = name
    self.games = []
  def wins(self):
    return len(self.won_games())
  def losses(self):
    return len(self.lost_games())
  def conclusive(self):
    return self.total() - self.inconclusive()
  def inconclusive(self):
    return len(self.inconclusive_games())  
  def total(self):
    return len(self.games)
  def won_games(self):
    return [game for game in self.games if game.won()]
  def lost_games(self):
    return [game for game in self.games if game.lost()]
  def inconclusive_games(self):
    return [game for game in self.games if game.inconclusive()]
  def winrate(self):
    return 0.0 if (self.conclusive() == 0) else self.wins() / self.conclusive()
    
class Game:
  def __init__(self, game_id, full_directory, timestamp, game_json):
    self.id         = game_id
    self.directory  = full_directory
    self.timestamp  = timestamp
    self.json       = game_json    
    self.map        = game_json['map_name']
    self.me         = game_json['bots'][0]
    self.foe        = game_json['bots'][1]
    self.crashed    = game_json['is_crashed']
    self.duration   = game_json['game_time']
    self.winner     = game_json['winner']
    self.loser      = game_json['loser']
    self.ran        = os.path.isfile(self.replay(0)) and os.path.isfile(self.replay(1)) and len(os.listdir(os.path.join(self.directory, 'write_0'))) > 0
  def won(self):
    return self.ran and self.winner == self.me
  def lost(self):
    return self.ran and self.winner == self.foe
  def inconclusive(self):
    return not self.ran or not (self.won() or self.lost())
  def replay(self, player=0):
    return os.path.join(self.directory, 'player_' + str(player) + '.rep')
    
def count_game(game_id):
  try:
    full_directory = os.path.join(games_root, game_id)
    full_path = os.path.join(full_directory, 'result.json')
    with open(full_path) as result_file:
      timestamp = os.path.getmtime(full_path)
      game = Game(game_id, full_directory, timestamp, json.load(result_file))
      foes.setdefault(game.foe, Matchup(game.foe)).games.append(game)
      maps.setdefault(game.map, Matchup(game.map)).games.append(game)
  except FileNotFoundError: pass
  except Exception as e:
    traceback.print_exc()
    print()

def print_matchups(matchup_dict):
  matchups = list(matchup_dict.values())
  games = list(itertools.chain.from_iterable([matchup.games for matchup in matchups]))
  matchups.sort(key=lambda x: x.winrate())
  matchups.append(Matchup("Overall"))
  matchups[-1].games = games
  
  left_width = 1 + max([len(matchup.name) for matchup in matchups])
  
  for matchup in matchups:
    print('{} {} ({} - {} - {} of {})'.format(
    '{}:'.format(matchup.name.ljust(left_width)),
    "{:.0%}".format(matchup.winrate())  .ljust(4),
    str(matchup.wins())                 .ljust(3),
    str(matchup.losses())               .ljust(3),
    str(matchup.inconclusive())         .ljust(3),
    str(matchup.total())))

def copy_losses():
  if len(replay_dir) < 20: raise Exception('Suspicious replay directory!')
  os.makedirs(replay_dir, exist_ok=True)
  for file in os.listdir(replay_dir): os.remove(os.path.join(replay_dir, file))
  matchups = foes.values()
  games = list(itertools.chain.from_iterable([matchup.games for matchup in matchups]))
  games.sort(key=lambda x: x.timestamp)
  for game in games:
    if game.lost():
      write_directory = os.path.join(game.directory, 'write_0')
      logs_directory = os.path.join(game.directory, 'logs_0')
      write_files = os.listdir(write_directory)
      log_files = os.listdir(logs_directory)
      filename_base = os.path.join(replay_dir, '{}-{}-{}'.format(game.timestamp, game.foe, game.id))
      shutil.copyfile(game.replay(), filename_base + '.rep')
      for written_file in write_files:
        shutil.copyfile(os.path.join(write_directory, written_file), filename_base + '.' + written_file)
      for logged_file in log_files:
        shutil.copyfile(os.path.join(logs_directory, logged_file), filename_base + '.' + logged_file)
  
def main():
  for game_id in os.listdir(games_root):
    count_game(game_id)
  print_matchups(foes)
  print_matchups(maps)
  copy_losses()

main()
