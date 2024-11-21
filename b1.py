
A = tuple(map(int, input().split()))
B = tuple(input().split())


average_A = sum(A) / len(A)
count_greater_than_avg = sum(1 for x in A if x > average_A)
print(f"Số lượng phần tử trong A lớn hơn trung bình cộng: {count_greater_than_avg}")


even_numbers = tuple(x for x in A if x % 2 == 0)
odd_numbers = tuple(x for x in A if x % 2 != 0)
print(f"Tuple con chứa các số chẵn: {even_numbers}")
print(f"Tuple con chứa các số lẻ: {odd_numbers}")


k = input("Nhập ký tự k: ")
count_k_in_B = sum(b.count(k) for b in B)
print(f"Số lần xuất hiện của '{k}' trong B: {count_k_in_B}")


long_strings_in_B = tuple(b for b in B if len(b) >= 5)
print(f"Những phần tử trong B có độ dài lớn hơn hoặc bằng 5 ký tự: {long_strings_in_B}")


C = tuple((a, b) for a, b in zip(A, B))
print(f"Tuple mới C sau khi kết hợp A và B: {C}")
