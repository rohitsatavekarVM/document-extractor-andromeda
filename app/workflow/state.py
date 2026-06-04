from typing import TypedDict


class ExtractionState(TypedDict, total=False):

    file_path: str

    document_text: str

    prompt: str

    llm_output: str

    extracted_data: dict

    validation_error: str