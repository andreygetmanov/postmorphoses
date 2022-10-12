import numpy as np
import pandas as pd

from model import GPTModel
from speech import SpeechGenerator


def get_data(path: str):
    data = pd.read_excel(path)
    return data['Left context'].fillna('') + data['Center'].fillna('') + \
           data['Punct'].fillna('') + data['Right context'].fillna('')


if __name__ == '__main__':
    texts = get_data('ruscorpora_content.xlsx')
    GPTModel = GPTModel()
    SpeechGenerator = SpeechGenerator(path='./audio.raw', folder_id='b1g7khuono0tf56uljpm')
    for text in texts:
        gen_text = GPTModel.generate(text)
        print(gen_text)
        SpeechGenerator.play(gen_text)
