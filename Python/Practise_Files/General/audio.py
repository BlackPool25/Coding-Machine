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

def convert_to_audio(text, output_path="output.mp3"):
    try:
        engine = pyttsx3.init()
        # Set properties (optional)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)  # Select voice index as needed
        
        # Save the speech to a file
        engine.save_to_file(text, output_path)
        print(f"Audio saved to {output_path}")
    except Exception as e:
        print(f"Error converting text to audio: {e}")

def main():
    pdf_input = input("Enter the path of your PDF file: ")
    
    if not os.path.exists(pdf_input):
        print("PDF file not found.")
        return
    
    extracted_text = read_pdf_file(pdf_input)
    
    if extracted_text:
        convert_to_audio(extracted_text)

if __name__ == "__main__":
    main()