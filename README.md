# Python Code Smells:

- Imprecise types: Loại không chính xác
- Duplicate code
- Not using available built-in function
- Vegue identifiers: Đặt tên không rõ ràng hoặc mang ý nghĩa
- Using isinstance to separate behavior
- Using Boolean flags to make a method do 2 different things
- Catching and then ignoring exceptions
- Not use custom exception
- Using the wrong data structure
- Using misleading names
- Classes with too many instance variables
- Verb/subject
- Backpedalling
- Hard-wired sequences with a fixed order
- Creating unrelated objects in the initializer
- Not relying on keyword arguments

# Functions vs Classes: When to Use Which and Why?

- Functions: focus on the flow of information (like processing data) in sequence
- Class: focus on state (like bank accounts) or collections of object need to be structured

# SOLID principles

1.  **[S] Single responsibility**

    - Classes and methods have a single reponsiblity

2.  **[O] Open/closed**

    - Open for extention the existing code with new function
    - Closed for modification the original code
      -> Create abstract class or function

3.  **[L] Liskov substitution**

    - If have object in program, we should replace those objects with instaces of their subtypes or subclasses without altering the correctness of the program
    - Ex: Payment class have many payment type like: debit, credit, paypal, ... and each of them have own configs: security code for debit and credit, authentication email for paypal -> Therefore, we must create own \_\_init\_\_ function in each PaymentClass to initialize the object
    - Extra ex: Trong đời sống, A là B (hình vuông là hình chữ nhật, chim cánh cụt là chim) không có nghĩa là class A nên kế thừa class B. Chỉ cho class A kế thừa class B khi class A thay thế được cho class B.

4.  **[I] Interface segregation**

    - Instead of one general purpose interface we split it so that subclasses have meaningful behavior
    - Ex: Nếu ta tạo ra 1 interface bự (hơn 100 method chẳng hạn), mỗi class sẽ phải implement toàn bộ 100 method đó, kể những method không bao giờ sử dụng đến. Nếu áp dụng ISP, ta sẽ chia interface này ra thành nhiều interface nhỏ, các class chỉ cần implement những interface có chức năng mà chúng cần, không cần phải implement những chức năng thừa nữa.

5.  **[D] Dependency inversion**

    - Các module cấp cao không nên phụ thuộc vào các module cấp thấp. Cả 2 nên phụ thuộc vào abstraction.
    - Interface (abstraction) không nên phụ thuộc vào chi tiết, mà ngược lại. (Các class giao tiếp với nhau thông qua interface, không phải thông qua implementation.)
    - Ex: Để dễ hiểu, bạn hãy nhìn vào cái mấy cái đèn điện trong nhà mình. Ở đây, module cấp cao chính là ổ điện, interface chính là đuôi đèn tròn, 2 module cấp thấp là bóng đèn tròn và bóng đèn huỳnh quang. Hai module này đều kế thừa interface đuổi tròn, Ta có thể dễ dàng thay đổi 2 loại bóng vì module cấp cao (ổ điện) chỉ quan tâm tới interface (đuôi tròn), không quan tâm tới implementation (bóng đèn tròn hay huỳnh quang).

# Protocol and ABC

- Protocol: Using when want to create a interface class
- ABC: Using when want to create a abstract class

# GRASP Design Principles
