# 在这里编写代码class Book:
    """书籍类，包含书籍属性和可借状态管理"""
    def __init__(self, title, author, isbn):
        self.title = title  # 书名
        self.author = author  # 作者
        self.isbn = isbn  # ISBN编号
        self.is_borrowed = False  # 可借状态，默认未借出

    def __str__(self):
        status = "已借出" if self.is_borrowed else "可借阅"
        return f"《{self.title}》- {self.author}（ISBN：{self.isbn}）- {status}"


class User:
    """用户类，包含用户属性和借书记录管理"""
    def __init__(self, name, card_id):
        self.name = name  # 姓名
        self.card_id = card_id  # 借书卡号
        self.borrowed_books = []  # 已借书籍列表

    def borrow_book(self, book):
        """借书功能：检查书籍状态并完成借阅"""
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"{self.name}成功借阅《{book.title}》")
            return True
        else:
            print(f"《{book.title}》已被借出，无法借阅")
            return False

    def return_book(self, book):
        """还书功能：检查借阅记录并完成归还"""
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name}成功归还《{book.title}》")
            return True
        else:
            print(f"{self.name}未借阅《{book.title}》，无法归还")
            return False

    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        borrowed_str = "、".join(borrowed_titles) if borrowed_titles else "无"
        return f"用户：{self.name}（借书卡：{self.card_id}），已借书籍：{borrowed_str}"


class LibrarySystem:
    """图书馆系统类，管理书籍和用户的整体交互"""
    def __init__(self):
        self.books = []  # 图书馆书籍库
        self.users = []  # 图书馆用户库

    def add_book(self, book):
        """添加书籍到图书馆"""
        self.books.append(book)
        print(f"书籍《{book.title}》已加入图书馆")

    def add_user(self, user):
        """添加用户到图书馆"""
        self.users.append(user)
        print(f"用户{user.name}已注册，借书卡号：{user.card_id}")

    def check_book_availability(self, isbn):
        """检查书籍可借状态（通过ISBN查询）"""
        for book in self.books:
            if book.isbn == isbn:
                status = "可借阅" if not book.is_borrowed else "已借出"
                print(f"书籍《{book.title}》的状态：{status}")
                return not book.is_borrowed
        print("未找到该ISBN对应的书籍")
        return False


# 测试系统功能
if __name__ == "__main__":
    # 初始化图书馆系统
    lib = LibrarySystem()

    # 添加书籍
    book1 = Book("Python编程：从入门到实践", "埃里克·马瑟斯", "9787115428028")
    book2 = Book("数据结构与算法分析", "马克·艾伦·维斯", "9787111640141")
    lib.add_book(book1)
    lib.add_book(book2)

    # 添加用户
    user1 = User("张三", "C001")
    user2 = User("李四", "C002")
    lib.add_user(user1)
    lib.add_user(user2)

    # 检查书籍可借状态
    lib.check_book_availability("9787115428028")

    # 借书操作
    user1.borrow_book(book1)
    lib.check_book_availability("9787115428028")

    # 还书操作
    user1.return_book(book1)
    lib.check_book_availability("9787115428028")

    # 尝试借阅已借出的书籍（测试）
    user1.borrow_book(book1)
    user2.borrow_book(book1)
