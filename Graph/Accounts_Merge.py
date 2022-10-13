"""
Accounts Merge

Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Understand
- given a list of lists, where each list contains [name, list of emails...]
    - merge accounts
        - common email to both accounts
        - same name != same person
- return in the following format
    - [name, emails in sorted order]

Match
- DFS

Plan
- keep track of the emails we've seen and where they're located
    - hashmap: key = email, value = index of the account
    - if it encounters an email its already seen before, add that account to a set to be merged with the previous ones
- iterate through the hashmap
    - if an email is a part of a set, add them to the merged accounts list
- sort the emails

Implement

Review

Evaluate
- Time Complexity: O(NK * NlogK)
    - N = # of accounts
    - K = max number of emails
    - Traversing = O(N*K)
    - Sorting at the end = O(NlogK)
- Space Complexity: O(NK)
"""
from collections import defaultdict
def accountsMerge(accounts):

    # list we'll output
    res = []

    # Build the graph
    # {email: [list of index that use this email]}
    graph=defaultdict(set)

    # get the name based on email
    email_to_name={}

    # iterate through all accounts
    for account in accounts:
        name=account[0]
        # iterate through all emails
        for email in account[1:]:
            # connect all emails to the first email
            graph[email].add(account[1])
            graph[account[1]].add(email)
            
            email_to_name[email]=name
    
    # {'johnsmith@mail.com': {'john00@mail.com', 'johnsmith@mail.com', 'john_newyork@mail.com'}, 'john_newyork@mail.com': {'johnsmith@mail.com'}, 'john00@mail.com': {'johnsmith@mail.com'}, 'mary@mail.com': {'mary@mail.com'}, 'johnnybravo@mail.com': {'johnnybravo@mail.com'}}
    print(graph)
    
    # {'johnsmith@mail.com': 'John', 'john_newyork@mail.com': 'John', 'john00@mail.com': 'John', 'mary@mail.com': 'Mary', 'johnnybravo@mail.com': 'John'}
    print(email_to_name)
    res=[]
    visited=set()

    # DFS
    for email in graph:
        if email not in visited:
            stack=[email]
            visited.add(email)
            local_res=[]
            while stack:
                node=stack.pop()
                local_res.append(node)
                
                for edge in graph[node]:
                    if edge not in visited:
                        stack.append(edge)
                        visited.add(edge)
            res.append([email_to_name[email]]+sorted(local_res))
    return res


accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])