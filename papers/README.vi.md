# 📚 Bài báo về mô phỏng và tối ưu điều khiển lượng tử

[English](README.md) · [Trang chính tiếng Việt](../README.vi.md)

Xem [14 trang paper chi tiết](PROFILES.md) và [19 trang repo chi tiết](../repositories/README.md). Trang chi tiết dùng tiếng Anh, bổ sung câu hỏi đọc, nội dung cần rút ra, liên hệ với mã nguồn, bài thực hành đề xuất và giới hạn diễn giải.

Khảo sát ngày 15 tháng 10 năm 2026. Danh mục gồm 14 bài, là tuyển chọn khởi đầu cho nghiên cứu, chưa phải tổng quan hệ thống. Tên bài và liên kết nguồn đầy đủ nằm trong [bảng tài liệu](README.md#reading-map). Năm của bản arXiv là năm tiền ấn phẩm, có thể khác năm xuất bản tạp chí.

| Mã | Chủ đề | Cần đọc để làm gì? |
| :--- | :--- | :--- |
| P01 | Tổng quan chiến lược của Koch và cộng sự | Định vị bài toán điều khiển, hệ mở và hướng nghiên cứu |
| P02 | Tổng quan thực hành của Mahesh và cộng sự | Chọn mục tiêu, ràng buộc và họ thuật toán |
| P03 | QuTiP 5 | Hiểu công cụ mô phỏng và các bộ giải |
| P04 | GRAPE của Khaneja và cộng sự | Tối ưu biên độ xung trên lưới thời gian |
| P05 | Gói Krotov | Hiểu cập nhật tuần tự và giả thiết hội tụ |
| P06 | CRAB | Tối ưu trên cơ sở hàm rút gọn |
| P07 | dCRAB | Thay đổi cơ sở hàm và xử lý giới hạn băng thông |
| P08 | GOAT | Tối ưu xung tham số hóa giải tích |
| P09 | DYNAMO | So sánh thuật toán, tham khảo framework MATLAB lịch sử |
| P10 | QuOCS | Kết nối tối ưu dựa trên mô hình với quy trình thực nghiệm |
| P11 | Spinach | Mô phỏng động lực học spin và không gian Liouville |
| P12 | Đạo hàm tự động trên GPU | Tối ưu với phạt rò rỉ và chi phí tính toán |
| P13 | Đạo hàm bán tự động | Tham khảo mã Julia và Python gắn với bài báo |
| P14 | Phản hồi Bayesian và Markov | Phân biệt phản hồi theo ước lượng trạng thái với phản hồi trực tiếp |

## Lộ trình đọc

1. Đọc P02 và P01, xác định hệ vật lý và mục tiêu điều khiển.
2. Dùng P03 cùng notebook QuTiP để kiểm tra mô phỏng chưa tối ưu.
3. Đọc P04 và chạy ví dụ GRAPE có giới hạn biên độ.
4. Đọc P05 và P09 để so sánh các quy tắc cập nhật trên cùng bài toán.
5. Đọc P06, P07, P08 và P10 khi cần xung trơn hoặc tối ưu ít tham số.
6. Đọc P12 và P13 khi cần hàm mục tiêu tùy biến hoặc tăng hiệu quả tính toán.
7. Đọc P11 cho MATLAB, hoặc P14 cho nhánh điều khiển phản hồi.

Tối ưu vòng kín giữa các lần thực nghiệm khác với phản hồi theo phép đo ngay trong quá trình tiến hóa. Hệ lượng tử mở mô tả tương tác với môi trường, không đồng nghĩa với điều khiển vòng kín.

## Mức kiểm chứng

Chưa tái lập kết quả của các bài báo. Liên kết mã được phân biệt rõ giữa gói của tác giả, bản triển khai phương pháp về sau và mã tái lập gắn với bài. Không mặc định rằng một thư viện thực hiện thuật toán là đã tái lập mọi kết quả trong bài gốc.

Khi tái lập, lưu phiên bản bài, hình hoặc bảng cần tái lập, commit mã, môi trường, đơn vị, trạng thái đầu và đích, kích thước không gian Hilbert, xung, mô hình nhiễu, sai số bộ giải, quy ước fidelity, seed, số lần khởi tạo, ngân sách tính toán và dữ liệu thô. Xuất BibTeX từ trang nguồn khi trích dẫn. Không sao chép PDF nếu chưa rõ quyền phân phối.
