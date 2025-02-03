package replace_all_digits_with_characters;
import java.util.ArrayList;
import java.util.Arrays;

public class Solution
{
    public static void main(String[] args) 
    {
        System.out.println(replaceDigits("a1c1e1"));
        System.out.println(replaceDigits("a1b2c3d4e")); // "abbdcfdhe"
    }

    public static String replaceDigits(String s)
    {
        String result = "";
        ArrayList<Character> letter = new ArrayList<>(Arrays.asList('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z'));

        for(int i = 0; i < s.length(); i++)
        {
            if(i % 2 != 0)
            {
                char l = s.charAt(i - 1);
                int n = s.charAt(i) - '0';

                int index = letter.indexOf(l) + n;

                result += letter.get(index);
            }
            else
            {
                result += s.charAt(i);
            }
        }

        return result;
    }

}
