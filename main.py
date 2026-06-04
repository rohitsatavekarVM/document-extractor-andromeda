from dotenv import load_dotenv

from app.workflow.extractor_workflow import (
    build_workflow
)


def main():

    load_dotenv()

    workflow = build_workflow()

    result = workflow.execute(
        state={
            "file_path":
                "documents/invoice.pdf"
        }
    )

    print("\n")
    print("=" * 50)
    print("EXTRACTED DATA")
    print("=" * 50)
    print("\n")

    print(
        result["extracted_data"]
    )


if __name__ == "__main__":
    main()