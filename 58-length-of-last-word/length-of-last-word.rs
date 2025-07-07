impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let mut last = s.len() - 1;
        let mut count = 0;
        let mut firstChar = false;

        for c in s.chars().rev(){

            if c == ' ' && firstChar == false{
                count = count - 1;
            } else if c != ' '  && firstChar == false{
                firstChar = true;
            } else if c == ' ' && firstChar == true{
                break;
            }

            count = count + 1;
        }
        return count;
    }
}