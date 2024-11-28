#Q: Find the Longest Common Prefix

# Input list of strings
strs = ["flower", "flow", "flight"]

# Initialize prefix to the first string
prefix = strs[0]

# Compare prefix with each string in the list
for s in strs[1:]:
    while not s.startswith(prefix):
        prefix = prefix[:-1]
        if not prefix:
            break

# Output the longest common prefix
print(prefix)
