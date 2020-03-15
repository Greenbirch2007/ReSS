
public class TestException{
    public static void main(String[] args){
        String test = "no";
        try{
            System.out.println("start try");
            doRish(test);
            System.out.println("end try");
        }catch (ScaryException se){
            System.out.println("scary exception");
        }finally{
            System.out.println("finally");
        }

        System.out.println("end of main");
    }


    static void doRish(String test) throws ScaryException{
        System.out.println("start risky");
        if ("yes".equals(test)){
            throw new ScaryException();

        }
        System.out.println("end risky");
        return;

    }
}




