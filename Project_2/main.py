HELP = """-----------------------------------------------------------
Правила приложения:
    Считаем, что пользователь вводит числа правильно
    Для шифратора нужно указать шифруемую строку, 
        а также числа k, m через пробел
    Для дешифратора нужно указать шифровку, 
        ключ и k, m через пробел
-----------------------------------------------------------
Команды:
    'encoder' или '1' - Шифратор
    'decoder' или '2' - Дешифратор
    'help' или '3' - Помощь
    'exit' или '0' - Выход
-----------------------------------------------------------"""


def getCaesar(s, m):
    return "".join([chr((ord(i) + m - 65) % 26 + 65) if 65 <= ord(i) <= 90 else chr((ord(i) + m - 97) % 26 + 97) if 97 <= ord(i) <= 122 else i for i in s])


def encoder(s, k, m):
    step2 = s.split()
    print("<W> Шаг 2", step2)

    step3 = step2[::-1]
    print("<W> Шаг 3", step3)

    step4 = step3[-k:] + step3[:-k]
    print("<W> Шаг 4", step4)

    step5 = [i[-1] + i[1:-1] + i[0] if len(i) >= 2 else i for i in step4]
    print("<W> Шаг 5", step5)

    step6 = [getCaesar(i, m) for i in step5]
    print("<W> Шаг 6", step6)

    step7 = " ".join(step6)
    print("<W> Шаг 7", step7)

    step8 = {v: 100 + i for i, v in enumerate(sorted(set(step7), key=lambda x: step7.find(x)))}
    print("<W> Шаг 8", step8, f"\n<key>{''.join(step8)}<key>")

    step9 = "".join([str(step8[i]) for i in step7])
    print("<W> Шаг 9 (итог)", step9)


def decoder(s, key, k, m):
    step2 = {100 + i: v for i, v in enumerate(key)}
    print("<W> Шаг 2", step2)

    step3 = [step2[int(s[i * 3:i * 3 + 3])] for i in range(len(s) // 3)]
    print("<W> Шаг 3", step3)

    step4 = [getCaesar(i, -m) for i in step3]
    print("<W> Шаг 4", step4)

    step5 = "".join(step4).split()
    print("<W> Шаг 5", step5)

    step6 = [i[-1] + i[1:-1] + i[0] if len(i) >= 2 else i for i in step5]
    print("<W> Шаг 6", step6)

    step7 = step6[k:] + step6[:k]
    print("<W> Шаг 7", step7)

    step8 = step7[::-1]
    print("<W> Шаг 8", step8)

    step9 = " ".join(step8)
    print("<W> Шаг 9 (итог)", step9)


def main():
    print(f"""===========================================================
    Добро пожаловать в приложении Шифратор/Дешифратор
{HELP}
============================================================""")

    while True:
        inp = input("</> Введите команду: ")
        if inp in ("encoder", "1"):
            s = input("<W> Шаг 1 (ввод)\n<I> Введите строку: ")
            k, m = map(int, input("<I> Введите числа k, m (через пробел): ").split())
            encoder(s, k, m)
        elif inp in ("decoder", "2"):
            s = input("<W> Шаг 1 (ввод)\n<I> Ввод шифровки: ")
            key = input("<I> Ввод ключа для расшифровки: ")
            k, m = map(int, input("<I> Введите числа k, m (через пробел): ").split())
            decoder(s, key, k, m)
        elif inp in ("help", "3"):
            print(HELP)
        elif inp in ("exit", "0"):
            break
        else:
            print("<E> Неправильная команда")
        


if __name__ == "__main__":
    main()