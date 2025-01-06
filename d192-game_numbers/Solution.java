package game_numbers;

import java.util.Scanner;

public class Solution
{
    public static void main(String[] args) 
    {
        Scanner teclado = new Scanner(System.in);

        System.out.println("Escolha a dificuldade (1 - fácil, 2 - médio, 3 - difícil): ");
        int dificuldade = Integer.parseInt(teclado.nextLine());

        if(dificuldade <= 0 || dificuldade >= 4)
        {
            System.out.println("Nível de dificuldade inválido");
            teclado.close();
            return;
        }

        Game game = new Game(dificuldade);
        System.out.println(game);

        int resultado = Integer.parseInt(teclado.nextLine());

        if(game.conferir(resultado))
        {
            System.out.println("Você ganhou");
        }
        else
        {
            System.out.println("Você perdeu. O resultado correto seria: " + game.getResultado());
        }

        teclado.close();
    }
}
