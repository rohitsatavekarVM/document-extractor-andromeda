from andromeda.utils import get_chat_model

from app.config import MODEL_CONFIG

model = get_chat_model(MODEL_CONFIG)


def call_llm(state):

    response = model.invoke(
        state["prompt"]
    )

    return {
        "llm_output":
            response.content
    }