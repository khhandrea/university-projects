import java.util.Scanner;

public class Assignment_04_1 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int[] count = new int[26];
		for(int i=0; i<26; i++)
			count[i] = -1;
		
		String S = scanner.next();
		
		for(int i=0; i<S.length(); i++)
			if(count[S.charAt(i) - 'a'] == -1)
				count[S.charAt(i) - 'a'] = i;
		
		for(int i=0; i<26; i++)
			System.out.print(count[i] + " ");
	}
}
