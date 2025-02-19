% Các phương tiện giao thông
phuong_tien(xe_may).
phuong_tien(xe_dap).
phuong_tien(taxi).
phuong_tien(di_bo).
phuong_tien(xe_bus).

% Quy tắc lựa chọn phương tiện dựa trên khoảng cách
lua_chon_phuong_tien(KhoangCach, di_bo) :- KhoangCach =< 1.

lua_chon_phuong_tien(KhoangCach, xe_dap) :- KhoangCach =< 1.
lua_chon_phuong_tien(KhoangCach, xe_dap) :- KhoangCach > 1, KhoangCach =< 5.

lua_chon_phuong_tien(KhoangCach, xe_may) :- KhoangCach > 1, KhoangCach =< 5.
lua_chon_phuong_tien(KhoangCach, xe_may) :- KhoangCach > 5, KhoangCach =< 10.

lua_chon_phuong_tien(KhoangCach, taxi) :- KhoangCach > 10, KhoangCach =< 20.

lua_chon_phuong_tien(KhoangCach, xe_bus) :- KhoangCach > 20.
