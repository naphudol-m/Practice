public class Global_Local {
    public static void main(String[] args) {
        //Global Variable
        int a=100;
        int b=200;
        System.out.println(a);

        {
            int c=300; //Local Variable
            System.out.println(c);
        }
        System.out.println(b);
    }
}
