from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Dev, Company, Freebie

# Sqlite connection
engine = create_engine('sqlite:///freebies.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# Create tables if not exist
Base.metadata.create_all(engine)

# ======== Developer management ========
def create_dev():
    name = input("Enter developer name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if session.query(Dev).filter_by(name=name).first():
        print("Developer already exists.")
        return
    dev = Dev(name=name)
    session.add(dev)
    session.commit()
    print(f"Developer '{name}' created!")

def view_devs():
    devs = session.query(Dev).all()
    if not devs:
        print("No developers found.")
        return
    for dev in devs:
        print(f"ID: {dev.id}, Name: {dev.name}, Freebies count: {dev.freebies_count(session)}")

def delete_dev():
    try:
        dev_id = int(input("Enter ID of developer to delete: "))
    except ValueError:
        print("Invalid ID")
        return
    dev = session.query(Dev).filter_by(id=dev_id).first()
    if not dev:
        print("Developer not found.")
        return
    session.delete(dev)
    session.commit()
    print(f"Developer ID {dev_id} deleted.")

# ======== Company  ========
def create_company():
    name = input("Enter company name: ")
    if not name:
        print("Name cannot be empty.")
        return
    if session.query(Company).filter_by(name=name).first():
        print("Company already exists.")
        return
    try:
        founding_year = int(input("Enter founding year: "))
    except ValueError:
        print("Invalid year.")
        return
    company = Company(name=name, founding_year=founding_year)
    session.add(company)
    session.commit()
    print(f"Company '{name}' created!")

def view_companies():
    companies = session.query(Company).all()
    if not companies:
        print("No companies found.")
        return
    for c in companies:
        print(f"ID: {c.id}, Name: {c.name}, Founded: {c.founding_year}, Total freebies value: {c.total_value_of_freebies(session)}")

# ======== Freebie  ========
def create_freebie():
    item_name = input("Enter freebie item name: ")
    if not item_name:
        print("Item name cannot be empty.")
        return

    try:
        value = int(input("Enter freebie value: "))
    except ValueError:
        print("Invalid value.")
        return

    devs = session.query(Dev).all()
    companies = session.query(Company).all()
    if not devs or not companies:
        print("Must have at least one developer and one company before adding freebies.")
        return

    print("Developers:")
    for dev in devs:
        print(f"{dev.id}: {dev.name}")
    try:
        dev_id = int(input("Enter developer ID for freebie: "))
    except ValueError:
        print("Invalid developer ID.")
        return
    dev = session.query(Dev).filter_by(id=dev_id).first()
    if not dev:
        print("Developer not found.")
        return

    print("Companies:")
    for c in companies:
        print(f"{c.id}: {c.name}")
    try:
        company_id = int(input("Enter company ID for freebie: "))
    except ValueError:
        print("Invalid company ID.")
        return
    company = session.query(Company).filter_by(id=company_id).first()
    if not company:
        print("Company not found.")
        return

    existing = session.query(Freebie).filter_by(item_name=item_name, dev_id=dev_id, company_id=company_id).first()
    if existing:
        print("This freebie already exists for the developer and company.")
        return

    freebie = Freebie(item_name=item_name, value=value, dev=dev, company=company)
    session.add(freebie)
    session.commit()
    print(f"Freebie '{item_name}' created for {dev.name} from {company.name}!")

def view_freebies():
    freebies = session.query(Freebie).all()
    if not freebies:
        print("No freebies found.")
        return
    for f in freebies:
        print(f"ID: {f.id}, Item: {f.item_name}, Value: {f.value}, Developer: {f.dev.name}, Company: {f.company.name}")

# ======== Manager ========
def main():
    while True:
        print("\n=== Freebie Tracker Menu ===")
        print("1. Manage Developers")
        print("2. Manage Companies")
        print("3. Manage Freebies")
        print("4. Exit")

        main_choice = input("Enter your choice : ")

        if main_choice == '1':
            while True:
                print("\n--- Developer Management ---")
                print("1. Create Developer")
                print("2. View Developers")
                print("3. Delete Developer")
                print("0. Back to Main Menu")

                dev_choice = input("Choose an option: ").strip()
                if dev_choice == '1':
                    create_dev()
                elif dev_choice == '2':
                    view_devs()
                elif dev_choice == '3':
                    delete_dev()
                elif dev_choice == '0':
                    break
                else:
                    print("Invalid option, try again.")

        elif main_choice == '2':
            while True:
                print("\n--- Company Management ---")
                print("1. Create Company")
                print("2. View Companies")
                print("0. Back to Main Menu")

                comp_choice = input("Choose an option: ").strip()
                if comp_choice == '1':
                    create_company()
                elif comp_choice == '2':
                    view_companies()
                elif comp_choice == '0':
                    break
                else:
                    print("Invalid option, try again.")

        elif main_choice == '3':
            while True:
                print("\n--- Freebie Management ---")
                print("1. Create Freebie")
                print("2. View Freebies")
                print("0. Back to Main Menu")

                freebie_choice = input("Choose an option: ").strip()
                if freebie_choice == '1':
                    create_freebie()
                elif freebie_choice == '2':
                    view_freebies()
                elif freebie_choice == '0':
                    break
                else:
                    print("Invalid option, try again.")

        elif main_choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

main()
