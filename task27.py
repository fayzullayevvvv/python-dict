def phonebook_menu(phonebook: dict[str, str]) -> None:
    while True:
        print('1.Kontakt qo‘shish.')
        print('2.Barcha kontaktlarni chiqarish.')
        print('3.Ism bo‘yicha telefon qidirish.')
        print('4.Chiqish.')

        choice = input('>').strip()

        if choice == '1':
            name = input('Ism: ').strip()
            phone = input('Telefon raqam: ').strip()
            phonebook[name] = phone

            print(f'{name.capitalize()} qo\'shildi.')
        
        
        elif choice == '2':
            if not phonebook:
                return 'Kontakt bo\'sh.'
            else:
                all_contacts = ''
                for name, phone in phonebook.items():
                    all_contacts += f'{name.title()} | {phone.title()}' + '\n'

                print(all_contacts)
            
            
        elif choice == '3':
            search = input('Ism: ').strip()
            for name, phone in phonebook.items():
                if search.lower() in name.lower():
                    print(name, phone)
        
        elif choice == '4':
            return 'Dastur tugadi.'
        
        else:
            print('Bunday menu mavjud emas.')
    
phonebook = {
    'Ali':'+998991223434',
    'Vali':'+9981234567'
}
print(phonebook_menu(phonebook))