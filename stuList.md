```c
/*
假如有一个学生表，每个学生包含学号、姓名和分 数。你如何设计相应的学生顺序表？ 如果需要对该学生表进行插入、修改和删除运算， 你如何实现相关算法？
用c语言实现
*/
#define MAX_SIZE 100  // 最大学生数量

// 学生结构体
typedef struct {
    int id;          // 学号
    char name[50];   // 姓名
    float score;     // 分数
} Student;

// 顺序表
typedef struct {
    Student data[MAX_SIZE];  // 存储学生的数组
    int length;                // 当前学生数量
} StudentList;

// 初始化学生顺序表
void initList(StudentList *list) {
    list->length = 0;
}
```