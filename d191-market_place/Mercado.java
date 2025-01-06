package market_place;

import java.util.ArrayList;
import java.util.Scanner;

public class Mercado
{
    ArrayList<Produto> produtos = new ArrayList<>();

    Mercado()
    {

    }

    public void adicionarPorduto(Scanner teclado)
    {
        System.out.println("\nCadastrando novo produto");
        System.out.println("Nome: ");
        String n = teclado.nextLine();
        System.out.println("Preço: ");
        double p = Double.parseDouble(teclado.nextLine());
        System.out.println("Quantidade: ");
        int q = Integer.parseInt(teclado.nextLine());

        Produto produto = new Produto(n, p, q);

        int i = verificaSeProdutoExiste(produto);

        if(i != -1)
        {
            System.out.println("Quantidade atualizada com sucesso\n");
            produtos.get(i).incrementaQuantidade(q);
        }
        else
        {
            produtos.add(produto);
            System.out.println("Produto cadastrado com sucesso\n");
        }
    }

    public void listarProdutos()
    {
        int i = 1;

        System.out.println();

        for(Produto p : produtos)
        {
            System.out.println(i + " " + p);
            i++;
        }

        System.out.println();
    }

    private int verificaSeProdutoExiste(Produto produto)
    {
        int i = 0;

        for(Produto p : produtos)
        {
            if(p.getNome().equals(produto.getNome()))
            {
                return i;
            }

            i++;
        }

        return -1;
    }

    public Produto getProduto(int indice)
    {
        return produtos.get(indice);
    }

    public int quantidadeProdutos()
    {
        return produtos.size();
    }
}
