public class Cell 
{
    private Object value;
    private Cell next;

    public Cell(Object value, Cell next)
    {
        this.value = value;
        this.next = next;
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

    @Override
    public String toString() 
    {
        return value.toString();
    }
}
