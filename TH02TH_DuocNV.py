# #1
# def check_letter_type(letter):
#     """
#     Kiểm tra một ký tự có phải là nguyên âm hay phụ âm
#     Input: một ký tự (không phân biệt hoa thường)
#     Output: Thông báo về loại ký tự (nguyên âm/phụ âm)
#     """
#     # Chuyển ký tự về chữ thường để dễ xử lý
#     letter = letter.lower()
    
#     # Danh sách các nguyên âm
#     vowels = ['a', 'e', 'i', 'o', 'u']
    
#     # Danh sách các phụ âm
#     consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 
#                  'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    
#     # Kiểm tra ký tự
#     if letter in vowels:
#         return f"Nhập vào một chữ cái: {letter}\nĐây là nguyên âm!"
#     elif letter in consonants:
#         return f"Nhập vào một chữ cái: {letter}\nĐây là phụ âm!"
#     else:
#         return "Vui lòng nhập một chữ cái trong bảng chữ cái tiếng Anh!"

# # Hàm chính để chạy chương trình
# def main():
#     while True:
#         # Nhập ký tự từ người dùng
#         user_input = input("Nhập một chữ cái (hoặc '1' để thoát): ")
        
#         # Kiểm tra nếu người dùng muốn thoát
#         if user_input.lower() == '1':
#             print("Tạm biệt!")
#             break
            
#         # Kiểm tra nếu người dùng nhập nhiều hơn 1 ký tự
#         if len(user_input) != 1:
#             print("Vui lòng chỉ nhập một ký tự!")
#             continue
            
#         # In kết quả
#         print(check_letter_type(user_input))

# if __name__ == "__main__":
#     main()
    
#2
def calculate_bmi(weight, height):
    """
    Tính chỉ số BMI
    weight: cân nặng (kg)
    height: chiều cao (m)
    """
    return weight / (height ** 2)

def evaluate_bmi(bmi):
    """
    Đánh giá cơ thể dựa trên chỉ số BMI
    """
    if bmi < 18.5:
        return "Thiếu cân (Underweight)"
    elif 18.5 <= bmi <= 24.9:
        return "Cân đối (Normal Weight)"
    elif 25 <= bmi <= 29.9:
        return "Thừa cân (Overweight)"
    else:
        return "Béo phì (Obese)"

def main():
    print("CHƯƠNG TRÌNH TÍNH CHỈ SỐ BMI")
    print("-" * 30)
    
    while True:
        try:
            # Nhập chiều cao và cân nặng
            height = float(input("Nhập chiều cao (m): "))
            weight = float(input("Nhập cân nặng (kg): "))
            
            # Kiểm tra giá trị hợp lệ
            if height <= 0 or weight <= 0:
                print("Chiều cao và cân nặng phải là số dương!")
                continue
                
            # Tính BMI
            bmi = calculate_bmi(weight, height)
            
            # In kết quả
            print("\nKẾT QUẢ:")
            print(f"Chỉ số BMI của bạn là: {bmi:.1f}")
            print(f"Đánh giá: {evaluate_bmi(bmi)}")
            
            # Hỏi người dùng có muốn tiếp tục
            choice = input("\nBạn có muốn tính tiếp không? (y/n): ")
            if choice.lower() != 'y':
                break
                
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")
        
    print("\nCảm ơn bạn đã sử dụng chương trình!")

if __name__ == "__main__":
    main()