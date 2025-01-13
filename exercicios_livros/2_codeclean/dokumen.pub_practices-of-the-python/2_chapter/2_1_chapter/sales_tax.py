TAX_RATES_BY_STATE = {
'MI': 1.06
    }

def add_sales_tax(total, state):
    tax_rate = TAX_RATES_BY_STATE[state]
    return total * tax_rate 