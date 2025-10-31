# goit-cs-hw-01

## Завдання 1 — Програми на асемблері (NASM + DOSBox)

### Опис
Завдання демонструє створення та виконання програм мовою **Assembler (NASM)** у середовищі **DOSBox**.

Реалізовано дві програми:
1. **hello.asm** — виводить текст «Hello from NASM!».
2. **calc.asm** — запитує два однозначні числа (0–9), складає їх і виводить результат.

---

### Вимоги
- **NASM** (версія 3.01 або новіша)
- **DOSBox 0.74-3**

---

### Компіляція

#### Для `hello.asm`:
```bash
nasm -f bin hello.asm -o hello.com
```

#### Для `calc.asm`:
```bash
nasm -f bin calc.asm -o calc.com
```

Після компіляції в папці `task1` з’являються відповідні `.com` файли.

---

### Запуск у DOSBox

```dos
mount c C:\Projects\goit-cs-hw-01\task1
C:
hello
calc
```

---

### Приклад роботи

**hello.asm**
```
Hello from NASM!
```

**calc.asm**
```
Enter first digit (0-9): 3
Enter second digit (0-9): 5
Result = 8
```

---

## Завдання 2 — Аріфметичний інтерпретатор (Python)

### Опис
Програма реалізує простий **інтерпретатор арифметичних виразів**, який підтримує:
- операції `+`, `-`, `*`, `/`
- дужки `(`, `)`
- пріоритети операцій
- унарні оператори `+` і `-`

---

### Граматика
```
expr   : term ((PLUS | MINUS) term)*
term   : factor ((MUL | DIV) factor)*
factor : (PLUS | MINUS) factor | INTEGER | LPAREN expr RPAREN
```

---

### Структура проєкту
```
goit-cs-hw-01/
│
├── task1/
│   ├── hello.asm
│   ├── calc.asm
│   ├── hello.com
│   ├── calc.com
│
├── task2/
│   ├── interpreter.py
│   ├── tests/
│   │   ├── test_basic.py
│   │   └── test_parentheses.py
│
├── .gitignore
├── requirements.txt
├── README.md
└── pytest.ini
```

---

### Тестування (Task 2)

```bash
pytest -q
```
Результат:
```
....                                                                                                                    [100%]
4 passed in 0.02s
```

---
