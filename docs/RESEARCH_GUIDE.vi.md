# Hướng dẫn nghiên cứu mô phỏng và điều khiển

[English](RESEARCH_GUIDE.md) · [Trang chính](../README.vi.md) · [Bài báo](../papers/README.vi.md)

## Mô hình trước, thuật toán sau

Xác định Hamiltonian dạng $H(t)=H_0+\sum_k u_k(t)H_k$, trạng thái đầu, trạng thái đích và đơn vị. Hệ kín có thể mô phỏng bằng phương trình Schrödinger; hệ mở Markov thường dùng phương trình Lindblad. Các toán tử suy hao phải bao gồm căn bậc hai của tốc độ. Không trộn Hz với rad/s.

| Mục tiêu | Công cụ bắt đầu | Điểm cần kiểm tra |
| :--- | :--- | :--- |
| Động lực học trạng thái và ma trận mật độ | QuTiP, notebook hướng dẫn | Sai số bộ giải và chuẩn hóa |
| GRAPE hoặc CRAB | qutip-qtrl | Giới hạn biên độ và lưới thời gian |
| Xung giải tích, GOAT hoặc JOPT | qutip-qoc | Tham số xung và phụ thuộc tùy chọn |
| Cập nhật trường tuần tự | krotov | Phiên bản QuTiP tương thích và điều kiện hội tụ |
| Hàm mục tiêu tùy biến | QuOCS | Ngân sách số lần đánh giá |
| Đạo hàm tự động và quét tham số | dynamiqs | Bộ nhớ, độ chính xác và thiết bị tính toán |
| MATLAB với hệ spin | Spinach | Phiên bản MATLAB và toolbox |
| Gửi mạch lên Quantum Inspire | SDK và provider Quantum Inspire | Không mặc định có quyền điều khiển dạng sóng tùy ý |

## Thang bài toán đề xuất

| Mã | Bài toán | Kết quả cần lưu |
| :--- | :--- | :--- |
| B01 | Chuyển trạng thái một qubit bằng GRAPE | Xung, population và đường hội tụ |
| B02 | Cổng X, so sánh GRAPE với GOAT hoặc CRAB | Fidelity, thời lượng và độ trơn |
| B03 | Bền vững trước sai lệch tần số và biên độ | Trung bình, giá trị thấp nhất và phân bố trên tập kiểm tra độc lập |
| B04 | Chuyển trạng thái có suy hao Lindblad | Trace, tính dương, population và purity |
| B05 | Cổng tạo rối hai qubit | Chỉ số cổng, độ rối và chi phí tính toán |
| B06 | Hệ ba mức có rò rỉ | Rò rỉ cuối và trong quá trình, hội tụ theo số mức |
| B07 | Ổn định hệ hai mức có phép đo liên tục | Phân bố quỹ đạo, khoảng tin cậy, hiệu suất đo và độ trễ |

Bắt đầu từ B01 và B02. B03 và B04 kiểm tra độ bền vững và suy hao. B05 và B06 tăng độ phức tạp mô hình. B07 là nhánh phản hồi riêng, cần phương trình ngẫu nhiên có điều kiện và bản ghi phép đo.

## Quy trình kiểm chứng

1. Chọn rõ bài toán chuyển trạng thái, cổng, đại lượng quan sát hoặc ổn định.
2. Ghi quy ước fidelity. Độ chồng lấp cổng không tự động bằng fidelity cổng trung bình; phép chiếu lên không gian tính toán khi có rò rỉ có thể không còn unitary.
3. Tách infidelity vật lý khỏi phạt năng lượng, độ trơn, tốc độ thay đổi xung và rò rỉ. Hàm chi phí tổng giảm không có nghĩa mọi đại lượng đều tốt hơn.
4. Kiểm tra mô hình chưa tối ưu bằng nghiệm giải tích nếu có. Kiểm tra chuẩn trạng thái, trace và tính vật lý của ma trận mật độ.
5. Đánh giá lại xung tối ưu bằng lưới mịn hơn hoặc sai số bộ giải nhỏ hơn, tăng số mức nếu có dao động tử hoặc rò rỉ.
6. Kiểm tra gradient bằng sai phân hữu hạn cho bài toán nhỏ nếu tự triển khai đạo hàm.
7. So sánh trên cùng mô hình, thời lượng, giới hạn và ngân sách. Ghi số lần đánh giá, thời gian, phần cứng và độ chính xác. Không chỉ so số vòng lặp.
8. Chạy nhiều seed, dùng tập tham số độc lập để kiểm tra độ bền vững, lưu commit, phiên bản gói, xung, đơn vị, dữ liệu thô và mã vẽ.

Chưa cài gói, chạy benchmark hoặc tái lập kết quả bài báo trong lần mở rộng này. Các bài toán trên là đề xuất; dùng ví dụ của từng dự án để bắt đầu. Xem [bản tiếng Anh](RESEARCH_GUIDE.md) để có phương trình đầy đủ và giải thích chi tiết. Tài liệu tham chiếu: [tổng quan thực hành](https://arxiv.org/abs/2205.15574) và [hướng dẫn qutip-qtrl](https://qutip.readthedocs.io/projects/qutip-qtrl/en/stable/guide/guide-control.html).
