// Character Queue ADO header file
#define MAXITEMS 10

void QueueInit();        // set up empty queue
int  QueueIsEmpty();     // check whether queue is empty
void QueueEnqueue(char); // insert char at end of queue
char QueueDequeue();     // remove char from front of queue
