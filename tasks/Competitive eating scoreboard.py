class Refereeing:
  def __init__(self, dict):
    self.dict = dict

  @property
  def count_of_points(self):
    lst_participant = []
    for participant in self.dict:
      # Рассчитываем общий счёт участника
      count = (participant.get('chickenwings', 0) * 5) + (participant.get('hamburgers', 0) * 3) + \
              (participant.get('hotdogs', 0) * 2)
      # Создаём словарь с именем и счётом участника
      property = {
        'name': participant["name"],
        'score': count
      }

      lst_participant.append(property)

    # Сортируем участников по убыванию очков, затем по имени
    lst_participant.sort(key=lambda x: (-x["score"], x["name"]))
    return  lst_participant


def scoreboard(who_ate_what):
    return Refereeing(who_ate_what).count_of_points
