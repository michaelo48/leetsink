impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        if strs.is_empty() {
        return String::new();
    }
    
    let first = &strs[0];
    
    // Check each character position
    for (i, ch) in first.chars().enumerate() {
        // Check if all strings have the same character at position i
        for str in strs.iter().skip(1) {
            if str.chars().nth(i).map_or(true, |c| c != ch) {
                return first[..i].to_string();
            }
        }
    }
    
    // If we get here, the first string is a prefix of all strings
    first.clone()
    }
}