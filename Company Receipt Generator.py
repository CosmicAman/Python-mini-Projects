def generate_company_receipt(company_name, company_address, company_contact, payer_name, payment_amount, payment_date, invoice_number):
    receipt = f"""
    Company Receipt
    ------------------------------
    Company Name: {company_name}
    Address: {company_address}
    Contact: {company_contact}
    
    Invoice Number: {invoice_number}
    Payer: {payer_name}
    Amount: ${payment_amount:.2f}
    Date: {payment_date}
    ------------------------------
    Thank you for your payment!
    """
    return receipt


company_name = "Lacchu Mistan Bhandar"
company_address = "Puralia, Bati chock"
company_contact = "Phone:172214"
payer_name = "Babu lal Marandi"
payment_amount = 69.99
payment_date = "2023-10-15"
invoice_number = "IND-1111"

receipt = generate_company_receipt(company_name, company_address, company_contact, payer_name, payment_amount, payment_date, invoice_number)
print(receipt)
