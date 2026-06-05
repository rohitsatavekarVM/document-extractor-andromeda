import fitz


def read_pdf(state):

    pdf_path = state["file_path"]

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    return {
        "document_text": text
    }