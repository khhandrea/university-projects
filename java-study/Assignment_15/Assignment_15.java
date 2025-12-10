import java.util.*;

public class Assignment_15 {
    public static void main(String[] args) {
        ArrayList<Integer> list1 =  new ArrayList<Integer>(10);
        list1.add(5); // list1.add(5);
        list1.add(4);
        list1.add(2);
        list1.add(0);
        list1.add(1);
        list1.add(3);
        ArrayList<Object> list2 = new ArrayList<Object>(list1.subList(1, 4));

        Collections.sort(list1);

        System.out.println("list1.containsAll(list2) : " + list1.containsAll(list2));

        list2.add("B");
        list2.add("C");
        list2.add(3, "A");
        print(list1, list2);

        list2.set(3, "AA");
        print(list1, list2);

        System.out.println("index : " + list1.indexOf(1));
        list1.remove(0); // list1.remove(1);

        System.out.println("list1.retainAll(list2) : " + list1.retainAll(list2));
        print(list1, list2);

        for(int i = list2.size()-1; i >= 0; i--) {
            if(list1.contains(list2.get(i))) {
                list2.remove(i);
            }
        }
        print(list1, list2);
    }

    static void print(ArrayList<Integer> list1, ArrayList<Object> list2) {
        System.out.println("list1 : " + list1);
        System.out.println("list2 : " + list2);
        System.out.println();
    }
}