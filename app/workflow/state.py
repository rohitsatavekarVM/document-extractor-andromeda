from typing import TypedDict
from typing import Type

from pydantic import BaseModel


class ExtractionState(TypedDict, total=False):

    file_path: str

    document_text: str

    llm_response: str

    schema: Type[BaseModel]

    extracted_data: dict