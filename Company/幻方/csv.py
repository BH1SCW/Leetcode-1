def ParseAndStats(csv_content):
    lines = csv_content.split("\n")
    ans = []
    for line in lines:
        words = line.split(",")
        ans.append([len(w) if "\"" in w else len(w.strip()) for w in words ])
    return ans
