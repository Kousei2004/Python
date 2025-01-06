def greeting(name, birth_year):
    try:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Tên không được để trống và phải là chuỗi ký tự")
        if not isinstance(birth_year, int):
            raise ValueError("Năm sinh phải là số nguyên")
        current_year = 2024
        if birth_year > current_year:
            raise ValueError("Năm sinh không thể lớn hơn năm hiện tại")
        if birth_year < 1900:
            raise ValueError("Năm sinh không hợp lệ (phải sau năm 1900)")
        
        return f"Xin chào {name}! Năm nay bạn {current_year - birth_year} tuổi."
    except ValueError as e:
        return f"Lỗi: {str(e)}"

def rabbit_count(months):
    try:
        if not isinstance(months, int):
            raise ValueError("Số tháng phải là số nguyên")
        if months < 0:
            raise ValueError("Số tháng không thể âm")
        if months > 35:  # Giới hạn để tránh tràn stack
            raise ValueError("Số tháng quá lớn, vui lòng nhập số nhỏ hơn 36")
            
        if months == 0:
            return 0
        elif months == 1:
            return 1
        else:
            return rabbit_count(months - 1) + rabbit_count(months - 2)
    except ValueError as e:
        return f"Lỗi: {str(e)}"

def count_mark(marks):
    try:
        if not isinstance(marks, list):
            raise ValueError("Danh sách điểm phải là một mảng")
        if not marks:
            raise ValueError("Danh sách điểm không được để trống")
            
        retake_count = 0
        total_students = len(marks)
        
        for mark in marks:
            if not isinstance(mark, (int, float)):
                raise ValueError("Điểm phải là số")
            if mark < 0 or mark > 10:
                raise ValueError("Điểm phải nằm trong khoảng từ 0 đến 10")
            if mark < 5:
                retake_count += 1
                
        return retake_count, total_students
    except ValueError as e:
        return f"Lỗi: {str(e)}", 0

# Chương trình chính
def main():
    try:
        # Phần greeting()
        print("--- Hàm greeting() ---")
        while True:
            try:
                name = input("Nhập họ tên: ").strip()
                if name:
                    break
                print("Tên không được để trống!")
            except Exception:
                print("Đã xảy ra lỗi khi nhập tên!")
                
        while True:
            try:
                birth_year = int(input("Nhập năm sinh: "))
                break
            except ValueError:
                print("Vui lòng nhập một số nguyên hợp lệ!")
        
        print(greeting(name, birth_year))

        # Phần rabbit_count()
        print("\n--- Hàm rabbit_count() ---")
        while True:
            try:
                months = int(input("Nhập số tháng: "))
                if months >= 0:
                    break
                print("Số tháng không được âm!")
            except ValueError:
                print("Vui lòng nhập một số nguyên hợp lệ!")
        
        result = rabbit_count(months)
        if isinstance(result, str):  # Kiểm tra nếu là thông báo lỗi
            print(result)
        else:
            print(f"Số thỏ sau {months} tháng là: {result}")

        # Phần count_mark()
        print("\n--- Hàm count_mark() ---")
        while True:
            try:
                n = int(input("Nhập số lượng sinh viên: "))
                if n > 0:
                    break
                print("Số lượng sinh viên phải lớn hơn 0!")
            except ValueError:
                print("Vui lòng nhập một số nguyên hợp lệ!")

        marks = []
        for i in range(n):
            while True:
                try:
                    mark = float(input(f"Nhập điểm của sinh viên thứ {i+1}: "))
                    if 0 <= mark <= 10:
                        marks.append(mark)
                        break
                    print("Điểm phải nằm trong khoảng từ 0 đến 10!")
                except ValueError:
                    print("Vui lòng nhập một số hợp lệ!")

        retake, total = count_mark(marks)
        if isinstance(retake, str):  # Kiểm tra nếu là thông báo lỗi
            print(retake)
        else:
            print(f"Số sinh viên học lại: {retake}")
            print(f"Tổng số sinh viên: {total}")

    except KeyboardInterrupt:
        print("\nChương trình đã bị dừng bởi người dùng.")
    except Exception as e:
        print(f"\nĐã xảy ra lỗi không mong muốn: {str(e)}")

if __name__ == "__main__":
    main()
    
#2
def bmi_show(height, weight):
    """
    Phân loại BMI dựa trên chiều cao (m) và cân nặng (kg)
    """
    try:
        if not isinstance(height, (int, float)) or not isinstance(weight, (int, float)):
            raise ValueError("Chiều cao và cân nặng phải là số")
            
        if height <= 0 or height > 3:
            raise ValueError("Chiều cao phải lớn hơn 0 và nhỏ hơn 3m")
        if weight <= 0 or weight > 500:
            raise ValueError("Cân nặng phải lớn hơn 0 và nhỏ hơn 500kg")
            
        bmi = weight / (height * height)
        
        if bmi < 18.5:
            return "Gầy"
        elif bmi < 25:
            return "Bình thường"
        elif bmi < 30:
            return "Thừa cân"
        else:
            return "Béo phì"
            
    except ZeroDivisionError:
        return "Lỗi: Chiều cao không thể bằng 0"
    except ValueError as e:
        return f"Lỗi: {str(e)}"
    except Exception as e:
        return f"Lỗi không xác định: {str(e)}"

def cal_point(marks):
    """
    Tính điểm trung bình với hệ số 10 và 4
    """
    try:
        if not isinstance(marks, list):
            raise ValueError("Danh sách điểm phải là một mảng")
        
        if not marks:
            raise ValueError("Danh sách điểm không được để trống")
            
        for mark in marks:
            if not isinstance(mark, (int, float)):
                raise ValueError("Điểm phải là số")
            if mark < 0 or mark > 10:
                raise ValueError("Điểm phải nằm trong khoảng từ 0 đến 10")
        
        avg_10 = sum(marks) / len(marks)
        
        if avg_10 < 4:
            avg_4 = 0
        elif avg_10 < 5:
            avg_4 = 1
        elif avg_10 < 6:
            avg_4 = 1.5
        elif avg_10 < 7:
            avg_4 = 2
        elif avg_10 < 8:
            avg_4 = 2.5
        elif avg_10 < 9:
            avg_4 = 3
        else:
            avg_4 = 4
            
        return avg_10, avg_4
        
    except ValueError as e:
        return f"Lỗi: {str(e)}", None
    except Exception as e:
        return f"Lỗi không xác định: {str(e)}", None

def list_prime(n):
    """
    Trả về danh sách các số nguyên tố từ 1 đến n
    """
    try:
        if not isinstance(n, int):
            raise ValueError("n phải là số nguyên")
            
        if n < 1:
            raise ValueError("n phải lớn hơn hoặc bằng 1")
        if n > 100000:
            raise ValueError("n quá lớn, vui lòng nhập số nhỏ hơn 100000")
            
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
            
        return [num for num in range(1, n + 1) if is_prime(num)]
        
    except ValueError as e:
        return f"Lỗi: {str(e)}"
    except Exception as e:
        return f"Lỗi không xác định: {str(e)}"

def main():
    while True:
        print("\n=== MENU ===")
        print("1. Tính chỉ số BMI")
        print("2. Tính điểm trung bình")
        print("3. Liệt kê số nguyên tố")
        print("4. Thoát")
        
        try:
            choice = input("Chọn chức năng (1-4): ").strip()
            
            if choice == "1":
                print("\n=== TÍNH CHỈ SỐ BMI ===")
                while True:
                    try:
                        height = float(input("Nhập chiều cao (m): "))
                        weight = float(input("Nhập cân nặng (kg): "))
                        result = bmi_show(height, weight)
                        print(f"Kết quả phân loại BMI: {result}")
                        break
                    except ValueError:
                        print("Vui lòng nhập số hợp lệ!")
                    
            elif choice == "2":
                print("\n=== TÍNH ĐIỂM TRUNG BÌNH ===")
                marks = []
                while True:
                    try:
                        n = int(input("Nhập số lượng điểm: "))
                        if n <= 0:
                            print("Số lượng điểm phải lớn hơn 0!")
                            continue
                        break
                    except ValueError:
                        print("Vui lòng nhập số nguyên!")
                
                for i in range(n):
                    while True:
                        try:
                            mark = float(input(f"Nhập điểm thứ {i+1}: "))
                            if 0 <= mark <= 10:
                                marks.append(mark)
                                break
                            print("Điểm phải nằm trong khoảng 0-10!")
                        except ValueError:
                            print("Vui lòng nhập số hợp lệ!")
                
                avg_10, avg_4 = cal_point(marks)
                if isinstance(avg_10, str):  # Nếu có lỗi
                    print(avg_10)
                else:
                    print(f"Điểm trung bình hệ 10: {avg_10:.2f}")
                    print(f"Điểm trung bình hệ 4: {avg_4:.2f}")
                    
            elif choice == "3":
                print("\n=== LIỆT KÊ SỐ NGUYÊN TỐ ===")
                while True:
                    try:
                        n = int(input("Nhập số n: "))
                        result = list_prime(n)
                        if isinstance(result, str):  # Nếu có lỗi
                            print(result)
                        else:
                            print(f"Các số nguyên tố từ 1 đến {n}:")
                            print(result)
                        break
                    except ValueError:
                        print("Vui lòng nhập số nguyên!")
                    
            elif choice == "4":
                print("Cảm ơn bạn đã sử dụng chương trình!")
                break
                
            else:
                print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1-4.")
                
        except KeyboardInterrupt:
            print("\nChương trình đã bị dừng bởi người dùng")
            break
        except Exception as e:
            print(f"Lỗi không mong muốn: {str(e)}")

if __name__ == "__main__":
    main()