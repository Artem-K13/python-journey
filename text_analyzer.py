text = input("Введите текст: ")

# Убираем знаки препинания
text = text.replace(",", "")
text = text.replace(".", "")
text = text.replace("!", "")
text = text.replace("?", "")

# Приводим к нижнему регистру и разбиваем на слова
words = text.lower().split()

# Считаем частоту каждого слова
freq = {}
for word in words:
    if word in freq:
        freq[word] = freq[word] + 1
    else:
        freq[word] = 1

# Уникальные слова
unique_words = set(words)

# Сортировка по частоте (от большего к меньшему)
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# Вывод статистики
print(f"\nВсего слов: {len(words)}")
print(f"Уникальных слов: {len(unique_words)}")

print("\nТоп-5 слов:")
for i, (word, count) in enumerate(sorted_freq[:5]):
    print(f"{i + 1}. {word} — {count} раз(а)")

print(f"\nУникальные слова: {', '.join(unique_words)}")