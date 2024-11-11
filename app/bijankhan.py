from hazm import *
from ambg_word_reader import MetadataReader
bijankhan = BijankhanReader(bijankhan_file='../custom_datasets/bijankhan.txt', joined_verb_parts=False)
meta_reader = MetadataReader()
final_sents = []
normalizer = Normalizer(remove_diacritics=False, remove_specials_chars=False, persian_numbers=False)
for idx, sent in enumerate(bijankhan.sents()):
    for word, pos in sent:
        if meta_reader.isin(word):
            final_sents.append(normalizer.normalize(meta_reader.label_ambg(sent)))
            break
    if idx % 100 == 0:
        print(f'___{idx}___')
print(len(final_sents))
with open('./bijankhan.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(final_sents))
