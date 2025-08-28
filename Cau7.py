import sys

# Kiểm tra xem có tham số dòng lệnh nào không
if len(sys.argv) > 1:
    # In chuỗi ký tự được nhập từ tham số dòng lệnh
    input_string = sys.argv[1]
    print("Chuỗi ký tự bạn nhập là:", input_string)
else:
    print("Vui lòng nhập chuỗi ký tự sau khi chạy chương trình.")