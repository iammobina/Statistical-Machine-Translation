from __future__ import unicode_literals
from __future__ import unicode_literals

import pandas as pd
import csv
import codecs
# cp1252
from char_normalizer import persian_normalizer, arabic_normalizer
import hazm
import nltk
import stop_words
from stop_words import get_stop_words
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
def nom(text):
    normalizer = Normalizer()
    s = normalizer.normalize(text)
    print(s)
    return s


def normalizer():
    with open('translationparallecorpus-sample1.csv', 'r', encoding="utf8") as file_reader:
        with open('translationparallecorpus-sample2.csv', 'w+', encoding="utf8") as file_writer:
            try:
                readers = csv.reader(file_reader)
                writer = csv.writer(file_writer, delimiter='|')
                for row in readers:
                    print(readers)
                    print(row)
                    persian = persian_normalizer(row[0])
                    arabic = arabic_normalizer(row[1])
                    print(persian)
                    print(arabic)
                    row[0] = persian
                    row[1] = arabic
                    print(row)
                    writer.writerow(row)
            except Exception as e:
                print("exception")
                for row in readers:
                    print(readers)
                    print(row)
                    text = persian_normalizer(readers[0])
                    ar = arabic_normalizer(readers[1])


def contains_number(sent):
    for char in sent:
        if char.isdigit():
            sent = sent.replace(char, " ")
    return sent


def contains_element(sent):
    element = ['ِ', 'ُ', 'َ', 'ً', 'ٍ', 'ٌ', '-', '_', '/', ':', '(   )', '(   )', '(  ،   ،   )', '(طه:    )', '( )',
               '?', '(ص    )', '(   / )', '   ', '  ','،', '*', '    ', '(    )', '!', '(', ')', "[", "]", '.', '؟']
    for char in sent:
        for el in element:
            if el in char:
                sent = sent.replace(el, '')
                sent = sent.strip()
    return sent


def remove_numbers():
    # normalizer = Normalizer()
    with open('machinet/src.csv', 'r', encoding="utf8") as file:

        src = open("./machinet/src3.txt", "a", encoding="utf-8")
        trg = open("./machinet/trg3.txt", "a", encoding="utf-8")
        arabic = []

        try:
            readers = csv.reader(file)
            for row in readers:
                arabic.append(nltk.sent_tokenize(row[0],'ar'))
                row[1] = hazm.sent_tokenize(row[1])
                if '.' not in str(row[0]) and str(row[1]):
                    row[0] = [normalizer.normalize(i) for i in row[0]]
                    row[1] = [normalizer.normalize(i) for i in row[1]]

                    row[0] = [persian_normalizer(i) for i in row[0]]
                    row[1] = [arabic_normalizer(i) for i in row[1]]

                    if '»' in row[0] or row[1]:
                        row[0] = [item.replace('»', '') for item in row[0]]
                        row[1] = [item.replace('»', '') for item in row[1]]

                    if '«' in row[1] or row[1]:
                        row[0] = [item.replace('«', '') for item in row[0]]
                        row[1] = [item.replace('«', '') for item in row[1]]

                    row[0] = [contains_number(i) for i in row[0]]
                    row[1] = [contains_number(i) for i in row[1]]

                    row[0] = [contains_element(i) for i in row[0]]
                    row[1] = [contains_element(i) for i in row[1]]

                    for sen in row[0]:
                        src.write(sen)
                        src.write(' ')
                        src.write("\n")
                    for tg in row[1]:
                        trg.write(tg)
                        trg.write(' ')
                        trg.write("\n")
        except Exception as e:
            print("{}".format(e))

    src.close()
    trg.close()


if __name__ == '__main__':
    # nltk.download('punkt')
    doc_a = "10 - أخرج أحمد و الطبراني في الكبير، و رجال أحمد رجال الصحيح، من طريق عبد اللّه بن حنظلة غسيل الملائكة مرفوعا: «درهم ربا يأكله الرجل و هو يعلم، أشدّ من ست و ثلاثين زنية»"
    doc_a = doc_a.encode().decode('utf-8')
    sw = stopwords.sents('arabic')
    tokens = nltk.sent_tokenize(doc_a)
    print(tokens)
    # remove_numbers()
