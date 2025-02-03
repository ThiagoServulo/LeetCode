package defuse_the_bomb;

public class Solution
{
    public static void main(String[] args) 
    {
        int result[] = decrypt(new int[]{5,7,1,4}, 3);

        for(int i = 0; i < result.length; i++)
        {
            System.out.println(result[i]);
        }

    }

    public static int[] decrypt(int[] code, int k)
    {
        int len = code.length;

        int[] result = new int[len];

        if (k == 0)
        {
            for(int i = 0; i < len; i++)
            {
                result[i] = 0;
            }
        }
        else if(k < 0)
        {
            for(int i = 0; i < len; i++)
            {
                int aux = Math.abs(k);
                int sum = 0;
                int pos = i - 1;
                while(aux > 0)
                {
                    if(pos < 0)
                    {
                        pos += len;
                    }
                    sum += code[pos];
                    //System.out.println(code[pos]);
                    aux -= 1;
                    pos -= 1;
                }
                //System.out.println("--" + sum);
                result[i] = sum;
            }
        }
        else
        {
            for(int i = 0; i < len; i++)
            {
                int aux = Math.abs(k);
                int sum = 0;
                int pos = i + 1;
                while(aux > 0)
                {
                    if(pos >= len)
                    {
                        pos -= len;
                    }
                    sum += code[pos];
                    aux -= 1;
                    pos += 1;
                }
                result[i] = sum;
            }
        }
        return result;
    }
}

