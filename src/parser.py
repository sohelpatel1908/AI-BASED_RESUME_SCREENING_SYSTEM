import pymupdf


def pdf_parser(filepath):
    try:
        text = ""
        doc = pymupdf.open(stream=filepath)
        # doc = pymupdf.open(filepath)
        for page in doc:
            text += page.get_text() + "\n"
        return text
    
    except Exception as exp:
        return exp

