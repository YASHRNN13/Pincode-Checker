import csv

def load_pincodes(file_path):
    pincodes = {}
    postoffices = {}
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pincodes[row['pincode']] = {
                'Officename': row['officename'],
                'District': row['district'],
                'State': row['statename']
            }
            postoffices[row['officename'].lower()] = {
                'Pincode': row['pincode'],
                'District': row['district'],
                'State': row['statename']
            }
    return pincodes, postoffices

def check_by_pincode(pincodes, pin):
    info = pincodes.get(pin)
    if info:
        print(f"Pincode: {pin}")
        print(f"Officename: {info['Officename']}")
        print(f"District: {info['District']}")
        print(f"State: {info['State']}")
    else:
        print("Pincode not found in local database.")

def check_by_postoffice(postoffices, name):
    info = postoffices.get(name.lower())
    if info:
        print(f"Officename: {name}")
        print(f"Pincode: {info['Pincode']}")
        print(f"District: {info['District']}")
        print(f"State: {info['State']}")
    else:
        print("Post Office not found in local database.")

if __name__ == "__main__":
    csv_file_path = r"C:\Users\NAVYA\OneDrive\Desktop\PYTHON CODES\india_pincodes.csv"
    pincodes, postoffices = load_pincodes(csv_file_path)

    while True:
        print("\n--- Pincode/Post Office Checker ---")
        print("1. Search by Pincode")
        print("2. Search by Post Office")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            pin = input("Enter a 6-digit pincode: ").strip()
            if len(pin) != 6 or not pin.isdigit():
                print("Invalid input! Enter exactly 6 digits.")
            else:
                check_by_pincode(pincodes, pin)
        elif choice == "2":
            name = input("Enter the Post Office name: ").strip()
            if not name:
                print("Invalid input! Please enter a valid Post Office name.")
            else:
                check_by_postoffice(postoffices, name)
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
