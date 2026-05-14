public class LogicTutorial {
    public static void main(String[] args) {
        /*
        AND && => และ
        OR  || =>หรือ
        NOT ! => ไม่ (ตรงข้าม)
        */

        int a=10,b=20;

        boolean c=(a==b); // false
        boolean d=(a<b); // true 

        System.out.println(c&&d);
        System.out.println(c||d);
        System.out.println(!c);
        System.out.println(!d);
    }
}
