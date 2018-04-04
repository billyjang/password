import java.io.Scanner;
import java.io.FileReader;

public class FormatText {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner infile = new Scanner(new FileReader("weak.txt"));
        ArrayList<String> foo = new ArrayList<String>();
        while(infile.hasNextLine()) {
            foo.add(infile.nextLine());
        }
        
    }
}