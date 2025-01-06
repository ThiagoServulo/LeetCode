public class Cell 
{
    private Object value;
    private Cell next;
    private Cell prev;

    public Cell(Object value, Cell prev, Cell next)
    {
        this.value = value;
        this.next = next;
        this.prev = prev;
    }

    public Object getValue()
    {
        return value;
    }

    public Cell getNext()
    {
        return next;
    }

    public void setNext(Cell next)
    {
        this.next = next;
    }

    public Cell getPrev()
    {
        return prev;
    }

    public void setPrev(Cell prev)
    {
        this.prev = prev;
    }

    @Override
    public String toString() 
    {
        return value.toString();
    }
}
