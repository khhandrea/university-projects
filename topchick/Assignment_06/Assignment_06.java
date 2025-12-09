import java.util.Scanner;

class KHHCalculator {
    double num1;
    double num2;
    static double min = 1L;
    static double max = 100L;
    double add() { return (num1 + num2); };
    double subtract() { return (num1 - num2); };
    double multiply() { return (num1 * num2); };
    double divide() { return (num1 / num2); };
}

public class Assignment_06 {
    public static void main(String[] args) {
        System.out.println("학번: 202111278 이름: 김환희");
        KHHCalculator calc = new KHHCalculator();
        Scanner scanner = new Scanner(System.in);

        while(true) {
            System.out.print("\n실수 2개를 입력하세요: ");
            calc.num1 = scanner.nextDouble();
            calc.num2 = scanner.nextDouble();

            if(calc.num1 == 0L && calc.num2 == 0L) {
                System.out.println("프로그램이 종료되었습니다.");
                break;
            }

            if(calc.num1 < KHHCalculator.min || calc.num1 > KHHCalculator.max || calc.num2 < KHHCalculator.min || calc.num2 > KHHCalculator.max) {
                System.out.println("범위에 알맞는 숫자를 입력해주세요.");
                continue;
            }

            switch((int)(Math.random()*4)) {
                case 0: 
                    System.out.printf("[Add] %.1f + %.1f = %.1f\n", calc.num1, calc.num2, calc.add());
                    break;
                case 1: 
                    System.out.printf("[Subtract] %.1f + %.1f = %.1f\n",calc.num1, calc.num2, calc.subtract());
                    break;
                case 2: 
                    System.out.printf("[Multiply] %.1f + %.1f = %.1f\n", calc.num1, calc.num2, calc.multiply());
                    break;
                case 3: 
                    System.out.printf("[Divide] %.1f + %.1f = %.1f\n", calc.num1, calc.num2, calc.divide());
                    break;
            }
        }
    }
}
