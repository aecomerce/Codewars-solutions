class Pong:
  def __init__(self, max_score):
    self.max_score = max_score;
    self.score_players = [0, 0]
    self.current_player = 0 # Текущий игрок: 0 - игрок 1, 1 - игрок 2
    self.game_over = False

  def play(self, ball_pos, player_pos):
    if self.game_over:
      return 'Game Over!'

    # Проверяем, попал ли игрок по мячу
    if (player_pos - 3) <= ball_pos <= (player_pos + 3):
      result = f'Player {self.current_player + 1} has hit the ball!'
    else:
      # Игрок промахнулся
      self.score_players[1 - self.current_player] += 1
      if self.score_players[1 - self.current_player] == self.max_score:
        self.game_over = True
        return f"Player {2 - self.current_player} has won the game!"
      result =  f'Player {self.current_player + 1} has missed the ball!'

    self.current_player = 1 - self.current_player
    return result
