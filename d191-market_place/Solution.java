package market_place;

import java.util.Scanner;

public class Solution
{
    public static void main(String[] args) 
    {
        Scanner teclado = new Scanner(System.in);
        int opcao = 0;
        Mercado mercado = new Mercado();
        Carrinho carrinho = new Carrinho();

        do
        {
            switch (opcao)
            {
                case 1:
                    mercado.adicionarPorduto(teclado);
                    break;

                case 2:
                    mercado.listarProdutos();
                    break;

                case 3:
                    carrinho.adicionarPorduto(teclado, mercado);
                    break;

                case 4:
                    carrinho.listarProdutos();;
                    break;

                case 5:
                    carrinho.finalizarCarrinho();
                    break;
            
                default:
                    break;
            }
            System.out.println("Escolha uma opçao");
            System.out.println("1 - Cadastrar produto");
            System.out.println("2 - Listar produtos");
            System.out.println("3 - Comprar produto");
            System.out.println("4 - Visualizar carrinho");
            System.out.println("5 - Finalizar carrinho");
            System.out.println("6 - Sair do sistema");

            opcao = Integer.parseInt(teclado.nextLine());

        }while(opcao >= 1 && opcao <= 5);

        teclado.close();
    }
}
