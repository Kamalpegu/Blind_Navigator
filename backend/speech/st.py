import pyttsx3


# Initialize Text-to-Speech engine
UserVoiceEngine = pyttsx3.init()


def text_to_speech(UserText):

    try:
        UserVoiceEngine.say(UserText)

        # Wait until the speech is completed
        UserVoiceEngine.runAndWait()

    except Exception as Error:
        print("Text-to-Speech Error:", Error)


# Test
if __name__ == "__main__":
    text_to_speech("rendi tuk bohut sudim kela")