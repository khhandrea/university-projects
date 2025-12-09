public class Assignment_04_2 {
	public static void main(String[] args) {
		int[][] array = new int[10][10];
		for(int i=0; i<10; i++)
			for(int j=0; j<10; j++)
				array[i][j] = (i+1)*(j+1);
		
		for(int i=0; i<10; i++)
		{
			for(int j=0; j<10; j++)
			{
				System.out.printf("%3d ", array[i][j]);
			}
			System.out.println();
		}
	}
}
