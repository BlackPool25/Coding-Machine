import PyPDF2
import sys
from pathlib import Path
import re

class PDFExtractor:
    def __init__(self, pdf_path):
        self.pdf_path = Path(pdf_path)
        self.text = ""
        
    def extract_text(self):
        #Extract text from PDF file and preserve newlines.
        try:
            with open(self.pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    # Extract text for the current page and ensure it preserves line breaks.
                    page_text = page.extract_text()
                    if page_text:
                        # Append with double newlines to separate pages clearly.
                        self.text += page_text + '\n\n'
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def search_keyword(self, keyword):
        """Search for keyword in extracted text"""
        matches = re.finditer(keyword, self.text, re.IGNORECASE)
        results = []
        for match in matches:
            start = max(0, match.start() - 50)
            end = min(len(self.text), match.end() + 50)
            context = self.text[start:end]
            results.append(f"...{context}...")
        return results
    
    def export_text(self, output_format="txt"):
        """Export extracted text to specified format"""
        output_path = self.pdf_path.with_suffix(f".{output_format}")
        try:
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(self.text)
            return True
        except Exception as e:
            print(f"Error exporting: {e}")
            return False

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python project.py <pdf_file> [keyword]")
    
    extractor = PDFExtractor(sys.argv[1])
    if not extractor.extract_text():
        sys.exit("Failed to extract text")
    
    if len(sys.argv) == 3:
        # Search mode
        keyword = sys.argv[2]
        results = extractor.search_keyword(keyword)
        print(f"\nFound {len(results)} matches for '{keyword}':")
        for i, result in enumerate(results, 1):
            print(f"\n{i}. {result}")
    else:
        # Export mode
        if extractor.export_text():
            print("Text exported successfully")

if __name__ == "__main__":
    main()