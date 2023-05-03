# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

names = 5
files = 'ffdsgdg'
s = 5
active = 5

def check_names(name) -> None:
    all_vars = [(var, values) for var, values in globals().items() if not var.startswith('__')]
    changed = {}
    for var in all_vars:
        if var[0] == 's':
            continue
        elif var[0].endswith('s') and len(var[0]) > 1:
            changed[var[0][:-1]] = var[1]
            changed[var[0]] = None
    for key in changed:
        globals()[key] = changed.get(key)

print(globals())
check_names()
print(globals())

