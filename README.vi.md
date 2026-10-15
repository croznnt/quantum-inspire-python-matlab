# ⚛️ Mô phỏng và tối ưu điều khiển lượng tử

<p align="center">
  <a href="https://github.com/qutip/qutip"><img src="https://avatars.githubusercontent.com/u/2517630?v=4" width="64" height="64" alt="QuTiP organization avatar"></a>&nbsp;&nbsp;
  <a href="https://github.com/Quantum-OCS/QuOCS"><img src="https://avatars.githubusercontent.com/u/80833925?v=4" width="64" height="64" alt="QuOCS organization avatar"></a>&nbsp;&nbsp;
  <a href="https://github.com/dynamiqs/dynamiqs"><img src="https://avatars.githubusercontent.com/u/135633837?v=4" width="64" height="64" alt="dynamiqs organization avatar"></a>&nbsp;&nbsp;
  <a href="https://github.com/QuTech-Delft/quantuminspire"><img src="https://avatars.githubusercontent.com/u/42680367?v=4" width="64" height="64" alt="QuTech organization avatar"></a>
</p>
<p align="center"><a href="https://github.com/qutip/qutip">QuTiP</a> · <a href="https://github.com/Quantum-OCS/QuOCS">QuOCS</a> · <a href="https://github.com/dynamiqs/dynamiqs">dynamiqs</a> · <a href="https://github.com/QuTech-Delft/quantuminspire">QuTech</a></p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&amp;logo=python&amp;logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/MATLAB-e16737?style=flat-square" alt="MATLAB">
  <img src="https://img.shields.io/badge/Repositories-19-2563eb?style=flat-square" alt="19 repositories">
  <img src="https://img.shields.io/badge/Papers-14-7c3aed?style=flat-square" alt="14 papers">
</p>

**Ngôn ngữ:** [English](README.md) · **Tiếng Việt**

Repo nghiên cứu về mô phỏng động lực học lượng tử, thiết kế xung, điều khiển bền vững và tối ưu điều khiển, ưu tiên Python và MATLAB. Tiếng Anh là trang mặc định trên GitHub.

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

**Chú giải:** ⚛️ mô phỏng · 🎛️ điều khiển · 📓 hướng dẫn · 🧪 mã tái lập · ☁️ nền tảng · ⚙️ biên dịch · 📐 đặc tả · 🗄️ lịch sử

## 🧭 Chọn theo nhu cầu

| Nhu cầu | Trang chi tiết | Bài báo liên quan |
| :--- | :--- | :--- |
| Mô phỏng động lực học | [QuTiP](repositories/qutip.md) | [P03](papers/profiles/P03.md) |
| Tối ưu xung theo lưới thời gian | [qutip-qtrl](repositories/qtrl.md) | [GRAPE, P04](papers/profiles/P04.md) |
| Cập nhật trường tuần tự | [Krotov](repositories/krotov.md) | [P05](papers/profiles/P05.md) |
| Xung tham số hóa trơn | [qutip-qoc](repositories/qoc.md) | [GOAT, P08](papers/profiles/P08.md) |
| Hàm mục tiêu tùy biến hoặc dCRAB | [QuOCS](repositories/quocs.md) | [P10](papers/profiles/P10.md) |
| MATLAB cho hệ spin | [Spinach](repositories/spinach.md) | [P11](papers/profiles/P11.md) |
| Phản hồi theo phép đo | [P14](papers/profiles/P14.md) | [Hướng dẫn nghiên cứu](docs/RESEARCH_GUIDE.vi.md) |

Xem đủ [19 trang repo](repositories/README.md) và [14 trang paper](papers/PROFILES.md). Các trang chi tiết hiện viết bằng tiếng Anh, gồm mục đích, hướng thực hành, điều cần kiểm tra, giới hạn và quan hệ giữa mã với bài báo. Bài thực hành là đề xuất biên tập, chưa được chạy hoặc xác nhận tái lập.

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

## 📋 Kiểm chứng và đóng góp

1. Bổ sung nguồn kèm mục đích sử dụng cụ thể và liên kết chính chủ.
2. Phân biệt mã của bài báo, bản triển khai phương pháp về sau và mã tái lập kết quả.
3. Đồng bộ số liệu, catalog, nhóm tải và hai trang ngôn ngữ.
4. Khi công bố kết quả, lưu phiên bản, commit, seed, đơn vị, mô hình, sai số bộ giải, xung, quy ước fidelity, log và dữ liệu thô.
5. Tôn trọng LICENSE và NOTICE, dẫn liên kết paper thay vì phân phối PDF khi chưa rõ quyền.

Cấu trúc tài liệu đầy đủ nằm ở [trang tiếng Anh](README.md). Nội dung repo là chú giải và liên kết; mã nguồn bên ngoài được giữ tại dự án gốc.
