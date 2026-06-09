
from app.workflow.extractor_workflow import (
    build_workflow
)


def main():

    

    workflow = build_workflow()

    result = workflow.execute(
        state={
            "file_path":
                "documents/invoice.pdf",
        }
    )
    print("=" * 50 )

    print("EXTRACTED DATA : ")
    

    print(
        result["extracted_data"]
    )


if __name__ == "__main__":
    main()