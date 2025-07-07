import time
def shorten_strings(strings, target_length, log_file="shorten_log.txt"):
    if target_length<3:
        raise ValueError("Довжина повинна бути не менше 3, щоб забезпечити щонайменше одну крапку між першою та останньою буквою")
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"\n{time.ctime()}: Початок скорочення\n")
        f.write(f"Вхідні рядки: {strings}\n")
        f.write(f"Цільова довжина: {target_length}\n")
    count={}
    for s in strings:
        count[s]=count.get(s, 0)+1
    unique_origs=list(dict.fromkeys(strings))
    short_map={} 
    used_shorts=set()
    for orig in unique_origs:
        if len(orig)<=target_length:
            short=orig
        else:
            for dots in [3, 2, 1]:
                if target_length==3 and dots!=1:
                    continue
                if target_length==4 and dots!=2:
                    continue
                if target_length==5 and dots!=3:
                    continue
                remaining=target_length-dots-2
                if remaining<0:
                    continue
                start_len=(remaining+1)//2
                end_len=remaining-start_len
                candidate=f"{orig[:start_len+1]}{'.' * dots}{orig[-(end_len+1):]}"
                if candidate not in used_shorts:
                    short=candidate
                    used_shorts.add(short)
                    break
            else:
                short=f"{orig[:start_len+1]}{'.' * dots}{orig[-(end_len+1):]}"
                used_shorts.add(short)
        short_map[orig]=short
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"Скорочено: {orig} -> {short}\n")
    shortened=[short_map[orig] for orig in strings]
    result=[]
    seen={}
    for orig, short in zip(strings, shortened):
        if orig in seen:
            seen[orig] += 1
            unique_short=f"{short}{seen[orig]}"
            result.append(unique_short)
            with open(log_file, 'a', encoding='utf-8') as f:
                f.write(f"Додано цифру до неунікального скороченого рядка: {short} -> {unique_short} (оригінал: {orig})\n")
        else:
            seen[orig]=0
            result.append(short)
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"Обробка: {orig} -> {result[-1]}\n")
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"Результат: {result}\n")
        f.write(f"{time.ctime()}: Кінець скорочення\n")
    return result
def main():
    print("Введіть рядки (вводьте порожній рядок для завершення):")
    strings=[]
    while True:
        s=input()
        if s=="":
            break
        strings.append(s)
    try:
        target_length=int(input("Введіть бажану довжину скорочення (не менше 3): "))
        if target_length<3:
            raise ValueError("Довжина повинна бути не менше 3, щоб забезпечити щонайменше одну крапку між першою та останньою буквою")
    except ValueError as e:
        print(f"Помилка: {e}")
        return
    result=shorten_strings(strings, target_length)
    print("\nСкорочені рядки:")
    for i, s in enumerate(result, 1):
        print(f"{i}. {s}")
if __name__=="__main__":
    main()