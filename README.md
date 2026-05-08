# Foundations of Data Structures & Algorithms in Python
___
Цей репозиторій – мій особистий прогрес-звіт з курсу DSA на Python. Кожна папка відповідає окремому модулю і містить теоретичні нотатки, реалізації та розв'язки задач з LeetCode.
Кожний блок містить свій детальний опис. В цьому ж документі лише короткі відмості та посилання на файли.
---
Я обрав цей курс з метою підготовки до іспиту по ООП та Структурах Даних. Даний курс містив багато практичних ідей для розвʼязання 
задач тому здебільшого був для мене корисним. Мені дуже сподобалось скільки часу було витрачено на звʼязні списки, та скільки задач було побудованих 
саме на них. Більшість задач у мене уже були розвʼязанв, тому я їх стирав і писав заново.
___
Найскладнішими для мене був не матеріал, а деякі задачі на літкоді, як от Перевірка Валідності Судоку та 3Sum. 
Також я дізнався нову інформацію про хеш таблиці, а саме теоретичну базу про хеш функцію та те, під капотом це буквально масив.
___
За це курс я відточив свої навички програмування. Я зрозумів, що краще писати if cur is not None замість if not cur. 
Я Зрозумів будову хеш таблиці, та різні способи обходу колізії. Написав свою імплементацію хеш таблиці. Розвʼязав більше 25 задачок на літкоді.
Пригадав метод реверсу для звʼязного списку. Пригадав імплементацію counting sort. 
___
Незмістовним був блок сортування. По перше, я знав кожний з цих алгоритмів, тому всі імплементації написав майже з памʼяті. Задачі на сортування
також не були якимись особливими. 
___

## Структура репозиторію

```
Mini-project/
├── Course Introduction/
├── Time & Space Complexity/
├── Arrays/
├── Sorting/
├── Linked List/
├── Hash Table/
├── Full Course short test passed.png
├── Grades from the course.png
├── Passed final test with all questions from whole course.png
└── Passed the course.png
```
---

## Модулі

### [Course Introduction](./Course%20Introduction/)
Стратегії для ефективного розв'язання задач, підходи до LeetCode та опис DSA курсу.

---

### [Time & Space Complexity](./Time%20&%20Space%20Complexity/)
Основи аналізу алгоритмів: часова та просторова складність, Big O нотація, рекурсія.

---

### [Arrays](./Arrays/)
Повторив структуру даних – масиви.
- Різниця між статичними та динамічними масивами.
- Вставка / видалення: `O(1)` vs `O(n)`.

**Розв'язані задачі:**
[Max Consecutive Ones](./Arrays/485.%20Max%20Consecutive%20Ones.py) ·
[Best Time to Buy and Sell Stock](./Arrays/121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock.py) ·
[Product of Array Except Self](./Arrays/238.%20Product%20of%20Array%20Except%20Self.py) ·
[Rotate Array](./Arrays/189.%20Rotate%20Array.py) ·
[Maximum Subarray](./Arrays/53.%20Maximum%20Subarray.py) ·
[Maximum Product Subarray](./Arrays/152.%20Maximum%20Product%20Subarray.py) ·
[Valid Sudoku](./Arrays/36.%20Valid%20Sudoku.py)

---

### [Sorting](./Sorting/)
Згадав основні алгоритми сортування, переваги та недоліки кожного.

| Алгоритм | Складність |
|---|---|
| Bubble Sort, Insertion Sort | `O(n²)` |
| Merge Sort, Quick Sort | `O(n log n)` |
| Counting Sort | `O(n)` |

**Розв'язані задачі:**
[Sort Colors](./Sorting/LeetCode%20problems/75.%20Sort%20Colors.py) ·
[Majority Element](./Sorting/LeetCode%20problems/169.%20Majority%20Element.py) ·
[Move Zeroes](./Sorting/LeetCode%20problems/283.%20Move%20Zeroes.py)

---

### [Linked List](./Linked%20List/)
Дані в пам'яті лежать розкидано, кожна нода вказує на наступну.
- Додавання / видалення з початку: `O(1)`.
- Пошук / видалення з кінця: `O(n)`.

**Розв'язані задачі:**
[Add Two Numbers](./Linked%20List/LeetCode%20Problems/2.%20Add%20Two%20Numbers.py) ·
[Remove Nth Node From End](./Linked%20List/LeetCode%20Problems/19.%20Remove%20Nth%20Node%20From%20End%20of%20List.py) ·
[Merge Two Sorted Lists](./Linked%20List/LeetCode%20Problems/21.%20Merge%20Two%20Sorted%20Lists.py) ·
[Linked List Cycle](./Linked%20List/LeetCode%20Problems/141.%20Linked%20List%20Cycle.py) ·
[Linked List Cycle II](./Linked%20List/LeetCode%20Problems/142.%20Linked%20List%20Cycle%20II.py) ·
[Intersection of Two Lists](./Linked%20List/LeetCode%20Problems/160.%20Intersection%20of%20Two%20Linked%20Lists.py) ·
[Reverse Linked List](./Linked%20List/LeetCode%20Problems/206.%20Reverse%20Linked%20List.py) ·
[Palindrome Linked List](./Linked%20List/LeetCode%20Problems/234.%20Palindrome%20Linked%20List.py) ·
[Middle of the Linked List](./Linked%20List/LeetCode%20Problems/876.%20Middle%20of%20the%20Linked%20List.py)

---

### [Hash Table](./Hash%20Table/)
Хеш-таблиця (словник у Python) це оптимальна структура для багатьох задачок з великими масивами даних. Ключ проходить через хеш-функцію і перетворюється на індекс у масиві.
- **Швидкість:** Доступ / додавання за `O(1)`.
- **Колізії:** Коли різні ключі мають один індекс.
- **Keys:** Тільки immutable типи (strings, numbers, tuples).

**Розв'язані задачі:**
[Two Sum](./Hash%20Table/LeetCode%20problems/1.%20Two%20Sum.py) ·
[3Sum](./Hash%20Table/LeetCode%20problems/15.%203Sum.py) ·
[Group Anagrams](./Hash%20Table/LeetCode%20problems/49.%20Group%20Anagrams.py) ·
[Longest Consecutive Sequence](./Hash%20Table/LeetCode%20problems/128.%20Longest%20Consecutive%20Sequence.py) ·
[Contains Duplicate](./Hash%20Table/LeetCode%20problems/217.%20Contains%20Duplicate.py)

---

## Результати

![Grades](./Grades%20from%20the%20course.png)
![Passed](./Passed%20the%20course.png)