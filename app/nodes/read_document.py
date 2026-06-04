import fitz


def read_document(state):

    pdf_path = state["documents"]

    document = fitz.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    return {
        "document_text": text
    }