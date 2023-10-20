#Manacher's Algorithm
def findLongestPalindrome(s):
    if not s:
        return ""

    # Step 1: Preprocess the input string
    modified_string = "#".join("^{}$".format(s))

    # Step 2: Initialize variables
    n = len(modified_string)
    palindrome_lengths = [0] * n
    center = 0
    right_boundary = 0

    # Step 3-6: Main loop
    for i in range(n):
        if i < right_boundary:
            mirror = 2 * center - i
            palindrome_lengths[i] = min(right_boundary - i, palindrome_lengths[mirror])

        # Attempt to expand palindrome centered at i
        left = i - (palindrome_lengths[i] + 1)
        right = i + (palindrome_lengths[i] + 1)

        while left >= 0 and right < n and modified_string[left] == modified_string[right]:
            palindrome_lengths[i] += 1
            left -= 1
            right += 1

        # If we find a longer palindrome, update center and right_boundary
        if i + palindrome_lengths[i] > right_boundary:
            center = i
            right_boundary = i + palindrome_lengths[i]

    # Step 7: Find the maximum palindrome length
    max_palindrome_length = max(palindrome_lengths)
    center_index = palindrome_lengths.index(max_palindrome_length)

    # Extract the longest palindromic substring
    start = (center_index - max_palindrome_length) // 2
    end = start + max_palindrome_length

    return s[start:end]

# Example usage
input_string = "abcdcbapqrstsrqp"
longest_palindrome = findLongestPalindrome(input_string)
print("Longest Palindromic Substring:", longest_palindrome)