import random
import time

def DiceGame(message):
    # parse command.
    command = message.content.split(" ")
    dice = command[2].split("d")
    try:
        dice_count = int(dice[0])
        point = int(dice[1])
        determination = int(command[3]) if len(command) == 4 else None
    except:
        return "投擲失敗（指令錯誤）。"

    # Run dice.
    points = list()
    random.seed(time.time())

    for i in range(dice_count):
        points.append(random.randint(1, point))

    result = f"投擲出了：{', '.join([str(i) for i in points])} - 總計：{sum(points)}"

    if determination != None:
        return f"{result} \n判定『{'失敗'if sum(points) < determination else '成功'}』"
    return result
