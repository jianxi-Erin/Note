#include <stdio.h>

// 冒泡排序函数
void Bubble_sort(int arr[], int size)
{
    int j, i, temp;
    for (i = 0; i < size - 1; i++)
    {                  // size-1是因为不用与自己比较，所以比较的次数减少一个
        int count = 0; // 标记本轮是否有交换
        for (j = 0; j < size - 1 - i; j++)
        { // 每轮比较的范围逐渐缩小
            if (arr[j] > arr[j + 1])
            { // 升序排序，前后两个数比较
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                count = 1; // 标记发生了交换
            }
        }
        if (count == 0) // 如果某一轮没有发生交换，说明已经排序完成
            break;
    }
}

// 二分查找函数
int BinSearch(int arr[], int len, int key)
{
    int low = 0;        // 定义初始下界
    int high = len - 1; // 定义初始上界
    int mid;            // 定义中间值
    while (low <= high)
    {                           // 继续查找直到上下界相交
        mid = (low + high) / 2; // 计算中间索引
        if (key == arr[mid])    // 如果找到目标值
            return mid;
        else if (key > arr[mid]) // 如果目标值大于中间值，调整下界
            low = mid + 1;
        else // 如果目标值小于中间值，调整上界
            high = mid - 1;
    }
    return -1; // 如果未找到目标值
}

int main(int argc, char const *argv[])
{
    int rr[] = {3, 2, 1, 4, 5, 6, 8, 9, 7, 10, 11}; // 初始数组
    int size = sizeof(rr) / sizeof(rr[0]);          // 计算数组大小

    // 对数组进行冒泡排序
    Bubble_sort(rr, size);

    // 打印排序后的数组
    printf("排序后的数组: ");
    for (int i = 0; i < size; i++)
    {
        printf("%d ", rr[i]);
    }
    printf("\n");

    printf("输入查询的数字:");
    int key;
    scanf("%d", &key);

    // 在排序后的数组中查找目标值
    int result = BinSearch(rr, size, key);

    // 输出查找结果
    if (result != -1)
    {
        printf("数字 %d 在数组中的位置是: %d\n", key, result);
    }
    else
    {
        printf("数字 %d 不在数组中。\n", key);
    }

    return 0;
}
