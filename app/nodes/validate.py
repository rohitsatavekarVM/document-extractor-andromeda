import json

from app.schemas.invoice import Invoice


def validate(state):

    try:

        data = json.loads(
            state["llm_output"]
        )

        invoice = Invoice.model_validate(
            data
        )

        return {
            "extracted_data":
                invoice.model_dump()
        }

    except Exception as e:

        return {
            "validation_error":
                str(e)
        }