# Hệ sinh thái Quantum Inspire

[English](QUANTUM_INSPIRE.en.md) · [Trang nghiên cứu](../README.vi.md)

Danh mục này giữ 10 nguồn nền tảng ban đầu, tách khỏi nhóm phần mềm mô phỏng và tối ưu điều khiển. Khảo sát ngày 15 tháng 10 năm 2026.

| Repo | Vai trò |
| :--- | :--- |
| [quantuminspire](https://github.com/QuTech-Delft/quantuminspire) | SDK và CLI Python cho nền tảng |
| [qiskit-quantuminspire](https://github.com/QuTech-Delft/qiskit-quantuminspire) | Bộ tích hợp Qiskit |
| [pennylane-quantuminspire](https://github.com/QuTech-Delft/pennylane-quantuminspire) | Bộ tích hợp PennyLane |
| [quantum-inspire-examples](https://github.com/QuTech-Delft/quantum-inspire-examples) | Ví dụ Python và notebook, cần kiểm tra API cũ |
| [OpenSquirrel](https://github.com/QuTech-Delft/OpenSquirrel) | Trình biên dịch Python |
| [libqasm](https://github.com/QuTech-Delft/libqasm) | Phân tích cQASM |
| [OpenQL](https://github.com/QuTech-Delft/OpenQL) | Framework lập trình C++ và Python |
| [QuIS](https://github.com/QuTech-Delft/QuIS) | Đặc tả tập lệnh |
| [qilib](https://github.com/QuTech-Delft/qilib) | Thư viện tiện ích, cần kiểm tra phụ thuộc |
| [quantuminspire2](https://github.com/QuTech-Delft/quantuminspire2) | SDK đã lưu trữ, chỉ tham khảo lịch sử |

Đọc README của SDK, kiểm tra phiên bản Python rồi làm theo hướng dẫn CLI: `pipx install quantuminspire`, `qi --help` và `qi login`. Môi trường CLI tách biệt với môi trường notebook. Dùng tài liệu riêng của [Qiskit](https://qutech-delft.github.io/qiskit-quantuminspire/) hoặc [PennyLane](https://qutech-delft.github.io/pennylane-quantuminspire/) khi tích hợp.

Chạy `./scripts/clone-sources.ps1 -Group platform` từ gốc repo để tải 9 nguồn, bỏ qua quantuminspire2. Script không cài gói hoặc chạy mã tải về.

Provider mạch không phải bộ giải Hamiltonian để tối ưu xung. Kiểm tra giao diện backend trước khi giả định có thể tải dạng sóng tùy ý, truy cập phép đo thời gian thực hoặc thực hiện phản hồi. Xem [hướng dẫn nghiên cứu](RESEARCH_GUIDE.vi.md) và [MATLAB](MATLAB.md) cho nhánh mô phỏng. Không mặc định mọi gói tương thích cùng phiên bản. Giữ LICENSE và NOTICE khi tái sử dụng mã.
