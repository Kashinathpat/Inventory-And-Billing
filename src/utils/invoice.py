import datetime
import os

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

store_name = "Tech World Electronics"
store_mail = "Gandhi Chowk, Bazarpeth, Main Road, Kudal, Sindhudurg"
store_addr = "support@techworld.com"

def create_invoice(products, discount_percent, tip_percent, customer_name, customer_mobile) -> str:
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%I:%M:%S %p")

    filename = getInvoicePath()
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 50, "INVOICE")

    # Company Info
    c.setFont("Helvetica", 10)
    c.line(50, height - 60, width - 50, height - 60)
    c.drawString(60, height - 90, f"Company Name: {store_name}")
    c.drawString(60, height - 110, f"Email ID: {store_mail}")
    c.drawString(60, height - 130, f"Address: {store_addr}")

    # Customer Info (Separate Section)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(60, height - 160, "Customer Information:")
    c.setFont("Helvetica", 10)
    c.drawString(80, height - 180, f"Name: {customer_name}")
    c.drawString(80, height - 200, f"Mobile: {customer_mobile}")

    # Date and Time
    c.setFont("Helvetica", 10)
    c.drawString(width - 180, height - 90, f"Date: {date}")
    c.drawString(width - 180, height - 110, f"Time: {time}")
    c.line(50, height - 220, width - 50, height - 220)

    # Table Headers
    c.setFont("Helvetica-Bold", 12)
    y = height - 250
    c.drawString(60, y, "Product Description")
    c.drawString(width / 2 - 80, y, "Quantity")
    c.drawString(width / 2, y, "Unit Price")
    c.drawRightString(width - 60, y, "Amount (INR)")
    c.line(50, y - 5, width - 50, y - 5)

    # Products Section
    c.setFont("Helvetica", 11)
    y -= 30
    total_amount = 0
    for product in products:
        name, quantity, price = product["name"], product["quantity"], float(product["price"])
        amount = quantity * price
        total_amount += amount

        c.drawString(60, y, name)
        c.drawString(width / 2 - 80, y, str(quantity))
        c.drawString(width / 2, y, f"{price:.2f}")
        c.drawRightString(width - 60, y, f"{amount:.2f}")
        y -= 20

    # Discount and Tip
    discount_amount = total_amount * (discount_percent / 100)
    tip_amount = total_amount * (tip_percent / 100)

    c.drawString(60, y, f"Discount ({discount_percent}%)")
    c.drawRightString(width - 60, y, f"-{discount_amount:.2f}")
    y -= 20

    c.drawString(60, y, f"Tip ({tip_percent}%)")
    c.drawRightString(width - 60, y, f"+{tip_amount:.2f}")
    y -= 30

    # Final Total
    final_total = total_amount - discount_amount + tip_amount
    c.setFont("Helvetica-Bold", 12)
    c.line(50, y, width - 50, y)
    y -= 25
    c.drawString(60, y, "Total Amount Payable")
    c.drawRightString(width - 60, y, f"{final_total:.2f} INR")
    c.line(50, y - 15, width - 50, y - 15)

    # Footer Message
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(60, 50, "Thank you for choosing us!")
    c.drawRightString(width - 60, 50, "We hope to serve you again soon.")

    c.save()
    return filename


def getInvoicePath():
    """
    Gets an available file path in the given directory with the given file name prefix.

    Increments a counter suffix until a non-existing file path is found.
    """
    directory = os.path.expanduser("~/Documents/Invoices")
    os.makedirs(directory, exist_ok=True)
    count = 1
    extension=".pdf"
    while True:
        filename = f"{count:05}"
        new_file_name = f"INVOICE_{filename}{extension}"
        new_file_path = os.path.join(directory, new_file_name)

        if not os.path.isfile(new_file_path):
            return new_file_path

        count += 1
