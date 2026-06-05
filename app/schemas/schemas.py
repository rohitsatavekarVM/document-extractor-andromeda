from pydantic import BaseModel
from pydantic import Field


class Invoice(BaseModel):

    invoice_number: str = Field(
        description="Invoice Number"
    )

    vendor_name: str = Field(
        description="Vendor Name"
    )

    invoice_date: str = Field(
        description="Invoice Date"
    )

    total_amount: float = Field(
        description="Total Amount"
    )

    currency: str = Field(
        description="Currency"
    )