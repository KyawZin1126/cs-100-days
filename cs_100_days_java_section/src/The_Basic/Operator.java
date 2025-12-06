package The_Basic;

public class Operator {
    public static void main(String[] args) {
        int a = 10;
        int b = 5;
        int sum = a + b;
        int sub = a - b;
        int mul = a * b;
        int div = a / b;
        int mod = a % b;

        System.out.println(sum);
        System.out.println(sub);
        System.out.println(mul);
        System.out.println(div);
        System.out.println(mod);

        System.out.println("+++++++++++++++++++");
        int c = 5 ;

        boolean comResult1 = a < b;
        boolean comResult2 = a > b;
        boolean comResult3 = c <= b;
        boolean comResult4 = a >= b;

        System.out.println(comResult1);
        System.out.println(comResult2);
        System.out.println(comResult3);
        System.out.println(comResult4);

        System.out.println("+++++++++++++++++++");
        boolean logicalResult1 = a > b && a < c;
        boolean logicalResult2 = a > b || a < c;

        System.out.println(logicalResult1);
        System.out.println(logicalResult2);

        System.out.println("+++++++++++++++++++");
        boolean preResult = a + b > b + c && b * c < a / b ;

        System.out.println("preresult is ==>" + preResult);
    }
}


// Operators
// Operator Precedence ==>

//Arithmetic Operator ==> + , - , * , /
//Relational Operator or Comparison ==> < , > , <= , >=
//Logical Operator ==> && , ||
//Assignment Operator ==> =