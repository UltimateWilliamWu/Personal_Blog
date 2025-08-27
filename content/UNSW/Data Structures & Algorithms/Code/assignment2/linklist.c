#include <stdio.h>
#include <stdlib.h>

// 定义链表结点结构
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// 创建新结点
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// 头插法插入新结点
void insertAtHead(Node** head, int data) {
    Node* newNode = createNode(data);
    newNode->next = *head; // 新结点的next指向当前头结点
    *head = newNode;       // 更新头指针
}

// 打印链表
void printList(Node* head) {
    while (head != NULL) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

// 主函数测试
int main() {
    Node* head = NULL; // 初始化空链表

    insertAtHead(&head, 10);
    insertAtHead(&head, 20);
    insertAtHead(&head, 30);

    printf("链表内容：");
    printList(head);

    return 0;
}
