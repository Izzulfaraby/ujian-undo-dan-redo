# Inisialisasi stack untuk undo dan redo
undo_stack = []
redo_stack = []
aksi_saat_ini = ""

# Aksi default
aksi_default = [
    "Menjalankan Office Word",
    "Membuka Google Chrome",
    "Menjalankan Visual Studio Code"
]

# Menambahkan aksi default ke dalam aksi_saat_ini dan undo_stack
for action in aksi_default:
    if aksi_saat_ini:
        undo_stack.append(aksi_saat_ini)  # Simpan aksi sebelumnya
    aksi_saat_ini = action  # Set aksi saat ini
    redo_stack.clear()  # Kosongkan redo stack

print("Sistem Undo dan Redo")
print(f"Aksi Saat Ini: {aksi_saat_ini}")

while True:
    print("\nMenu:")
    print("1. Tambahkan Aksi")
    print("2. Undo")
    print("3. Redo")
    print("4. Lihat Aksi Saat Ini")
    print("5. Keluar")
    
    pilihan = input("Pilih opsi (1-5): ")
    
    if pilihan == '1':
        aksi_baru = input("Masukkan aksi baru: ")
        if aksi_saat_ini:
            undo_stack.append(aksi_saat_ini)  # Simpan aksi sebelumnya
        aksi_saat_ini = aksi_baru  # Set aksi saat ini
        redo_stack.clear()  # Kosongkan redo stack
        print(f"Aksi ditambahkan: {aksi_saat_ini}")
        
    elif pilihan == '2':
        if undo_stack:
            redo_stack.append(aksi_saat_ini)  # Simpan aksi saat ini ke redo stack
            aksi_saat_ini = undo_stack.pop()  # Kembalikan aksi sebelumnya
            print(f"Undo: {aksi_saat_ini}")
        else:
            print("Tidak ada aksi yang bisa di-undo.")
            
    elif pilihan == '3':
        if redo_stack:
            undo_stack.append(aksi_saat_ini)  # Simpan aksi saat ini ke undo stack
            aksi_saat_ini = redo_stack.pop()  # Kembalikan aksi yang di-redo
            print(f"Redo: {aksi_saat_ini}")
        else:
            print("Tidak ada aksi yang bisa di-redo.")
            
    elif pilihan == '4':
        print(f"Aksi Saat Ini: {aksi_saat_ini if aksi_saat_ini else 'Tidak ada aksi'}")
        
    elif pilihan == '5':
        print("Keluar dari program.")
        break
        
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
