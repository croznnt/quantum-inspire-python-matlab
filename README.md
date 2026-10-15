# Quantum Inspire: Python và MATLAB

**Ngôn ngữ / Language:** **Tiếng Việt** · [English](README.en.md)

Danh mục mã nguồn, notebook và công cụ trong hệ sinh thái Quantum Inspire, ưu tiên Python và hướng kết nối MATLAB.

**Cập nhật khảo sát:** 15 tháng 10 năm 2026 · **Tài khoản:** `croznnt` · **Repo đề xuất:** `quantum-inspire-python-matlab`

## 📊 Tổng quan danh mục

| Chỉ số | Số lượng | Phạm vi thống kê |
| :--- | :--- | :--- |
| Repo được tổng hợp | **10** | Các repo trong ba bảng bên dưới |
| Nguồn Python ưu tiên | **6** | SDK, bộ tích hợp, ví dụ, trình biên dịch và tiện ích |
| Công cụ và đặc tả bổ trợ | **3** | OpenQL, libqasm và QuIS; OpenQL cũng có giao diện Python |
| Repo tham khảo lịch sử | **1** | quantuminspire2 đã lưu trữ |
| SDK MATLAB chính thức đã xác minh | **0** | Chưa tìm thấy trong phạm vi khảo sát |
| Repo có trong script tải nguồn | **9** | Không gồm quantuminspire2 |

Các nhóm trên phục vụ điều hướng, không phải thống kê toàn bộ GitHub. Số liệu được đếm từ danh mục này, không biểu thị mức độ hoạt động hoặc khả năng tương thích đã kiểm thử.

**Đi nhanh:** [Nguồn Python](#python-sources) · [Công cụ bổ trợ](#supporting-tools) · [MATLAB](#matlab) · [Tải nguồn](#download) · [Đưa lên GitHub](#publish)

<a id="python-sources"></a>

## 🐍 Nguồn Python

Python là nguồn chính trong danh mục. Nếu mới bắt đầu, đọc SDK trước, chọn Qiskit hoặc PennyLane, rồi tham khảo notebook.

| Repo | Loại nguồn | Dùng để làm gì? | Gợi ý lựa chọn |
| :--- | :--- | :--- | :--- |
| [quantuminspire](https://github.com/QuTech-Delft/quantuminspire) | SDK và CLI | Đăng nhập và tương tác với nền tảng | **Bắt đầu ở đây** |
| [qiskit-quantuminspire](https://github.com/QuTech-Delft/qiskit-quantuminspire) | Bộ tích hợp Qiskit | Làm việc với mạch lượng tử qua Qiskit | Khi dùng Qiskit |
| [pennylane-quantuminspire](https://github.com/QuTech-Delft/pennylane-quantuminspire) | Bộ tích hợp PennyLane | Kết nối backend với quy trình PennyLane | Khi dùng PennyLane |
| [quantum-inspire-examples](https://github.com/QuTech-Delft/quantum-inspire-examples) | Python và Jupyter Notebook | Học thuật toán qua ví dụ | Kiểm tra API cũ, Qiskit và ProjectQ |
| [OpenSquirrel](https://github.com/QuTech-Delft/OpenSquirrel) | Trình biên dịch Python | Xử lý và chuyển đổi chương trình lượng tử | Nghiên cứu biên dịch |
| [qilib](https://github.com/QuTech-Delft/qilib) | Thư viện tiện ích | Tham khảo các lớp tiện ích của Quantum Inspire | Kiểm tra phụ thuộc riêng |

### Bắt đầu với Python

1. Đọc README và yêu cầu phiên bản Python tại repo `quantuminspire`.
2. Cài CLI theo hướng dẫn chính thức bằng `pipx install quantuminspire`, sau đó chạy `qi --help` và `qi login`.
3. Chọn một bộ tích hợp Qiskit hoặc PennyLane và làm theo tài liệu của chính bộ tích hợp đó. Môi trường pipx của CLI tách biệt với môi trường Python chứa notebook và các bộ tích hợp.
4. Tạo môi trường riêng khi chạy ví dụ cũ. Không mặc định trộn mọi repo vào một môi trường.

Tài liệu: [Qiskit](https://qutech-delft.github.io/qiskit-quantuminspire/) và [PennyLane](https://qutech-delft.github.io/pennylane-quantuminspire/).

<a id="supporting-tools"></a>

## 🧩 Công cụ và đặc tả bổ trợ

| Repo | Công nghệ hoặc nội dung | Vai trò |
| :--- | :--- | :--- |
| [OpenQL](https://github.com/QuTech-Delft/OpenQL) | C++ và Python | Framework lập trình và biên dịch lượng tử |
| [libqasm](https://github.com/QuTech-Delft/libqasm) | Thư viện phân tích cQASM | Tham khảo xử lý ngôn ngữ cQASM |
| [QuIS](https://github.com/QuTech-Delft/QuIS) | Đặc tả tập lệnh | Tra cứu tập lệnh dùng trong hệ sinh thái |

### Nguồn lịch sử

| Repo | Trạng thái | Mục đích |
| :--- | :--- | :--- |
| [quantuminspire2](https://github.com/QuTech-Delft/quantuminspire2) | Đã lưu trữ | Tra cứu lịch sử SDK; ưu tiên quantuminspire cho dự án mới |

<a id="matlab"></a>

## 🔬 MATLAB và Python: mức hỗ trợ

| Tiêu chí | Python | MATLAB |
| :--- | :--- | :--- |
| Mã nguồn trong danh mục | Có SDK, bộ tích hợp và notebook | Chưa xác minh được SDK chính thức |
| Điểm bắt đầu | quantuminspire | Hướng dẫn kết nối Python bên dưới |
| Hướng sử dụng | Làm theo tài liệu từng repo | Gọi Python hoặc trao đổi JSON |
| Đã chạy thử trong dự án này | Chưa | Chưa |

Khảo sát với các truy vấn `quantuminspire matlab` và `quantum-inspire matlab` chưa xác định được SDK MATLAB chính thức trên GitHub. Điều này không chứng minh rằng không có dự án cộng đồng.

Hướng tích hợp đề xuất là gọi Python từ MATLAB hoặc trao đổi kết quả qua JSON. Đây là đề xuất kiến trúc, chưa phải bộ tích hợp đã kiểm thử. Xem [hướng dẫn MATLAB](docs/MATLAB.md).

<a id="download"></a>

## 📥 Tải các repo nguồn

Chạy từ thư mục repo bằng PowerShell:

```powershell
./scripts/clone-sources.ps1
```

Script chỉ clone các repo chính vào `sources/`, bỏ qua đường dẫn đã tồn tại, không cài gói và không chạy mã bên trong repo nguồn. Mỗi repo giữ nguyên lịch sử và giấy phép của nó. Thư mục `sources/` không được commit vào repo tổng hợp.

### Cấu trúc thư mục

```text
.
├── README.md                  Danh mục và thống kê nguồn
├── README.en.md               Bản tiếng Anh
├── docs/
│   ├── MATLAB.md              Hướng dẫn MATLAB tiếng Việt
│   └── MATLAB.en.md           Hướng dẫn MATLAB tiếng Anh
├── scripts/
│   └── clone-sources.ps1       Tải 9 repo nguồn
└── sources/                   Xuất hiện sau khi tải, được Git bỏ qua
```

<a id="publish"></a>

## ☁️ Đưa lên GitHub

Sau khi cài GitHub CLI và đăng nhập bằng `gh auth login`, chạy từ thư mục dự án:

```powershell
gh repo create croznnt/quantum-inspire-python-matlab --private --source . --remote origin --push
```

Lệnh này dành cho lần xuất bản đầu tiên: tạo repo riêng tư và đẩy commit hiện có lên GitHub. Khi đã có remote `origin`, dùng `git push` cho các lần cập nhật tiếp theo.

## Nguồn và bản quyền

Khi cập nhật danh mục, số liệu hoặc hướng dẫn, cập nhật cả `README.md` và `README.en.md`. Hướng dẫn MATLAB cũng được duy trì bằng hai ngôn ngữ trong `docs/`.

Danh mục ưu tiên repo của tổ chức QuTech Delft. Liên kết ở từng dòng là nguồn kiểm chứng. Trạng thái và API có thể thay đổi sau ngày khảo sát. Nội dung tổng hợp được viết riêng; mã nguồn bên thứ ba không được sao chép vào đây. Khi tái sử dụng mã, đọc LICENSE và NOTICE tại đúng phiên bản nguồn, giữ nguyên thông báo bản quyền theo yêu cầu của từng repo.
