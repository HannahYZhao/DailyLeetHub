class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board)
    {
        bool m[9][9] = {0}, m2[9][9] = {0}, m3[9][9] = {0};

        for (int i = 0; i < 9; i++)
            for (int j = 0; j < 9; j++)
                if (board[i][j] != '.') {
                    int num = board[i][j] - '0' - 1;
                    int k = i / 3 * 3 + j / 3;

                    if (m[i][num] || m2[j][num] || m3[k][num])
                        return false;

                    m[i][num] = m2[j][num] = m3[k][num] = 1;
                }

        return true;
    }
};