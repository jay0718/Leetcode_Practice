/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

#define N 100001

int** findWinners(int** matches, int matchesSize, int* matchesColSize, int* returnSize, int** returnColumnSizes){
    int lossesCount[N];
    *returnSize = 2;
    int **ans = (int **) malloc(*returnSize * sizeof(int *));
    int *ansCol = (int *) calloc(*returnSize, sizeof(int));
    
    for (int i = 0; i < N; i++)
        lossesCount[i] = -1;

    for (int i = 0; i < matchesSize; i++) {
        int winner = matches[i][0], loser = matches[i][1];
        if (lossesCount[winner] == -1) {
            lossesCount[winner] = 0;
        }
        if (lossesCount[loser] == -1) {
            lossesCount[loser] = 1;
        } else {
            lossesCount[loser]++;
        }
    }
    
    for (int i = 1; i < N; i++) {
        if (lossesCount[i] == 0) {
            ansCol[0]++;
        } else if (lossesCount[i] == 1) {
            ansCol[1]++;
        }
    }
    
    ans[0] = (int *) malloc(ansCol[0] * sizeof(int));
    ans[1] = (int *) malloc(ansCol[1] * sizeof(int));
    int h = 0, k = 0;
    for (int i = 1; i < N; i++) {
        if (lossesCount[i] == 0) {
            ans[0][k++] = i;
        } else if (lossesCount[i] == 1) {
            ans[1][h++] = i;
        }
    }
    *returnColumnSizes = ansCol;
    return ans;
}