import tkinter as tk
from tkinter import ttk, messagebox
from pyswip import Prolog
from query_samples import query_samples, quan_huyen, dia_diem_list, phuong_tien

# Khởi tạo Prolog và nạp cơ sở tri thức từ file
prolog = Prolog()
prolog.consult("main.pl")

# Hàm cập nhật truy vấn với giá trị nhập
def update_query():
    selected_query = query_combobox.get()
    if selected_query in queries:
        raw_query = queries[selected_query]

        # Lấy giá trị từ các input
        quan = quan_combobox.get()
        diem_khoi_hanh = diem_khoi_hanh_combobox.get()
        diem_den = diem_den_combobox.get()
        phuong_tien = phuong_tien_combobox.get()

        # Thay thế các tham số trong truy vấn
        formatted_query = raw_query.replace("{QUAN}", quan)\
                                   .replace("{DIEM_KHOI_HANH}", diem_khoi_hanh)\
                                   .replace("{DIEM_DEN}", diem_den)\
                                   .replace("{PHUONG_TIEN}", phuong_tien)

        query_entry.delete(0, tk.END)
        query_entry.insert(0, formatted_query)

# Hàm thực hiện truy vấn Prolog
def truy_van_prolog():
    query_str = query_entry.get().strip()
    if not query_str:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn hoặc nhập truy vấn Prolog!")
        return
    try:
        results = list(prolog.query(query_str))
        result_text.delete("1.0", tk.END)
        if results:
            for res in results:
                formatted_result = "Kết quả:\n"
                for key, value in res.items():
                    formatted_result += f"  - {key}: {value}\n"
                result_text.insert(tk.END, formatted_result + "\n")
        else:
            result_text.insert(tk.END, "Không tìm thấy kết quả.")
    except Exception as e:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Lỗi truy vấn: " + str(e))

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Gợi ý du lịch Cần Thơ với Prolog")
root.geometry("800x550")

# Danh sách câu hỏi từ query_samples
queries = {}
for category in query_samples:
    for question, query in query_samples[category]:
        queries[question] = query

# Nhãn danh mục truy vấn
tk.Label(root, text="Chọn truy vấn:", font=("Arial", 12)).pack(pady=5)

# Combobox chọn câu hỏi
query_combobox = ttk.Combobox(root, values=list(queries.keys()), font=("Arial", 11), width=80)
query_combobox.pack(pady=5)
query_combobox.bind("<<ComboboxSelected>>", lambda event: update_query())

# **Ô nhập tham số động**
param_frame = tk.Frame(root)
param_frame.pack(pady=5)

tk.Label(param_frame, text="Quận:", font=("Arial", 11)).grid(row=0, column=0, padx=5, pady=2)
quan_combobox = ttk.Combobox(param_frame, values=quan_huyen, font=("Arial", 11), width=12)
quan_combobox.grid(row=0, column=1, padx=5, pady=2)

tk.Label(param_frame, text="Điểm khởi hành:", font=("Arial", 11)).grid(row=0, column=2, padx=5, pady=2)
diem_khoi_hanh_combobox = ttk.Combobox(param_frame, values=dia_diem_list, font=("Arial", 11), width=15)
diem_khoi_hanh_combobox.grid(row=0, column=3, padx=5, pady=2)

tk.Label(param_frame, text="Điểm đến:", font=("Arial", 11)).grid(row=1, column=0, padx=5, pady=2)
diem_den_combobox = ttk.Combobox(param_frame, values=dia_diem_list, font=("Arial", 11), width=15)
diem_den_combobox.grid(row=1, column=1, padx=5, pady=2)

tk.Label(param_frame, text="Phương tiện:", font=("Arial", 11)).grid(row=1, column=2, padx=5, pady=2)
phuong_tien_combobox = ttk.Combobox(param_frame, values=phuong_tien, font=("Arial", 11), width=12)
phuong_tien_combobox.grid(row=1, column=3, padx=5, pady=2)

# Nút cập nhật truy vấn
tk.Button(root, text="Cập nhật truy vấn", command=update_query, font=("Arial", 11)).pack(pady=5)

# Ô nhập truy vấn
query_entry = tk.Entry(root, width=80, font=("Arial", 11))
query_entry.pack(pady=5)

# Nút thực hiện truy vấn
tk.Button(root, text="Thực hiện truy vấn", command=truy_van_prolog, font=("Arial", 11)).pack(pady=5)

# Kết quả hiển thị
result_text = tk.Text(root, height=12, width=90, font=("Arial", 11))
result_text.pack(pady=5)

root.mainloop()
