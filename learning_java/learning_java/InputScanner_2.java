import java.util.Scanner;
class InputScanner_2 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("ป้อนชื่อของคุณ: ");
        String name=sc.nextLine(); //อ่านข้อความที่รับจากแป้นพิมพ์ทั้งบรรทัด
        System.out.println("ชื่อของคุณคือ = "+name);


    }
}