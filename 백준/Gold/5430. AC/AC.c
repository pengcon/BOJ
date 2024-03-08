#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int max;
    int num;
    int front;
    int rear;
    int *que;
} Deck;

int Initialize(Deck *d, int max) {
    
    d->front = d->rear = d->num = 0;
    
    if((d->que = calloc(max, sizeof(int))) == NULL) {
        d->max = 0;
        return -1;
    }
    
    d->max = max;
    return 0;
}


int EnqueFront(Deck *d, int v) {
    
    if(d->num >= d->max)
        return -1;
    
    
    d->num++;
    if(--d->front < 0)
        d->front = d->max - 1;
    
    d->que[d->front] = v;
    return 0;
    
}

int EnqueRear(Deck *d, int v) {
    
    if(d->num >= d->max)
        return -1;
    
    d->num++;
    d->que[d->rear++]= v;
    
    d->rear = d->rear % d->max;
    return 0;
}

int DequeFront(Deck *d, int *v) {
    if(d->num <= 0)
        return -1;
    
    d->num--;
    *v = d->que[d->front++];
    
    d->front = d->front % d->max;
    return 0;
    
}

int DequeRear(Deck *d, int *v) {
    if(d->num <= 0)
        return -1;
    
    d->num--;
    
    if(--d->rear < 0)
        d->rear = d->max - 1;
    
    *v = d->que[d->rear];
    return 0;
}


void Clear(Deck *d) {
    d->num = d->front = d->rear = 0;
}

int Size(Deck *d) {
    return d->num;
}

int IsEmpty(Deck *d) {
    return (d->num <= 0);
}

int PeekFront(Deck *d, int *v) {
    
    if(d->num <= 0)
        return -1;
    
    *v = d->que[d->front];
    return 0;
    
    
}

int PeekRear(Deck *d, int *v) {
    
    if(d->num <= 0)
        return -1;
    
    int temp = d->rear - 1;
    if(temp < 0)
        temp = d->max - 1;
    *v = d->que[temp];
    return 0;
    
}

void Print_Front(Deck *d) {
    
    printf("[");
    for(int i = 0; i < d->num; i++) {
        
        printf("%d", d->que[(i + d->front) % d->max]);
        if(i != d->num - 1)
            printf(",");
    }
    printf("]\n");
    
}

void Print_Rear(Deck *d) {
    
    int temp;
    
    printf("[");
    for(int i = 0; i < d->num; i++) {
        
        if((temp = d->rear - 1 - i) < 0)
            temp = d->max - 1;
        
        printf("%d", d->que[temp]);
        if(i != d->num - 1)
            printf(",");
    }
    printf("]\n");
    
}


int T, N;
char com[400001];
int temp;

int SWAP = 0; // 리버스 체킹.
int r = 0; // Deque의 결과를 받기 위해

char c; // 문자들을 단순히 버리기 위함.

int main() {
    Deck deck;

    Initialize(&deck, 100000);
    
    scanf("%d", &T);
    
    while(T--) {
        // 입력 포맷에 문제가 있었다..
        Clear(&deck);
        SWAP = 0;
        r = 0;
        
        scanf("%s", com);
        
        scanf("%d", &N);
        getchar(); // N 다음 엔터값을 비우기 위함.
        
        
        // 입력 포맷에 문제가 있었던 핵심은
        // 숫자가 0개일 때 []
        // 숫자가 하나일 때, [1]
        // 숫자가 하나 이상일 때, [1,2] 같은 경우에 대해 포맷을 고려해줬어야했는데
        // 숫자가 0개일 때에는 고려하지 않았다 보니 입력 버퍼에 문제가 생겨서 매 테스트케이스마다 입력이 제대로 이루어지지 않음.
        // + fflush(stdin) 은 정식방법이 아님. fflush는 출력 버퍼를 위한 것.
        if(N != 0 ) {
            scanf("%c", &c); // [ 버림
            for(int i = 0; i < N; i++) {
                scanf("%d", &temp); // 숫자 받음
                getchar(); // , 이나 ] 버림
                
                EnqueRear(&deck, temp);
            }
        } else // 입력이 없을 때 = [] 일 경우를 받아내야 한다.
            scanf("%c %c", &c, &c);
        
        for(int i = 0; ; i++) {
            
            if(com[i] == 'R')
                SWAP = !SWAP;
            
            else if(com[i] == 'D') {
                r = ((SWAP == 0)?DequeFront(&deck, &temp):DequeRear(&deck, &temp));
            }
            else if(com[i] == '\0')
                break;
        }
        if(r == -1)
            printf("error\n");
        else
            (SWAP == 0)?Print_Front(&deck):Print_Rear(&deck);

    }
    

}