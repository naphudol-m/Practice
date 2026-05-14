class TypeCasting{
    public static void main(String[] args){
        //WideningCasting เล็ก -> ใหญ่
        // int numInt = 10;
        // double numDouble = numInt ;
        // System.out.println(numInt);
        // System.out.println(numDouble);

        //NarrowingCasting ใหญ่->เล็ก
        double numDouble = 10.0 ;
        int numInt = (int)numDouble;

        System.out.println(numInt);
        System.out.println(numDouble);

    }
}
