"""
This script will transcribe an audio file using the Whisper ASR model.
It will download the model to download_root=".cache/whisper" if it is not already present.
It will save the transcription to a text file named "transcription_{model_name}.txt".
"""

from enum import StrEnum
import whisper


class ModelName(StrEnum):
    TINY = "tiny"
    BASE = "base"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


def transcribe_to_file(model_name: ModelName, audio_path: str) -> None:
    model = whisper.load_model(name=model_name, download_root=".cache/whisper")
    result: dict = model.transcribe(audio_path, language="pl", verbose=True)
    with open(f"transcription_{model_name}.txt", "w", encoding="UTF-8") as f:
        f.write(result["text"])


if __name__ == "__main__":
    transcribe_to_file(model_name=ModelName.TINY, audio_path="audio/apel.m4a")
