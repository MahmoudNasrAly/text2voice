from gtts import gTTS

def text_to_speech(text, lang='ar', filename='output.mp3'):
    tts = gTTS(text, lang=lang)
    tts.save(filename)
    print(f"Saved speech to {filename}")

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

if __name__ == "__main__":
    # Ask the user for the path to the text file
    file_path = input("Enter the path to the text file: ")

    try:
        # Read text from the file
        text = read_text_from_file(file_path)

        # Convert the text to speech
        text_to_speech(text)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")