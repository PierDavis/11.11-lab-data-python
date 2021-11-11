open_file = open("CupcakeInvoices.csv")

# for row in open_file:
#     print(row)

# for row in open_file:
#     splitted = row.split(",")
#     # print(splitted[2])
    
#     quantity = float(splitted[3])
#     price = float(splitted[4])

#     invoice = (quantity * price)
#     print(invoice)
    
   
revenue = 0
for row in open_file:
    splitted = row.split(",")
    print(splitted[2])
        
    quantity = float(splitted[3])
    price = float(splitted[4])

    invoice = quantity * price
    
    revenue += invoice
print(revenue)