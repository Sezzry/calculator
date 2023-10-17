import java.util.Scanner;

public class calculator {

    public static void main(String[] args) throws Exception {

        double x, y;

        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Choose calculation:");
            System.out.println("1.Addition");
            System.out.println("2.Subtraction");
            System.out.println("3.Multiply");
            System.out.println("4.Divide");

            x = sc.nextDouble();
            y = sc.nextDouble();
        }

    }

}
