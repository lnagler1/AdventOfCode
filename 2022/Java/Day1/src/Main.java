import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

import static java.util.Arrays.*;

public class Main {
    public static void main(String[] args) throws IOException {
        FileReader reader = new FileReader("src/day1Input");
        BufferedReader bufferedReader = new BufferedReader(reader);

        // Primitive Lösung not pretty
        String line;
        int[] max = new int[]{0,0,0};
        int calories = 0;
        while ((line = bufferedReader.readLine()) != null){
            if(line.isBlank()){
                System.out.println(stream(max).sum());
                if (max[0] < calories){
                    max[2] = max[1];
                    max[1] = max[0];
                    max[0] = calories;
                } else if (max[1] < calories) {
                    max[2] = max[1];
                    max[1] = calories;
                }else if(max[2] < calories){
                    max[2] = calories;
                }

                calories = 0;
            }else {
                calories += Integer.parseInt(line);

            }
        }
        System.out.println(stream(max).sum());
    }
}