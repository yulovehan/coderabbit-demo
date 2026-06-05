from datetime import datetime

def days_between(date1, date2):
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def average(numbers):
    """
    计算平均值
    """
    if not numbers:
        raise ValueError("numbers must not be empty")
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

if __name__ == "__main__":
    print(days_between("2025-01-10", "2025-01-01"))
    print(average([1, 2, 3]))
