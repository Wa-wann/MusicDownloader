import pydub as pd
import warnings


def slice_audio(audio: pd.AudioSegment, begin: int = 0, end: int = None) -> pd.AudioSegment:
    """
    :param audio: the music to slice
    :param begin: begin of the music in second
    :param end: end of the music in second
    :return: music sliced
    """
    is_begin_set = 0 < begin < audio.duration_seconds * 1000
    is_end_set = end is not None and end < audio.duration_seconds * 1000
    are_timer_ordered = begin < end

    if is_begin_set and is_end_set:
        if are_timer_ordered:
            new_audio = audio[begin * 1000: end * 1000]
        else:
            new_audio = audio[end * 1000: begin * 1000]
        return new_audio
    elif is_begin_set and not is_end_set:
        new_audio = audio[begin * 1000:]
        return new_audio
    elif not is_begin_set and is_end_set:
        new_audio = audio[:end * 1000]
        return new_audio

    else:
        if begin == 0 and end == -1:
            warnings.warn("Slice is called but there is nothing to slice")
        else:
            warnings.warn(f"Begin and End Timecode are incorrect begin:{begin} end:{end}")
        return audio
