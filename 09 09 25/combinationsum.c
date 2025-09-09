#include <stdio.h>
#include <stdlib.h>

void backtrack(int* candidates, int candidatesSize, int target,
               int* path, int pathSize, int start,
               int** res, int* returnSize, int* returnColumnSizes) {
    if (target == 0) {
        // Save current path
        res[*returnSize] = (int*)malloc(sizeof(int) * pathSize);
        for (int i = 0; i < pathSize; i++)
            res[*returnSize][i] = path[i];
        returnColumnSizes[*returnSize] = pathSize;
        (*returnSize)++;
        return;
    }
    for (int i = start; i < candidatesSize; i++) {
        if (candidates[i] <= target) {
            path[pathSize] = candidates[i];
            backtrack(candidates, candidatesSize, target - candidates[i],
                      path, pathSize + 1, i, res, returnSize, returnColumnSizes);
        }
    }
}

int** combinationSum(int* candidates, int candidatesSize, int target, int* returnSize, int** returnColumnSizes) {
    *returnSize = 0;
    int maxCombinations = 1000; // adjust if needed
    int** res = (int**)malloc(sizeof(int*) * maxCombinations);
    *returnColumnSizes = (int*)malloc(sizeof(int) * maxCombinations);
    int* path = (int*)malloc(sizeof(int) * target); // worst case all 1s

    backtrack(candidates, candidatesSize, target, path, 0, 0, res, returnSize, *returnColumnSizes);

    free(path);
    return res;
}

int main() {
    int candidates[] = {2, 3, 6, 7};
    int target = 7;
    int returnSize;
    int* returnColumnSizes;
    int** res = combinationSum(candidates, 4, target, &returnSize, &returnColumnSizes);

    for (int i = 0; i < returnSize; i++) {
        for (int j = 0; j < returnColumnSizes[i]; j++) {
            printf("%d ", res[i][j]);
        }
        printf("\n");
        free(res[i]);
    }
    free(res);
    free(returnColumnSizes);

    return 0;
}
