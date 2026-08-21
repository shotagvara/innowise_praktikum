"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 105
s consists of English letters, digits, symbols and spaces.
"""

def has_repeats(s)->bool:
    l=set()
    for x in s:
        if x in l: return True
        else: l.add(x)
    return False
def max_substring(s):
        max=0
        max_substring=""
        for i in range (0, len(s)+1):
            for j in range(i+1, len(s)+1):
                if  (has_repeats(s[i:j])== False) and (max<j-i):
                    max=j-i
                    max_substring=s[i:j]
        return (max_substring, max)


s="abcabcbb"
s1 = "bbbbb"
s2 = "pwwkew"
s3 = "asdfghjklnbvcdfg"

print(max_substring("abcde"))
print(max_substring(s))
print(max_substring(s1))
print(max_substring(s2))
print(max_substring(s3))


#Gemini
def length_of_longest_substring(s: str) -> int:
    # Словарь для хранения символа и его последнего увиденного индекса
    char_index_map = {}
    max_length = 0
    left = 0  # Левая граница скользящего окна
    
    # Перебираем строку правым указателем
    for right, char in enumerate(s):
        # Если символ уже есть в окне, сдвигаем левую границу за его прошлую позицию
        if char in char_index_map and char_index_map[char] >= left:
            left = char_index_map[char] + 1
            
        # Обновляем или добавляем позицию текущего символа
        char_index_map[char] = right
        
        # Считаем текущую длину окна и обновляем максимум
        max_length = max(max_length, right - left + 1)
        
    return max_length

# Проверка примеров
print(length_of_longest_substring("abcabcbb"))  # Выведет: 3 (подстрока "abc")
print(length_of_longest_substring("bbbbb"))     # Выведет: 1 (подстрока "b")
print(length_of_longest_substring("pwwkew"))    # Выведет: 3 (подстрока "wke")
print(length_of_longest_substring(s3))    # Выведет: 3 (подстрока "wke")
