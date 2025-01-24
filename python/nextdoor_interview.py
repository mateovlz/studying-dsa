class Comment:
    def __init__(self, id, parentId):
        self.id = id
        self.parentId = parentId

def print_hierarchy(comments):
    # Step 1: Organize comments by parentId
    comment_map = {}
    for comment in comments:
        if comment.parentId not in comment_map:
            comment_map[comment.parentId] = []
        comment_map[comment.parentId].append(comment)

    print(comment_map)
    
    # Step 2: Recursive function to print hierarchy
    def dfs(comment, depth):
        print("    " * depth + str(comment.id))
        for child in comment_map.get(comment.id, []):
            dfs(child, depth + 1)

    # Step 3: Process root comments and build the hierarchy
    for root_comment in comment_map.get(None, []):
        dfs(root_comment, 0)

# Example usage
comments = [
    Comment(1, None),
    Comment(2, None),
    Comment(3, 2),
    Comment(4, 2),
    Comment(5, 4),
    Comment(6, None),
]

print_hierarchy(comments)
