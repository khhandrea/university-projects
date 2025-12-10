public class Assignment_10 {
    public static void main(String[] args) {
        System.out.println("202111278 김환희");

        Ticket t1 = new Ticket(1000);
        t1.showInfo();

        Ticket t2 = new Ticket(1000);
        t2.showInfo();

        CreditCardTicket c1 = new CreditCardTicket(1000);
        c1.showInfo();

        CreditCardTicket c2 = new CreditCardTicket(5000);
        c2.showInfo();
    }
}

class Ticket {
    protected static int number = 0;
    protected int price;

    Ticket(int price) {
        number = number + 1;
        this.price = price;
    }

    public void showInfo() {
        System.out.println("티켓 번호: " + this.number);
        System.out.println("티켓 가격: " + this.price);
        System.out.println("==============================");
    }
}

final class CreditCardTicket extends Ticket {
    int price;

    CreditCardTicket(int price) {
        super(price);
    }

    public void showInfo() {
        System.out.println("※ 카드 결제로 가격 2배 적용");
        super.showInfo();
    }
}