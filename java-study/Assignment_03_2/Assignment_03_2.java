import java.util.Scanner;

public class Assignment_03_2 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int answer;
		int input;
		int count = 0;
		
		answer = (int)(Math.random()*100) + 1;
		while(true)
		{
			count++;
			input = scanner.nextInt();
			if(input > answer) System.out.println("Down");
			else if(input < answer) System.out.println("Up");
			else break;
		}
		System.out.println("정답입니다!");
		System.out.println("시도 횟수 :" + count);
	}
}
