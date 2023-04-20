import random
import csv
import datetime

# Set the start and end dates for the two-year period
start_date = datetime.date(2019, 1, 1)
end_date = datetime.date(2020, 12, 31)

# Generate 5000 client purchases
num_records = 5000
purchases = []

for i in range(num_records):
    # Generate random purchase data
    order_id = i + 1
    product = random.choice(['Product A', 'Product B', 'Product C', 'Product D', 'Product E'])
    quantity = random.randint(1, 5)
    price = round(random.uniform(10.0, 1000.0), 2)
    date = start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days))
    customer_name = 'Customer {}'.format(i + 1)
    customer_email = 'customer{}@example.com'.format(i + 1)
    customer_city = random.choice(['New York', 'Los Angeles', 'Chicago', 'Miami', 'Houston', 'Dallas', 'Philadelphia', 'San Antonio', 'San Diego', 'Phoenix'])
    
    # Append the purchase data to the list
    purchase = [order_id, product, quantity, price, date, customer_name, customer_email, customer_city]
    purchases.append(purchase)

# Write the purchase data to a CSV file
with open('client_purchases.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write the header row
    writer.writerow(['Order ID', 'Product', 'Quantity', 'Price', 'Date', 'Customer Name', 'Customer Email', 'Customer City'])
    # Write the data rows
    writer.writerows(purchases)

print('Client purchases data has been generated and written to client_purchases.csv.')
