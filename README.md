# MINI CONTACTS - V1

## V0 → V1 Değişiklikleri

### Eklenen Özellikler:
1. **list** - Artık tüm kişileri görüntüleyebiliyorsunuz
2. **search** - ID ile kişi arama özelliği eklendi
3. **delete** - ID ile kişi silme özelliği eklendi
4. **export** - Kişileri başka bir dosyaya aktarma özelliği eklendi

### İyileştirmeler:
- Aynı ID ile tekrar ekleme yapılmaya çalışılırsa hata mesajı verilir
- Dosya yoksa komutlar hata mesajı döndürür

## Kullanım

| Komut | Açıklama | Örnek |
|-------|----------|-------|
| init | Depolama dosyasını oluşturur | init |
| add | Yeni kişi ekler | add 1 Ahmet 5551234 |
| list | Tüm kişileri listeler | list |
| search | ID ile kişi arar | search 1 |
| delete | ID ile kişi siler | delete 1 |
| export | Kişileri dışa aktarır | export yedek.txt |

V2 GÖREVLERİ:
1. ID format kontrolü eklendi (sadece rakam kabul edilir)
2. Telefon numarası doğrulaması eklendi (7-15 karakter, sadece rakam)
3. "help" komutu eklendi (tüm komutları listeler)
