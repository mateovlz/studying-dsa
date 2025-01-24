def numJewelsInStones(jewels: str, stones: str) -> int:
    j = set(jewels)
    cont = 0
    for s in stones:
        if s in j:
            cont+=1
    return cont

def numJewelsInStones_2(J, S):
    Jset = set(J)
    return sum(s in Jset for s in S)

print(numJewelsInStones("aA", "aAAbbbb"))