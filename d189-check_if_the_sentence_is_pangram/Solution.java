package check_if_the_sentence_is_pangram;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Solution
{
    public static boolean checkIfPangram(String sentence)
    {
        Set<String> columnmapping  = new HashSet<String>(Arrays.asList(sentence.split("")));
        return columnmapping.size() == 26;
    }

    public static void main(String[] args) 
    {
        System.out.println(checkIfPangram("sapo"));
        System.out.println(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"));
        
    }
}
