import com.tinacg.gilmera.*;
import static assist.Shortcuts.print;

import java.util.Date;
import java.text.SimpleDateFormat;
import java.text.ParseException;

import java.util.Map;
import java.util.HashMap;

public class CLI {
    public static void main(String[] args) {
        /*
        Currency usd = new Currency("U.S. Dollars", "USD", "$");
        Amount ps3 = new Amount("599.99", usd);

        print(ps3.toVerboseString());

        SimpleDateFormat dateFormatter = new SimpleDateFormat("yyyy-MM-dd HH:mm ZZZZZ");

        String date1 = "2015-04-02 23:14 +0000";
        String date2 = "2015-4-2 9:10 -0000";

        Date d;
        try {
            d = dateFormatter.parse(date1);
            print(d);
        } catch (ParseException pe) {
            print("Could not parse date " + date1);
        }
        */

        // query DB to build accounts,
        // then query DB to get transactions
        
        Account games = new Account("Games", "games");
        Account wallet = new Account("Wallet", "wal");

        User me = new User("heitor");

        me.addCurrency(new Currency("U.S. Dollar", "USD", "$"));
        me.addCurrency(new Currency("New Taiwan Dollar", "TWD", "NT$"));
        me.addCurrency(new Currency("Brazilian Real", "BRL", "R$"));

        me.addAccount(new Account("Games", "games"));
        me.addAccount(new Account("Wallet", "wal"));
        
        me.addTransaction(new Transaction("ymd", "0000", "PlayStation 3",
                                          new Amount("599.99", me.getCurrency("USD")),
                                          games, wallet));
        
        me.addTransaction(new Transaction("ymd", "0000", "PlayStation 3",
                                          new Amount("1400.00", me.getCurrency("USD")),
                                          games, wallet));

        print(me.simplySumTransactions());

        HashMap<String, Amount> accountSummary = me.accountSummary(me.getAllTransactions(), "games");

        for (Amount a : accountSummary.values()) {
            print(a);
        }

        me.computeBalances(me.getAllTransactions());

        me.addToAccountBalance("games", "USD", new Amount("9999.99", new Currency("USD", "USD", "$")));
        me.addToAccountBalance("games", "USD", new Amount("10000", new Currency("USD", "USD", "$")));
        print(me.getAccountBalance("games", "USD").toString());
        print(me.getAccountBalance("games", "TWD").toString());
        // print(me.getAccount("games"));
    }
}





