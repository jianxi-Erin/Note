#include <stdio.h>
#include <stdlib.h>

typedef int InfoType;
#define MAXV 100 /* 最大顶点数 */

/* 顶点类型定义 */
typedef struct
{
    int no;        /* 顶点编号 */
    InfoType info; /* 顶点附加信息 */
} VertexType;

/* 邻接矩阵类型定义 */
typedef struct
{
    int edges[MAXV][MAXV]; /* 邻接矩阵 */
    int n, e;              /* 顶点数和边数 */
    VertexType vexs[MAXV]; /* 顶点信息 */
} MGraph;

/* 弧结点结构类型 */
typedef struct ANode
{
    int adjvex;            /* 弧的终点编号 */
    struct ANode *nextarc; /* 指向下一条弧的指针 */
    InfoType info;         /* 弧的权值 */
} ArcNode;

/* 邻接表头结点类型 */
typedef struct Vnode
{
    int data;         /* 顶点编号 */
    int count;        /* 顶点入度，仅在拓扑排序中使用 */
    ArcNode *firstarc; /* 指向第一条弧 */
} VNode;

/* 邻接表类型 */
typedef VNode AdjList[MAXV];
typedef struct
{
    AdjList adjlist; /* 邻接表 */
    int n, e;        /* 顶点数和边数 */
} ALGraph;

/* 将邻接矩阵转换为邻接表 */
void MatToList(MGraph g, ALGraph **G)
{
    int i, j, n = g.n; /* 获取顶点数 */
    ArcNode *p;

    /* 为邻接表分配内存 */
    *G = (ALGraph *)malloc(sizeof(ALGraph));
    for (i = 0; i < n; i++)
        (*G)->adjlist[i].firstarc = NULL; /* 初始化邻接表指针域 */

    /* 遍历邻接矩阵，将非零元素转换为弧结点 */
    for (i = 0; i < n; i++)
        for (j = n - 1; j >= 0; j--)
            if (g.edges[i][j] != 0) /* 若邻接矩阵中存在边 */
            {
                p = (ArcNode *)malloc(sizeof(ArcNode)); /* 创建弧结点 */
                p->adjvex = j;                          /* 设置终点编号 */
                p->info = g.edges[i][j];                /* 设置权值 */
                p->nextarc = (*G)->adjlist[i].firstarc; /* 头插法插入链表 */
                (*G)->adjlist[i].firstarc = p;          /* 更新头指针 */
            }

    /* 设置顶点数和边数 */
    (*G)->n = n;
    (*G)->e = g.e;
}

/* 将邻接表转换为邻接矩阵 */
void ListToMat(ALGraph *G, MGraph *g)
{
    int i, n = G->n;
    ArcNode *p;

    /* 初始化邻接矩阵为0 */
    for (i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            g->edges[i][j] = 0;

    /* 遍历邻接表，将结点信息转换为邻接矩阵元素 */
    for (i = 0; i < n; i++)
    {
        p = G->adjlist[i].firstarc; /* 获取顶点的第一条弧 */
        while (p != NULL)
        {
            g->edges[i][p->adjvex] = p->info; /* 设置矩阵权值 */
            p = p->nextarc;                   /* 移动到下一条弧 */
        }
    }

    /* 设置顶点数和边数 */
    g->n = n;
    g->e = G->e;
}

/* 打印邻接表 */
void PrintAdjList(ALGraph *G)
{
    printf("\nAdjacency List:\n");
    for (int i = 0; i < G->n; i++)
    {
        printf("Vertex %d: ", i);
        ArcNode *p = G->adjlist[i].firstarc;
        while (p)
        {
            printf("-> [%d|Weight:%d] ", p->adjvex, p->info);
            p = p->nextarc;
        }
        printf("\n");
    }
}

/* 打印邻接矩阵 */
void PrintAdjMatrix(MGraph *g)
{
    printf("\nAdjacency Matrix:\n   ");
    /* 打印列顶点编号 */
    for (int j = 0; j < g->n; j++)
        printf("%4d", j);
    printf("\n");

    /* 打印矩阵内容及行顶点编号 */
    for (int i = 0; i < g->n; i++)
    {
        printf("%2d", i); /* 行顶点编号 */
        for (int j = 0; j < g->n; j++)
            printf("%4d", g->edges[i][j]);
        printf("\n");
    }
}

int main()
{
    MGraph g;
    ALGraph *G;

    /* 输入顶点数和边数 */
    printf("Enter the number of vertices and edges: ");
    scanf("%d%d", &g.n, &g.e);

    /* 初始化邻接矩阵 */
    for (int i = 0; i < g.n; i++)
        for (int j = 0; j < g.n; j++)
            g.edges[i][j] = 0;

    /* 输入边及权值 */
    printf("Enter the start vertex, end vertex, and weight of each edge (Format: start end weight):\n");
    for (int i = 0; i < g.e; i++)
    {
        int u, v, w;
        scanf("%d%d%d", &u, &v, &w);
        g.edges[u][v] = w; /* 设置邻接矩阵权值 */
    }

    /* 打印输入的邻接矩阵 */
    PrintAdjMatrix(&g);

    /* 转换为邻接表并打印 */
    MatToList(g, &G);
    PrintAdjList(G);

    /* 转换回邻接矩阵并打印 */
    MGraph g2;
    ListToMat(G, &g2);
    PrintAdjMatrix(&g2);

    /* 释放邻接表的内存 */
    for (int i = 0; i < G->n; i++)
    {
        ArcNode *p = G->adjlist[i].firstarc;
        while (p)
        {
            ArcNode *temp = p;
            p = p->nextarc;
            free(temp);
        }
    }
    free(G);

    return 0;
}
