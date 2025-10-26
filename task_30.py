# todo: Вы работаете с данными цен товаров, которые приходят в разном формате.
# Создайте список числовых значений цен,  игнорируя некорректные записи.
# Все цены переведите в рубли. Задачу следует решить с использованием списковых включений.

prices = ["₽1500", "20.50 USD", "invalid", "€25.00", "$15.99",  "18.99", "N/A", "¥5000"]

prices = [p for p in prices if '₽' in p or 'USD' in p or '€' in p or '$' in p or '¥' in p]
prices = ['₽' + str(79.6 * float(''.join([c for c in p if c.isdigit() or c == '.']))) if 'USD' in p else p for p in prices]
prices = ['₽' + str(93.8 * float(''.join([c for c in p if c.isdigit() or c == '.']))) if '€' in p else p for p in prices]
prices = ['₽' + str(round(79.6 * float(''.join([c for c in p if c.isdigit() or c == '.'])), 2)) if '$' in p else p for p in prices]
prices = ['₽' + str(0.52 * float(''.join([c for c in p if c.isdigit() or c == '.']))) if '¥' in p else p for p in prices]
print(prices)
