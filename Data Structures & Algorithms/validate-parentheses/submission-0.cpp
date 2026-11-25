class Solution {
public:
    bool isValid(string s) {
        stack<char> brackets;
        unordered_map<char, char> map = {{')', '('}, {'}', '{'}, {']', '['}};

        for(int i = 0; i < s.length() ; i++){
            
            //if the i'th character is not in the map (key) aka closing 
            //this means the character is an opening bracket
            if(map.find(s[i]) == map.end()){ 
                brackets.push(s[i]); //push the open bracket into stack
            }
            else{ //if its a closing bracket
                if(brackets.empty()) //and if the stack is empty
                    return false; 
                    //return false bc there is no pair for the closed bracket
                //the stack isn't empty
                //if top open bracket doesn't match the value pair 
                else if(brackets.top() != map[s[i]])
                    return false;

                //the stack isn't empty
                //if the top does match the close bracket
                else if (brackets.top() == map[s[i]])
                    brackets.pop(); //then pop it off
            }
        }

        return brackets.empty();
    }
};
