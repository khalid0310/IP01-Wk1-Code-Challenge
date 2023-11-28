    # Converts a 12-hour time to 24-hour time.
def convert_to_24_hour(hour, minute, period):

    # Convert hour based on the period (am/pm)
    if period.lower() == "am":
        if hour == 12:  # Handle midnight (12 am)
            hour = 0
    else:
        if hour != 12:  # Handle noon (12 pm)
            hour += 12

    # Return the time in 24-hour format as a four-digit string
    return f"{hour:02d}{minute:02d}"

   def exactly_two_positive(a, b, c):
    positive_count = sum(1 for num in (a, b, c) if num > 0)
    return positive_count == 2

# Example usage:
print(exactly_two_positive(2, 4, -3))  # Output: True
print(exactly_two_positive(-4, 6, 8))  # Output: True

def solve(word):
    def consonant_value(s):
        return sum(ord(char) - ord("a") + 1 for char in s)

    consonant_substrings = [s for s in word.split("aeiou") if s]
    values = [consonant_value(s) for s in consonant_substrings]

    return max(values)

# Example usage:
print(solve("zodiacs"))  # Output: 26
print(solve("strength"))  # Output: 57

 