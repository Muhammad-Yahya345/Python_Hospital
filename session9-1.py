# Hospital Management System (Lite Edition)

# Step 1: Create lists for patients and bills
patients = []  # Corrected from 'students'
bills = []

# Step 2: Create a dictionary for health issues mapping to respective doctors
doctors = {
    "fever": "Doctor Hussain",
    "eye": "Doctor Zeus",
    "skin": "Doctor Ali",
    "leg": "Doctor Ahmed"
}

# Step 3: Create a dictionary for services and respective cost
services = {
    "X-ray": 200,
    "Check up": 50,
    "Blood Test": 150,
    "Medicine": 50
}

# Print welcome message
print("Welcome to Atomcamp Hospital")

# Step 5: Main loop
while True:
    print("\nPick an option:")
    print("Enter 1 to register a new patient")
    print("Enter 2 to view all patients")
    print("Enter 3 to view patient based on doctor or symptoms")
    print("Enter 4 to generate a bill for a patient")
    print("Enter 5 to show unique symptoms")
    print("Enter 6 to exit the Hospital")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter the name of the patient: ")
        age = input("Enter the patient's age: ")
        occupation = input("Enter the patient's occupation: ")
        symptom = input("Enter the patient's symptom: ").lower()

        doctor = doctors.get(symptom, "General Physician")
        patients.append([name, age, occupation, symptom, doctor])
        print(f"Patient {name} registered successfully and assigned to {doctor}.")

    elif choice == "2":
        if not patients:
            print("No patients are registered yet.")
        else:
            print("\nList of Registered Patients:")
            for patient in patients:
                print(f"Name: {patient[0]} | Age: {patient[1]} | Occupation: {patient[2]} | Symptom: {patient[3]} | Doctor: {patient[4]}")

    elif choice == "3":
        search_key = input("Enter the name of the doctor or the symptom: ").lower()
        found = False
        print("\nSearch Results:")
        for patient in patients:
            if search_key in patient[3].lower() or search_key in patient[4].lower():
                print(f"Name: {patient[0]} | Age: {patient[1]} | Occupation: {patient[2]} | Symptom: {patient[3]} | Doctor: {patient[4]}")
                found = True
        if not found:
            print("No matching patients found.")

    elif choice == "4":
        name = input("Enter the name of the patient: ")
        found = False
        for patient in patients:
            if patient[0].lower() == name.lower():
                found = True
                print("\nAvailable Services:")
                for service, charges in services.items():
                    print(f"{service}: €{charges}")

                selected_services = []
                total = 0

                while True:
                    service_name = input("Enter service name to add (type 'done' to finish): ")
                    if service_name.lower() == 'done':
                        break
                    elif service_name in services:
                        selected_services.append(service_name)
                        total += services[service_name]
                    else:
                        print("Invalid service name. Try again.")

                bills.append([name, selected_services, total])
                print(f"Bill generated for {name}:")
                print("Services Taken:", ", ".join(selected_services))
                print("Total Amount: €", total)
                break
        if not found:
            print("Patient not found.")

    elif choice == "5":
        unique_symptoms = set()
        for patient in patients:
            unique_symptoms.add(patient[3].lower())
        if unique_symptoms:
            print("Unique Symptoms:")
            for symptom in unique_symptoms:
                print("-", symptom)
        else:
            print("No symptoms recorded yet.")

    elif choice == "6":
        print("Thank you for visiting Atomcamp Hospital. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

