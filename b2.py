registered = {"Alice", "Bob", "Charlie", "David", "Eve"}
checked_in = {"Alice", "Charlie", "David"}

not_checked_in = registered - checked_in
print(f"Các bạn chưa check-in: {not_checked_in}")


total_participants = len(registered | checked_in)
print(f"Tổng số bạn đã đăng ký và check-in: {total_participants}")


sorted_registered = sorted(registered)
print(f"Danh sách đã đăng ký theo thứ tự từ điển: {sorted_registered}")
