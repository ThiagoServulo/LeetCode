package check_if_two_string_arrays_are_equivalent;
class Solution 
{
    public static boolean arrayStringsAreEqual(String[] word1, String[] word2)
    {
        String w1 = "";
        String w2 = "";

        for (String string : word1) 
        {
            w1 += string;
        }

        for (String string : word2) 
        {
            w2 += string;
        }

        return w1.equals(w2);
    }
    
    public static void main(String[] args) 
    {
        String[] word1 = {"ab", "c"};
        String[] word2 = {"a", "bc"};

        System.out.println(arrayStringsAreEqual(word1, word2));
    }
}