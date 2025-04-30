import time

def shorten_strings(strings, target_length, log_file="shorten_log.txt"):
    """
    Сокращает строки до заданной длины, обеспечивая уникальность, и логирует процесс.
    Args:
        strings: Список входных строк.
        target_length: Желаемая длина сокращенных строк.
        log_file: Файл для логирования.
    Returns:
        Список сокращенных уникальних строк.
    """
    if target_length <= 0:
        raise ValueError("Довжина повинна бути додатньою")

    with open(log_file, 'a', encoding='utf-8') as f:
        # Логирование начала процесса
        f.write(f"\n{time.ctime()}: Початок скорочення\n")
        f.write(f"Вхідні рядки: {strings}\n")
        f.write(f"Цільова довжина: {target_length}\n")

        # Шаг 1: Обеспечиваем уникальность входных строк
        unique_strings = []
        count = {}
        for s in strings:
            if s in count:
                count[s] += 1
                unique_s = f"{s}{count[s]}"
                unique_strings.append(unique_s)
                f.write(f"Додано цифру до неунікального рядка: {s} -> {unique_s}\n")
            else:
                count[s] = 0
                unique_strings.append(s)

        # Шаг 2: Сокращаем строки
        shortened = []
        for s in unique_strings:
            if len(s) <= target_length:
                shortened.append(s)
            else:
                if target_length == 1:
                    shortened.append(s[0])
                elif target_length == 2:
                    shortened.append(s[:2])
                elif target_length == 3:
                    shortened.append(f"{s[0]}.{s[-1]}")
                elif target_length == 4:
                    shortened.append(f"{s[0]}..{s[-1]}")
                else:
                    dots = 3
                    start_len = (target_length - dots) // 2
                    end_len = target_length - dots - start_len
                    shortened.append(f"{s[:start_len]}...{s[-end_len:]}")
            f.write(f"Скорочено: {s} -> {shortened[-1]}\n")

        # Шаг 3: Обеспечиваем уникальность сокращенных строк
        result = []
        count = {}
        for s in shortened:
            if s in count:
                count[s] += 1
                result.append(f"{s}{count[s]}")
                f.write(f"Додано цифру до неунікального скороченого рядка: {s} -> {s}{count[s]}\n")
            else:
                count[s] = 0
                result.append(s)

        # Логирование результата
        f.write(f"Результат: {result}\n")
        f.write(f"{time.ctime()}: Кінець скорочення\n")

    return result

def main():
    print("Введіть рядки (вводьте порожній рядок для завершення):")
    strings = []
    while True:
        s = input()
        if s == "":
            break
        strings.append(s)

    try:
        target_length = int(input("Введіть бажану довжину скорочення: "))
        if target_length <= 0:
            raise ValueError("Довжина повинна бути додатною")
    except ValueError as e:
        print(f"Помилка: {e}")
        return

    result = shorten_strings(strings, target_length)

    print("\nСкорочені рядки:")
    for i, s in enumerate(result, 1):
        print(f"{i}. {s}")

if __name__ == "__main__":
    main()
