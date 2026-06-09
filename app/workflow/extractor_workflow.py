from andromeda.core.workflow import WorkflowBuilder

from app.workflow.state import ExtractionState

from app.nodes.read_pdf import read_pdf
from app.nodes.extract_invoice import extract_invoice
from app.nodes.validate_output import validate_output


def build_workflow():

    workflow = WorkflowBuilder(
        name="InvoiceExtractor",
        state_schema=ExtractionState
    )

    (
        workflow

        .start("read_pdf")
        .run(read_pdf)

        .then("extract_invoice")
        .run(extract_invoice)

        .finish("validate_output")
        .run(validate_output)
    )

    return workflow