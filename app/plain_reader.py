class PlainReader:
    def __init__(self, paths = []) -> None:
        self.paths = paths 
        self.__generate_sentences()
    
    def __generate_sentences(self):
        self.sentences = []
        for path in self.paths:
            with open(path, 'r', encoding='utf-8') as f:
                self.sentences += [[(word, '') for word in sent.strip('.').split()] for sent in f.read().split('\n')]
    
    def sents(self): return self.sentences