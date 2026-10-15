# Quantum Inspire: Python và MATLAB

Danh mục các repo nguồn phục vụ học tập, nghiên cứu và phát triển với Quantum Inspire. Chủ tài khoản dự kiến: `croznnt`. Tên repo đề xuất: `quantum-inspire-python-matlab`.

Ngày khảo sát: 15 tháng 10 năm 2026. Đây là repo tổng hợp liên kết và công cụ tải nguồn, không phải bản phân phối chung của các SDK.

## Danh mục nguồn

| Repo | Vai trò | Cách sử dụng trong dự án |
| :--- | :--- | :--- |
| [quantuminspire](https://github.com/QuTech-Delft/quantuminspire) | SDK và CLI Python | Điểm bắt đầu để đăng nhập và làm việc với nền tảng |
| [qiskit-quantuminspire](https://github.com/QuTech-Delft/qiskit-quantuminspire) | Bộ tích hợp Qiskit | Xây dựng và gửi mạch qua Qiskit |
| [pennylane-quantuminspire](https://github.com/QuTech-Delft/pennylane-quantuminspire) | Bộ tích hợp PennyLane | Nghiên cứu thuật toán và học máy lượng tử |
| [quantum-inspire-examples](https://github.com/QuTech-Delft/quantum-inspire-examples) | Notebook và ví dụ Python | Tham khảo thuật toán; kiểm tra phiên bản trước khi chạy vì có ví dụ dùng ProjectQ và API cũ |
| [OpenSquirrel](https://github.com/QuTech-Delft/OpenSquirrel) | Trình biên dịch chương trình lượng tử bằng Python | Tham khảo xử lý và chuyển đổi chương trình |
| [libqasm](https://github.com/QuTech-Delft/libqasm) | Phân tích cQASM | Tham khảo ngôn ngữ và công cụ phân tích |
| [OpenQL](https://github.com/QuTech-Delft/OpenQL) | Framework lập trình lượng tử C++ và Python | Nghiên cứu biên dịch ở mức sâu hơn |
| [QuIS](https://github.com/QuTech-Delft/QuIS) | Định nghĩa tập lệnh lượng tử | Tham khảo tập lệnh dùng trong hệ sinh thái |
| [qilib](https://github.com/QuTech-Delft/qilib) | Thư viện tiện ích Quantum Inspire | Tham khảo bổ sung, kiểm tra phụ thuộc riêng |
| [quantuminspire2](https://github.com/QuTech-Delft/quantuminspire2) | SDK đã lưu trữ | Chỉ tham khảo lịch sử, không chọn làm điểm bắt đầu |

## Bắt đầu với Python

1. Đọc README và yêu cầu phiên bản Python tại repo `quantuminspire`.
2. Cài CLI theo hướng dẫn chính thức bằng `pipx install quantuminspire`, sau đó chạy `qi --help` và `qi login`.
3. Chọn một bộ tích hợp Qiskit hoặc PennyLane và làm theo tài liệu của chính bộ tích hợp đó. Môi trường pipx của CLI tách biệt với môi trường Python chứa notebook và các bộ tích hợp.
4. Tạo môi trường riêng khi chạy ví dụ cũ. Không mặc định trộn mọi repo vào một môi trường.

Tài liệu: [Qiskit](https://qutech-delft.github.io/qiskit-quantuminspire/) và [PennyLane](https://qutech-delft.github.io/pennylane-quantuminspire/).

## MATLAB

Khảo sát với các truy vấn `quantuminspire matlab` và `quantum-inspire matlab` chưa xác định được SDK MATLAB chính thức trên GitHub. Điều này không chứng minh rằng không có dự án cộng đồng.

Hướng tích hợp đề xuất là gọi Python từ MATLAB hoặc trao đổi kết quả qua JSON. Đây là đề xuất kiến trúc, chưa phải bộ tích hợp đã kiểm thử. Xem [hướng dẫn MATLAB](docs/MATLAB.md).

## Tải các repo nguồn

Chạy từ thư mục repo bằng PowerShell:

```powershell
./scripts/clone-sources.ps1
```

Script chỉ clone các repo chính vào `sources/`, bỏ qua đường dẫn đã tồn tại, không cài gói và không chạy mã bên trong repo nguồn. Mỗi repo giữ nguyên lịch sử và giấy phép của nó. Thư mục `sources/` không được commit vào repo tổng hợp.

## Đưa lên GitHub

Sau khi cài GitHub CLI và đăng nhập bằng `gh auth login`, chạy từ thư mục dự án:

```powershell
gh repo create croznnt/quantum-inspire-python-matlab --private --source . --remote origin --push
```

Lệnh này tạo repo riêng tư và đẩy commit hiện có lên GitHub. Chưa có repo từ xa nào được tạo trong lần chuẩn bị này.

## Nguồn và bản quyền

Danh mục ưu tiên repo của tổ chức QuTech Delft. Liên kết ở từng dòng là nguồn kiểm chứng. Trạng thái và API có thể thay đổi sau ngày khảo sát. Nội dung tổng hợp được viết riêng; mã nguồn bên thứ ba không được sao chép vào đây. Khi tái sử dụng mã, đọc LICENSE và NOTICE tại đúng phiên bản nguồn, giữ nguyên thông báo bản quyền theo yêu cầu của từng repo.
