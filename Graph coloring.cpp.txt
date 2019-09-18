#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <sys/time.h>
#define random(number) rand()%number+1
#define Max 10001

int Twotier(int N)
{
    int i;
    int randomseed=90;
    if(random(randomseed)<=40){
        return random(N/10);
    }
    else return random(N);
}

int Skewed(int N)
{
    int i;
    int count=0;
    int *a;
    int *flag;
    int p=0;
    a = (int*)malloc((N*N+N)*sizeof(int));
    flag = (int*)malloc(N*sizeof(int));
    flag[0]=2*N-1;
    for(i=1;i<N;i++)
        flag[i]=0;
    for(i=1;i<N;i++){
        flag[i]=flag[i-1]+2*N-2*i;
        //printf("%d,",flag[i]);
    }
    for(i=0;i<N*N+N;i++){
        a[i]=count;
        if(i>=flag[p])
        {
            count++;
            p++;
        }
    }
    return a[random(N*N+N)]+1;
}

int Mydistribution(int N)
{
    int i;
    int randomseed=100;
    if(random(randomseed)<=80){
        return random(N/2);
    }
    else return random(N);
}

int FindSmallestDegree(int **DegreeList,int N)
{
    int j,i,findflag=0;
    for(j=2;j<=N;j++){
        for(i=0;i<=N;i++){
            if(DegreeList[j][i]!=0&&DegreeList[j][i]!=-1){
                //printf("%d ",DegreeList[j][i]);
                findflag++;
            }
            if(findflag==1)
                break;
        }
        if(findflag==1)
                break;
    }
    return DegreeList[j][i];
}

int FindBiggestDegree(int **DegreeList,int N)
{
    int j,i,findflag=0;
    for(j=N;j>=2;j--){
        for(i=0;i<=N;i++){
            if(DegreeList[j][i]!=0&&DegreeList[j][i]!=-1){
                //printf("%d ",DegreeList[j][i]);
                findflag++;
            }
            if(findflag==1)
                break;
        }
        if(findflag==1)
                break;
    }
    return j-1;
}

void ChangeDegreeList(int N,int value,int **DegreeList,int M,int *Method1Order,int M1Count,int *degree,int value2)
{
    int i,j,count=0,lastcount=0;
    for(j=2;j<=N;j++){
        for(i=0;i<=N;i++){
            if(DegreeList[j][i]==M)
            {
                DegreeList[j][i]=-1;
                printf("Vertice to be deleted : %d \n",M);
                printf("degree when deleted : %d \n",j-1);
                printf("Maximum Degree when deleted : %d \n", value2);
            }
            if(DegreeList[j][i]!=0)
            {
                count++;
            }
            if(DegreeList[j][i]==value){
                DegreeList[j][i]=-1;
                DegreeList[j-1][lastcount]=value;
                if((j-1)==1){
                    Method1Order[M1Count]=value;
                    printf("degree when deleted : %d \n",degree[value]);
                    printf("Maximum Degree when deleted : %d \n", value2);
                }
                //printf("%d\n",value);
            }
        }
        lastcount = count;
        count = 0;
    }
}

int ExistInM3(int N,int *Method3Order,int value)
{
    int i = 1;
    for(i=1;i<=N;i++){
        if(Method3Order[i]==value)
            return 1;
    }
    return 0;

}

void Coloring(int *Color,int *Order,int **VerticeList,int N)
{
    int i=1,j=1,flag=0;
    for(i=1;i<=N;i++)
        Color[Order[i]]=1;
    i=1;
    for(j=2;j<=N;j++){
        for(i=1;i<=N;i++){
            if(Color[Order[j]]==Color[VerticeList[Order[j]][i]]&&VerticeList[Order[j]][i]!=0){
                Color[Order[j]]++;
                flag=1;
            }
        }
        if(flag==1){
            j--;
            flag=0;
        }
    }
    printf("\n");
}

float AverageDegree(int *degree, int N)
{
    int i=1,sum=0;
    for(i=1;i<=N;i++)
        sum+=degree[i];
    return (float)sum/N;
}

int ColorUsed(int *Color,int N)
{
    int i=1,maxcolor=0;
    for(i=1;i<=N;i++){
        if(Color[i]>maxcolor)
            maxcolor=Color[i];
    }
    return maxcolor;
}

/*int main()
{
        FILE *fpWrite=NULL;
    int i,j,temp;
    int a[101]={0};
    fpWrite=fopen("I:\\data.txt","w");
    for(i=0;i<10000;i++){
        temp = Mydistribution(100);
        for(j=1;j<=100;j++)
            if(temp ==j)
                a[j]++;
        //printf("%d,", temp);
    }
    for(j=1;j<=100;j++)
       fprintf(fpWrite,"%d\n",a[j]);
    fclose(fpWrite);

}
*/

int main()
{
    struct timeval start;
    struct timeval end;
    unsigned long timer;

    srand(time(0));

    int Color1[10001]={0};
    int Color2[10001]={0};
    int Color3[10001]={0};

    int M1Count = 1;
    int ReverseCount;

    int Method1Order[10001]={0};
    int ReverseM1[10001]={0};

    int Method2Order[10001]={0};

    int M3Count = 1;

    int Method3Order[10001]={0};

    int judge = 0;

    int degree[10000] = {0};

    int degreecount=0;

    int FinalCount=0;

    int value=0;

    int countf=0;

    int tempsmallest=0;

    int Choice=0;
    int sessioncount=0;
    int sessioncountk=0;
    int repeatflag = 0;
    int temp;
    int i=0,j=0,m=0;
    int countm=0;
    int N;
    int S;
    int K;
    int ** VerticeList;
    int ** Sarray;
    int ** Earray;
    int ** DegreeList;
    int Karray[100000] = {0};/*100,000*/
    char DIST[10];
    int M;
    int T;
    int E[100000]={0};
    int P[100000]={0};
    int pflag=0;
    int phavevalue=0;
    printf("Type N Number of session (MAX = 10,000) :");
    scanf("%d",&N);
    Sarray =(int**)malloc(Max*sizeof(int*));
    for(i=0;i<Max;i++){
        Sarray[i]=(int*)malloc(Max*sizeof(int));
    }
    for(i=0;i<Max;i++){
        for(j=0;j<Max;j++){
            Sarray[i][j]=0;
        }
    }

    i=0,j=0;
    Earray =(int**)malloc(Max*sizeof(int*));
    for(i=0;i<Max;i++){
        Earray[i]=(int*)malloc(Max*sizeof(int));
    }
    for(i=0;i<Max;i++){
        for(j=0;j<Max;j++){
            Earray[i][j]=0;
        }
    }

    i=0,j=0;
    VerticeList =(int**)malloc(Max*sizeof(int*));
    for(i=0;i<Max;i++){
        VerticeList[i]=(int*)malloc(Max*sizeof(int));
    }
    for(i=0;i<Max;i++){
        for(j=0;j<Max;j++){
            VerticeList[i][j]=0;
        }
    }

    for(i=1;i<=N;i++)
        Method2Order[i]=i;

    i=0,j=0;
    DegreeList =(int**)malloc(Max*sizeof(int*));
    for(i=0;i<Max;i++){
        DegreeList[i]=(int*)malloc(Max*sizeof(int));
    }
    for(i=0;i<Max;i++){
        for(j=0;j<Max;j++){
            DegreeList[i][j]=0;
        }
    }

    i=0,j=0;
    printf("Type S Number of attendees (MAX = 100,000) :");
    scanf("%d",&S);
    printf("Type K Number of session per attendee(MAX = N for uniform and two-tiered distributions,\
MAX = 0.1N for skewed and self-defined distributions;) :");
    scanf("%d",&K);
    if(K>N){
        printf("K is too large.");
        return 0;
    }
    printf("Type DIST :");
    scanf("%s",&DIST);
    //printf("project : (1 for Project1, 2 for Project2)");
    //scanf("%d",&Choice);
    Choice = 2;

    gettimeofday(&start, NULL);

    while(sessioncount < S){
    while(i < K){
        if(strcmp(DIST,"UNIFORM")==0||strcmp(DIST,"1")==0)
            temp = random(N);//produce different distribution base on DIST.
        else if(strcmp(DIST,"TIERED")==0||strcmp(DIST,"2")==0)
            temp = Twotier(N);
        else if(strcmp(DIST,"SKEWED")==0||strcmp(DIST,"3")==0)
            temp = Skewed(N);
        else if(strcmp(DIST,"YOURS")==0||strcmp(DIST,"4")==0)
            temp = Mydistribution(N);
        else{
            printf("Distribution is invalid!");
            return 0;
        }
        for(j=0;j<i;j++){
            if(Karray[j] == temp){
                repeatflag = 1;
            }
        }
        if(repeatflag == 0){
            Karray[i++] = temp;
        }
        else
        {
            repeatflag = 0;
            continue;
        }
    }
    i=0;
    for(sessioncountk=0;sessioncountk<K;sessioncountk++)
        Sarray[sessioncount][sessioncountk] = Karray[sessioncountk];
    sessioncount++;
    }


/*Output"*/
    printf("\n--------------Belows are Outputs--------------\n");
    printf("N = %d\n",N);
    printf("T = %d\n",S * K * (K-1) / 2);
    printf("S = %d\n",S);
    printf("K = %d\n",K);
    printf("DIST = %s",DIST);

    for(j=0;j<S;j++)
        for(i=0;i<K-1;i++){
            for(m=i+1;m<K;m++){
                Earray[Sarray[j][i]][Sarray[j][m]]=1;
                Earray[Sarray[j][m]][Sarray[j][i]]=1;
            }
        }
    printf("\n");
    printf("Adjacent Matrix of Graph : \n");
    for(j=1;j<=N;j++)
        for(i=1;i<=N;i++){
            printf("%d ",Earray[j][i]);
            if(Earray[j][i]==1){
                E[countm]=i;
                countm++;
                phavevalue=1;
                degree[j]++; //new
            }
            if(i==N){
                printf("\n"); //printf("%d,%d",j,degree[j]);
                if(phavevalue==1){
                    P[++pflag]=countm;
                    phavevalue=0;
                }
            }
        }
    printf("M = %d\n",countm/2);
    for(i=0;i<countm;i++){
        if(i!= countm-1&&Choice==1)
            printf("E[%d] = %d ,",i,E[i]);
        if(i== countm-1&&Choice==1)
            printf("E[%d] = %d\n",i,E[i]);
    }
    for(i=0;i<pflag;i++){
        if(i!= pflag-1&&Choice==1)
            printf("P[%d] = %d ,",i,P[i]);
        if(i== pflag-1&&Choice==1)
            printf("P[%d] = %d\n",i,P[i]);
    }

    for(j=1;j<=N;j++){
        for(i=1;i<=N;i++){
            if(i == 1){
            printf("vertice %d ", j);
            }
            if(Earray[j][i]==1){
                    VerticeList[j][i]= i;
                printf("-> vertice %d",VerticeList[j][i]);
            }
            if(i==N)
                printf(" | vertex %d degree: %d \n",j,degree[j]);
        }
    }

    printf("Degree List below :\n");
    for(j=1;j<=N;j++){
        printf("degree %d : ", j-1);
        for(i=1;i<=N;i++){
            if(degree[i]==j-1){
                DegreeList[j][degreecount]=i;
                printf("%d ",DegreeList[j][degreecount]);
                if((j-1) == 0)
                {
                    Method1Order[M1Count++]=DegreeList[j][degreecount];
                }
                degreecount++;
            }
            if(i==N)
              printf("\n");
        }
         degreecount = 0;
    }

    printf("Degree List below :\n");
    for(j=2;j<=N;j++)
        for(i=0;i<=N;i++){
                printf("%d ",DegreeList[j][i]);
                if(i==N)
              printf("\n");
        }

    //print the least degreed vertice
    FindSmallestDegree(DegreeList,N);

    //delete relevant vertice

    for(countm=0;countm<=N;countm++){
    tempsmallest = FindSmallestDegree(DegreeList,N);
    for(FinalCount=1;FinalCount<=N;FinalCount++){
            if(VerticeList[tempsmallest][FinalCount]!=0)
            {
                if(judge != tempsmallest){
                    //printf("%d \n",tempsmallest);
                    judge = tempsmallest;
                    Method1Order[M1Count++]=tempsmallest;
                }
                if(degree[tempsmallest]==degree[VerticeList[tempsmallest][FinalCount]]){;}
                    //printf("%d \n",VerticeList[tempsmallest][FinalCount]);
                //printf("%d \n",VerticeList[tempsmallest][FinalCount]);
                ChangeDegreeList(N,VerticeList[tempsmallest][FinalCount],DegreeList,tempsmallest,Method1Order,M1Count,degree,FindBiggestDegree(DegreeList,N));
                if(Method1Order[M1Count]!=0)
                    M1Count++;
            }
    }


 /*   for(j=2;j<=N;j++)
        for(i=0;i<=N;i++){
                printf("%d ",DegreeList[j][i]);
                if(i==N)
              printf("\n");
        }
        */
    }

    printf("\n");
    printf("Method 1 Vertex Ordering :\n");
    ReverseCount = N;
    for(i=1;i<=N;i++){
        ReverseM1[ReverseCount--] = Method1Order[i];
    }


    for(i=1;i<=N;i++){
        Method1Order[i]=ReverseM1[i];
        printf("%d ",Method1Order[i]);
    }

    printf("\n");



    printf("Method 2 Vertex Ordering\n");
    for(i=1;i<=N;i++)
        printf("%d ",Method2Order[i]);

        printf("\n");


    for(j=1;j<=N;j++){
        for(i=1;i<=N;i++){
            if(i == 1&&ExistInM3(N,Method3Order,j)!=1){
            Method3Order[M3Count++]=j;
            }
            if(Earray[j][i]==1&&ExistInM3(N,Method3Order,i)!=1){
                     Method3Order[M3Count++] = i;
            }
        }
    }


    printf("Method 3 Vertex Ordering\n");
     for(i=1;i<=N;i++)
        printf("%d ",Method3Order[i]);

    printf("\n");

    printf("==========================================");
    printf("\nMethod 1 Coloring Result : \n");
    printf("Average Original Degrees : %f \n", AverageDegree(degree,N));
    Coloring(Color1,Method1Order,VerticeList,N);
    printf("Total Color Used : %d \n\n",ColorUsed(Color1,N));
    for(i=1;i<=N;i++){
        printf("V%d,Color=%d,Original Degree=%d | ",Method1Order[i],Color1[Method1Order[i]],degree[Method1Order[i]]);
        if(i%3==0)
            printf("\n");
    }
    printf("\n");

    printf("==========================================");
    printf("\nMethod 2 Coloring Result : \n");
    printf("Average Original Degrees : %f \n", AverageDegree(degree,N));
    Coloring(Color2,Method2Order,VerticeList,N);
    printf("Total Color Used : %d \n\n",ColorUsed(Color2,N));
    for(i=1;i<=N;i++){
        printf("V%d,Color=%d,Original Degree=%d | ",Method2Order[i],Color2[Method2Order[i]],degree[Method2Order[i]]);
        if(i%3==0)
            printf("\n");
    }
    printf("\n");

    printf("==========================================");
    printf("\nMethod 3 Coloring Result : \n");
    printf("Average Original Degrees : %f \n", AverageDegree(degree,N));
    Coloring(Color3,Method3Order,VerticeList,N);
    printf("Total Color Used : %d \n\n",ColorUsed(Color3,N));
    for(i=1;i<=N;i++){
        printf("V%d,Color=%d,Original Degree=%d | ",Method3Order[i],Color3[Method3Order[i]],degree[Method3Order[i]]);
        if(i%3==0)
            printf("\n");
    }
    printf("\n");


    gettimeofday(&end, NULL);

    timer = 1000000 * (end.tv_sec - start.tv_sec) + end.tv_usec - start.tv_usec;

    printf("timer = %ld us\n", timer);

    free(Sarray);
    free(Earray);

    return 0;
}
