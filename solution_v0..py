# Bu fonksiyon kullanıcıdan gelen komutu çalıştırır
def run_command(command):

    parts = command.split(" ")
    cmd = parts[0]

    # init komutu: contacts.txt dosyasını oluşturur
    if cmd == "init":
        f = open("contacts.txt", "w")
        f.close()
        return "Contact storage initialized"

    # add komutu: yeni kişi ekler
    elif cmd == "add":

        # parametre eksik mi kontrol edilir
        if len(parts) < 4:
            return "Error: Missing arguments"

        contact_id = parts[1]
        name = parts[2]
        phone = parts[3]

        f = open("contacts.txt", "a")
        f.write(contact_id + "|" + name + "|" + phone + "\n")
        f.close()

        return "Contact added"

    # diğer komutlar henüz yapılmadı
    elif cmd == "list":
        return "Not implemented"

    elif cmd == "search":
        return "Not implemented"

    elif cmd == "delete":
        return "Not implemented"

    elif cmd == "export":
        return "Not implemented"

    # bilinmeyen komut
    else:
        return "Error: Unknown command"
