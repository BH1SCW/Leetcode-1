import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

// store the Parameter
class Parameter {
    double rate;
    double loan;
    double down_payment;
    int years;
    Parameter(String[] t) {
        loan = Double.parseDouble(t[0]);
        years = Integer.parseInt(t[1]);
        rate = Double.parseDouble(t[2]);
        down_payment = Double.parseDouble(t[3]);
    }
}
 
public class Main {
       
    // parse the input
    static Parameter parse(String line) {
        String[] tokens = line.split("~");
        return new Parameter(tokens);
    }
    
   static double[] calculate(Parameter param) {
        double r = param.rate / 12 / 100;
        double loan = param.loan - param.down_payment;
        int n = param.years * 12;
        double monthly_payment = (r * loan) / (1 - Math.pow(1 + r, -n));
        double total_interest = monthly_payment * n - loan;
        double[] ans = {monthly_payment,  total_interest};
        return ans;
    }

    
  /**
   * Iterate through each line of input.
   */
    public static void main(String[] args) throws IOException {
        InputStreamReader reader = new InputStreamReader(System.in, StandardCharsets.UTF_8);
        BufferedReader in = new BufferedReader(reader);
        String line;
        while ((line = in.readLine()) != null) {
        //   System.out.println(line);
            Parameter p = parse(line);
            double[] ans = calculate(p);
            System.out.printf("$%.2f~$%d\n", ans[0], Math.round(ans[1]));

        }
    }
}
