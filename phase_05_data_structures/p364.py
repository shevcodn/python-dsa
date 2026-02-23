def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    mapping_s_to_t = {}
    mapping_t_to_s = {}

    for char_s, char_t in zip(s, t):
        if char_s in mapping_s_to_t and mapping_s_to_t[char_s] != char_t:
            return False
        if char_t in mapping_t_to_s and mapping_t_to_s[char_t] != char_s:
            return False
        
        mapping_s_to_t[char_s] = char_t
        mapping_t_to_s[char_t] = char_s

    return True

print(is_isomorphic("egg", "add"))
print(is_isomorphic("foo", "bar"))
print(is_isomorphic("paper", "title"))