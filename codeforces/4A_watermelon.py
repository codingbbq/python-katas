# https://codeforces.com/problemset/problem/4/A
# A. Watermelon


class Solution:

    def solve(self, w):
        if w<=2:
            return "NO"
        elif (w-2)%2==0:
            return "YES"
        else:
            return "NO"


if __name__ == "__main__":
    w = int(input())
    wm = Solution()
    print(wm.solve(w))
