def find_numbers(result_list):
    # 遍历从2000到3200的所有数字
    for num in range(2000, 3201):
        # 判断数字是否可被7整除且不是5的倍数
        if num % 7 == 0 and num % 5!= 0:
            # 将符合条件的数字转换为字符串后添加到列表中
            result_list.append(str(num))
    return result_list

# 在函数外部创建一个空列表，用于存储符合条件的数字
result_list = []
# 调用函数，将空列表传入，函数会将符合条件的数字填充到列表中
result = find_numbers(result_list)
# 使用join方法将列表中的字符串元素用逗号连接起来，并打印输出
print(",".join(result))