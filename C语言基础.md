## C语言基础
#### 一. 第一个C程序
`Hello World!`
```c
// 头文件:包含标准输入输出库
#include <stdio.h>
int main() {
    // 打印"Hello, World!"
    printf("Hello, World!\n");
    return 0; // 返回 0 表示程序成功结束
}

```
#### 二. 变量
```c
#include <stdio.h>
int main(){
     //变量
    int num1 = 10;
    int num2;
    num2 = 20;
    //对于局部int变量.如果不赋值默认为随机的值.全局变量默认为0
    int num3;
    printf("变量num1=%d,num2=%d,num3=%d\n", num1, num2,num3);
    return 0;
}

```
#### 三. 常量
```c
#include <stdio.h>
//define 常量名=value  宏定义:后不可以加分号
#define CONST_VALUE 10;
int main(){
    //定义常量const 类型 常量名=value
    const double pi=3.1415926;
    printf("常量pi的值为%f",pi);
    printf("常量CONST_VALUE=%d\n",CONST_VALUE);
    return 0;
}
```
#### 四. 数据类型
##### 1. 基本数据类型

| 数据类型 | 关键字       | 内存大小 | 说明                                              |
| -------- | ------------ | -------- | ------------------------------------------------- |
| 整型     | `int`        | 2或4字节 | 整数类型，取决于编译器                            |
| 短整型   | `short int`  | 2字节    | 范围小的整数类型                                  |
| 长整型   | `long int`   | 4或8字节 | 范围大的整数类型                                  |
| 字符型   | `char`       | 1字节    | 字符数据类型，存储单个字符                        |
| 浮点型   | `float`      | 4字节    | 单精度浮点数                                      |
| 双精度型 | `double`     | 8字节    | 双精度浮点数                                      |
| 长双精度 | `long double`| 10或12字节 | 精度更高的双精度浮点数（取决于系统架构）        |
| 布尔型   | `_Bool`      | 1字节    | C99标准引入的布尔类型，值为 `0`（假） 或 `1`（真）|

##### 2. 派生数据类型
派生数据类型是基于基本数据类型进行扩展的类型，用于创建更复杂的数据结构。

| 数据类型  | 说明                          |
| --------- | ----------------------------- |
| 数组      | 一组相同类型的数据             |
| 指针      | 存储变量地址的变量             |
| 结构体    | 一种聚合数据类型，包含多个不同类型的成员 |
| 联合体    | 类似结构体，但成员共享同一块内存 |
| 函数      | 函数作为一种类型，可以返回值    |

##### 3. 枚举类型
枚举类型使用 `enum` 关键字来定义。枚举类型允许为变量定义一组命名的整数常量。

```c
enum Day {Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday};
```

##### 4. 空类型
空类型主要用于表示无类型数据或函数没有返回值。

| 数据类型 | 关键字 | 说明                 |
| -------- | ------ | -------------------- |
| 空类型   | `void` | 没有返回值的函数类型 |
##### 5. 占位符
在C语言中，printf 和 scanf 函数常用的占位符（格式说明符）用于格式化输入和输出数据。不同的数据类型有不同的占位符，以下是常用的占位符及其用途：
以下是包含所有常用占位符的一个整合表格：

| 数据类型               | 占位符     | 说明                                                         | 示例                |
|------------------------|------------|--------------------------------------------------------------|---------------------|
| **整数类型**           |            |                                                              |                     |
| `int`                  | `%d`       | 十进制整数                                                   | `42 -> %d -> 42`    |
| `unsigned int`         | `%u`       | 无符号十进制整数                                             | `42 -> %u -> 42`    |
| `int`                  | `%i`       | 十进制整数（与 `%d` 类似）                                   | `42 -> %i -> 42`    |
| `int`                  | `%o`       | 八进制整数                                                   | `42 -> %o -> 52`    |
| `int`                  | `%x`       | 无符号十六进制整数（小写字母）                               | `42 -> %x -> 2a`    |
| `int`                  | `%X`       | 无符号十六进制整数（大写字母）                               | `42 -> %X -> 2A`    |
| `short int`            | `%hd`      | 短整型十进制整数                                             | `42 -> %hd -> 42`   |
| `long int`             | `%ld`      | 长整型十进制整数                                             | `42L -> %ld -> 42`  |
| `long int`             | `%lo`      | 长整型八进制整数                                             | `42L -> %lo -> 52`  |
| `long int`             | `%lx`      | 长整型十六进制整数                                           | `42L -> %lx -> 2a`  |
| **字符类型**           |            |                                                              |                     |
| `char`                 | `%c`       | 单个字符                                                     | `'A' -> %c -> A`    |
| `char*`                | `%s`       | 字符串                                                       | `"Hello" -> %s -> Hello` |
| **浮点数类型**         |            |                                                              |                     |
| `float`                | `%f`       | 单精度浮点数                                                 | `3.14 -> %f -> 3.140000` |
| `double`               | `%lf`      | 双精度浮点数                                                 | `3.14 -> %lf -> 3.140000` |
| `float`/`double`       | `%e`       | 科学计数法表示的浮点数（小写e）                              | `3.14 -> %e -> 3.140000e+00` |
| `float`/`double`       | `%E`       | 科学计数法表示的浮点数（大写E）                              | `3.14 -> %E -> 3.140000E+00` |
| `float`/`double`       | `%g`       | 自动选择普通浮点数或科学计数法                               | `3.14 -> %g -> 3.14` |
| `float`/`double`       | `%G`       | 与 `%g` 类似，但使用大写字母                                 | `3.14 -> %G -> 3.14` |
| `long double`          | `%Lf`      | 长双精度浮点数                                               | `3.14L -> %Lf -> 3.140000` |
| **指针类型**           |            |                                                              |                     |
| `void*`                | `%p`       | 输出指针地址的十六进制表示                                   |                     |
| **打印特殊符号**       |            |                                                              |                     |
| `%`                    | `%%`       | 打印百分号                                                   | `% -> %% -> %`      |
| **格式化选项**         |            |                                                              |                     |
| **宽度控制**           | `%5d`      | 输出宽度至少为5                                              | `42 -> %5d -> "   42"` |
| **精度控制**           | `%.2f`     | 小数点后保留两位                                             | `3.14159 -> %.2f -> 3.14` |
| **左对齐**             | `%-10s`    | 输出左对齐，宽度为10                                         | `"Hello" -> %-10s -> "Hello     "` |
| **填充字符**           | `%04d`     | 输出宽度为4，左边用0填充                                     | `42 -> %04d -> 0042` |

#### 五. 运算符

##### 1. 算术运算符

| 运算符 | 说明             | 示例           |
| ------ | ---------------- | -------------- |
| `+`    | 加法             | `a + b`        |
| `-`    | 减法             | `a - b`        |
| `*`    | 乘法             | `a * b`        |
| `/`    | 除法             | `a / b`        |
| `%`    | 取模（取余数）   | `a % b`        |
| `++`   | 自增，值加1      | `a++` 或 `++a` |
| `--`   | 自减，值减1      | `a--` 或 `--a` |

##### 2. 关系运算符

| 运算符 | 说明                     | 示例           |
| ------ | ------------------------ | -------------- |
| `==`   | 等于                     | `a == b`       |
| `!=`   | 不等于                   | `a != b`       |
| `>`    | 大于                     | `a > b`        |
| `<`    | 小于                     | `a < b`        |
| `>=`   | 大于等于                 | `a >= b`       |
| `<=`   | 小于等于                 | `a <= b`       |

##### 3. 逻辑运算符

| 运算符 | 说明               | 示例          |
| ------ | ------------------ | ------------- |
| `&&`   | 逻辑与（AND）      | `a && b`      |
| `\|\|` | 逻辑或（OR）       | `a \|\| b`    |
| `!`    | 逻辑非（NOT）      | `!a`          |

##### 4. 位运算符

| 运算符 | 说明                       | 示例        |
| ------ | -------------------------- | ----------- |
| `&`    | 按位与（AND）               | `a & b`     |
| `\|`   | 按位或（OR）                | `a \| b`    |
| `^`    | 按位异或（XOR）             | `a ^ b`     |
| `~`    | 按位取反（NOT）             | `~a`        |
| `<<`   | 左移位操作（左移n位）       | `a << n`    |
| `>>`   | 右移位操作（右移n位）       | `a >> n`    |

##### 5. 赋值运算符

| 运算符 | 说明                       | 示例        |
| ------ | -------------------------- | ----------- |
| `=`    | 赋值                       | `a = b`     |
| `+=`   | 加后赋值                   | `a += b`    |
| `-=`   | 减后赋值                   | `a -= b`    |
| `*=`   | 乘后赋值                   | `a *= b`    |
| `/=`   | 除后赋值                   | `a /= b`    |
| `%=`   | 取模后赋值                 | `a %= b`    |
| `&=`   | 按位与后赋值               | `a &= b`    |
| `\|=`  | 按位或后赋值               | `a \|= b`   |
| `^=`   | 按位异或后赋值             | `a ^= b`    |
| `<<=`  | 左移位后赋值               | `a <<= n`   |
| `>>=`  | 右移位后赋值               | `a >>= n`   |

##### 6. 条件运算符（三元运算符）

| 运算符 | 说明                               | 示例               |
| ------ | ---------------------------------- | ------------------ |
| `? :`  | 条件运算符（根据条件返回值）       | `(a > b) ? a : b`  |

##### 7. 其他运算符

| 运算符 | 说明                       | 示例        |
| ------ | -------------------------- | ----------- |
| `sizeof` | 返回数据类型的大小        | `sizeof(int)`|
| `&`    | 取地址                     | `&a`        |
| `*`    | 指针解引用                 | `*ptr`      |
| `,`    | 逗号运算符                 | `a = (b, c)`|
| `->`   | 结构体指针成员访问          | `ptr->member`|
| `.`    | 结构体成员访问              | `obj.member` |

##### 运算符优先级
不同运算符有不同的优先级。通常算术运算符的优先级高于关系运算符，逻辑运算符的优先级最低。此外，括号 `()` 可以用来显式地控制运算顺序。
#### 六. 流程控制
##### 1. 条件语句
- if语句
```c
//方法一
if (/*condition*/) {
    /*code*/
}

//方法二
if (/* condition */) {
    /* code */
}else{
    /* code */
}

// 方法三
if (/* condition */) {
    /* code */
}else if (/* condition2 */) {
    /* code */
}else{
    /* code */
}
```
- 三元运算符
```c
/*condition*/? /*true_value*/ : /*false_value*/;
```
- switch语句
```c
//条件只能为整数、字符形
switch (表达式) {
    case 常量1:
        // 当表达式的值等于常量1时执行的代码
        break;
    case 常量2:
        // 当表达式的值等于常量2时执行的代码
        break;
    default:
        // 当表达式的值不匹配任何case时执行的代码
}
```
##### 2. 循环语句
- for语句
```c
for (初始化; 条件; 迭代) {
    // 循环体

    // break;用于立即终止循环
    // continue;跳过本次循环,进入下一次循环的判断。

}

```
- while语句
```c
while (条件) {
    // 循环体
}

```
- do...while语句(至少执行一次)
```c
do {
    // 循环体
} while (条件);

```

#### 七. 内存与指针
指针是C语言中的一个核心概念，它存储了变量的内存地址。指针可以用来直接操作内存，进行高效的数据处理。

##### 1. 指针的定义和基本操作

**定义指针变量：**
指针变量存储的是另一个变量的地址。定义指针时需要指定指针指向的数据类型。

**语法结构：**
```c
数据类型 *指针变量名;
```

**示例：**
```c
int *ptr;
```
这里，`ptr` 是一个指向 `int` 类型的指针变量。

**获取变量的地址（取地址符 `&`）：**
```c
int num = 10;
int *ptr = &num;  // ptr 指向 num 的地址
```

**解引用指针（取值符 `*`）：**
```c
int value = *ptr;  // 通过指针 ptr 获取其指向的变量的值
```

**完整示例：**
```c
#include <stdio.h>

int main() {
    int num = 10;   // 定义一个整型变量
    int *ptr = &num; // 定义一个指向 num 的指针

    printf("num 的值: %d\n", num);
    printf("num 的地址: %p\n", (void*)&num);
    printf("ptr 存储的地址: %p\n", (void*)ptr);
    printf("ptr 指向的值: %d\n", *ptr);

    return 0;
}
```

##### 2. 指针的运算

**指针加法：**
```c
int arr[5] = {1, 2, 3, 4, 5};
int *ptr = arr;     // 数组名即为数组首元素的地址

// 通过指针访问数组元素
for (int i = 0; i < 5; i++) {
    printf("arr[%d] = %d\n", i, *(ptr + i));
}
```

**指针减法：**
```c
int *ptr1 = &arr[4];
int *ptr2 = &arr[1];
int diff = ptr1 - ptr2; // 计算两个指针之间的元素数量差
printf("ptr1 和 ptr2 之间的元素差: %d\n", diff);
```

##### 3. 指针与数组

**示例：**
```c
#include <stdio.h>

int main() {
    int arr[3] = {10, 20, 30};
    int *ptr = arr; // 数组名即为指向数组首元素的指针

    for (int i = 0; i < 3; i++) {
        printf("arr[%d] = %d\n", i, *(ptr + i));
    }

    return 0;
}
```

##### 4. 指针的高级应用

**指针作为函数参数：**

指针可以用来修改函数外的变量值，因为函数参数是传递变量的地址。

**示例：**
```c
#include <stdio.h>

void increment(int *p) {
    (*p)++;
}

int main() {
    int num = 5;
    increment(&num);
    printf("num 增加后的值: %d\n", num);

    return 0;
}
```

**指针和动态内存分配：**

使用指针可以实现动态内存分配，管理内存更灵活。

**示例：**
```c
#include <stdio.h>
#include <stdlib.h> // 包含 malloc 和 free 函数

int main() {
    int *arr = (int *)malloc(5 * sizeof(int)); // 动态分配内存
    if (arr == NULL) {
        printf("内存分配失败\n");
        return 1;
    }

    for (int i = 0; i < 5; i++) {
        arr[i] = i * 10;
    }

    for (int i = 0; i < 5; i++) {
        printf("arr[%d] = %d\n", i, arr[i]);
    }

    free(arr); // 释放分配的内存

    return 0;
}
```

##### 5. 指针的常见错误

- **悬空指针**：指针指向的内存已经释放，但指针还存在。
- **空指针**：指针未初始化或指向 `NULL`。
- **野指针**：指针指向未定义的内存区域。

使用指针时需特别小心，确保指针的合法性和有效性，以避免内存泄漏或程序崩溃。

##### 6. 内存分配与释放
在C语言中，内存管理是非常重要的概念。主要的内存区域包括栈内存和堆内存

###### 1. 栈内存（Stack）
栈内存是用于存储局部变量和函数调用的相关信息。栈内存的分配和释放是由编译器在编译时自动完成的，

特点：

自动分配和释放：栈内存中的数据在函数调用时自动分配，在函数返回时自动释放。
内存访问快：由于栈内存的分配和释放遵循先进后出（LIFO）原则，内存访问速度较快。
空间有限：栈的大小通常是有限的，如果栈空间用尽，会导致栈溢出（Stack Overflow）。

###### 2. 堆内存（Heap）
堆内存是由程序员显式管理的内存区域，通常用于动态分配内存。堆内存的管理更灵活，但也容易导致内存泄漏和其他内存管理问题。

特点：

手动分配和释放：通过 malloc、calloc、realloc 函数分配内存，通过 free 函数释放内存。
内存访问相对较慢：由于堆内存的管理涉及更多的操作，内存访问速度较栈内存慢。
空间较大：堆的大小通常由操作系统限制，适合大规模数据的动态内存分配。
在C语言中，内存管理是通过一组标准库函数来完成的，这些函数主要用于动态分配、重新分配和释放内存。下面是这些内存管理函数的详细介绍：


| 函数名   | 功能                                       | 语法                                | 示例代码                              |
| -------- | ------------------------------------------ | ----------------------------------- | ------------------------------------- |
| `malloc` | 分配指定大小的内存块                       | `void *malloc(size_t size);`        | `int *ptr = (int *)malloc(10 * sizeof(int));` |
| `calloc` | 分配并初始化指定数量的内存块               | `void *calloc(size_t num, size_t size);` | `int *ptr = (int *)calloc(10, sizeof(int));` |
| `realloc`| 重新调整已分配内存块的大小                 | `void *realloc(void *ptr, size_t new_size);` | `ptr = (int *)realloc(ptr, 20 * sizeof(int));` |
| `free`   | 释放之前分配的内存块                       | `void free(void *ptr);`             | `free(ptr);`                           |

#### 八. 数组

数组是一种用于存储相同类型元素的集合。并且这些值可以通过索引进行访问和操作
##### 1. 数组的声明与初始化
 
```c
数据类型 数组名[数组大小]={元素};
//当初始化元素时，可以省略部分元素，剩下的元素自动初始化为0
```
##### 2. 访问或修改数组元素

数组元素通过索引访问，索引从0开始。可以使用下标操作符 `[]` 来访问和修改数组中的元素。

```c
int arr[5] = {10, 20, 30, 40, 50};

printf("第一个元素: %d\n", arr[0]); // 输出: 10
arr[2] = 100; // 修改第三个元素的值
printf("修改后的第三个元素: %d\n", arr[2]); // 输出: 100
```

##### 3. 数组的大小

可以使用 `sizeof` 运算符来获取数组的总字节数和元素个数。计算数组的元素个数时，可以通过总字节数除以单个元素的字节数来实现。

```c
int arr[5] = {10, 20, 30, 40, 50};

size_t total_size = sizeof(arr); // 数组总字节数
size_t element_size = sizeof(arr[0]); // 单个元素的字节数
size_t num_elements = total_size / element_size; // 元素个数

printf("数组的总字节数: %zu\n", total_size);
printf("数组的元素个数: %zu\n", num_elements);
```
##### 4. 多维数组

C语言支持多维数组，最常见的是二维数组，用于表示矩阵或表格数据。

```c
int matrix[3][4] = { 
    {1, 2, 3, 4}, 
    {5, 6, 7, 8}, 
    {9, 10, 11, 12} 
};
```

```c
// 使用多个索引访问元素
printf("matrix[1][2] = %d\n", matrix[1][2]); // 输出: 7
```
##### 5. 数组作为函数参数

在函数中使用数组时，实际上传递的是数组的首地址（即指针）。函数内对数组的修改会影响到原始数组。

` 通过对数组指针的加减操作，可以访问数组中的任意位置。`
```c
#include <stdio.h>

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    printArray(arr, 5);
    return 0;
}
```

##### 6. 数组的常见操作

- **遍历数组：** 使用循环结构遍历数组元素。
- **排序数组：** 可以使用排序算法如冒泡排序、选择排序等对数组进行排序。
- **搜索数组：** 可以使用线性搜索或二分搜索算法查找特定元素。

**示例：**
```c
#include <stdio.h>

void bubbleSort(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int arr[5] = {64, 25, 12, 22, 11};
    int size = sizeof(arr) / sizeof(arr[0]);

    bubbleSort(arr, size);

    printf("排序后的数组: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
```
#### 九.函数

在C语言中，函数是程序的基本构建块，用于组织和复用代码。函数通过将特定的代码段封装起来，能够执行某个特定的任务。函数的使用可以使程序更加模块化、可读性更强，并且方便调试和维护。

##### 1. 函数的定义与声明

**函数定义：** 包含函数的返回类型、函数名、参数列表以及函数体。函数体包含了实际的代码逻辑。

**函数声明：** 函数声明是告诉编译器函数的名字、返回类型和参数类型，但不包含具体的实现。函数声明通常放在程序的开头部分或头文件中。

**示例：**

```c
// 函数声明
int add(int a, int b);
// 函数定义
int add(int a, int b) {
    return a + b;
}
 // 调用函数(先声明在调用)
int main() {
    int sum = add(5, 3);
    printf("Sum = %d\n", sum);
    return 0;
}


```

##### 2. 函数的参数

函数可以接受参数，并且这些参数在函数体内作为局部变量使用。函数参数可以是基本数据类型、指针、结构体等。

```c
void printDetails(const char *name, int age) {
    printf("Name: %s\n", name);
    printf("Age: %d\n", age);
}

int main() {
    printDetails("Alice", 30);
    return 0;
}
```

##### 3. 函数的返回值

函数可以返回一个值，也可以没有返回值。返回值的类型由函数的返回类型决定。如果函数不需要返回值，使用 `void` 作为返回类型。

```c
// 函数返回整数值
int multiply(int a, int b) {
    return a * b;
}

// 函数没有返回值
void printHello() {
    printf("Hello, World!\n");
}

```

##### 4. 函数的递归

在函数内部调用自身的函数。递归需要一个或多个基准条件来停止递归，否则会导致无限递归。


```c
// 计算阶乘的递归函数
int factorial(int n) {
    if (n == 0) {
        return 1; // 基准条件
    } else {
        return n * factorial(n - 1); // 递归调用
    }
}

int main() {
    int num = 5;
    printf("Factorial of %d = %d\n", num, factorial(num));
    return 0;
}
```

##### 5. 函数指针

函数指针是指向函数的指针，可以用于动态调用函数。函数指针可以作为函数参数传递，也可以用于实现回调机制。

```c
#include <stdio.h>

// 定义函数指针类型
typedef int (*Operation)(int, int);

// 函数实现
int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

// 使用函数指针
void performOperation(Operation op, int x, int y) {
    printf("Result = %d\n", op(x, y));
}

int main() {
    performOperation(add, 10, 5);
    performOperation(subtract, 10, 5);
    return 0;
}
```

##### 6. 内联函数

内联函数使用 `inline` 关键字声明，编译器会尝试将函数的代码直接嵌入到调用处，从而减少函数调用的开销。


```c
#include <stdio.h>

// 内联函数声明
inline int square(int x) {
    return x * x;
}

int main() {
    int num = 4;
    printf("Square of %d = %d\n", num, square(num));
    return 0;
}
```

##### 7. 函数的作用域和生命周期

- **作用域**：函数在定义它的文件中可以被调用，除非函数声明在头文件中被引用。
- **生命周期**：函数在程序执行期间存在，函数调用完成后，局部变量的生命周期结束，但函数代码的生命周期直到程序结束。
#### 十. static关键字
用于控制变量和函数的生命周期和作用域。它可以用于局部变量、全局变量和函数。理解 static 的作用对于编写高效和可维护的代码非常重要。

| 作用       | 描述                                     | 示例                      |
|------------|------------------------------------------|---------------------------|
| **局部变量** | 生命周期从函数开始到程序结束，值在函数调用之间保持不变(局部变量值会保留) | `static int count = 0;`  |
| **全局变量** | 作用域限定在定义它的文件中，其他文件不可访问 | `static int globalVar = 10;` |
| **函数**   | 作用域限定在定义它的文件中，其他文件不可调用 | `static void helperFunction() {}` |
#### 十一. 字符串
字符串是由字符组成的数组，以空字符（'\0'）作为结束标志。C语言没有内建的字符串类型，字符串实际上是字符数组的特例。
- 字符串也可以进行指针加减运算,来获取字符串的任何字符

| 特性           | 描述                                     | 示例                       |
|----------------|------------------------------------------|----------------------------|
| **定义与初始化** | 使用字符数组或指针来定义和初始化字符串    | `char str[] = "Hello";`    |
| **基本操作**   | 使用标准库函数如 `strlen长度`、`strcpy复制`、`strcat拼接`、`strcmp比较` | `strlen(str)`            |
| **输入与输出** | 使用 `scanf` 和 `printf` 来处理字符串      | `scanf("%s", str);`       |
| **内存布局**   | 字符串在内存中是字符数组，以 `'\0'` 结尾  | `char str[] = "Hello";`   |
| **指针**       | 字符串可以通过字符指针来处理              | `const char *str = "Hello";` |
#### 十二. 结构体


在C语言中，结构体（`struct`）是一种用户定义的数据类型，用于将不同类型的数据组合在一起。结构体可以包含基本数据类型、数组、其他结构体或指针等各种类型的数据。

##### 1. 结构体的定义与声明
```c
#include <stdio.h>

// 定义结构体
struct Person {
    char name[50];
    int age;
    float height;
};

```
##### 2. 结构体的初始化

结构体可以在声明时进行初始化，也可以在程序运行时逐个赋值。

**示例：**

```c
#include <stdio.h>

int main() {
    // 声明并初始化结构体变量
    struct Person person1 = {"Bob", 25, 6.0};

    // 逐个赋值
    struct Person person2;
    person2.age = 40;
    person2.height = 5.8;
    // 使用 strcpy 复制字符串
    strcpy(person2.name, "Charlie");

    // 输出结构体成员
    printf("Person1 - Name: %s, Age: %d, Height: %.2f\n", person1.name, person1.age, person1.height);
    printf("Person2 - Name: %s, Age: %d, Height: %.2f\n", person2.name, person2.age, person2.height);

    return 0;
}
```

##### 3. 结构体的嵌套

结构体可以包含其他结构体作为成员，这称为结构体的嵌套。

```c
#include <stdio.h>

// 定义嵌套结构体
struct Date {
    int day;
    int month;
    int year;
};

struct Person {
    char name[50];
    int age;
    struct Date birthDate;
};

int main() {
    // 声明并初始化嵌套结构体变量
    struct Person person = {"David", 28, {15, 4, 1996}};

    // 输出嵌套结构体成员
    printf("Name: %s\n", person.name);
    printf("Age: %d\n", person.age);
    printf("Birth Date: %02d/%02d/%d\n", person.birthDate.day, person.birthDate.month, person.birthDate.year);

    return 0;
}
```
##### 4. 结构体指针

可以通过结构体指针来操作结构体，使用 `->` 操作符访问结构体的成员。


```c
#include <stdio.h>

// 定义结构体
struct Person {
    char name[50];
    int age;
    float height;
}别名;

int main() {
    // 声明并初始化结构体变量
    struct Person person = {"Eve", 22, 5.7};
    
    // 使用结构体指针
    struct Person *ptr = &person;
    
    // 通过指针访问结构体成员
    printf("Name: %s\n", ptr->name);
    printf("Age: %d\n", ptr->age);
    printf("Height: %.2f\n", ptr->height);

    return 0;
}
```

##### 5. 结构体的内存对齐

结构体的内存对齐可能会影响结构体的大小。编译器可能会添加填充字节以确保结构体的对齐要求。

```c
#include <stdio.h>

struct Example {
    char c;
    int i;
    float f;
};

int main() {
    printf("Size of struct Example: %lu\n", sizeof(struct Example));
    return 0;
}
```

##### 6. 结构体的传递

结构体可以作为函数参数传递，支持按值传递和按引用传递（通过指针）。

```c
#include <stdio.h>

// 定义结构体
struct Person {
    char name[50];
    int age;
};

// 函数接收结构体作为参数
void printPerson(struct Person p) {
    printf("Name: %s, Age: %d\n", p.name, p.age);
}

int main() {
    struct Person person = {"Frank", 35};
    printPerson(person); // 通过值传递

    return 0;
}
```
##### 7. typedef 的基本用法
用于创建别名,typedef 常用于简化复杂的类型声明，尤其是在结构体、指针和函数指针等方面。

| 用法                | 描述                          | 示例                                    |
|---------------------|-------------------------------|-----------------------------------------|
| **简单类型别名**    | 为基本数据类型创建别名        | `typedef unsigned long ulong;`          |
| **结构体类型别名**  | 为结构体创建别名              | `typedef struct { ... } Person;`        |
| **指针类型别名**    | 为指针类型创建别名            | `typedef int* IntPtr;`                  |
| **函数指针类型别名**| 为函数指针创建别名            | `typedef void (*FuncPtr)(int);`         |
#### 十三. 共用体(union)
共用体（union）是一种特殊的数据结构，它允许在同一内存位置上存储不同的数据类型。共用体中的所有成员共享相同的内存空间，因此同一时间只能存储一个成员的值。

| 用法               | 描述                                | 示例                                    |
|--------------------|-------------------------------------|-----------------------------------------|
| **定义和声明**     | 定义共用体并声明变量                | `union Data { int intValue; ... };`     |
| **存储不同类型数据** | 使用共用体存储不同类型的数据        | `data.intValue = 10;`                  |
| **共用体与结构体** | 共用体的内存与结构体的不同           | `sizeof(struct)`, `sizeof(union)`     |

#### 十四. 枚举(enum)
枚举（enum）是一种用户定义的数据类型，它允许将一组常量定义为一个类型，以提高代码的可读性和可维护
1. 定义与使用
```c
#include <stdio.h>

// 定义枚举类型
enum Weekday {
    SUNDAY,    // 默认值为 0
    MONDAY,    // 默认值为 1
    TUESDAY,   // 默认值为 2
    WEDNESDAY, // 默认值为 3
    THURSDAY,  // 默认值为 4
    FRIDAY,    // 默认值为 5
    SATURDAY   // 默认值为 6
};

int main() {
    // 使用枚举类型
    enum Weekday today;

    today = WEDNESDAY;

    printf("Day %d\n", today); // 输出: Day 3

    return 0;
}
```


| 用法                     | 描述                              | 示例                                      |
|--------------------------|-----------------------------------|-------------------------------------------|
| **定义枚举类型**         | 定义枚举类型和枚举常量            | `enum Weekday { SUNDAY, MONDAY, ... };`   |
| **指定枚举常量的值**     | 手动指定枚举常量的整数值          | `enum Status { OK = 200, ... };`          |
| **枚举的内存大小**       | 查询枚举类型的内存大小            | `sizeof(enum Color);`                    |
| **枚举类型的转换**       | 将枚举值转换为整数或整数转换为枚举值 | `int monthNum = (int)month;`            |


#### 十五. 头文件
在 C 语言中，头文件（`header files`）用于声明函数、宏、常量和数据类型等，使得在多个源文件中可以共享这些声明。头文件通常具有 `.h` 扩展名，并通过 `#include` 指令被包含在源文件中。这样可以避免代码重复，并使程序结构更加清晰。


##### - 创建和包含头文件

**示例：**

**`example.h`（头文件）**

```c
#ifndef EXAMPLE_H
#define EXAMPLE_H

// 宏定义
#define PI 3.14159

// 函数声明
void printHello(void);
int add(int a, int b);

// 数据类型声明
typedef struct {
    int x;
    int y;
} Point;

#endif // EXAMPLE_H
```

**`main.c`（源文件）**

```c
#include <stdio.h>
#include "example.h" // 包含自定义头文件

// 函数定义
void printHello(void) {
    printf("Hello, World!\n");
}

int add(int a, int b) {
    return a + b;
}

int main() {
    printHello();

    Point p = {10, 20};
    printf("Point: (%d, %d)\n", p.x, p.y);

    int result = add(5, 7);
    printf("Sum: %d\n", result);

    return 0;
}
```

##### - 头文件保护

为了避免头文件被多次包含导致的编译错误，使用预处理指令 `#ifndef`、`#define` 和 `#endif` 来进行头文件保护。

**示例：**

```c
#ifndef MY_HEADER_H
#define MY_HEADER_H

// 头文件内容

#endif // MY_HEADER_H
```

##### - 标准库头文件

标准库头文件提供了 C 标准库函数和宏的声明。常见的标准库头文件包括：

| 头文件      | 描述                                    |
|-------------|-----------------------------------------|
| `<stdio.h>` | 标准输入输出函数，如 `printf`、`scanf`  |
| `<stdlib.h>`| 标准库函数，如动态内存管理、程序退出等  |
| `<string.h>`| 字符串处理函数，如 `strlen`、`strcpy`   |
| `<math.h>`  | 数学函数，如 `sqrt`、`sin`、`cos`       |
| `<ctype.h>` | 字符处理函数，如 `isdigit`、`isalpha`   |
| `<time.h>`  | 时间和日期函数，如 `time`、`clock`     |

##### - 自定义头文件

自定义头文件用于声明项目中特定的函数、数据结构和常量。自定义头文件一般包括函数声明、宏定义和数据结构声明。

**示例：**

**`math_utils.h`**

```c
#ifndef MATH_UTILS_H
#define MATH_UTILS_H

// 函数声明
int factorial(int n);
double power(double base, int exponent);

#endif // MATH_UTILS_H
```

**`math_utils.c`**

```c
#include "math_utils.h"

// 函数定义
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

double power(double base, int exponent) {
    double result = 1.0;
    for (int i = 0; i < exponent; i++) {
        result *= base;
    }
    return result;
}
```

- 总结

| 用法                   | 描述                              | 示例                                          |
|------------------------|-----------------------------------|-----------------------------------------------|
| **创建和包含头文件**   | 定义和包含头文件                  | `#include "example.h"`                       |
| **头文件保护**         | 避免头文件多次包含导致的编译错误   | `#ifndef MY_HEADER_H ... #endif`             |
| **标准库头文件**       | 提供标准库函数和宏的声明          | `<stdio.h>`, `<stdlib.h>`, `<string.h>`     |
| **自定义头文件**       | 声明项目中特定的函数、数据结构等  | `#include "math_utils.h"`                    |

头文件在 C 语言中用于组织和共享代码，通过适当地定义和使用头文件，可以提高代码的模块化和可维护性。
