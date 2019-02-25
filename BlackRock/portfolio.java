import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.*; 

public class Main {
    // the order is really confusing, should be linkedhashmap
    static HashMap<String, StockBond> portfolios_map = new HashMap<String, StockBond>(); 
    static HashMap<String, StockBond> benchmarks_map = new HashMap<String, StockBond>(); 
    
    // main function
    public static void transact() {
        for (Map.Entry<String, StockBond> p : portfolios_map.entrySet()) {
            String key = p.getKey();
            StockBond value = p.getValue();
            // System.out.printf("%s, %d\n", key, value.share);
            if (benchmarks_map.containsKey(key)) {
                StockBond target = benchmarks_map.get(key);
                // System.out.printf("%s, %d\n", key, target.share);
                if (target.share < value.share) {
                    System.out.printf("SELL,%s,%d\n", value.name, value.share - target.share);
                }
                if (target.share > value.share) {
                    System.out.printf("BUY,%s,%d\n", value.name, target.share - value.share);
                }
            } else {
                // sell all of them if it doesn't exist in the benchmarks
                    System.out.printf("SELL,%s,%d\n", value.name, value.share);
            }
        }
        
        for (Map.Entry<String, StockBond> b : benchmarks_map.entrySet()) {
            String key = b.getKey();
            StockBond value = b.getValue();
            // buy all of them if it doesn't exist in the portfolios
            if (!portfolios_map.containsKey(key)) {
                System.out.printf("BUY,%s,%d\n", value.name, value.share);
            }
        }
    } 

   
    public static void main(String[] args) throws IOException {
        InputStreamReader reader = new InputStreamReader(System.in, StandardCharsets.UTF_8);
        BufferedReader in = new BufferedReader(reader);
        String line;
        while ((line = in.readLine()) != null) {
            // get the information and store in the map
            String[] p = line.split(":");
            String[] portfolios = p[0].split("\\|");
            String[] benchmarks = p[1].split("\\|");
            //System.out.println(Arrays.toString(portfolios));
            //System.out.println(Arrays.toString(benchmarks));
            for (String pf : portfolios) {
                StockBond stock = new StockBond(pf);
                portfolios_map.put(stock.name, stock);
            }
            for (String pf : benchmarks) {
                StockBond stock = new StockBond(pf);
                benchmarks_map.put(stock.name, stock);
            }
        //   System.out.println(line);
        transact();
        // clear map
        portfolios_map.clear();
        benchmarks_map.clear();
        }
    }
  
    // data structure to hold stock or bond
    public static class StockBond {
        public String name;
        public int share;
        public double price;
        public double interest;
        StockBond(String line) {
            String[] tokens = line.split("\\,");
            // System.out.println(Arrays.toString(tokens));
            name = tokens[0];
            share =  Integer.parseInt(tokens[2]);
            price =  Double.parseDouble(tokens[3]);
            interest =  Double.parseDouble(tokens[4]);
        }
    }
}












