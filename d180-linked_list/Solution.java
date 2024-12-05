class Solution 
{  
    public static void main(String[] args) 
    {
        LinkedList list = new LinkedList();

        list.addElementInit("sapo");
        list.addElementInit("gato");

        list.addElementEnd("rato");
        list.addElementEnd("a");
        list.addElementEnd("b");
        list.addElementInit("c");

        System.out.println(list);
        //list.addElement(0, "cachorro");
        list.addElement(2, "galo");
        //list.addElement(4, "xxxx");

        System.out.println(list);

        list.removeFirst();
        list.removeLast();

        System.out.println(list);

        list.remove(3);

        System.out.println(list);

        System.out.println(list.getElement(2).toString());

        System.out.println(list.hasElement("gato"));
        System.out.println(list.hasElement("1234"));
    }
}