# 15 - Century or Half-Century
def check_score(runs):
    if runs >= 100:
        return "Century"
    elif runs >= 50:
        return "Half-Century"
    else:
        return "Less than a Half-Century"

# Example usage
runs_scored = 75
result = check_score(runs_scored)
print(result)  # Output: Half-Century
