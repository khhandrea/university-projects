class Items {
    String name;
    int price;

    Items(String name, int price) {
        this.name = name;
        this.price = price;
    }

    void showItems() {
        System.out.println("이름: " + name);
        System.out.println("가격: " + price);
    }
}

class Books extends Items {
    String author;

    Books(String name, int price, String author) {
        super(name, price);
        this.author = author;
    }

    void showItems() {
        super.showItems();
        System.out.println("저자: " + author);
    }
}

class Foods extends Items {
    int amount;
    int price;

    Foods(String name, int price, int amount) {
        super(name, price);
        this.amount = amount;
        this.price = super.price * amount;
    }

    void showItems() {
        System.out.println("이름: " + name);
        System.out.println("가격: " + price);
        System.out.println("개수: " + amount);
    }
}

public class Assignment_09 {
    public static void main(String[] args) {
        System.out.println("202111278 김환희");
        Items item = new Items("아이템", 1000);

        item.showItems(); 
        
        System.out.println("----------");
        Books mybooks = new Books("자바의 정석", 25000, "남궁성"); 

        mybooks.showItems();

        System.out.println("----------");
        Foods myfoods = new Foods("사과", 3000, 5);
        myfoods.showItems();
    }
}