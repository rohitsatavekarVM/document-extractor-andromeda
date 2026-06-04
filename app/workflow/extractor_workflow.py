from andromeda.core.workflow import WorkflowBuilder

from app.workflow.state import (
    ExtractionState
)

from app.nodes.read_document import (
    read_document
)

from app.nodes.build_prompt import (
    build_prompt
)

from app.nodes.call_llm import (
    call_llm
)

from app.nodes.validate import (
    validate
)


def build_workflow():

    workflow = WorkflowBuilder(
        name="InvoiceExtractionWorkflow",
        state_schema=ExtractionState
    )

    (
        workflow

        .start("read_document")
        .run(read_document)

        .then("build_prompt")
        .run(build_prompt)

        .then("call_llm")
        .run(call_llm)

        .finish("validate")
        .run(validate)

    )

    return workflow