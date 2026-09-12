from random import randrange

    
HELP = """-----------------------------------------------------------
Правила приложения:
    Считаем, что пользователь вводит числа правильно
    Пользователь вводит размер лабиринта n, m через пробел 
    n >= 1, m >= 1
-----------------------------------------------------------
Команды:
    'start' или '1' - Начать создание лабиринта
    'help' или '2' - Помощь
    'exit' или '0' - Выход
-----------------------------------------------------------"""


def draw(maze, size):
    maze_list = [[" " for _ in range(size[0])] for _ in range(size[1])]
    maze_list[0] = ["#" for _ in range(size[0])]
    maze_list[-1] = ["#" for _ in range(size[0])]

    for i in range(1, size[1] - 1):
        maze_list[i][0] = "#"
        maze_list[i][-1] = "#"

    print(f"(Инициализация) лабиринта {size[0]} x {size[1]} размера")
    print("\n".join([" ".join(i) for i in maze_list]))

    for i, level in enumerate(maze, 1):
        input("<W> 'Enter чтобы продолжить'")
        print(f"\n Уровень {i} ======================================================\n")
        for k, v in enumerate(level, 1):
            print(f"\n<W> Уровень {i} шаг {k} -----------------------------------------------------\n")
            # Стена
            if v[0][1][0] == 1:
                for y in range(v[0][0][1], v[0][0][1] + v[0][1][1]):
                    maze_list[y][v[0][0][0]] = "#"
            else:
                for x in range(v[0][0][0], v[0][0][0] + v[0][1][0]):
                    maze_list[v[0][0][1]][x] = "#"

            # Дверь
            maze_list[v[1][1]][v[1][0]] = " "

            # Рисуем
            print("\n".join([" ".join(i) for i in maze_list]))


def maze(pos, size):
    if min(size) < 3 or max(size) < 7:
        return []
    
    if size[0] == max(size):
        wall = ((randrange(4, size[0] - 3 + 1, 2) + pos[0], 1 + pos[1]), (1, size[1]))
        door = (wall[0][0], randrange(1, size[1] + 1, 2) + pos[1])
        
        left = maze(pos, (wall[0][0] - 1 - pos[0], size[1]))
        right = maze((wall[0][0], pos[1]), (pos[0] + size[0] - wall[0][0], size[1]))
    else:
        wall = ((1 + pos[0], randrange(4, size[1] - 3 + 1, 2) + pos[1]), (size[0], 1))
        door = (randrange(1, size[0] + 1, 2) + pos[0], wall[0][1])

        left = maze(pos, (size[0], wall[0][1] - 1 - pos[1]))
        right = maze((pos[0], wall[0][1]), (size[0], pos[1] + size[1] - wall[0][1]))

    levels = [[[wall, door]]]
    for branch in (left, right):
        for i, lvl in enumerate(branch):
            if i + 1 < len(levels):
                levels[i + 1] = levels[i + 1] + lvl
            else:
                levels += [list(lvl)]
    return levels
        

def start(n, m):
    draw(maze((0, 0), (n - 2, m - 2)), (n, m))


def main():
    print(f"""===========================================================
    Добро пожаловать в создание лабиринта
{HELP}
============================================================""")

    while True:
        inp = input("</> Введите команду: ")
        if inp in ("help", "2"):
            print(HELP)
        elif inp in ("start", "1"):
            n, m = map(int, input("<I> Ввод размера n, m лабиринта (через пробел): ").split())
            start(n, m)
        elif inp in ("exit", "0"):
            break
        else:
            print("<E> Неправильная команда")
        

if __name__ == "__main__":
    main()