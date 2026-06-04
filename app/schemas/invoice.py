from pydantic import BaseModel


class Invoice(BaseModel):
    invoice_number: str
    vendor_name: str
    invoice_date: str
    total_amount: float
    currency: str