#1
def check_letter_type(letter):
    """
    Kiểm tra một ký tự có phải là nguyên âm hay phụ âm
    Input: một ký tự (không phân biệt hoa thường)
    Output: Thông báo về loại ký tự (nguyên âm/phụ âm)
    """
    # Chuyển ký tự về chữ thường để dễ xử lý
    letter = letter.lower()
    
    # Danh sách các nguyên âm
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Danh sách các phụ âm
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 
                 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    
    # Kiểm tra ký tự
    if letter in vowels:
        return f"Nhập vào một chữ cái: {letter}\nĐây là nguyên âm!"
    elif letter in consonants:
        return f"Nhập vào một chữ cái: {letter}\nĐây là phụ âm!"
    else:
        return "Vui lòng nhập một chữ cái trong bảng chữ cái tiếng Anh!"

# Hàm chính để chạy chương trình
def main():
    while True:
        # Nhập ký tự từ người dùng
        user_input = input("Nhập một chữ cái (hoặc '1' để thoát): ")
        
        # Kiểm tra nếu người dùng muốn thoát
        if user_input.lower() == '1':
            print("Tạm biệt!")
            break
            
        # Kiểm tra nếu người dùng nhập nhiều hơn 1 ký tự
        if len(user_input) != 1:
            print("Vui lòng chỉ nhập một ký tự!")
            continue
            
        # In kết quả
        print(check_letter_type(user_input))

if __name__ == "__main__":
    main()
    
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
    
#3
def determine_season(month):
    """
    Xác định mùa dựa vào tháng sinh
    Input: tháng (1-12)
    Output: tên mùa hoặc thông báo lỗi
    """
    if month in [1, 2, 3]:
        return "Mùa xuân"
    elif month in [4, 5, 6]:
        return "Mùa hạ"
    elif month in [7, 8, 9]:
        return "Mùa thu"
    elif month in [10, 11, 12]:
        return "Mùa đông"
    else:
        return "Tháng sinh không hợp lệ"

def main():
    print("CHƯƠNG TRÌNH XÁC ĐỊNH MÙA SINH")
    print("-" * 30)
    
    while True:
        try:
            # Nhập tháng sinh
            month = int(input("Nhập tháng sinh của bạn (1-12): "))
            
            # Xác định và in kết quả
            result = determine_season(month)
            print(f"\nKết quả: Bạn sinh vào {result}")
            
            # Hỏi người dùng có muốn tiếp tục
            choice = input("\nBạn có muốn thử lại không? (y/n): ")
            if choice.lower() != 'y':
                break
                
        except ValueError:
            print("Vui lòng nhập một số nguyên!")
    
    print("\nCảm ơn bạn đã sử dụng chương trình!")

if __name__ == "__main__":
    main()
    
#4
def print_multiplication_table(n):
    """
    In bảng cửu chương cho số n
    Input: số nguyên n từ 1-10
    """
    print(f"\nBảng cửu chương {n}:")
    print("-" * 20)
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def is_valid_number(n):
    """
    Kiểm tra số nhập vào có hợp lệ không
    Input: số nguyên n
    Output: True nếu n trong khoảng [1,10], False nếu không
    """
    return 1 <= n <= 10

def main():
    print("CHƯƠNG TRÌNH IN BẢNG CỬU CHƯƠNG")
    print("=" * 30)
    
    while True:
        try:
            # Nhập số từ người dùng
            number = int(input("\nNhập số từ 1 đến 10 (0 để thoát): "))
            
            # Kiểm tra nếu người dùng muốn thoát
            if number == 0:
                break
                
            # Kiểm tra tính hợp lệ của số nhập vào
            if is_valid_number(number):
                print_multiplication_table(number)
            else:
                print("Vui lòng chỉ nhập số từ 1 đến 10!")
                
        except ValueError:
            print("Vui lòng nhập một số nguyên!")
    
    print("\nCảm ơn bạn đã sử dụng chương trình!")

if __name__ == "__main__":
    main()

#5
def get_letter_grade(score):
    """
    Chuyển đổi điểm số hệ 10 sang điểm chữ
    """
    if 9.0 <= score <= 10:
        return 'A+'
    elif 8.5 <= score < 9.0:
        return 'A'
    elif 8.0 <= score < 8.5:
        return 'B+'
    elif 7.0 <= score < 8.0:
        return 'B'
    elif 6.5 <= score < 7.0:
        return 'C+'
    elif 5.5 <= score < 6.5:
        return 'C'
    elif 5.0 <= score < 5.5:
        return 'D+'
    elif 4.0 <= score < 5.0:
        return 'D'
    else:
        return 'F'

def get_grade_4(score):
    """
    Chuyển đổi điểm số hệ 10 sang hệ 4
    """
    if 9.0 <= score <= 10:
        return 4.0
    elif 8.5 <= score < 9.0:
        return 3.7
    elif 8.0 <= score < 8.5:
        return 3.5
    elif 7.0 <= score < 8.0:
        return 3.0
    elif 6.5 <= score < 7.0:
        return 2.5
    elif 5.5 <= score < 6.5:
        return 2.0
    elif 5.0 <= score < 5.5:
        return 1.5
    elif 4.0 <= score < 5.0:
        return 1.0
    else:
        return 0.0

def main():
    # Điểm hệ 10
    scores_10 = [8.4, 6.5, 7.3, 2.6, 9.0, 5.8, 6.0, 9.7, 8.1]
    
    # Chuyển đổi sang điểm chữ
    letter_grades = [get_letter_grade(score) for score in scores_10]
    
    # Chuyển đổi sang điểm hệ 4 để tính trung bình
    scores_4 = [get_grade_4(score) for score in scores_10]
    
    # Tính điểm trung bình
    average_10 = sum(scores_10) / len(scores_10)
    average_4 = sum(scores_4) / len(scores_4)
    
    # In kết quả
    print("Điểm hệ 10:", scores_10)
    print("Điểm chữ tương ứng:", letter_grades)
    print("-" * 10 + "Điểm Trung Bình" + "-" * 10)
    print(f"Tổng số môn học: {len(scores_10)}")
    print(f"ĐTB hệ 10: {average_10}")
    print(f"ĐTB hệ 4: {average_4}")

if __name__ == "__main__":
    main()
    
#6
def is_prime(n):
    """
    Kiểm tra số n có phải là số nguyên tố hay không
    Input: số nguyên n > 1
    Output: True nếu n là số nguyên tố, False nếu không phải
    """
    # Nếu n <= 1, không phải số nguyên tố
    if n <= 1:
        return False
        
    # Kiểm tra từ 2 đến căn bậc 2 của n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    print("CHƯƠNG TRÌNH KIỂM TRA SỐ NGUYÊN TỐ")
    print("=" * 35)
    
    while True:
        try:
            # Nhập số từ người dùng
            n = int(input("\nNhập vào một số nguyên dương N (N>1) (0 để thoát): "))
            
            # Kiểm tra nếu người dùng muốn thoát
            if n == 0:
                break
                
            # Kiểm tra giá trị hợp lệ
            if n <= 1:
                print("Vui lòng nhập số lớn hơn 1!")
                continue
                
            # Kiểm tra và in kết quả
            if is_prime(n):
                print(f"Số {n} là số nguyên tố!")
            else:
                print(f"Số {n} không phải là số nguyên tố!")
                
        except ValueError:
            print("Vui lòng nhập một số nguyên!")
            
    print("\nCảm ơn bạn đã sử dụng chương trình!")

if __name__ == "__main__":
    main()

#7
def is_prime(n):
    """
    Kiểm tra số n có phải là số nguyên tố hay không
    Input: số nguyên n > 1
    Output: True nếu n là số nguyên tố, False nếu không phải
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes_up_to_n(n):
    """
    Tìm tất cả các số nguyên tố từ 2 đến n
    Input: số nguyên n > 1
    Output: list các số nguyên tố
    """
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def format_prime_list(primes):
    """
    Format list số nguyên tố để in ra màn hình đẹp hơn
    Input: list các số nguyên tố
    Output: chuỗi được format
    """
    return ', '.join(str(x) for x in primes)

def main():
    print("CHƯƠNG TRÌNH LIỆT KÊ SỐ NGUYÊN TỐ")
    print("=" * 35)
    
    while True:
        try:
            # Nhập số từ người dùng
            n = int(input("\nNhập vào một số nguyên dương N (N>1) (0 để thoát): "))
            
            # Kiểm tra nếu người dùng muốn thoát
            if n == 0:
                break
                
            # Kiểm tra giá trị hợp lệ
            if n <= 1:
                print("Vui lòng nhập số lớn hơn 1!")
                continue
                
            # Tìm và in các số nguyên tố
            primes = get_primes_up_to_n(n)
            print(f"\nCác số nguyên tố từ 2 tới {n}:")
            print(format_prime_list(primes))
            print(f"Tổng cộng có {len(primes)} số nguyên tố")
                
        except ValueError:
            print("Vui lòng nhập một số nguyên!")
            
    print("\nCảm ơn bạn đã sử dụng chương trình!")

if __name__ == "__main__":
    main()
    
#8
# Nhập vào số tự nhiên N
N = int(input("Nhập vào một số tự nhiên N (N > 0): "))

# Kiểm tra nếu N > 0
if N > 0:
    # Chuyển đổi số N sang hệ nhị phân
    binary_representation = bin(N)[2:]  # Loại bỏ '0b' ở đầu
    print(f"Số nhị phân của {N} là: {binary_representation}")
else:
    print("Vui lòng nhập một số tự nhiên lớn hơn 0.")

#9
# Khởi tạo dãy số là chiều cao của sinh viên trong lớp
heights = [170, 165, 180, 155, 160, 175, 185, 170]  ``

# 1. Hiển thị chiều cao của sinh viên cao nhất và thấp nhất
max_height = max(heights)
min_height = min(heights)
print(f"Chiều cao cao nhất trong lớp: {max_height} cm")
print(f"Chiều cao thấp nhất trong lớp: {min_height} cm")

# 2. Tính chiều cao trung bình của sinh viên trong lớp
average_height = sum(heights) / len(heights)
print(f"Chiều cao trung bình của sinh viên trong lớp: {average_height:.2f} cm")

# 3. Số lượng sinh viên có chiều cao lớn hơn hoặc bằng chiều cao trung bình
count_above_average = sum(1 for height in heights if height >= average_height)
print(f"Số lượng sinh viên có chiều cao >= chiều cao trung bình: {count_above_average}")


#Bai 2