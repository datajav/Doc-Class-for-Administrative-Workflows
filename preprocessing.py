from random import random
import spacy
import pandas as pd
from faker import Faker

fake = Faker()
catergories = ['Finance', 'HR', 'Legal', 'Support', 'Ops', 'Sales']

def generate_document(category):
    based_text = {
        'Finance': f"Invoice total is ${fake.random_number(digits=4)}. Payment due by {fake.date_this_month()}",
        'HR': f"Employee {fake.name()} submitted leave request for {fake.date_this_year()}",
        'Legal': f"Contract between {fake.company()} and {fake.company()} signed on {fake.date()}",
        'Support': f"Customer reported issue with {fake.word()} via {random.choice(['email', 'chat', 'phone'])}",
        'Operations': f"Shipment from {fake.city()} delayed due to {fake.word()}",
        'Sales': f"Lead {fake.name()} interested in {fake.bs()} product"
    }
    return based_text[category]
data = []
for _ in range(5000):
    category = random.choice(catergories)
    text = generate_document(category)
    data.append({'category': category, 'text': text})

documents_df = pd.DataFrame(data)

print(documents_df.head())

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    doc = nlp(text)
    return "".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])
