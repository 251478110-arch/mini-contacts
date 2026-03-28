
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