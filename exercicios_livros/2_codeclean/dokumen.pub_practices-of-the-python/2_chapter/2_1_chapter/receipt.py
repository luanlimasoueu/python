from sales_tax import add_sales_tax

def print_receipt():
    total = 1.6
    state = 'MI'
    print(f'TOTAL: {total}')
    print(f'AFTER TAX: {add_sales_tax(total, state)}')

print_receipt()
