import pytest
from unittest.mock import Mock, patch, mock_open
from pathlib import Path
from fpdf import FPDF
import PyPDF2
from project import PDFExtractor

@pytest.fixture
def sample_pdf_text():
    return "This is a sample PDF document.\nIt contains text for testing purposes.\nKeyword is included here."

@pytest.fixture
def pdf_extractor(tmp_path, sample_pdf_text):
    pdf_path = tmp_path / "test.pdf"
    
    # Create a PDF with text
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=12)
    pdf.multi_cell(0, 10, sample_pdf_text)
    pdf.output(str(pdf_path))
    
    extractor = PDFExtractor(pdf_path)
    return extractor

def test_extract_text(pdf_extractor, sample_pdf_text):
    with patch("PyPDF2.PdfReader") as MockPdfReader:
        mock_reader = Mock()
        mock_page = Mock()
        mock_page.extract_text.return_value = sample_pdf_text
        mock_reader.pages = [mock_page]
        MockPdfReader.return_value = mock_reader

        success = pdf_extractor.extract_text()

        assert success is True
        assert pdf_extractor.text == sample_pdf_text + '\n\n'

def test_search_keyword(pdf_extractor):
    pdf_extractor.text = "This is a test. Keyword is here. More text follows."
    results = pdf_extractor.search_keyword("Keyword")

    assert len(results) == 1
    assert "Keyword is here" in results[0]

def test_export_text(pdf_extractor):
    pdf_extractor.text = "This is a test."

    with patch("project.open", mock_open(), create=True) as mock_file:
        success = pdf_extractor.export_text()

        assert success is True
        mock_file.assert_called_once_with(pdf_extractor.pdf_path.with_suffix(".txt"), 'w', encoding='utf-8')
        mock_file().write.assert_called_once_with("This is a test.")

def test_export_text_failure(pdf_extractor):
    pdf_extractor.text = "This is a test."

    with patch("builtins.open", side_effect=Exception("Error exporting")) as mock_file:
        success = pdf_extractor.export_text()

        assert success is False
