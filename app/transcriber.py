import io
import tempfile

from faster_whisper import WhisperModel

from app.config import settings

_model = None


def get_model() -> WhisperModel:
    """モデルを遅延ロード"""
    global _model
    if _model is None:
        _model = WhisperModel(
            settings.whisper_model,
            device=settings.device,
            compute_type=settings.compute_type,
        )
    return _model


def transcribe_audio(
    audio_bytes: bytes,
    language: str = "auto",
) -> tuple[str, str]:
    """音声を文字起こしする"""
    # 一時ファイルに保存
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
        tmp.write(audio_bytes)
        tmp_path = tmp.name

    model = get_model()

    lang = None if language == "auto" else language

    segments, info = model.transcribe(
        tmp_path,
        language=lang,
        beam_size=5,
    )

    text = "".join(segment.text for segment in segments)
    detected_lang = info.language

    return text.strip(), detected_lang