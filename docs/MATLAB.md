# Làm việc từ MATLAB

**Ngôn ngữ / Language:** **Tiếng Việt** · [English](MATLAB.en.md) · [Trang chính](../README.vi.md)

## Mô phỏng và điều khiển trực tiếp bằng MATLAB

[Spinach](https://github.com/IlyaKuprov/Spinach) là thư viện MATLAB cho động lực học spin, có [module tối ưu điều khiển](https://spindynamics.org/wiki/index.php?title=Optimal_control_module), gồm các quy trình GRAPE và phạt xung. Bắt đầu từ ví dụ và tutorial của dự án. Kiểm tra phiên bản MATLAB và toolbox yêu cầu trong README nguồn.

Đọc P11, P04 và [hướng dẫn nghiên cứu](RESEARCH_GUIDE.vi.md) trước khi dựng bài toán nhỏ. P09 giới thiệu framework MATLAB DYNAMO trong lịch sử; chưa xác minh được bản nguồn GitHub hiện tại trong lần khảo sát này.

Chưa xác minh được SDK MATLAB chính thức cho Quantum Inspire chỉ nói về tích hợp nền tảng, không nói rằng MATLAB thiếu công cụ mô phỏng và điều khiển. Phần kết nối Python dưới đây là hướng triển khai đề xuất, chưa kiểm thử.

## Gọi Python

1. Cài Python tương thích với phiên bản MATLAB của bạn và các gói Quantum Inspire cần dùng.
2. Trong MATLAB, kiểm tra `pyenv` và cấu hình đúng trình thông dịch trước khi gọi Python.
3. Đăng nhập bằng CLI theo hướng dẫn của SDK. Không ghi token vào tệp `.m`, notebook hoặc Git.
4. Viết lớp Python nhỏ thực hiện tác vụ và trả về kiểu dữ liệu đơn giản. Gọi lớp này từ MATLAB bằng giao diện `py`.
5. Kiểm tra luồng bằng dữ liệu mô phỏng trước khi gửi tác vụ thật lên nền tảng.

Ví dụ kiểm tra môi trường, chưa gửi mạch lượng tử:

```matlab
pe = pyenv;
disp(pe);
qi = py.importlib.import_module('quantuminspire');
disp(qi);
```

Nếu import thất bại, kiểm tra gói đã được cài trong đúng môi trường mà `pyenv` đang dùng. Môi trường pipx của CLI không tự động trở thành môi trường Python của MATLAB.

## Trao đổi JSON

Có thể để Python phụ trách gửi job và lấy kết quả, lưu JSON rồi đọc trong MATLAB bằng `jsondecode(fileread('results.json'))`. Cần định nghĩa rõ schema, thứ tự bit, số shot và cách biểu diễn xác suất trước khi phân tích kết quả.

## Giới hạn xác minh

Chưa chạy MATLAB, chưa đăng nhập Quantum Inspire và chưa gửi job thật. Không có cam kết về tương thích phiên bản. Tham khảo README của các repo được dẫn trong danh mục chính và tài liệu Python interface của đúng bản MATLAB đang sử dụng.
