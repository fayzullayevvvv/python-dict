def phonebook_menu(phonebook: dict[str, str]) -> None:
    print('1.Kontakt qo‘shish.')
    print('2.Barcha kontaktlarni chiqarish.')
    print('3.Ism bo‘yicha telefon qidirish.')

    choice = input('Tanlov: ')

    if choice == '1':
        name = input('Ism: ').strip().capitalize()
        phone = input('Telefon raqam: ').strip()
        phonebook[name] = phone

        return f'{name.capitalize()} qo\'shildi.'
    
    
    elif choice == '2':
        if not phonebook:
            return 'Kontakt bo\'sh.'
        else:
            all_contacts = ''
            for name, phone in phonebook.items():
                all_contacts += f'{name.title()} | {phone.title()}' + '\n'

            return all_contacts
        
        
    elif choice == '3':
        name = input('Ism: ').strip().capitalize()
        if name.title() in phonebook.keys():
            return phonebook[name]
        else:
            return 'Bunday ismli kontakt mavjud emas.'
    
    else:
        return 'Siz boshqa son yoki belgi kiritdingiz. Iltimos 1 dan 3 gacha kiriting.'
    
phonebook = {
    'Ali':'+998991223434',
    'Vali':'+9981234567'
}
print(phonebook_menu(phonebook))