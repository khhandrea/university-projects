import java.util.Scanner;

public class Playground{
    public static void main(String[] args){
        try(Scanner in = new Scanner(System.in);){
           int x = in.nextInt();
           int y = in.nextInt();
           double z = (double)x/(double)y;
        
           if(y!=0){
           System.out.println(x + y);
           System.out.println(x - y);
           System.out.println(x * y);
           System.out.printf(String.format("%.2f\n", z));
           }
           else {
           System.out.print("y에 0이 입력되면 안됩니다.");
           }
        }
    }
}