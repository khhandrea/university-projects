public class Assignment_11 {
    public static void main(String[] args) {
        System.out.println("202111278 김환희");

        Items item1 = new Items("기본 아이템", 1000);
        Items item2 = new Books("건국 자바", 15000, "지정희");
        Items item3 = new Shoes("그린신발", 20000, 270, "그린");

        Buyer man1 = new Buyer("김환희1", 30000);
        man1.buy(item1);
        man1.buy(item2);
        man1.buy(item3);

        item1.showInfo();
        item2.showInfo();
        item3.showInfo();

        Buyer man2 = new Buyer("김환희2", 50000);
        man2.buy(item1);
        man2.buy(item2);
        man2.buy(item3);

        item1.showInfo();
        item2.showInfo();
        item3.showInfo();
    }
}

class Items {
    protected String name;
    protected int price;
    protected int buyer_count = 0;
    protected String[] buyer_list = new String[10];

    Items(String name, int price) {
        this.name = name;
        this.price = price;
    }

    public void showInfo() {
        System.out.println("이름: " + name);
        System.out.println("가격: " + price);
        System.out.println("구매자 수: " + buyer_count);
        System.out.print("구매자 list: ");
        for(int i=0; i<buyer_count; i++) System.out.print(buyer_list[i] + " ");
        System.out.println("\n--------------------------");
    }

    public void buy(String name) {
        System.out.println(name + "님이 " + this.name + "(을)를 구매하셨습니다.");
        buyer_list[buyer_count++] = name;
    }
}

final class Books extends Items {
    private String author;

    Books(String name, int price, String author) {
        super(name, price);
        this.author = author;
    }

    public void showInfo() {
        System.out.println("저자: " + author);
        super.showInfo();
    }
}

final class Shoes extends Items {
    private int size;
    private String color;

    Shoes(String name, int price, int size, String color) {
        super(name, price);
        this.size = size;
        this.color = color;
    }

    public void showInfo() {
        System.out.println("신발 크기: " + size);
        System.out.println("신발 색깔: " + color);
        super.showInfo();
    }
}

final class Buyer {
    private String name;
    private int money;

    Buyer(String name, int money) {
        this.name = name;
        this.money = money;
    }

    public void buy(Items i) {
        if (money >= i.price) {
            money -= i.price;
            i.buy(name);
        }
        else {
            System.out.println("**************************");
            System.out.println("*** 잔액이 부족합니다. ***");
            System.out.println("**************************");
        }
    }
}