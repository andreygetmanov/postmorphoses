import requests
import sounddevice
import soundfile


class SpeechGenerator:

    def __init__(self,
                 path: str,
                 folder_id: str,
                 api_token: str = None,
                 voice: str = 'filipp',
                 lang: str = 'ru-RU',
                 format: str = 'lpcm',
                 sample_rate_hz: int = 48000,
                 channels: int = 1,
                 subtype: str = 'pcm_16'
                 ):
        """
        :param path: path to created file
        :param folder_id: YandexCloud folder id
        :param api_token: YandexCloud auth token
        :param voice: voice type
        :param lang: language
        :param format: format of synthesized data
        :param sample_rate_hz: sample rate in Hz
        :param channels: number of channels
        :param subtype: subtype of the sound file
        """
        self.path = path
        self.folder_id = folder_id
        self.api_token = api_token if api_token else self._get_api_token()
        self.voice = voice
        self.lang = lang
        self.format = format
        self.sample_rate_hz = sample_rate_hz
        self.channels = channels
        self.subtype = subtype

    def play(self, text: str) -> None:
        """
        Synthesizes speech from the input string of text and plays it.
        :param text: text for synthesis
        :return: plays audio
        """
        with open(self.path, "wb") as f:
            for audio_content in self._synthesize(text=text):
                f.write(audio_content)
        audiodata, samplerate = soundfile.read(self.path, channels=self.channels,
                                               samplerate=self.sample_rate_hz, subtype=self.subtype)
        sounddevice.play(audiodata, blocking=True)

    def _synthesize(self, text: str) -> bytes:
        """
        Synthesizes speech (in binary format) from the input string of text.
        :param text: text for synthesis
        :return: array of bytes
        """
        url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'
        headers = {
            'Authorization': 'Api-Key ' + self.api_token,
        }

        data = {
            'text': text,
            'folderId': self.folder_id,
            'voice': self.voice,
            'lang': self.lang,
            'format': self.format,
            'sampleRateHertz': self.sample_rate_hz
        }

        with requests.post(url, headers=headers, data=data, stream=True) as resp:
            if resp.status_code != 200:
                raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))

            for chunk in resp.iter_content(chunk_size=None):
                yield chunk

    @staticmethod
    def _get_api_token() -> str:
        with open('auth.txt', 'r') as f:
            token = f.read().split(':')[1]
        return token
