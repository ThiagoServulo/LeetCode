package market_place;

import java.util.ArrayList;
import java.util.Scanner;

public class Carrinho
{
    ArrayList<Produto> produtos = new ArrayList<>();

    Carrinho()
    {

    }

    public void listarProdutos()
    {
        System.out.println("\nImprimindo seu carrinho");
        
        for(Produto p : produtos)
        {
            System.out.println(p);
        }

        System.out.println();
    }

    public void finalizarCarrinho()
    {       
        System.out.println("\nFinalizando sua compra");
        double total = 0;

        for(Produto p : produtos)
        {
            System.out.println(p);
            total += (p.getQuantidade() * p.getPreco());
        }

        System.out.println("Valor total da compra: " + total + "\n");

        produtos.clear();
    }

    private boolean verificaSeProdutoExiste(Produto produto)
    {
        for(Produto p : produtos)
        {
            if(p.getNome().equals(produto.getNome()))
            {
                return true;
            }
        }

        return false;
    }

    public void adicionarPorduto(Scanner teclado, Mercado mercado)
    {
        System.out.println("\nSelecione o produto que deseja comprar: ");
        mercado.listarProdutos();
        int indice = Integer.parseInt(teclado.nextLine());
        indice--;

        if(indice < 0 || indice >= mercado.quantidadeProdutos())
        {
            System.out.println("Indice invalido");
            return;
        }

        Produto produto = mercado.getProduto(indice);

        if(produto == null)
        {
            System.out.println("Indice inválido");
            return;
        }

        System.out.println("Informe a quantidade");
        int quantidade = Integer.parseInt(teclado.nextLine());

        if(quantidade <= 0 || quantidade > produto.getQuantidade())
        {
            System.out.println("Quantidade invalida. Quantidade disponivel: " + produto.getQuantidade());
            return;
        }

        Produto p1 = new Produto(produto.getNome(), produto.getPreco(), quantidade);

        if(verificaSeProdutoExiste(p1))
        {
            int i = 0;
            for(Produto p : produtos)
            {
                if(p.getNome() == p1.getNome())
                {
                    produtos.get(i).incrementaQuantidade(p1.getQuantidade());
                    System.out.println("Quantidade atualizada com sucesso");
                    break;
                }

                i++;
            }
        }
        else
        {
            System.out.println("Produto adicionado ao carrinho com sucesso");
            produtos.add(p1);
        }

        mercado.getProduto(indice).decrementaQuantidade(quantidade);
    }
}
