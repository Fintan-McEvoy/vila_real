def PowerSpectrum(path_to_mp3):
    from pydub import AudioSegment
    audio_file = AudioSegment.from_file(path_to_mp3)
    
    # This will open and read the audio file with pydub.  Replace the file path with
    # your own file.


    # Set up a list for us to dump PCM samples into, and create a 'data' variable
    # so we don't need to type audio_file._data again
    data = audio_file._data
    global pcm16_signed_integers
    pcm16_signed_integers = []

    # This loop decodes the bytestring into PCM samples.
    # The bytestring is a stream of little-endian encoded signed integers.
    # This basically just cuts each two-byte sample out of the bytestring, converts
    # it to an integer, and appends it to the list of samples.
    for sample_index in range(len(data)//2):
        sample = int.from_bytes(data[sample_index*2:sample_index*2+2], 'little', signed=True)
        pcm16_signed_integers.append(sample)

    return(pcm16_signed_integers)
