import re
import time


def preprocessing(content):
    try:
        # Converting all text into lowercase
        print("\nConverting Text to lowercase...")
        content = str(content).lower()

        # Removing Commas from numbers
        print("Removing Commas from Numbers...")
        content = re.sub(r'(?<=\d),(?=\d)', "", content)
        
        # Removing all special characters from the Text
        content = re.sub(r'[^\w\d\s.,\-+@#]', " ", content)
        print("Removing special characters...")

        # Removing Unwanted Whitespaces from the Text
        print("Removing unwanted whitespaces...")
        content = re.sub(r'\s{2,}', ' ', content)
        content = content.strip()

        return content
    
    except Exception as exp:
        print("Error Occured: ", exp)
