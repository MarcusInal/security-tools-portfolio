import re

def extract_emails(filename):
    with open(filename, 'r') as f:
        content = f.read()

    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern, content)
    return emails

def main():
    file = input("Ange filnamnet att extrahera e-postadresser från: ")
    emails = extract_emails(file)

    print("Hittade e-postadresser: ")
    for email in emails:
        print('*', email)
    
if __name__ == "__main__":
    main()