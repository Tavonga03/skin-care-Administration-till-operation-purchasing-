import datetime
import csv
import os
import tkinter as tk
from tkinter import ttk, messagebox

# Data Produk
produk = {
    "Wardah": {"UV Shield Sunscreen": 30000, "Light Moisturizer Gel": 35000, "Hydrating Toner": 32000, "Crystal Secret Facial Wash": 28000, "C-Defense Serum": 45000},
    "Emina": {"Sun Battle SPF 50": 28000, "Bright Stuff Moisturizer": 32000, "Bright Stuff Toner": 30000, "Ms. Pimple Facial Wash": 27000, "Bright Stuff Serum": 40000},
    "Azarine": {"Hydrasoothe Sunscreen": 40000, "Oil Free Moisturizer": 42000, "Hydrasoothe Toner": 38000, "Cleansing Gel": 35000, "Niacinamide Serum": 50000},
    "Somethinc": {"Holyshield Sunscreen": 55000, "Ceramide Moisturizer": 60000, "Glow Toner": 58000, "Low pH Cleanser": 50000, "Niacinamide Serum": 65000},
    "Hada Labo": {"Perfect UV Gel": 45000, "Gokujyun Moisturizer": 50000, "Gokujyun Toner": 48000, "Face Wash Ultimate": 40000, "Shirojyun Serum": 55000}
}

CSV_FILE = "history_penjualan.csv"

def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Tanggal", "Brand", "Produk", "Jumlah", "Harga", "Subtotal", "Total", "Diskon", "Total Bayar"])

class KasirApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kasir Toko Skincare")
        self.root.geometry("950x650")
        
        self.keranjang = []
        init_csv()
        self.tampilan_menu_utama()

    def tampilan_menu_utama(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="KASIR TOKO SKINCARE", font=("Arial", 20, "bold")).pack(pady=30)
        
        tk.Button(self.root, text="Transaksi Baru", font=("Arial", 14), width=30, height=2, command=self.transaksi_baru).pack(pady=12)
        tk.Button(self.root, text="Lihat Riwayat Penjualan", font=("Arial", 14), width=30, height=2, command=self.lihat_riwayat).pack(pady=12)
        tk.Button(self.root, text="Keluar", font=("Arial", 14), width=30, height=2, command=self.root.quit).pack(pady=12)

    def transaksi_baru(self):
        self.keranjang = []
        self.tampilan_transaksi()

    def tampilan_transaksi(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Kiri: Pilih Produk
        left = tk.Frame(self.root, padx=20, pady=20)
        left.pack(side=tk.LEFT, fill=tk.Y)
        
        tk.Label(left, text="Pilih Brand:", font=("Arial", 12, "bold")).pack(anchor="w")
        self.brand_combo = ttk.Combobox(left, values=list(produk.keys()), state="readonly", width=35)
        self.brand_combo.pack(pady=5)
        self.brand_combo.bind("<<ComboboxSelected>>", self.update_produk)
        
        tk.Label(left, text="Pilih Produk:", font=("Arial", 12, "bold")).pack(anchor="w", pady=(10,0))
        self.produk_combo = ttk.Combobox(left, width=35, state="readonly")
        self.produk_combo.pack(pady=5)
        
        tk.Label(left, text="Jumlah:", font=("Arial", 12, "bold")).pack(anchor="w", pady=(10,0))
        self.jumlah_spin = tk.Spinbox(left, from_=1, to=50, width=15)
        self.jumlah_spin.pack(pady=5)
        
        tk.Button(left, text="Tambah ke Keranjang", font=("Arial", 11), command=self.tambah_keranjang).pack(pady=20)

        # Kanan: Keranjang + Pembayaran
        right = tk.Frame(self.root, padx=20, pady=20)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        tk.Label(right, text="Keranjang Belanja", font=("Arial", 14, "bold")).pack(anchor="w")
        
        self.tree = ttk.Treeview(right, columns=("brand", "produk", "jumlah", "subtotal"), show="headings", height=12)
        self.tree.heading("brand", text="Brand")
        self.tree.heading("produk", text="Produk")
        self.tree.heading("jumlah", text="Jml")
        self.tree.heading("subtotal", text="Subtotal (Rp)")
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.total_label = tk.Label(right, text="Total: Rp 0", font=("Arial", 12))
        self.total_label.pack(anchor="w", pady=5)
        
        # Kolom Pembayaran
        pay_frame = tk.LabelFrame(right, text="Pembayaran", padx=10, pady=10)
        pay_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(pay_frame, text="Uang Dibayar (Rp):").pack(anchor="w")
        self.bayar_entry = tk.Entry(pay_frame, font=("Arial", 12))
        self.bayar_entry.pack(fill=tk.X, pady=5)
        
        tk.Button(right, text="Hitung & Bayar", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=self.proses_bayar).pack(pady=10)
        tk.Button(right, text="Kembali ke Menu", command=self.tampilan_menu_utama).pack()

    def update_produk(self, event=None):
        brand = self.brand_combo.get()
        if brand:
            self.produk_combo['values'] = list(produk[brand].keys())

    def tambah_keranjang(self):
        brand = self.brand_combo.get()
        produk_nama = self.produk_combo.get()
        try:
            jumlah = int(self.jumlah_spin.get())
        except:
            messagebox.showwarning("Salah", "Jumlah harus berupa angka!")
            return
        
        if not brand or not produk_nama:
            messagebox.showwarning("Salah", "Pilih Brand dan Produk terlebih dahulu!")
            return
        
        harga = produk[brand][produk_nama]
        subtotal = harga * jumlah
        
        self.keranjang.append({
            "brand": brand, "nama": produk_nama, "jumlah": jumlah,
            "harga": harga, "subtotal": subtotal
        })
        
        self.update_keranjang()
        messagebox.showinfo("Berhasil", f"{produk_nama} x{jumlah} ditambahkan ke keranjang")

    def update_keranjang(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        total = 0
        for item in self.keranjang:
            self.tree.insert("", tk.END, values=(item["brand"], item["nama"], item["jumlah"], f"{item['subtotal']:,}"))
            total += item["subtotal"]
        
        self.total_label.config(text=f"Total: Rp {total:,}")

    def proses_bayar(self):
        if not self.keranjang:
            messagebox.showwarning("Kosong", "Keranjang masih kosong!")
            return
        
        total = sum(item["subtotal"] for item in self.keranjang)
        diskon = int(0.1 * total) if total > 150000 else 0
        total_bayar = total - diskon
        
        try:
            bayar = int(self.bayar_entry.get())
        except:
            messagebox.showwarning("Salah", "Masukkan uang pembayaran dengan angka!")
            return
        
        if bayar < total_bayar:
            messagebox.showwarning("Kurang", f"Uang kurang! Total bayar adalah Rp {total_bayar:,}")
            return
        
        kembalian = bayar - total_bayar
        self.cetak_struk(total, diskon, total_bayar, bayar, kembalian)
        self.simpan_ke_csv(total, diskon, total_bayar, bayar)
        
        messagebox.showinfo("Sukses", "Transaksi berhasil!\nTerima kasih telah berbelanja.")
        self.tampilan_menu_utama()

    def cetak_struk(self, total, diskon, total_bayar, bayar, kembalian):
        struk = f"""
=== STRUK PEMBAYARAN ===
Tanggal : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}

"""
        for item in self.keranjang:
            struk += f"{item['brand']} - {item['nama']} x{item['jumlah']} = Rp{item['subtotal']:,}\n"
        
        struk += f"""
Total          : Rp{total:,}
Diskon         : Rp{diskon:,}
Total Bayar    : Rp{total_bayar:,}
Uang Dibayar   : Rp{bayar:,}
Kembalian      : Rp{kembalian:,}

Terima kasih telah berbelanja!
"""
        messagebox.showinfo("Struk Pembayaran", struk)

    def simpan_ke_csv(self, total, diskon, total_bayar, bayar):
        tanggal = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for item in self.keranjang:
            with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([
                    tanggal, item["brand"], item["nama"], item["jumlah"],
                    item["harga"], item["subtotal"], total, diskon, total_bayar
                ])

    def lihat_riwayat(self):
        if not os.path.exists(CSV_FILE):
            messagebox.showinfo("Riwayat", "Belum ada transaksi.")
            return
        
        win = tk.Toplevel(self.root)
        win.title("Riwayat Penjualan")
        win.geometry("1100x550")
        
        tree = ttk.Treeview(win, columns=("tgl","brand","produk","jml","sub","total","diskon","bayar"), show="headings")
        for col, text in zip(tree["columns"], ["Tanggal","Brand","Produk","Jumlah","Subtotal","Total","Diskon","Total Bayar"]):
            tree.heading(col, text=text)
            tree.column(col, width=120)
        
        tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        with open(CSV_FILE, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                tree.insert("", tk.END, values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = KasirApp(root)
    root.mainloop()