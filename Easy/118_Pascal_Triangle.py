class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []

        for i in range(numRows):
            if i == 0:
                output.append([1])
            elif i == 1:
                output.append([1,1])
            else:
                print(output)
                temp_out = [1]*(i+1)
                for j in range(1, i):
                    temp_out[j] = output[i-1][j-1] + output[i-1][j]
                output.append(list(temp_out))

        return output