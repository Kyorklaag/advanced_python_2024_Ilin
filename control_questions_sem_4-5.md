# Ответы на контрольные вопросы
1. Суть полиморфизма - единый интерфейс на множественные реализации. Не нужно прописывать функции для разных комбинаций типов данных.
2. Метод __radd__ нужен на тот случай, если реализация сложения зависит от расположения слагаемых, например можно прибавить число к структуре данных, но не наоборот.
3. Дочерний класс наследует методы родительского, то есть методы предка так же выполняются и у потомка, при том, что их не нужно прописывать отдельно.
4. Ключевое слово Super() применяется для вызова реализации из материнского класса для дополнения в дочернем классе.
5. Порядок классов определяет то, из какого материнского класса будут вызываться определённые методы.
6. Обработка исключений нужна для того, чтобы понять, есть ли ошибка в программе и как её исправить в случае её наличия.
7. Вне зависимости от того, есть исключение или нет, в конце нужно выполнить некоторое действие, за которое и отвечает finally.
8. Можно реализовать класс, который будет наследоваться от исключения. Вызываться этот класс будет с помощью команды raise.
9. Генератор создаёт значения по требованию, то есть не имеет привязки к какому-либо итерируемому файлу. Итератор же производит какие-то действия над файлом.
10. С декоратором функция работает медленнее.
