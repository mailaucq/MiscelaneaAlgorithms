__author__ = 'laura'
# Identificar opiniones
# Identificar entidades
# Identificar propiedades
# Temporalidad
# Analizar sentimiento
#


name_coca_cola = ["coca light", "coca cola", "cocacola", "bug bunny"]


def n_grams(num_gram, sentence):
    sentence = sentence.lower()
    words_n_grams = []
    words = sentence.split(" ")

    word_n_gram = ""
    i = 0
    while i < len(words):
        cont = 0
        while (i + cont) < len(words) and cont < num_gram:
            word_n_gram += words[i + cont]
            if cont < num_gram - 1:
                word_n_gram += " "
            cont += 1
        if word_n_gram in name_coca_cola:
            words_n_grams.append(word_n_gram)
            i = i + cont
        else:
            words_n_grams.append(words[i])
            i += 1
        word_n_gram = ""
    return words_n_grams


def main():
    sentences_text = "Bug Bunny, me gusta mi coca cola"
    sentences = sentences_text.split(", ")
    for sentence in sentences:
        words = n_grams(2, sentence)
        print(words)


if __name__ == "__main__":
    main()