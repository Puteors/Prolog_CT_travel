import tkinter as tk
from tkinter import ttk, messagebox
from pyswip import Prolog
from query_samples import query_samples
from utils import translations_keys, translations_values, quan_huyen, dia_diem, phuong_tien, thoi_gian, \
    convert_thoi_gian, convert_quan_huyen, convert_dia_diem, convert_phuong_tien, convert_thoi_gian

# Khởi tạo Prolog và nạp cơ sở tri thức từ file
prolog = Prolog()
prolog.consult("main.pl")

# Hàm cập nhật truy vấn với giá trị nhập
def update_query():
    selected_query = query_combobox.get()
    if selected_query in queries:
        raw_query = queries[selected_query]

        # Lấy giá trị từ các input và chuyển nó sang đúng format dựa trên ultils
        
        quan = quan_combobox.get()
        diem_khoi_hanh = diem_khoi_hanh_combobox.get()
        diem_den = diem_den_combobox.get()
        phuong_tien = phuong_tien_combobox.get()
        thoi_gian = thoi_gian_combobox.get()

        # Thay thế các tham số trong truy vấn
        formatted_query = raw_query.replace("Quận", convert_quan_huyen[quan] if quan != "" else "")\
                                   .replace("Điểm khởi hành", convert_dia_diem[diem_khoi_hanh] if diem_khoi_hanh != "" else "")\
                                   .replace("Điểm đến", convert_dia_diem[diem_den] if diem_den != "" else "")\
                                   .replace("Phương tiện", convert_phuong_tien[phuong_tien] if phuong_tien != "" else "")\
                                   .replace("Thời gian", convert_thoi_gian[thoi_gian] if thoi_gian != "" else "")


        query_entry.delete("1.0", tk.END)
        query_entry.insert("1.0", formatted_query)


# Hàm thực hiện truy vấn Prolog và hiển thị kết quả bằng tiếng Việt có dấu
def Query():
    query_str = query_entry.get("1.0", tk.END).strip()
    if not query_str:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn hoặc nhập truy vấn Prolog!")
        return
    try:
        results = list(prolog.query(query_str))
        result_text.delete("1.0", tk.END)
        if results:
            for res in results:
                formatted_result = "🔹 Kết quả:\n"
                for key, value in res.items():
                    # Dịch khóa (key) sang tiếng Việt
                    key_vietnamese = translations_keys.get(key, key)

                    # Dịch giá trị (value) sang tiếng Việt nếu có
                    value_vietnamese = translations_values.get(value, value)

                    # Nếu là số thì giữ nguyên
                    if isinstance(value, (int, float)):
                        value_vietnamese = f"{value} km"

                    formatted_result += f"  - {key_vietnamese}: {value_vietnamese}\n"
                
                result_text.insert(tk.END, formatted_result + "\n")
        else:
            result_text.insert(tk.END, "⚠️ Không tìm thấy kết quả.")
    except Exception as e:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"❌ Lỗi truy vấn: {str(e)}")


# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Gợi ý du lịch Cần Thơ với Prolog")
root.geometry("900x650")

# Danh sách câu hỏi từ query_samples
queries = {}
for category in query_samples:
    for question, query in query_samples[category]:
        queries[question] = query

# Nhãn danh mục truy vấn
tk.Label(root, text="Hãy đặt câu hỏi", font=("Arial", 12)).pack(pady=5)

# Combobox chọn câu hỏi
query_combobox = ttk.Combobox(root, values=list(queries.keys()), font=("Arial", 11), width=90)
query_combobox.pack(pady=5)
query_combobox.bind("<<ComboboxSelected>>", lambda event: update_query())

# **Ô nhập tham số động**
param_frame = tk.Frame(root)
param_frame.pack(pady=5)

tk.Label(param_frame, text="Quận:", font=("Arial", 11)).grid(row=0, column=0, padx=5, pady=2)
quan_combobox = ttk.Combobox(param_frame, values=quan_huyen, font=("Arial", 11), width=15)
quan_combobox.grid(row=0, column=1, padx=5, pady=2)

tk.Label(param_frame, text="Điểm khởi hành:", font=("Arial", 11)).grid(row=0, column=2, padx=5, pady=2)
diem_khoi_hanh_combobox = ttk.Combobox(param_frame, values=dia_diem, font=("Arial", 11), width=15)
diem_khoi_hanh_combobox.grid(row=0, column=3, padx=5, pady=2)

tk.Label(param_frame, text="Điểm đến:", font=("Arial", 11)).grid(row=1, column=0, padx=5, pady=2)
diem_den_combobox = ttk.Combobox(param_frame, values=dia_diem, font=("Arial", 11), width=15)
diem_den_combobox.grid(row=1, column=1, padx=5, pady=2)

tk.Label(param_frame, text="Phương tiện:", font=("Arial", 11)).grid(row=1, column=2, padx=5, pady=2)
phuong_tien_combobox = ttk.Combobox(param_frame, values=phuong_tien, font=("Arial", 11), width=15)
phuong_tien_combobox.grid(row=1, column=3, padx=5, pady=2)

tk.Label(param_frame, text="Thời gian:", font=("Arial", 11)).grid(row=2, column=0, padx=5, pady=2)
thoi_gian_combobox = ttk.Combobox(param_frame, values=thoi_gian, font=("Arial", 11), width=15)
thoi_gian_combobox.grid(row=2, column=1, padx=5, pady=2)

# Nút cập nhật truy vấn
tk.Button(root, text="Cập nhật truy vấn", command=update_query, font=("Arial", 11)).pack(pady=5)

# Ô nhập truy vấn (với định dạng đậm)
query_entry = tk.Text(root, height=4, width=90, font=("Arial", 11))
query_entry.pack(pady=5)

# Nút thực hiện truy vấn
tk.Button(root, text="Thực hiện truy vấn", command=Query, font=("Arial", 11)).pack(pady=5)

# Kết quả hiển thị
result_text = tk.Text(root, height=12, width=100, font=("Arial", 11))
result_text.pack(pady=5)

root.mainloop()
