public class Assignment_07 {
    public static void main(String[] args) {
        System.out.println("202111278 김환희");

        Figure f = new Figure();
        System.out.println("반지름이 5인 원의 둘레: " + f.length(5));
        System.out.println("10 ~ 20 선분의 길이: " + f.length(10, 20));
        System.out.println("(2,8) ~ (5,2) 사각형의 둘레: " + f.length(2, 8, 5, 2));
    }
}

class Figure {
    float length(int r) { 
        return (2 * (float)Math.PI * r);
    };
    float length(int a, int b) { 
        return Math.abs(a - b);
    };
    float length(int x1, int y1, int x2, int y2) { 
        return (2 * (Math.abs(x2 - x1) + Math.abs(y2 - y1)));
    };
}
