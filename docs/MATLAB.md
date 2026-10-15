# Làm việc từ MATLAB

Chưa xác minh được SDK MATLAB chính thức cho Quantum Inspire trong phạm vi khảo sát. Tích hợp dưới đây là hướng triển khai đề xuất.

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
