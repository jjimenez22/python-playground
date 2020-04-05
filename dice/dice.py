import random


def roll_die():
    return random.choice([1, 2, 3, 4, 5, 6])


def roll_dice(dice_num):
    result = 0
    for _ in range(dice_num):
        result += roll_die()
    return result


if __name__ == '__main__':
    sim_num = int(input('Insertate tu numero de simulaciones -> '))
    dice_num = int(input('Insertate tu numero de dados por simulacion -> '))
    expected = int(input('Inserta el valor esperado -> '))
    success_count = 0
    for _ in range(sim_num):
        if roll_dice(dice_num) == expected:
            success_count += 1

    print(f'prob: {success_count / sim_num}')
