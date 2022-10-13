"""
Cheapest Flights within K Stops

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Understand
- return cheapest price from src to dst, at most k stops
    - even if its shorter to go another path, if its greater than k stops, you can't go through it
- can the edges have negative weights?
    - if so, go with bellman ford
- if not
    - go with dijkstras

Match
- Find shortest paths from src to dst on weighted graph = dijkstra or bellman ford
- bellman ford time complexity: O(VE)
- dijkstra: O(ElogV)

Plan
- create prices array where prices[destination we want to go to from source] = price
    - [float("Inf")] * number of vertices
- iterate through k + 1 (k+1 to reach the level of the destination vertex)
    - iterate through edges
        - if prices is not infinity and new price is less than old price
            - update prices to new path
- return prices[dest]

Implement

Review
[[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1

price = [inf, inf, inf]
price = [0, inf, inf]

iterate till 0, 1

0
price = [0, 100, 500]

1
price = [0, 100, 200]


Evaluate
- Time Complexity: O(k*E), where k is the at most stops we can make (iterate through k+1) and E is the number of edges (iterate through flights)
- Space Complexity: O(N), where N represents the number of vertices in the graph

"""
def findCheapestPrice(n, flights, src, dst, k):

    # Create price array where price[destination] = price
    price = [float("Inf")] * n

    # Set src price to 0
    price[src] = 0

    for i in range(k+1):
        print(i)
        tmpPrice = price.copy()
        for s,d,p in flights:
            if price[s] != float("Inf") and price[s] + p < tmpPrice[d]:
                tmpPrice[d] = price[s] + p
        print(tmpPrice)
        price = tmpPrice

    return -1 if price[dst] == float("Inf") else price[dst]


print("Expected Output: 700")
print("Actual Output: ", findCheapestPrice(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))

print("Expected Output: 200")
print("Actual Output: ", findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))