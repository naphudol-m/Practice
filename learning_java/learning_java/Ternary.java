import java.util.Scanner;
public class Ternary {
    public static void main(String[] args){
        Scanner kb=new Scanner(System.in); //รับค่า

        System.out.print("ป้อนตัวเลข : "); //เก็บค่าในตัวแปร number
        int number=kb.nextInt();

        String result ="";

        //เงื่อนไข
        // if(number % 2 == 0){
        //     result=number+" เป็นจำนวนคู่";
        // }
        // else{
        //     result=number+" เป็นจำนวนคี่";
        // }
        //ตัวแปร =(เงื่อนไข) ? คำสั่งเมื่อเงื่อนไขเป็นจริง : คำสั่งเมื่อเงื่อนไขเป็นเท็จ ;
        result = (number%2 == 0) ? number+" เป็นจำนวนคู่" : number+" เป็นจำนวนคี่" ;
        System.out.println(result);
    }    
}
