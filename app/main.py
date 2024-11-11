from hazm import *
# tagger = POSTagger(model='pos_tagger.model')
# print(tagger.tag(word_tokenize(Normalizer().normalize('کتاب نیلی عالی.'))))
# print(Normalizer().normalize('علی به یک آدم خل و چل تَبدیل شده که کتاب ها رو نِصفه رها می کند.'))
# print(Lemmatizer().lemmatize(Normalizer().normalize('میروم')))

bijankhan = BijankhanReader(bijankhan_file='./custom_datasets/bijankhan.txt')
sent = next(bijankhan.sents())
print(sent)