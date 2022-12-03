import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        File file = new File("D:\\Lukas\\AdventOfCode\\2015\\day2Problem\\src\\dimensions");
        FileReader fileReader = new FileReader(file);
        BufferedReader reader = new BufferedReader(fileReader);
        String line = "";
        final String splitter = "x";
        int length = 0;
        int width = 0;
        int height = 0;
        int wrapingPaper = 0;
        int right = 0;
        int bottom = 0;
        int front = 0;
        int slack = 0;
        int sum = 0;

        while ((line = reader.readLine()) != null) {
            length = Integer.parseInt(line.split(splitter)[0]);
            width = Integer.parseInt(line.split(splitter)[1]);
            height = Integer.parseInt(line.split(splitter)[2]);
            right = (2 * length * width);
            bottom =(2 * width * height);
            front =(2 * height * length);

           slack = Math.min(length * width, width * height);
           if (front / 2 < slack){
               slack = front / 2;
           }
            wrapingPaper += right + front + bottom + slack;
        }
        System.out.println(wrapingPaper);
        System.out.println("Hello world!");
    }
}