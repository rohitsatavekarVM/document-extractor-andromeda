from litellm import completion

def extract_invoice(state):

    prompt = f"""
Extract:

invoice_number
vendor_name
invoice_date
total_amount
currency

Return ONLY valid JSON.

Document:

{state["document_text"]}
"""

    response = completion(
        model="ollama/qwen3:8b",
        api_base="http://localhost:11434",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "llm_response":
            response.choices[0].message.content
    }