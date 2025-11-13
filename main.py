class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__medical_history = []


    def _add_diagnosis(self, doctor, diagnosis):
        if isinstance(doctor, Doctor):
            self.__medical_history.append(diagnosis)
            print(f" {self.name} uchun yangi tashxis qo‘shildi: {diagnosis}")
        else:
            print(" Faqat shifokor tibbiy tarixni o‘zgartirishi mumkin!")


    def _get_medical_history(self, doctor):
        if isinstance(doctor, Doctor):
            return self.__medical_history
        else:
            return " Sizda tibbiy tarixni ko‘rish huquqi yo‘q!"


class Doctor:
    def __init__(self, name):
        self.name = name

    def view_medical_history(self, patient):
        print(f" Shifokor {self.name} {patient.name} bemorning tarixini ko‘ryapti:")
        history = patient._get_medical_history(self)
        if isinstance(history, list):
            if history:
                for i, h in enumerate(history, 1):
                    print(f"   {i}. {h}")
            else:
                print("   Tarix bo‘sh.")
        else:
            print(history)

    def add_diagnosis(self, patient, diagnosis):
        patient._add_diagnosis(self, diagnosis)


class Receptionist:
    def __init__(self, name):
        self.name = name

    def schedule_appointment(self, patient, time):
        print(f" Qabulchi {self.name} {patient.name} uchun uchrashuv vaqtini belgiladi: {time}")

    def view_patient_info(self, patient):
        print(f"  Qabulchi {self.name} {patient.name} bemorning ma'lumotlarini ko‘ryapti:")
        print(f"   Ism: {patient.name}")
        print(f"   Yosh: {patient.age}")
        print("   (Tibbiy tarixga kirish taqiqlangan!)")



patient1 = Patient("Ali", 30)


doctor1 = Doctor("Dr. Karimov")
receptionist1 = Receptionist("Madina")


receptionist1.view_patient_info(patient1)
receptionist1.schedule_appointment(patient1, "2025-11-14, 10:00")


doctor1.add_diagnosis(patient1, "Yuqori qon bosimi")
doctor1.add_diagnosis(patient1, "Allergiya")


doctor1.view_medical_history(patient1)


print("\n--- Qabulchi tibbiy tarixni ko‘rishga urinmoqda ---")
print(patient1._get_medical_history(receptionist1))

