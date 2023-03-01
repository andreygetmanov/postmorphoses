import sounddevice
import soundfile
import pyttsx3


class SpeechGenerator:

    def __init__(self,
                 path: str = './audio.raw',
                 sample_rate_hz: int = 19200,
                 channels: int = 1,
                 subtype: str = 'pcm_16'
                 ):
        """
        :param path: path to created file
        :param sample_rate_hz: sample rate in Hz
        :param channels: number of channels
        :param subtype: subtype of the sound file
        """
        self.path = path
        self.sample_rate_hz = sample_rate_hz
        self.channels = channels
        self.subtype = subtype
        self.tts = pyttsx3.init()
        self.voices = self.tts.getProperty('voices')

    def play(self, text: str) -> None:
        """
        Synthesizes speech from the input string of text and plays it.
        :param text: text for synthesis
        :return: plays audio
        """
        self.tts.setProperty('voice', 'ru')
        self.tts.save_to_file(text, self.path)
        self.tts.runAndWait()
        audiodata, samplerate = soundfile.read(self.path, samplerate=self.sample_rate_hz,
                                               channels=self.channels, subtype=self.subtype)
        sounddevice.play(audiodata, samplerate=samplerate)
