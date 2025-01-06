package game_numbers;

import java.util.Random;

public class Game
{
    int dificuldade;
    int valor1;
    int valor2;
    char operacao;
    Random rand;

    Game(int dificuldade)
    {
        this.dificuldade = dificuldade;
        rand = new Random();
        valor1 = sortearNumero();
        valor2 = sortearNumero();
        operacao = sortearOperacao();
    }

    private int sortearNumero()
    {
        int num;

        switch (dificuldade) 
        {
            case 1:
                num = rand.nextInt(10);
                break;

            case 2:
                num = rand.nextInt(100);
                break;
        
            default:
                num = rand.nextInt(1000);
                break;
        }

        return num;
    }

    private char sortearOperacao()
    {
        int num = rand.nextInt(3);

        switch (num) 
        {
            case 0:
                return '+';

            case 1:
                return '-';
        
            default:
                return '*';
        }
    }

    public boolean conferir(int resultado)
    {
        switch (dificuldade) 
        {
            case '+':
                return resultado == (valor1 + valor2);

            case '-':
                return resultado == (valor1 - valor2);
        
            default:
                return resultado == (valor1 * valor2);
        }
    }

    public int getResultado()
    {
        switch (dificuldade) 
        {
            case '+':
                return valor1 + valor2;

            case '-':
                return valor1 - valor2;
        
            default:
                return valor1 * valor2;
        }
    }

    @Override
    public String toString()
    {
        return valor1 + " " + operacao + " " + valor2 + " = ";
    }
}
