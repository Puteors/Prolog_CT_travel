
dia_diem_list = [
    "ben_ninh_kieu", "cho_noi_cai_rang", "nha_co_binh_thuy", 
    "vuon_du_lich_my_khanh", "thien_vien_truc_lam_phuong_nam", 
    "con_son", "cho_dem_tay_do", "khach_san_azerai", "khach_san_vinpearl", 
    "khach_san_muong_thanh", "hoa_yen_cafe", "tiem_tra_co_ngot", 
    "bo_nuong_ngoi_cu_lan", "sui_cao_a_chay"
]

quan_huyen = ["ninh_kieu", "binh_thuy", "cai_rang", "phong_dien"]
phuong_tien = ["xe_may", "di_bo", "xe_dap", "taxi", "xe_bus"]
loai_dia_diem = ["quan_an", "quan_cafe", "khu_du_lich", "khach_san"]

# Truy vấn mẫu với tham số động
query_samples = {
    "🍽️ Quán ăn": [
        ("Tìm quán ăn ở {QUAN} có thể đi từ {DIEM_KHOI_HANH} bằng {PHUONG_TIEN}",
         "vi_tri(DiaDiem, {QUAN}), loai_dia_diem(DiaDiem, quan_an), "
         "khoang_cach({DIEM_KHOI_HANH}, DiaDiem, KhoangCach), "
         "lua_chon_phuong_tien(KhoangCach, {PHUONG_TIEN})."),

        ("Danh sách tất cả quán ăn ở {QUAN}",
         "vi_tri(DiaDiem, {QUAN}), loai_dia_diem(DiaDiem, quan_an)."),

        ("Tìm quán ăn cách {DIEM_KHOI_HANH} dưới 5km",
         "khoang_cach({DIEM_KHOI_HANH}, DiaDiem, KhoangCach), "
         "loai_dia_diem(DiaDiem, quan_an), KhoangCach < 5.")
    ],

    "☕ Quán cà phê": [
        ("Tìm quán cà phê trong bán kính 5km từ {DIEM_KHOI_HANH}",
         "khoang_cach({DIEM_KHOI_HANH}, DiaDiem, KhoangCach), "
         "loai_dia_diem(DiaDiem, quan_cafe), KhoangCach =< 5."),

        ("Danh sách tất cả quán cà phê ở {QUAN}",
         "vi_tri(DiaDiem, {QUAN}), loai_dia_diem(DiaDiem, quan_cafe)."),

        ("Tìm quán cà phê có thể đến từ {DIEM_KHOI_HANH} bằng {PHUONG_TIEN}",
         "loai_dia_diem(DiaDiem, quan_cafe), khoang_cach({DIEM_KHOI_HANH}, DiaDiem, KhoangCach), "
         "lua_chon_phuong_tien(KhoangCach, {PHUONG_TIEN}).")
    ],

    "🏞️ Địa điểm du lịch": [
        ("Danh sách các khu du lịch sinh thái ở {QUAN}",
         "loai_dia_diem(DiaDiem, khu_du_lich), loai_hinh_dia_diem(DiaDiem, du_lich_sinh_thai), "
         "vi_tri(DiaDiem, {QUAN})."),

        ("Các địa điểm du lịch trong bán kính 10km từ {DIEM_KHOI_HANH}",
         "khoang_cach({DIEM_KHOI_HANH}, DiaDiem, KhoangCach), "
         "loai_dia_diem(DiaDiem, khu_du_lich), KhoangCach =< 10."),

        ("Tìm địa điểm du lịch có thể đến từ {DIEM_KHOI_HANH} bằng {PHUONG_TIEN}",
         "loai_dia_diem(DiaDiem, khu_du_lich), khoang_cach({DIEM_KHOI_HANH}, DiaDiem, KhoangCach), "
         "lua_chon_phuong_tien(KhoangCach, {PHUONG_TIEN}).")
    ],

    "🚕 Phương tiện di chuyển": [
        ("Tìm phương tiện phù hợp từ {DIEM_KHOI_HANH} đến {DIEM_DEN}",
         "khoang_cach({DIEM_KHOI_HANH}, {DIEM_DEN}, Y), lua_chon_phuong_tien(Y, X)."),

        ("Phương tiện đi từ {DIEM_KHOI_HANH} đến các địa điểm trong bán kính 10km",
         "khoang_cach({DIEM_KHOI_HANH}, DiaDiem, KhoangCach), KhoangCach =< 10, "
         "lua_chon_phuong_tien(KhoangCach, X).")
    ],

    "📏 Khoảng cách": [
        ("Danh sách địa điểm cách {DIEM_KHOI_HANH} dưới 5km",
         "khoang_cach({DIEM_KHOI_HANH}, DiaDiem, KhoangCach), KhoangCach < 5."),

        ("Khoảng cách từ {DIEM_KHOI_HANH} đến {DIEM_DEN}",
         "khoang_cach({DIEM_KHOI_HANH}, {DIEM_DEN}, KhoangCach).")
    ]
}