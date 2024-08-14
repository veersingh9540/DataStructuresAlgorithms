# Check if the given string is palindrome or not

def isPalindrome(arr: str) -> bool:
    left = 0 
    right = len(arr)-1 
    arr = arr.upper()
    while left < right: 
        if arr[left] != arr[right]:
            return False
        
        left +=1
        right -=1

    return True

if(isPalindrome("RACECAR")):
    print("It is a palindrome")
else:
    print("It is not a palindrome")