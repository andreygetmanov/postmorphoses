import pandas as pd
import re

from scripts.model import GPTModel
from scripts.speech import SpeechGenerator
from scripts.manifest import Manifest


def offensive_filter(text_to_clean: str, offensive_words: list) -> str:
    swear_words = ['((х|x)(у|y)(й|е|ё|и|я|ли[^а-я]|э))',
                   '(п(и|е|ё)(з|с)д)', '([^а-я])(би?ля(д|т|[^а-я]))',
                   '(пид(о|а)р|п(е|и)дри)', '(муд(ак|ач|о|и))',
                   '(([^а-я]|по|на|от|не|ни)(х|x)(е|e)(р|p))', '(з(а|о)луп(а|и))',
                   '(([^а-я]у?|под?|на|за|от|вы|ь|ъ)(е|ё|и)б(а|ыр|у|нут|ись|ище))',
                   '([^а-я])((на|по)х)([^а-я])', '(pizd)', '(п(е|ё)рд(а|у|и|е|ё))'] + offensive_words
    pattern = re.compile('|'.join(swear_words), re.IGNORECASE)
    clean_text = pattern.sub('', text_to_clean)
    return clean_text


def censorship(text_to_clean: str) -> str:
    words_to_del = ['путин', 'хох', 'украин', 'войн', 'террор', 'правительств']
    pattern = re.compile('|'.join(words_to_del), re.IGNORECASE)
    clean_text = pattern.sub('у меня нет слов', text_to_clean)
    return clean_text


def get_data(path: str):
    data = pd.read_excel(path)
    return data['Left context'].fillna('') + data['Center'].fillna('') + \
           data['Punct'].fillna('') + data['Right context'].fillna('')


if __name__ == '__main__':
    texts = get_data('data/ruscorpora_content.xlsx')
    offensive_words = open('data/offensive_words.txt', 'r', encoding='utf-8').read().split(', ')
    text_file = 'data/text_for_gen.txt'
    manifest = Manifest(pause=0.07)
    history = manifest.read_txt(text_file)
    GPTModel = GPTModel()
    SpeechGenerator = SpeechGenerator()
    while True:
        for text in texts:
            new_text = manifest.read_txt(text_file)
            if new_text != history:
                text = new_text if new_text else text
                history = text
            gen_text = censorship(offensive_filter(GPTModel.generate(text), offensive_words))
            SpeechGenerator.play(gen_text)
            manifest.print_one_by_one(gen_text)
