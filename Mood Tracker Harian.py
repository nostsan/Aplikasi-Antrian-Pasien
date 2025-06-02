import csv
import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

CSV_FILE = "antrian_pasien.csv"
antrian = []

def simpan_ke_csv():
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["nama", "prioritas", "waktu"])
        writer.writeheader()
        writer.writerows(antrian)

def tambah_pasien():
    nama = simpledialog.askstring("Tambah Pasien", "Masukkan nama pasien:")
    if nama:
        prioritas = messagebox.askyesno("Prioritas", "Apakah pasien darurat?")
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data_pasien = {"nama": nama, "prioritas": prioritas, "waktu": waktu}
        if prioritas:
            antrian.insert(0, data_pasien)
        else:
            antrian.append(data_pasien)
        simpan_ke_csv()
        messagebox.showinfo("Sukses", f"Pasien '{nama}' berhasil ditambahkan.")

def panggil_pasien():
    if antrian:
        pasien = antrian.pop(0)
        simpan_ke_csv()
        messagebox.showinfo("Panggil Pasien", f"Memanggil: {pasien['nama']}")
    else:
        messagebox.showwarning("Kosong", "Tidak ada pasien dalam antrian.")

def lihat_antrian():
    if not antrian:
        messagebox.showinfo("Antrian Kosong", "Belum ada pasien.")
        return

    daftar = ""
    for i, pasien in enumerate(antrian, start=1):
        status = "Darurat" if pasien["prioritas"] else "Biasa"
        daftar += f"{i}. {pasien['nama']} - {status} ({pasien['waktu']})\n"
    messagebox.showinfo("Daftar Antrian", daftar)

# GUI
root = tk.Tk()
root.title("Sistem Antrian Pasien")
root.geometry("400x300")

tk.Button(root, text="Tambah Pasien", command=tambah_pasien, height=2, width=20).pack(pady=10)
tk.Button(root, text="Panggil Pasien", command=panggil_pasien, height=2, width=20).pack(pady=10)
tk.Button(root, text="Lihat Daftar Antrian", command=lihat_antrian, height=2, width=20).pack(pady=10)
tk.Button(root, text="Keluar", command=root.destroy, height=2, width=20).pack(pady=10)

root.mainloop()
