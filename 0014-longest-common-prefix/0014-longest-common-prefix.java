class Solution {
    public String longestCommonPrefix(String[] strs) {
            // Sort the array in lexicographical order
            Arrays.sort(strs);
            // Get the first and last string from the sorted array
            // These two strings will have the maximum potential common prefix
            String str1 = strs[0];
            String str2 = strs[strs.length - 1];

            // Variable to keep track of the longest common prefix length
            int index = 0;

            // Compare characters of the first and last string character by character
            // The first string (str1) is the smallest lexicographically, and the last string (str2) is the largest
            while (index < str1.length()) {
                // If the characters at the current index match in both strings
                if (str1.charAt(index) == str2.charAt(index)) {
                    // Increment the index to check the next character
                    index++;
                } else {
                    // If characters don't match, break out of the loop
                    break;
                }
            }

            // If the index is 0, it means no common prefix was found
            if (index == 0) {
                return "";
            } else {
                // If common prefix exists, print the prefix
                // str1.substring(0, index) gives the substring starting from index 0 up to 'index' 
                return str1.substring(0, index);
            }
        }
}