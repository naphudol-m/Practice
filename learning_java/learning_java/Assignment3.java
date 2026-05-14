import java.util.Scanner;
public class Assignment3 {
    //โปรแกรมคำนวณเลขคู่ เลขคี่
    public static void main(String[] args){
        Scanner kb=new Scanner(System.in); //รับค่า

        System.out.print("ป้อนตัวเลข : "); //เก็บค่าในตัวแปร number
        int number=kb.nextInt();

        //เงื่อนไข
        if(number % 2 == 0){
            System.out.println(number+" เป็นจำนวนคู่");
        }
        else{
            System.out.println(number+" เป็นจำนวนคี่");
        }
    }
}
