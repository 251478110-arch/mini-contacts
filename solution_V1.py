
"""
MINI CONTACTS - V1
Simple contact manager that stores contacts in a text file.

V1 GÖREV LİSTESİ:
1. list komutu - tüm kişileri ekrana yazdır
2. search komutu - id ile kişi ara ve göster
3. delete komutu - id ile kişi sil
4. export komutu - kişileri belirtilen dosyaya aktar
"""

import os

FILE_NAME = "contacts.txt"

def run_command(command):
    """
    Main function that processes user commands.
    Returns output string.
    """
    if not command or command.strip() == "":
        return "Error: Missing arguments"
    
    parts = command.strip().split()
    cmd = parts[0].lower()
    
    # INIT
    if cmd == "init":
        open(FILE_NAME, 'w').close()
        return "Contact storage initialized"
    
    #  ADD 
    elif cmd == "add":
        if len(parts) < 4:
            return "Error: Missing arguments"
        
        contact_id = parts[1]
        name = parts[2]
        phone = parts[3]
        
        # ID kontrolü - aynı ID varsa ekleme
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, 'r') as f:
                for line in f:
                    if line.startswith(contact_id + "|"):
                        return "Error: ID already exists"
        
        with open(FILE_NAME, 'a') as f:
            f.write(f"{contact_id}|{name}|{phone}\n")
        return "Contact added"
    
    #  LIST 
    elif cmd == "list":
        if not os.path.exists(FILE_NAME):
            return "Error: Storage not initialized"
        
        with open(FILE_NAME, 'r') as f:
            content = f.read()
            if content:
                return content.rstrip('\n')
            return "No contacts found"
    
    #  SEARCH 
    elif cmd == "search":
        if not os.path.exists(FILE_NAME):
            return "Error: Storage not initialized"
        
        if len(parts) < 2:
            return "Error: Missing arguments"
        
        search_id = parts[1]
        with open(FILE_NAME, 'r') as f:
            for line in f:
                if line.startswith(search_id + "|"):
                    return line.rstrip('\n')
        return "Contact not found"
    
    # DELETE 
    elif cmd == "delete":
        if not os.path.exists(FILE_NAME):
            return "Error: Storage not initialized"
        
        if len(parts) < 2:
            return "Error: Missing arguments"
        
        delete_id = parts[1]
        with open(FILE_NAME, 'r') as f:
            lines = f.readlines()
        
        found = False
        with open(FILE_NAME, 'w') as f:
            for line in lines:
                if line.startswith(delete_id + "|"):
                    found = True
                else:
                    f.write(line)
        
        if found:
            return "Contact deleted"
        return "Contact not found"
    
    # EXPORT 
    elif cmd == "export":
        if not os.path.exists(FILE_NAME):
            return "Error: Storage not initialized"
        
        if len(parts) < 2:
            return "Error: Missing arguments"
        
        export_file = parts[1]
        with open(FILE_NAME, 'r') as f:
            content = f.read()
        
        with open(export_file, 'w') as f:
            f.write(content)
        
        return "Contacts exported"
    
    # UNKNOWN 
    else:
        return "Error: Unknown command"

"""
V2 GÖREVLERİ:
1. ID format kontrolü ekle (sadece rakam kabul et)
2. Telefon numarası format kontrolü (min 7, max 15 karakter, sadece rakam)
3. "help" komutu ekle – tüm komutları listele
"""
"""
MINI CONTACTS - V2
"""

import os

FILE_NAME = "contacts.txt"


def is_valid_id(contact_id):
    return contact_id.isdigit()


def is_valid_phone(phone):
    return phone.isdigit() and 7 <= len(phone) <= 15


def run_command(command):
    if not command or command.strip() == "":
        return "Error: Missing arguments"

    parts = command.strip().split()
    cmd = parts[0].lower()

    # INIT
    if cmd == "init":
        open(FILE_NAME, 'w').close()
        return "Contact storage initialized"

    # ADD
    elif cmd == "add":
        if len(parts) < 4:
            return "Error: Missing arguments"

        contact_id = parts[1]
        phone = parts[-1]
        name = " ".join(parts[2:-1])

        if not is_valid_id(contact_id):
            return "Error: ID must contain only digits"

        if not is_valid_phone(phone):
            return "Error: Invalid phone number"

        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, 'r') as f:
                for line in f:
                    if line.startswith(contact_id + "|"):
                        return "Error: ID already exists"

        with open(FILE_NAME, 'a') as f:
            f.write(f"{contact_id}|{name}|{phone}\n")

        return "Contact added"

    # LIST
    elif cmd == "list":
        if not os.path.exists(FILE_NAME):
            return "Error: Storage not initialized"

        with open(FILE_NAME, 'r') as f:
            content = f.read()
            if content:
                return content.rstrip('\n')
            return "No contacts found"

    # SEARCH (ID veya isimle)
    elif cmd == "search":
        if not os.path.exists(FILE_NAME):
            return "Error: Storage not initialized"

        if len(parts) < 2:
            return "Error: Missing arguments"

        keyword = parts[1].lower()
        results = []

        with open(FILE_NAME, 'r') as f:
            for line in f:
                contact_id, name, phone = line.strip().split("|")

                if keyword in contact_id.lower() or keyword in name.lower():
                    results.append(line.strip())

        if results:
            return "\n".join(results)

        return "Contact not found"

    # UPDATE
    elif cmd == "update":
        if not os.path.exists(FILE_NAME):
            return "Error: Storage not initialized"

        if len(parts) < 4:
            return "Error: Missing arguments"

        update_id = parts[1]
        new_phone = parts[-1]
        new_name = " ".join(parts[2:-1])

        if not is_valid_id(update_id):
            return "Error: ID must contain only digits"

        if not is_valid_phone(new_phone):
            return "Error: Invalid phone number"

        with open(FILE_NAME, 'r') as f:
            lines = f.readlines()

        found = False
        with open(FILE_NAME, 'w') as f:
            for line in lines:
                if line.startswith(update_id + "|"):
                    f.write(f"{update_id}|{new_name}|{new_phone}\n")
                    found = True
                else:
                    f.write(line)

        if found:
            return "Contact updated"

        return "Contact not found"

    # DELETE
    elif cmd == "delete":
        if not os.path.exists(FILE_NAME):
            return "Error: Storage not initialized"

        if len(parts) < 2:
            return "Error: Missing arguments"

        delete_id = parts[1]

        with open(FILE_NAME, 'r') as f:
            lines = f.readlines()

        found = False
        with open(FILE_NAME, 'w') as f:
            for line in lines:
                if line.startswith(delete_id + "|"):
                    found = True
                else:
                    f.write(line)

        if found:
            return "Contact deleted"

        return "Contact not found"

    # EXPORT
    elif cmd == "export":
        if not os.path.exists(FILE_NAME):
            return "Error: Storage not initialized"

        if len(parts) < 2:
            return "Error: Missing arguments"

        export_file = parts[1]

        with open(FILE_NAME, 'r') as f:
            content = f.read()

        with open(export_file, 'w') as f:
            f.write(content)

        return "Contacts exported"

    # HELP
    elif cmd == "help":
        return (
            "Available commands:\n"
            "init - initialize storage\n"
            "add <id> <name> <phone>\n"
            "list - list all contacts\n"
            "search <id|name>\n"
            "update <id> <name> <phone>\n"
            "delete <id>\n"
            "export <filename>\n"
            "help - show this message"
        )

    # UNKNOWN
    else:
        return "Error: Unknown command"
