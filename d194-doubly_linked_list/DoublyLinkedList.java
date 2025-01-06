public class DoublyLinkedList
{
    private Cell first = null;
    private int total = 0;

    public void addElementInit(Object element)        
    {
        Cell newCell = new Cell(element, null, first);
        if(first!= null)
        {
            first.setPrev(newCell);
        }
        first = newCell;
        ++total;
    }

    public void addElementEnd(Object element)        
    {
        Cell currCell = first;

        if(currCell == null)
        {
            addElementInit(element);
            return;
        }

        for(int i = 0; i < total - 1; i++)
        {
            currCell = currCell.getNext();
        }

        Cell newCell = new Cell(element, currCell, null);
        currCell.setNext(newCell);

        total++;
    }

    public void addElement(int position, Object element)        
    {
        if(position <= 0)
        {
            addElementInit(element);
        } 
        else if (position >= total)
        {
            addElementEnd(element);
        }
        else
        {
            Cell currCell = first;

            for(int i = 0; i < position - 1; i++)
            {
                currCell = currCell.getNext();
            }

            Cell newCell = new Cell(element, currCell, currCell.getNext());
            (currCell.getNext()).setPrev(newCell);
            currCell.setNext(newCell);

            total++;
        }
    }

    public Object getElement(int position)        
    {
        Cell currCell = first;

        for (int i = 0; i < position; i++)
        {
            currCell = currCell.getNext();
        }

        return currCell;
    }

    public boolean hasElement(Object value)        
    {
        Cell currCell = first;

        for (int i = 0; i < total; i++)
        {
            if(currCell.getValue().equals(value))
            {
                return true;
            }
            currCell = currCell.getNext();
        }

        return false;
    }

    public void removeFirst()        
    {
        first = first.getNext();
        first.setPrev(null);
        --total;
    }

    public void removeLast()        
    {
        Cell currCell = first;
        for(int i = 0; i < total - 1; i++)
        {
            currCell = currCell.getNext();
        }

        currCell.setNext(null);

        --total;
    }

    public void remove(int position)        
    {
        if(position <= 0)
        {
            removeFirst();
        } 
        else if (position >= total)
        {
            removeLast();
        }
        else
        {
            Cell prevCell = first;
            for (int i = 0; i < position - 1; i++)
            {
                prevCell = prevCell.getNext();
            }
            
            Cell currCell = prevCell.getNext();
            prevCell.setNext(currCell.getNext());
            (currCell.getNext()).setPrev(prevCell);

            total--;
        }
    }

    @Override
    public String toString()
    {
        String ret = "[";

        Cell currCell = first;

        for(int i = 0; i < total; i++)
        {
            ret += currCell.getValue();
            ret += ", ";
            currCell = currCell.getNext();
        }

        ret += "]";

        return ret;
    }
}
