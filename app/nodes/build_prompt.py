def build_prompt(state):

    document_text = state["document_text"]

    prompt = f"""
You are an invoice extraction engine.

Extract:

- invoice_number
- vendor_name
- invoice_date
- total_amount
- currency

Return ONLY JSON.

Document:

{document_text}
"""

    return {
        "prompt": prompt
    }