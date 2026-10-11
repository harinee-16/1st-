patients = []

while True:
    print("\n===== Hospital Patient Record System =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Delete Patient")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # ADD PATIENT
    if choice == "1":
        pid = input("Enter Patient ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        disease = input("Enter Disease: ")

        patient = {
            "ID": pid,
            "Name": name,
            "Age": age,
            "Disease": disease
        }

        patients.append(patient)
        print("Patient Added Successfully!")

    # VIEW PATIENTS
    elif choice == "2":
        if len(patients) == 0:
            print("No patient records found.")
        else:
            for p in patients:
                print("\n-------------------")
                print("ID:", p["ID"])
                print("Name:", p["Name"])
                print("Age:", p["Age"])
                print("Disease:", p["Disease"])

    # SEARCH PATIENT
    elif choice == "3":
        pid = input("Enter Patient ID: ")
        found = False

        for p in patients:
            if p["ID"] == pid:
                print("\nPatient Found!")
                print("ID:", p["ID"])
                print("Name:", p["Name"])
                print("Age:", p["Age"])
                print("Disease:", p["Disease"])
                found = True
                break

        if not found:
            print("Patient Not Found")

    # DELETE PATIENT
    elif choice == "4":
        pid = input("Enter Patient ID to delete: ")
        found = False

        for p in patients:
            if p["ID"] == pid:
                patients.remove(p)
                print("Patient Deleted Successfully!")
                found = True
                break

        if not found:
            print("Patient Not Found")

    # EXIT
    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
