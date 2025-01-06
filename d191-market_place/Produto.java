package market_place;

public class Produto
{
    String nome;
    double preco;
    int quantidade;

    Produto(String n, double p, int q)
    {
        nome = n;
        preco = p;
        quantidade = q;
    }

    public String getNome()
    {
        return nome;
    }

    public double getPreco()
    {
        return preco;
    }

    public int getQuantidade()
    {
        return quantidade;
    }

    public void setQuantidade(int q)
    {
        quantidade = q;
    }

    public void incrementaQuantidade(int valor)
    {
        quantidade += valor;
    }

    public void decrementaQuantidade(int valor)
    {
        quantidade -= valor;
    }

    @Override
    public String toString()
    {
        return nome + " - " + quantidade + " - " + preco;
    }
}
