# Mô phỏng và tối ưu điều khiển lượng tử

**Ngôn ngữ:** [English](README.md) · **Tiếng Việt**

Repo nghiên cứu về mô phỏng động lực học lượng tử, thiết kế xung, điều khiển bền vững và tối ưu điều khiển, ưu tiên Python và MATLAB. Tiếng Anh là trang mặc định trên GitHub.

**Ngày khảo sát:** 15 tháng 10 năm 2026.

## 📊 Thống kê

| Tài nguyên | Số lượng | Nội dung |
| :--- | :--- | :--- |
| Phần mềm mô phỏng và điều khiển | **7** | QuTiP, qtrl, qoc, Krotov, QuOCS, dynamiqs, Spinach |
| Repo hướng dẫn và mã gắn với bài báo | **2** | Notebook QuTiP và mã đạo hàm bán tự động |
| Repo hệ sinh thái Quantum Inspire | **10** | SDK, provider, ví dụ, trình biên dịch và nguồn lịch sử |
| Tổng repo | **19** | Các mục duy nhất trong catalog |
| Bài báo có chú giải | **14** | Tổng quan, phương pháp, phần mềm và phản hồi |
| Bài toán mô phỏng đề xuất | **7** | Từ một qubit đến phản hồi theo phép đo |

Chưa chạy benchmark, kiểm thử tương thích gói hoặc tái lập kết quả bài báo. Số liệu chỉ mô tả danh mục này.

**Đi nhanh:** [Bài báo](papers/README.vi.md) · [Hướng dẫn nghiên cứu](docs/RESEARCH_GUIDE.vi.md) · [MATLAB](docs/MATLAB.md) · [Quantum Inspire](docs/QUANTUM_INSPIRE.vi.md) · [Catalog](catalog/repositories.csv)

## 🧰 Chọn công cụ

| Công cụ | Ngôn ngữ | Vai trò | Bài tham chiếu |
| :--- | :--- | :--- | :--- |
| [QuTiP](https://github.com/qutip/qutip) | Python | Mô phỏng hệ kín, hệ mở và Hamiltonian phụ thuộc thời gian | P03 |
| [qutip-qtrl](https://github.com/qutip/qutip-qtrl) | Python | Tối ưu xung bằng GRAPE và CRAB | P04, P06 |
| [qutip-qoc](https://github.com/qutip/qutip-qoc) | Python | GOAT, JOPT và giao diện với qtrl | P08 |
| [krotov](https://github.com/qucontrol/krotov) | Python | Cập nhật trường tuần tự theo Krotov | P05 |
| [QuOCS](https://github.com/Quantum-OCS/QuOCS) | Python | GRAPE, dCRAB và tìm kiếm trực tiếp | P07, P10 |
| [dynamiqs](https://github.com/dynamiqs/dynamiqs) | Python, JAX | Mô phỏng khả vi và xử lý theo lô | Theo trích dẫn của dự án |
| [Spinach](https://github.com/IlyaKuprov/Spinach) | MATLAB | Động lực học spin và tối ưu điều khiển | P04, P11 |

Đây là bảng khả năng, không phải xếp hạng hiệu suất. qutip-qoc phát triển dựa trên qutip-qtrl. Kiểm tra phụ thuộc và phiên bản tại từng dự án, dùng môi trường riêng khi chưa xác minh tương thích.

Nguồn thực hành: [notebook QuTiP](https://github.com/qutip/qutip-tutorials) và [mã Julia và Python gắn với P13](https://github.com/ARLQCI/2022-04_semiad_paper).

## 📚 Lộ trình đọc và thực hành

| Nhánh | Bài cần đọc | Mục đích |
| :--- | :--- | :--- |
| Tổng quan | P01, P02 | Chọn hệ, nhiệm vụ và ràng buộc |
| Mô phỏng | P03, P11 | Hiểu bộ giải và mô hình spin |
| Gradient | P04, P05, P09 | So sánh GRAPE và Krotov |
| Xung ít tham số | P06, P07, P08, P10 | Chọn CRAB, dCRAB hoặc GOAT |
| Đạo hàm tự động | P12, P13 | Đánh giá khả năng tùy biến và chi phí |
| Phản hồi đo lường | P14 | Thiết kế mô phỏng có điều kiện |

Tên bài, tác giả và nguồn nằm trong [bảng bài báo](papers/README.md). Bắt đầu từ P02, P03, P04 và hai bài toán B01, B02 trong [hướng dẫn nghiên cứu](docs/RESEARCH_GUIDE.vi.md). Sau đó mở rộng sang bất định, suy hao, hai qubit, rò rỉ và phản hồi.

Tối ưu vòng kín giữa các lần thực nghiệm khác với phản hồi theo phép đo trong quá trình tiến hóa. Hệ lượng tử mở mô tả tương tác với môi trường, không đồng nghĩa với điều khiển vòng kín.

## 🔬 MATLAB và Quantum Inspire

MATLAB có Spinach cho mô phỏng và điều khiển spin. Kiểm tra phiên bản MATLAB và toolbox tại dự án gốc. Chưa xác minh được SDK MATLAB chính thức riêng cho Quantum Inspire không có nghĩa là thiếu công cụ MATLAB cho điều khiển lượng tử.

SDK nền tảng để gửi mạch không mặc định cho phép điều khiển dạng sóng tùy ý hoặc phản hồi đo lường liên tục. Xem [hướng dẫn MATLAB](docs/MATLAB.md) và [danh mục nền tảng](docs/QUANTUM_INSPIRE.vi.md).

## 📥 Tải mã nguồn

```powershell
./scripts/clone-sources.ps1
./scripts/clone-sources.ps1 -Group research
./scripts/clone-sources.ps1 -Group platform
./scripts/clone-sources.ps1 -Group all
./scripts/clone-sources.ps1 -Group all -ListOnly
```

Mặc định tải 7 repo khởi đầu. Nhóm research có 9 repo, platform có 9 repo, all có 18 repo. Repo lịch sử quantuminspire2 không được tải tự động. Script đọc catalog, tải vào `sources/<owner>/<repo>` và bỏ qua đường dẫn đã có. Script không cài gói, chạy mã tải về, cập nhật hoặc xóa bản clone hiện có. Thư mục nguồn được Git bỏ qua.

## Kiểm chứng và đóng góp

1. Bổ sung nguồn kèm mục đích sử dụng cụ thể và liên kết chính chủ.
2. Phân biệt mã của bài báo, bản triển khai phương pháp về sau và mã tái lập kết quả.
3. Đồng bộ số liệu, catalog, nhóm tải và hai trang ngôn ngữ.
4. Khi công bố kết quả, lưu phiên bản, commit, seed, đơn vị, mô hình, sai số bộ giải, xung, quy ước fidelity, log và dữ liệu thô.
5. Tôn trọng LICENSE và NOTICE, dẫn liên kết paper thay vì phân phối PDF khi chưa rõ quyền.

Cấu trúc tài liệu đầy đủ nằm ở [trang tiếng Anh](README.md). Nội dung repo là chú giải và liên kết; mã nguồn bên ngoài được giữ tại dự án gốc.
