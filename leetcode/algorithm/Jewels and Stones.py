class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        m = 0
        j = {'num': m}
        for i in S:
            if i in J:
                m += 1
                j['num'] = m
        return int(j['num'])


if __name__ == '__main__':
    J = 'z'
    S = 'ZZ'
    so = Solution()
    num = so.numJewelsInStones(J, S)
    print(f'J:{J} \nS:{S} \nnum:{num}')