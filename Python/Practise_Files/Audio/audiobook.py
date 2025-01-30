import os
from PyPDF2 import PdfReader
import pyttsx3

def read_pdf_file(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            text = ''
            for page in range(len(reader.pages)):
                text += reader.pages[page].extract_text()
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

def init_tts():
    try:
        engine = pyttsx3.init()
        # Set properties (optional)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)  # Select voice index as needed
        rate = engine getProperty('rate')  # Get the current speaking rate
        print(f"Current rate: {rate}")  # Print current rate
        
        if not os.path.exists("output"):
            os.makedirs("output")
            
        return engine
    except Exception as e:
        print(f"Error initializing TTS: {e}")
        return None

def convert_to_audio(text, engine, output_path="output/output.mp3"):
    try:
        # Initialize the text to speech engine with specific settings
        if not engine:
            print("TTS Engine is not initialized. Please check initialization.")
            return
            
        # Save the speech to a file using async method and callback
        def on_post(event):
            pass  # No action needed; we'll write directly

        sound =	engine.begin_audio()
        
        for i, chunk in enumerate(text.split("\n\n")):  # Split into paragraphs or adjust as per your needs
            engine.say(chunk)
            
            if (i+1) % 5 ==0:
                engine.runAndWait()  # Wait for a few sentences to be processed before moving on
            
        while not os.path.exists(output_path):
            pass
        
    except Exception as e:
        print(f"Error converting text to audio: {e}")
        
def main():
    pdf_input = input("Enter the path of your PDF file: ")
    
    if not os.path.exists(pdf_input):
        print("PDF file not found.")
        return
    
    extracted_text = read_pdf_file(pdf_input)
    
    if extracted_text:
        engine = init_tts()
        convert_to_audio(extracted_text, engine)

if __name__ == "__main__":
    main()