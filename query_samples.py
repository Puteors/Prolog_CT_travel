# Truy vấn mẫu với tham số động
query_samples = {
    "🍽️ Quán ăn": [
        ("Tìm quán ăn ở Quận có thể đi từ Điểm khởi hành bằng Phương tiện",
         "vi_tri(DiaDiem, Quận), loai_dia_diem(DiaDiem, quan_an), "
         "khoang_cach(Điểm khởi hành, DiaDiem, KhoangCach), "
         "lua_chon_phuong_tien(KhoangCach, Phương tiện)."),

        ("Danh sách tất cả quán ăn ở Quận",
         "vi_tri(DiaDiem, Quận), loai_dia_diem(DiaDiem, quan_an)."),

        ("Tìm quán ăn cách Điểm khởi hành dưới 5km",
         "khoang_cach(Điểm khởi hành, DiaDiem, KhoangCach), "
         "loai_dia_diem(DiaDiem, quan_an), KhoangCach < 5.")
    ],

    "☕ Quán cà phê": [
        ("Tìm quán cà phê trong bán kính 5km từ Điểm khởi hành",
         "khoang_cach(Điểm khởi hành, DiaDiem, KhoangCach), "
         "loai_dia_diem(DiaDiem, quan_cafe), KhoangCach =< 5."),

        ("Danh sách tất cả quán cà phê ở Quận",
         "vi_tri(DiaDiem, Quận), loai_dia_diem(DiaDiem, quan_cafe)."),

        ("Tìm quán cà phê có thể đến từ Điểm khởi hành bằng Phương tiện",
         "loai_dia_diem(DiaDiem, quan_cafe), khoang_cach(Điểm khởi hành, DiaDiem, KhoangCach), "
         "lua_chon_phuong_tien(KhoangCach, Phương tiện).")
    ],

    "🏞️ Địa điểm du lịch": [

        ("Các địa điểm du lịch trong bán kính 10km từ Điểm khởi hành",
         "khoang_cach(Điểm khởi hành, DiaDiem, KhoangCach), "
         "loai_dia_diem(DiaDiem, khu_du_lich), KhoangCach =< 10."),

        ("Tìm địa điểm du lịch có thể đến từ Điểm khởi hành bằng Phương tiện",
         "loai_dia_diem(DiaDiem, khu_du_lich), khoang_cach(Điểm khởi hành, DiaDiem, KhoangCach), "
         "lua_chon_phuong_tien(KhoangCach, Phương tiện).")
    ],

    "🚕 Phương tiện di chuyển": [
        ("Tìm phương tiện phù hợp từ Điểm khởi hành đến Điểm đến",
         "khoang_cach(Điểm khởi hành, Điểm đến, KhoangCach), lua_chon_phuong_tien(KhoangCach, PhuongTien)."),

        ("Phương tiện đi từ Điểm khởi hành đến các địa điểm trong bán kính 10km",
         "khoang_cach(Điểm khởi hành, DiaDiem, KhoangCach), KhoangCach =< 10, "
         "lua_chon_phuong_tien(KhoangCach, X).")
    ],

    "📏 Khoảng cách": [
        ("Danh sách địa điểm cách Điểm khởi hành dưới 5km",
         "khoang_cach(Điểm khởi hành, DiaDiem, KhoangCach), KhoangCach < 5."),

        ("Khoảng cách từ Điểm khởi hành đến Điểm đến",
         "khoang_cach(Điểm khởi hành, Điểm đến, KhoangCach).")
    ],
    "⏳ Thời gian phù hợp": [
        ("Thời gian phù hợp để tham quan Điểm khởi hành",
        "thoi_gian_phu_hop(Điểm khởi hành, ThoiGian)."),

        ("Danh sách các địa điểm phù hợp vào Thời gian",
        "thoi_gian_phu_hop(DiaDiem, Thời gian)."),

        ("Tìm quán cà phê mở cửa vào Thời gian",
        "thoi_gian_phu_hop(DiaDiem, Thời gian), loai_dia_diem(DiaDiem, quan_cafe)."),

        ("Tìm quán ăn mở cửa vào Thời gian",
        "thoi_gian_phu_hop(DiaDiem, Thời gian), loai_dia_diem(DiaDiem, quan_an)."),

        ("Tìm địa điểm du lịch mở cửa vào Thời gian",
        "thoi_gian_phu_hop(DiaDiem, Thời gian), loai_dia_diem(DiaDiem, khu_du_lich).")
    ]
}