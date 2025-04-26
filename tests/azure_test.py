import os 
os.environ['AZURE_SPEECH_KEY'] = 'E1lgRaKZjlQfl7WOQL7rRw9T37vA5rRJQ10vpawcGtsvsOqVZesBJQQJ99BDAC3pKaRXJ3w3AAAYACOGHL69' 
os.environ['AZURE_SPEECH_REGION'] = 'eastasia'
if __name__ == "__main__":
    import os
    from RealtimeTTS import TextToAudioStream, AzureEngine
    

    def dummy_generator():
        yield "你好，欢迎使用Azure语音合成服务。"
        yield "今天的天气真不错。"
        yield "今天的天气真不错。"
    
    # text = '请介绍人工智能发展历史'
    def genai_stream(apikey, text):
        genai.configure(api_key=AIzaSyCR-J-KZD-UvzHc7oQfLHC9pTALhNFYU7s)
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(text, stream=True)
        for chunk in response:
            print(chunk.text, end='', flush=True)


    # for normal use with minimal logging:
    import os
    engine = AzureEngine(
        os.environ["AZURE_SPEECH_KEY"],
        os.environ["AZURE_SPEECH_REGION"],
        audio_format="riff-48khz-16bit-mono-pcm"
    )
    print("完成引擎设置")

    import string
    last_word = None
    def process_word(word):
        global last_word
        if last_word and word.word not in set(string.punctuation):
            print(" ", end="", flush=True)

        print(f"{word.word}", end="", flush=True)
        last_word = word.word

    engine.set_voice("zh-CN-XiaoxiaoNeural")
    print("voice设置完成")

    stream = TextToAudioStream(engine, on_word=process_word,muted=True)

    print("Starting to play stream")
    stream.feed(dummy_generator()).play(output_wavfile = "output.wav")

    engine.shutdown()
