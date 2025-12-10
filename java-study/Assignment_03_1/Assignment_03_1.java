import java.util.*;

public class Assignment_03_1 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int a, b;
		a = scanner.nextInt();
		b = scanner.nextInt();
		
		for(int i=a; i<=b; i++)
		{
			for(int j=1; j<=9; j++)
			{
				System.out.printf("%d x %d = %2d\n", i, j, i*j);
			}
			System.out.println();
		}
	}
}
