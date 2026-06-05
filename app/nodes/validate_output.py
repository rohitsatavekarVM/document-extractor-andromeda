import json

from app.schemas.schemas import Invoice


def validate_output(state):

    data = json.loads(
        state["llm_response"]
    )

    validated = Invoice.model_validate(
        data
    )

    return {
        "extracted_data":
            validated.model_dump()
    }