#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This script generates a function to clean text data using the spaCy library which allows for preprocessing of text by removing special characters and extra spaces as well as any stop words.
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import spacy

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    """
    Cleans the input text by removing special characters and extra spaces.
    """
    doc = nlp(text)
    cleaned_text = ' '.join(token.text for token in doc if not token.is_punct and not token.is_space)
    return cleaned_text
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------