#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This script generates a synthetic dataset of documents with various categories for testing purposes.
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import os
from faker import Faker
import random
import pandas as pd

os.makedirs('data', exist_ok=True)

fake = Faker()
categories = ['Finance', 'HR', 'Legal', 'Support', 'Operations', 'Sales']

print("Generating synthetic document dataset...")
print("Categories:", categories)

def generate_document(category):
    templates = {
        'Finance': f"Invoice total is ${fake.random_number(digits=4)} due by {fake.date_this_month()}",
        'HR': f"Employee {fake.name()} submitted leave request for {fake.date_this_year()}",
        'Legal': f"Contract signed between {fake.company()} and {fake.company()} on {fake.date()}",
        'Support': f"Customer reported issue with {fake.word()} via {random.choice(['email', 'chat'])}",
        'Operations': f"Shipment from {fake.city()} delayed due to {fake.word()}",
        'Sales': f"Lead {fake.name()} interested in {fake.bs()} product"
    }
    return templates[category]

data = [{'category': random.choice(categories), 'text': generate_document(random.choice(categories))} for _ in range(5000)]

pd.DataFrame(data).to_csv('data/documents.csv', index=False)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------