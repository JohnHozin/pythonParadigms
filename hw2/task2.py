number = input()
number = int(number) if number.isdigit() else 10


def multiplication_table(n):
    for i in range(1, n):
        for j in range(1, 10):
            print(i, "*", j, "=", i * j)
        print("")


multiplication_table(number)

# Использовал структурную и процедурную парадигмы:
# процедурную, чтобы была возможность использовать этот метод в других файлах
# структурную, потому что использовал два цикла for и не использовал goto
