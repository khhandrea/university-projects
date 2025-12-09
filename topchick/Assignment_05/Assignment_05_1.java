import java.util.Scanner;

class Student {
    String name;
    int id;
    int score;

    void scoreUp() { score += 5; };
}

public class Assignment_05_1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Student[] student = new Student[3];
        for(int i=0; i<student.length; i++) {
            student[i] = new Student();
            student[i].name = "김환희" + (i+1);
            student[i].id = 202111278;
            student[i].score = 0;
        }
        int sum = 0;

        for(int i=0; i<student.length; i++) {
            System.out.printf("%s 학생이 맞은 문제의 개수를 입력하세요: ", student[i].name);
            int answer = scanner.nextInt();
            
            for(int j=0; j<answer; j++) student[i].scoreUp();
        }

        for(int i=0; i<student.length; i++) {
            System.out.printf("%s 학생의 점수: %3d\n", student[i].name, student[i].score);
            sum += student[i].score;
        }
        System.out.printf("학생 %d명의 평균 점수: %3.2f\n", student.length, (float)sum/student.length);
    }
}