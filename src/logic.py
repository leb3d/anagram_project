def is_anagram(text_one, text_two):
feature
    # Додаткова функціональність: ігнорування пробілів та регістру
    clean_one = str(text_one).replace(" ", "").lower()
    clean_two = str(text_two).replace(" ", "").lower()
    return sorted(clean_one) == sorted(clean_two)
    return sorted(text_one) == sorted(text_two)
main
