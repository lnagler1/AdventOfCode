import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Objects;

public class Main {
    public static void main(String[] args) throws IOException {
        FileReader fileReader = new FileReader("C:\\2022\\AdventOfCode\\Day2\\src\\day2Input");
        BufferedReader reader = new BufferedReader(fileReader);

        String result = "";
        String line = "";
        int score;
        int fullScore = 0;
        while((line = reader.readLine()) != null) {
            String[] input = line.split(" ");

            if (Objects.equals(input[1], "X")){
                score = 1;
            }else if(Objects.equals(input[1], "Y")){
                score = 2;
            }else {
                score = 3;
            }

            String input0 = input[0];
            String input1 = input[1];

            switch(input){
                case(input[0].equals("A") && input[1].equals("Y")) -> fullScore += 1 +3; 
            }

            if (input0.equals("A") && input1.equals("Y")){
                fullScore +=  1 + 3;
            }
            if (input0.equals("B") && input1.equals("Y")){
                fullScore +=  2 + 3;
            }
            if (input0.equals("C") && input1.equals("Y")){
                fullScore +=  3 + 3;
            }
            if (input0.equals("A") && input1.equals("X")){
                fullScore +=  3;
            }
            if (input0.equals("B") && input1.equals("X")){
                fullScore +=  1;
            }
            if (input0.equals("C") && input1.equals("X")){
                fullScore +=  2;
            }
            if (input0.equals("A") && input1.equals("Z")){
                fullScore +=  2 + 6;
            }
            if (input0.equals("B") && input1.equals("Z")){
                fullScore +=  3 + 6;
            }
            if (input0.equals("C") && input1.equals("Z")){
                fullScore +=  1 + 6;
            }
        }
        System.out.println(fullScore);
        System.out.println(part1(reader));
    }

    public static int part1(BufferedReader reader) throws IOException {
        String result = "";
        String line = "";
        int score;
        int fullScore = 0;
        while((line = reader.readLine()) != null){
            String[] input = line.split(" ");
            if (Objects.equals(input[1], "X")){
                score = 1;
            }else if(Objects.equals(input[1], "Y")){
                score = 2;
            }else {
                score = 3;
            }
            System.out.println(score);
            if ((Objects.equals(input[0], "A") && Objects.equals(input[1], "X")) || (Objects.equals(input[0], "B") && Objects.equals(input[1], "Y")) || (Objects.equals(input[0], "C") && Objects.equals(input[1], "Z"))){
                result = "draw";
                fullScore += 3 + score;
            } else if ((Objects.equals(input[0], "A") && Objects.equals(input[1], "Z")) || (Objects.equals(input[0], "B") && Objects.equals(input[1], "X")) || (Objects.equals(input[0], "C") && Objects.equals(input[1], "Y"))) {
                result = "lose";
                fullScore += score;
            }else {
                fullScore += 6 + score;
                System.out.println("win");
            }

        }
        return fullScore;
    }
}