# Задание 2.10. Считать с клавиатуры произвольную строку.
# Преобразовать строку так, чтобы каждое слово начиналось с заглавной буквы.

text = input('Введите строку: ')
final_text = ''
# Флаг, указывающий, что предыдущий символ был пробелом (начало слова)
new_word = True

for i in range(len(text)):
    if text[i].isalpha():
        if new_word:
            # Преобразуем букву в заглавную через ord и chr
            if 'a' <= text[i] <= 'z':
                final_text += chr(ord(text[i]) - 32)
            elif 'а' <= text[i] <= 'я':
                final_text += chr(ord(text[i]) - 32)
            else:
                final_text += text[i]
            new_word = False
        else:
            final_text += text[i]
    else:
        final_text += text[i]
        new_word = True

print("Результат преобразования:", final_text)