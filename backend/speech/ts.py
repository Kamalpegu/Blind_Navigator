import speech_recognition


# Initialize the Speech Recognizer
UserVoiceRecognizer = speech_recognition.Recognizer()


# ==========================================
# VOICE TO TEXT FUNCTION
# ==========================================

def voice_to_text():

    try:

        with speech_recognition.Microphone() as UserVoiceInputSource:

            print("\nListening...")

            # Adjust microphone for background noise
            UserVoiceRecognizer.adjust_for_ambient_noise(
                UserVoiceInputSource,
                duration=0.5
            )

            # Listen to user's voice
            UserVoiceInput = UserVoiceRecognizer.listen(
                UserVoiceInputSource,
                timeout=5,
                phrase_time_limit=10
            )

            print("Processing...")

            # Convert voice to text
            UserVoiceInput_converted_to_Text = (
                UserVoiceRecognizer.recognize_google(
                    UserVoiceInput,
                    language="en-IN"
                )
            )

            # Convert text to lowercase
            UserVoiceInput_converted_to_Text = (
                UserVoiceInput_converted_to_Text.lower()
            )

            print(
                "You said:",
                UserVoiceInput_converted_to_Text
            )

            return UserVoiceInput_converted_to_Text


    except speech_recognition.WaitTimeoutError:

        print("No voice detected.")
        return None


    except speech_recognition.UnknownValueError:

        print(
            "No User Voice detected OR unintelligible "
            "audio detected."
        )

        return None


    except speech_recognition.RequestError as Error:

        print(
            "Speech Recognition Service Error:",
            Error
        )

        return None


    except Exception as Error:

        print(
            "Unexpected Error:",
            Error
        )

        return None


# ==========================================
# MAIN PROGRAM
# ==========================================

if __name__ == "__main__":

    print("Voice Recognition Started")
    print("Press Ctrl + C to stop.")

    while True:

        try:

            UserCommand = voice_to_text()

            if UserCommand:

                print(
                    f"\nRecognized Text: {UserCommand}"
                )


        except KeyboardInterrupt:

            print(
                "\nProgram terminated."
            )

            break