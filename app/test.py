from plain_reader import PlainReader
from ambg_word_reader import MetadataReader
reader = PlainReader(['./bj-test.txt'])
meta_reader = MetadataReader()
for sent in reader.sents():
    print(meta_reader.label_ambg(sent))