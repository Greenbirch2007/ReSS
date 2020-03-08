import java.util.regex.*;


public class DateDemo{
    public static void main(String args[]) {
        String content = " i am noob"+
        "from runno.com";


        String pattern = ".*runnob.*";
        boolean isMatch = Pattern.matches(pattern, content);
        System.out.println(isMatch);
    }

    public static int max(int num1,int num2) {
        int result;
        if (num1>num2)
            result = num1;
        else
            result = num2;
        return result;
    }
}