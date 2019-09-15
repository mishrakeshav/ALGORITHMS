#include<bits/stdc++.h>
#define N 8
//prints out the board
void printSolution(char board[N][N])
{
    static int k = 1;
    printf("Solution: %d\n", k);
    int i, j;
    for(int i = 0; i<N; i++){
        for(int j=0; j<N; j++){
            printf(" %c ", board[i][j]);
        }
        printf("\n");

    }
    k++;
}
// check if any position is safe
//i.e if any queen is atacking any other queen
// in that position
bool isSafe(char board[N][N], int row, int column)
{
    int i, j;

    //Check this row on left side
    for(i=0;i<N;i++)
    {
        if(board[row][i] == 'Q')
            return false;
    }

    //check upper diagonal on left side
    for(i=row, j=column; i>=0 && j>=0; i--, j--)
    {
        if(board[i][j] == 'Q')
            return false;
    }

    //check lower diagonal on left side
    for(i=row, j=column; j>=0 && i< N; i++, j--)
    {
        if(board[i][j] == 'Q')
            return false;
    }

    //if all the above condition are false
    return true;

}
//Helper function
bool Solve(char board[N][N], int col)
{
    // Base case:
    // If all the queens are placed
    //then return true
    if(col == N)
    {
        printSolution(board);
        return true;
    }
    bool res = false;
    int i;
    for(i=0; i<N; i++){
        if(isSafe(board, i, col)){
             //this is
            //choose
            board[i][col] = 'Q';

            //explore the next column
            //if queen can be placed in the next column
            //if not then return false
            //keep repeating the same by placing the queen in the
            //next row
            res = Solve(board,col+1) || res;

            //un-choose the selected position
            //try for next position
            board[i][col] = '-';
        }


    }
    //if queen cannot be placed in any row in
    //this column then return false
    return res;
}

void SolveNQueen()
{
    char board[N][N];
    memset(board, '-', sizeof(board));
    if(Solve(board, 0)==false){
        printf("Solution Does not exist");
        return ;

    }
    return ;
}
//main driver function
int main(){
    SolveNQueen();
    return 0;
}















