#!/usr/bin/env python3

import re

email_pattern = r"[\w.+%-]+@[\w.-]+\.[a-zA-Z]+"
phone_pattern = r"\+?\(?\d{1,3}\)?[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}"

with open("data/sample_text.txt", "r") as file:
    text = file.read()
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    print("Extracted Emails:")
    for email in emails:
        print(email)
        
    print("\nExtracted Phone Numbers:")
    for phone in phones:
        print(phone)  
        
with open("results/output.txt", "w") as result:  
    result.write("Extracted Emails:\n")
    for email in emails:
        result.write(email + "\n")
        
    result.write("\nExtracted Phone Numbers:\n")
    for phone in phones:
        result.write(phone + "\n")