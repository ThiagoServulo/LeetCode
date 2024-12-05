package remove_trailing_zeros_from_a_string;

public class Solution
{
    public static String removeTrailingZeros(String num) 
    {
        int aux = num.length() - 1;
        while(aux >= 0)
        {
            if(num.charAt(aux) != '0')
            {
                break;
            }
            --aux;
        }
        return num.substring(0, aux + 1);
    }

    public static void main(String[] args) 
    {
        System.out.println(removeTrailingZeros("51230100"));
    }
}
