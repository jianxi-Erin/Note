#include <stdio.h>      // 引入标准输入输出库
#include <stdlib.h>     // 引入动态内存分配函数库

#define ID_LENGTH 10    // 学生ID长度
#define NAME_LENGTH 50  // 学生姓名长度

// 学生信息结构体
typedef struct Student {
    unsigned char ID[ID_LENGTH];  // 学生ID，长度为ID_LENGTH
    unsigned char Name[NAME_LENGTH];  // 学生姓名，长度为NAME_LENGTH
    int Score;  // 学生成绩
} Stu;

// 链表节点结构体
typedef struct LNode {
    Stu data;  // 存储学生信息
    struct LNode *next;  // 指向下一个节点
} ListNode;

// 链表类型
typedef ListNode* Linklist;

// 返回值类型，用于操作状态
typedef enum {
    OK = 0,    // 操作成功
    ERROR1 = 1 // 操作失败
} Result_Status;

// 创建一个空链表
Linklist List_Create(void) {
    ListNode *L = NULL;
    L = (ListNode *)malloc(sizeof(ListNode));  // 动态分配内存
    if (L == NULL) {  // 检查内存分配是否成功
        printf("内存分配失败\n");
        return NULL;
    }
    L->next = NULL;  // 初始化链表为空
    return L;
}

// 插入学生信息到链表
Result_Status ListInsert_L(Linklist L, int Pos, Stu e) {
    Linklist p;
    int j = 0;
    ListNode *L_temp = NULL;
    p = L;

    // 动态分配内存给新节点
    L_temp = (ListNode *)malloc(sizeof(ListNode));
    if (L_temp == NULL) {
        printf("内存分配失败\n");
        return ERROR1;
    }
    L_temp->next = NULL;

    // 查找插入位置
    while (p && (j < (Pos - 1))) {
        p = p->next;
        ++j;
    }
    if (j < (Pos - 1)) {  // 如果位置无效，返回错误
        printf("插入位置超出范围\n");
        free(L_temp);  // 释放内存
        return ERROR1;
    } else {
        // 复制学生信息到新节点
        for (int i = 0; i < ID_LENGTH; i++) {
            L_temp->data.ID[i] = e.ID[i];
        }
        for (int i = 0; i < NAME_LENGTH; i++) {
            L_temp->data.Name[i] = e.Name[i];
        }
        L_temp->data.Score = e.Score;
    }

    // 插入新节点
    L_temp->next = p->next;
    p->next = L_temp;

    return OK;
}

// 删除指定位置的学生信息
Result_Status ListDelete_L(Linklist L, int Pos) {
    Linklist p, s;
    int j = 0;
    p = L;

    // 查找待删除节点的前一个节点
    while (p && (j < (Pos - 1))) {
        p = p->next;
        ++j;
    }
    if (j < (Pos - 1)) {  // 如果位置无效，返回错误
        printf("删除位置超出范围\n");
        return ERROR1;
    }

    // 删除节点
    s = p->next;
    p->next = p->next->next;
    free(s);  // 释放内存

    return OK;
}

// 打印所有学生信息
Result_Status ListPrint_L(Linklist L) {
    int i = 0, j = 0;
    Linklist p;

    if (L == NULL || L->next == NULL) {  // 检查链表是否为空
        printf("链表为空\n");
        return ERROR1;
    }

    p = L->next;  // 跳过头节点
    printf("学生信息链表内容如下:\n");

    while (p) {
        printf("序号%d ", j + 1);
        j++;

        // 打印ID
        printf("ID:");
        i = 0;
        while (p->data.ID[i]) {
            printf("%c", p->data.ID[i]);
            i++;
        }

        // 打印Name
        printf(" Name:");
        i = 0;
        while (p->data.Name[i]) {
            printf(" %c", p->data.Name[i]);
            i++;
        }

        // 打印Score
        printf(" score:%d\n", p->data.Score);

        // 移动到下一个节点
        p = p->next;
    }
    return OK;
}

// 主函数，测试链表操作
int main() {
    
    Linklist L;
    Stu s1 = { "1001", "zhangsan", 85 };
    Stu s2 = { "1002", "lisi", 90 };
    Stu s3 = { "1003", "wangwu", 78 };
    
    // 创建空链表
    L = List_Create();
    if (L == NULL) {
        return -1;  // 内存分配失败
    }

    // 插入学生信息
    ListInsert_L(L, 1, s1);
    ListInsert_L(L, 2, s2);
    ListInsert_L(L, 3, s3);

    // 打印学生信息
    ListPrint_L(L);

    // 删除第二个学生
    ListDelete_L(L, 2);

    // 打印删除后的链表
    printf("删除第二个学生后的链表:\n");
    ListPrint_L(L);

    return 0;
}
