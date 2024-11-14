#include <stdio.h>
#include <stdlib.h>

// 定义树二叉树节点类型
typedef struct Tree_t {
    int data;                      // 节点数据
    struct Tree_t *Lchild;         // 左子树指针
    struct Tree_t *Rchild;         // 右子树指针
} BiTree_t;

// 插入节点函数
void insert(BiTree_t** tree, int gain) {
    BiTree_t* temp = NULL;
    
    // 判断当前树是否为空（如果为空则插入根节点）
    if (!(*tree)) {
        // 分配新节点内存并初始化
        temp = (BiTree_t*)malloc(sizeof(BiTree_t));
        temp->Lchild = temp->Rchild = NULL; // 初始化左右子树为空
        temp->data = gain;                  // 设置节点数据
        *tree = temp;                       // 赋值给根节点
        return;
    }

    // 如果插入数据小于当前节点数据，插入到左子树
    if (gain < (*tree)->data) {
        insert(&(*tree)->Lchild, gain); // 递归插入左子树
    }
    // 如果插入数据大于当前节点数据，插入到右子树
    else if (gain > (*tree)->data) {
        insert(&(*tree)->Rchild, gain); // 递归插入右子树
    }
    // 如果插入数据等于当前节点数据，不进行任何操作（可选）
}

// 前序遍历函数：先访问根节点，再遍历左子树，最后遍历右子树
void PreShowBitree(BiTree_t *r) {
    if (r == NULL) { // 如果节点为空则返回
        return;
    }
    printf(" %d ", r->data);       // 访问根节点
    PreShowBitree(r->Lchild);      // 递归遍历左子树
    PreShowBitree(r->Rchild);      // 递归遍历右子树
}

// 中序遍历函数：先遍历左子树，再访问根节点，最后遍历右子树
void midShowBitree(BiTree_t *r) {
    if (r == NULL) { // 如果节点为空则返回
        return;
    }
    midShowBitree(r->Lchild);      // 递归遍历左子树
    printf(" %d ", r->data);       // 访问根节点
    midShowBitree(r->Rchild);      // 递归遍历右子树
}

// 后序遍历函数：先遍历左子树，再遍历右子树，最后访问根节点
void PostShowBitree(BiTree_t *r) {
    if (r == NULL) { // 如果节点为空则返回
        return;
    }
    PostShowBitree(r->Lchild);     // 递归遍历左子树
    PostShowBitree(r->Rchild);     // 递归遍历右子树
    printf(" %d ", r->data);       // 访问根节点
}

// 删除二叉树（释放所有节点内存）
void deltree(BiTree_t* tree) {
    if (tree) {
        deltree(tree->Lchild);     // 递归删除左子树
        deltree(tree->Rchild);     // 递归删除右子树
        free(tree);                // 释放当前节点
    }
}

// 主函数
int main() {
    /*
        50
       /  \
     30    70
    / \    / \
   20 40  60 80

    */
    BiTree_t* root = NULL; // 初始化根节点为空

    // 插入节点数据
    int arr[] = {50, 30, 20, 40, 70, 60, 80};
    int n = sizeof(arr) / sizeof(arr[0]);
    for (int i = 0; i < n; i++) {
        insert(&root, arr[i]);
    }
    

    // 前序遍历
    printf("前序遍历: ");
    PreShowBitree(root);
    printf("\n");

    // 中序遍历
    printf("中序遍历: ");
    midShowBitree(root);
    printf("\n");

    // 后序遍历
    printf("后序遍历: ");
    PostShowBitree(root);
    printf("\n");

    // 删除二叉树
    deltree(root);
    root = NULL; // 删除后将根节点指针置空
    printf("二叉树已删除。\n");

    return 0;
}
