import pandas as pd
from hazm import Lemmatizer

class MetadataReader:
    def __init__(self) -> None:
        self.df = pd.read_csv('ambg_words.csv')
        self.words = self.df['word'].unique()
        self.__init_word_map()
        self.modifier = '#'
        self.lem = Lemmatizer()
        
    def __init_word_map(self):
        self.word_map = {}
        for w in self.words:
            self.word_map[w] = True
    
    def isin(self, w):
        possibles = [w] + self.lem.lemmatize(w).split('#')
        for poss in possibles:
            if self.word_map.get(poss, False):
                return True
        return False

    def label_ambg(self, sentence):
        labeled_sentence = []
        for word, _ in sentence:
            if self.isin(word):
                labeled_sentence.append(f'{self.modifier}{word}{self.modifier}')
            else:
                labeled_sentence.append(word)
        return ' '.join(labeled_sentence)
    
    def show_isin(self, sent):
        words = sent.split()
        for word in words:
            if self.word_map.get(word, False):
                print(word)
                break

if __name__ == "__main__":
    meta_reader = MetadataReader()
    while True:
        meta_reader.show_isin(input('sentence: '))