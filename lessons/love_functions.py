"""given a subject as a  paramater, returns a loving string."""
def love(subject: str) -> str:
    return f"i love you {subject}!"

def spreadLove(to: str, n: int) -> str:
    """generates a str repeating a loving message n times"""
    love_note = ""
    counter = 0
    while counter < n:
        love_note += love(to) + "\n"
        counter += 1
    return love_note

print(spreadLove("robert", 4))