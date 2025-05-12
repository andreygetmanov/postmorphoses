import pandas as pd

from scripts.model import GPTModel
from scripts.speech import SpeechGenerator
from scripts.manifest import Manifest


def get_data(path: str):
    """
    Concatenates columns from an Excel file into a single string series.

        Reads an Excel file, extracts specified columns ('Left context', 'Center',
        'Punct', and 'Right context'), fills any missing values with empty strings,
        and concatenates the values in each row into a single string.

        Args:
            path: The path to the Excel file.

        Returns:
            pd.Series: A Pandas Series containing the concatenated strings.
    """
    data = pd.read_excel(path)
    return (
        data["Left context"].fillna("")
        + data["Center"].fillna("")
        + data["Punct"].fillna("")
        + data["Right context"].fillna("")
    )


if __name__ == "__main__":
    texts = get_data("data/ruscorpora_content.xlsx")
    text_file = "data/text_for_gen.txt"
    manifest = Manifest(pause=0.07)
    history = manifest.read_txt(text_file)
    GPTModel = GPTModel()
    SpeechGenerator = SpeechGenerator(folder_id="b1g7khuono0tf56uljpm", voice="alena")
    while True:
        for text in texts:
            new_text = manifest.read_txt(text_file)
            if new_text != history:
                text = new_text if new_text else text
                history = text
            gen_text = GPTModel.generate(text)
            SpeechGenerator.play(gen_text)
            manifest.print_one_by_one(gen_text)
