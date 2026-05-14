public class Variable_02 {
    public static void main(String[] args) {
       
        String a="100" , b="200" ;
        
        //String => Double
        Double c =Double.parseDouble(a);
        c = c+3.14159;
        System.out.println(c);

        //Integer => String
        int num1 = 100;
        String age = String.valueOf(num1);
        System.out.println("อายุ "+age+" ปี");
        
    }
}
