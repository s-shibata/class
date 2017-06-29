#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BYTE 256
#define kind 35536
#define spell 16
#define N 2

int count[BYTE] = {0};
int total=0;
char word[150000];
char word2[150000];
void Read ( FILE *fp1 )
{
	
	int c;
	int i  = 0;
	while( (c = getc(fp1)) != EOF ) {
		word[i] = c;
		i++;
		count[c]++;
		total++;
	}
	for(i=0;i < BYTE;i++){
		//printf("%c\t%d\n",i ,count[i]);
		//printf("%c",moji[i]);
	}

}

void rank ( )
{
	int i,j;
	int ran[BYTE];      //順位
	double fre;
	
	for( i = 0; i < BYTE; i++){
		ran[i] = BYTE;
	}
	for( j = 0; j < BYTE; j++ ) {
		for( i = 0; i < BYTE; i++ ) {
			if( count[j] >= count[i] ) {
				ran[j]--;
			}
		}
	}
	for( j = 0; j < 68; j++ ) {
		for( i = 0; i < BYTE; i++ ) {
			if( ran[i] == j ) {
				fre = (double)count[i]/(double)total;
				if( i == 10 ) printf(" %d位 \t \\n \t %d \t %1.5f\n", ran[i]+1, count[i], fre );
				else if( i == 32 ) printf(" %d位 \t space \t %d\t %1.5f\n", ran[i]+1, count[i], fre );
				else printf(" %d位 \t %c \t %d \t %1.5f\n", ran[i]+1, i, count[i], fre );
			}
		}
	}
}

void Write( FILE *fp1,FILE *fp2)
{
	int i;
	for(i = 0;word[i] != '\0';i++){
		if ((word[i] >= 'a' && word[i] <= 'z') || (word[i] >= 'A' && word[i] <= 'Z') || word[i] == ' ' || word[i] == '\n' ){
			fprintf(fp2,"%c",word[i]);
			word2[i] = word[i];
		}
	}
	
}
void TenWrite(FILE *fp2)
{
	int i,j;
	for(j = 0;j < 10;j++){
		for(i = 0;word[i] != '\n';i++){
			printf("%c",word[i]);
		}
	}
	printf("\n\n\n");
	for(j = 0;j < 10;j++){
		for(i = 0;word2[i] != '\n';i++){
			printf("%c",word2[i]);
		}
	}
}
void findWord( void )
{
	char tango[kind][spell];
	char tan[spell];
	int i = 0;
	int j = 0,k = 0,m = 0;
	
	int flag = 0;                     //flagはfor文を終わらせるため
	int tango_count[kind] = {0};
	int tango_total=0;
	int tango_rank[kind] = {0};
	int tango_max=0;
	int kind_total=0;
	double fre;
	
	for (m = 0;m < 144000;m++){
		if(word2[m] == ' ' || word2[m] == '\n' || word2[m] == '\0' ){
			i=0;
			for(j = 0;j < kind && flag == 0;j++){
				if(strcmp(tango[j],tan)==0){
					tango_count[j]++;
					flag = 1;
				}
				else if( tango[j][0] == '\0'){
					for(k = 0;k < spell && tan[k] != '\0';k++){        //無駄をなくす
						tango[j][k] = tan[k];
					}
					tango_count[j]++;
					flag = 1;
				}
			}
			/*初期化*/
			for(j = 0;j < spell;j++){
				tan[j] = '\0';
			}
			flag = 0;
		}
		else{
			tan[i] = word2[m];
			i++;
		}
	}
	/*単語の種類数*/
	for (i = 0;i < kind && tango[i][0] != '\0';i++){
		tango_max = i;
	}
	printf("%d\n",tango_max);
	/*単語頻出度ランク*/
	/*初期化*/
	for (i = 0;i < tango_max ;i++){
		tango_rank[i] = tango_max;
	}
	for (j = 0;j < tango_max;j++){
		for ( i = 0;i < tango_max;i++){
			if(tango_count[j] >= tango_count[i]){
				tango_rank[j]--;
			}
		}
	}
	/*単語合計*/
	for( i = 0; i < tango_max;i++){
		tango_total += tango_count[i];
	}
	printf("%d\n",tango_total);
	/*ランキング*/
	for( j = 0; j < 60;j++){
		for( i = 0; i < tango_max; i++){
			if(tango_rank[i] == j){
				fre = (double)tango_count[i]/(double)tango_total;
				printf("%d位 \t",j+1);
				for( k = 0; k < 128 && tango[i][k] != '\0';k++){
					printf("%c",tango[i][k]);
				}
				printf("\t %d \t %1.5f\n",tango_count[i],fre);
			}
			
		}
	}
}
/*
void pair_N( FILE *fp2 ){
	char pair[kind][spell];
	char pai[spell];
	char pai2[spell];
	int i,j,k,m;
	int pair_count[kind] = { 0 };
	int pair_rank[kind] = { 0 };
	int flag = 0;
	int pair_total = 0;
	double fre;
	
	for( m = 0; m < 144000; m++){
		if( m == N ){
			for(j = 0;j < kind && flag ==0; j++){
				if (strcmp(pair[j],pai) == 0){
					pair_max[j]++;
					flag = 1;
				}
				else if( word[j][0] == '\0'){
					for( k = 0; k < N && pai[k] != '\0'; k++){
						word[j][k] = pai[k];
					}
					pair_count[j]++;
					flag = 1;
				}
			}
		}
		else {
			if ( word2[m] == ' '){
				pai[i] = '_';
				i++
			}
			else if ( word2[m] == '\n'){
				
			}
			else{
				pai[i] = word2[m];
				i++
			}
		}	
	}
}*/
int main(void)
{
    FILE *fp1,*fp2;
    if ((fp1 = fopen("Alice.txt", "r")) == NULL) {   /* ファイルを開けなければ */
                                                    /* メッセージを表示して */
        fprintf ( stderr, "Can't Open C Source File!\n" );
        return 0;                                   /* 終了 */
    }
	if ((fp2 = fopen( "Alice1.txt", "w+" )) == NULL ){
		fprintf ( stderr, "Can't Open C Source File!\n" );
        return 0;
	}
    //printf("Alice.txt ファイルにおけるアルファベットの出現頻度\n");
    //CountLett(fp) ;        /* 文字の出現頻度を調べて */
    //juge(  );       /* 表示する */
	Read(fp1);
	//rank();
	Write(fp1,fp2);
	//TenWrite(fp2);
	findWord();
	//pair_N( FILE *fp2 );
	printf("%d",total);
    fclose(fp1);
	fclose(fp2);            /* ファイルを閉じる */
 }
