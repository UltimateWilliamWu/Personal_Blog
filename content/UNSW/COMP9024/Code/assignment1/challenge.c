#include <stdio.h>

// 检查数字是否包含数字9
int contains_nine(int number) {
    while (number > 0) {
        if (number % 10 == 9) {
            return 1; // 包含数字9
        }
        number /= 10;
    }
    return 0; // 不包含数字9
}

int main(void) {
    // 遍历所有5位数
    for (int num1 = 10000; num1 < 100000; num1++) {
        if (contains_nine(num1)) continue; // 跳过包含9的5位数

        // 遍历所有3位数
        for (int num2 = 100; num2 < 1000; num2++) {
            if (contains_nine(num2)) continue; // 跳过包含9的3位数

            // 检查是否符合初始条件：num1能被num2整除
            if (num1 % num2 == 0) {
                int result1 = num1 / num2;

                // 递增后的数字
                int num1_inc = num1 + 11111;
                int num2_inc = num2 + 111;

                // 检查递增后的条件
                if (!contains_nine(num1_inc) && !contains_nine(num2_inc) &&
                    num1_inc % num2_inc == 0) {
                    // 检查结果的差值是否为100
                    if (num1_inc/num2_inc-num1/num2== 100|| (num1 / num2 - num1_inc / num2_inc == 100)) {
                        // 输出结果
                        printf("5-digit number: %d, 3-digit number: %d\\n", num1, num2);
                        return 0; // 找到答案后退出程序
                    }
                }
            }
        }
    }

    // 如果没有找到符合条件的结果
    printf("No solution found.\n");
    return 0;
}
