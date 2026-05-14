import java.util.Scanner;
class InputScanner {
    public static void main (String[] args) {
        //รับค่า

        //ประกาศใช้งาน class | new
        Scanner sc=new Scanner(System.in);
        System.out.print("ป้อนชื่อของคุณ: ");
        String name=sc.nextLine(); //รับค่า String จากคีย์บอร์ด => name
        
        System.out.print("ป้อน พ.ศ.เกิดของคุณ: ");
        int year = sc.nextInt(); //รับค่า interger จากคีย์บอร์ด => year

        int age = 2569-year ; //คำนวณอายุ

        System.out.println("ชื่อของคุณคือ "+name); //แสดงข้อความที่พิมพ์
        System.out.println("ปีพ.ศ.ของคุณคือ "+year);
        System.out.println("อายุของคุณคือ "+age+" ปี");
    }
}
