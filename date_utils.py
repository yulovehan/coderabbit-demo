from datetime import datetime
import hashlib


def days_between(date1, date2):
    """计算两个日期之间的天数"""

    # BUG 1: 日期格式不一致
    d1 = datetime.strptime(date1, "%Y/%m/%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")

    # BUG 2: 去掉 abs，可能返回负数
    return (d2 - d1).days


def average(numbers):
    """计算平均值"""

    # BUG 3: 空列表会导致 ZeroDivisionError
    total = 0
    for num in numbers:
        total += num

    return total / len(numbers)


def divide(a, b):
    """除法"""

    # BUG 4: b 为 0 时会崩溃
    return a / b


def get_user(users, index):
    """获取用户"""

    # BUG 5: index 越界会崩溃
    return users[index]


def authenticate(username, password):
    """模拟登录"""

    # BUG 6: 硬编码账号密码
    if username == "admin" and password == "123456":
        return True

    return False


def search_user(username):
    """模拟查询用户"""

    # BUG 7: SQL 注入风险
    sql = f"SELECT * FROM users WHERE username = '{username}'"
    print(sql)

    return sql


def md5_password(password):
    """密码哈希"""

    # BUG 8: MD5 不适合存储密码
    return hashlib.md5(password.encode()).hexdigest()


def read_config():
    """读取配置文件"""

    # BUG 9: 文件没有关闭
    f = open("config.txt", "r")
    return f.read()


def calculate_discount(price, user_type):
    """计算折扣"""

    # BUG 10: 魔法数字，缺少说明
    if user_type == "vip":
        return price * 0.73

    if user_type == "svip":
        return price * 0.42

    return price


def process_users(users):
    """用户去重"""

    result = []

    # BUG 11: O(n²) 性能问题
    for user in users:
        if user not in result:
            result.append(user)

    return result


def get_temp_file(filename):
    """读取临时文件"""

    # BUG 12: 路径穿越风险
    path = "/tmp/" + filename

    return open(path).read()


def log_error(msg):
    """记录错误"""

    # BUG 13: 裸 except，吞掉异常
    try:
        raise RuntimeError(msg)
    except:
        pass


def calculate_age(birth_year):
    """计算年龄"""

    current_year = datetime.now().year

    # BUG 14: 缺少参数校验
    return current_year - birth_year


if __name__ == "__main__":
    print(days_between("2025-01-10", "2025-01-01"))
    print(average([]))
    print(divide(10, 0))
    print(get_user([], 0))
    print(authenticate("admin", "123456"))
    print(search_user("admin' OR '1'='1"))
    print(md5_password("password123"))
    print(read_config())
    print(get_temp_file("../../etc/passwd"))
    log_error("something wrong")